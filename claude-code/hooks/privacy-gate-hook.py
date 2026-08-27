#!/usr/bin/env python3
"""Agentic Rules — PreToolUse privacy gate (layer L1 of gate A).

Guards writes that cross from the member-private tier into the team tier:
  * kg_add / kg_link on the TEAM KG server (kg-dgx) when a private daemon is
    also configured,
  * Write / Edit / MultiEdit of files under team_memory_path,
  * Bash commands copying from memory_path, the user config dir, or any
    private/ path into team_memory_path.
Emits deny (definite pattern / structural violation), ask (heuristic), or
nothing (allow). Inactive when no team tier is configured. On internal error
it asks instead of allowing — L2/L3 still enforce, but the user should see it.
Audit lines (pattern ids only, never matched text) go to
<memory_path>/private/gate-log/YYYY-MM-DD.jsonl.
"""
import datetime
import json
import os
import re
import sys

from hook_common import opt, private_kg_configured, team_root, team_tier_active

ROOT = os.environ.get("CLAUDE_PLUGIN_ROOT", "")
sys.path.insert(0, os.path.join(ROOT, "tools"))
try:
    import privacy_gate as pg  # noqa: E402
except Exception:  # pragma: no cover
    pg = None

PATTERNS_FILE = os.path.join(ROOT, "settings", "privacy-gate.json")
TEAM_KG_RE = re.compile(r"^mcp__.*kg-dgx__kg_(add|link)$")
FILE_TOOLS = {"Write", "Edit", "MultiEdit", "NotebookEdit"}
COPY_VERB_RE = re.compile(r"\b(cp|rsync|mv|tee|install|git\s+add)\b|>\s*\S")
# NOTE: no bare "/private/" here — macOS realpath()s /tmp to /private/tmp, so a
# literal "/private/" fragment false-positives on any command that spells out a
# resolved temp path (e.g. `cp /private/tmp/build.log ...`) without it actually
# touching the memory store's own private/ subfolder. That case is instead
# caught relative to mp (memory_path) in decide()'s Bash branch below.
PRIVATE_SRC_MARKERS = ("/.claude/", "~/.claude")


def _out(decision, reason):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": decision,
        "permissionDecisionReason": reason,
    }}))


def _audit(record):
    mp = os.path.expanduser((opt("MEMORY_PATH") or "").strip())
    if not mp:
        return
    try:
        d = os.path.join(mp, "private", "gate-log")
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, datetime.date.today().isoformat() + ".jsonl"), "a", encoding="utf-8") as h:
            h.write(json.dumps(record) + "\n")
    except Exception:
        # Audit logging is best-effort. The decision has already been written
        # to stdout by _out() before _audit() runs; any exception here must
        # never propagate and produce a second stdout write.
        pass


def _within(base, path):
    base, path = os.path.realpath(base), os.path.realpath(os.path.expanduser(path))
    try:
        return os.path.commonpath([base, path]) == base
    except ValueError:
        return False


def _findings_to_reason(findings, errors=()):
    ids = sorted({f"{f.pattern_id}@{f.path}:{f.line}" for f in findings})
    parts = list(errors) + ids
    return "privacy gate: " + "; ".join(parts)


def _payload_text(o):
    # Recursively join all leaf values with REAL newlines. json.dumps() would
    # collapse the payload to one line and rewrite real newlines as the two
    # literal characters "\" + "n" — since "n" is a word character, every
    # scanner pattern anchored with a leading \b (word boundary) then fails
    # to match anything after the first line.
    if isinstance(o, dict):
        return "\n".join(_payload_text(k) + "\n" + _payload_text(v) for k, v in o.items())
    if isinstance(o, (list, tuple)):
        return "\n".join(_payload_text(v) for v in o)
    return str(o)


def decide(payload, patterns):
    name = str(payload.get("tool_name", ""))
    inp = payload.get("tool_input")
    if not isinstance(inp, dict):
        raise ValueError("tool_input is not an object")
    team = team_root()
    mp = os.path.expanduser((opt("MEMORY_PATH") or "").strip())
    terms = pg.load_lines(os.path.join(mp, "private", "gate-terms.txt")) if mp else []
    allow = pg.load_lines(os.path.join(team, "settings", "allowlist.txt")) if team else []

    if TEAM_KG_RE.match(name) and private_kg_configured():
        # Scan the whole payload rather than a fixed key list, so a future KG
        # server field (e.g. scope, metadata) isn't silently unscanned. Real
        # newlines are preserved (see _payload_text) so multi-line content is
        # still caught by \b-anchored scanner patterns.
        text = _payload_text(inp)
        f = pg.scan_text(text, patterns, allow, terms, path=name)
        return pg.verdict(f), _findings_to_reason(f), name

    if name in FILE_TOOLS and team:
        # NotebookEdit addresses the file via notebook_path, not file_path.
        path = str(inp.get("file_path") or inp.get("notebook_path", ""))
        if path and _within(team, path):
            if name == "MultiEdit":
                text = "\n".join(str(e.get("new_string", "")) for e in inp.get("edits", []) if isinstance(e, dict))
            elif name == "NotebookEdit":
                # NotebookEdit's cell content is in new_source; fall back to
                # content/new_string defensively in case the shape differs.
                text = str(inp.get("new_source", inp.get("content", inp.get("new_string", ""))))
            else:
                text = str(inp.get("content", inp.get("new_string", "")))
            rel = os.path.relpath(os.path.realpath(os.path.expanduser(path)), os.path.realpath(team))
            # frontmatter (audience/category) check only applies to Write, which creates/replaces
            # the whole file; Edit/MultiEdit/NotebookEdit only touch a fragment, and L3 (team repo
            # pre-commit) catches a frontmatter violation introduced via partial edits
            errors = pg.check_team_file(rel, text) if name == "Write" else []
            f = pg.scan_text(text, patterns, allow, terms, path=rel)
            code = pg.verdict(f)
            if errors:
                code = 2
            return code, _findings_to_reason(f, errors), rel

    if name == "Bash" and team:
        cmd = str(inp.get("command", ""))
        team_hit = team in cmd or os.path.realpath(team) in cmd
        priv_subdir_hit = bool(mp) and os.path.join(mp, "private") in cmd
        src_hit = (mp and mp in cmd) or priv_subdir_hit or any(m in cmd for m in PRIVATE_SRC_MARKERS)
        if team_hit and COPY_VERB_RE.search(cmd):
            if src_hit:
                return 2, "privacy gate: copying from a private location into the team root is blocked", "Bash"
            # No named private-source marker, but the command still writes into the
            # team root (e.g. `echo secret > team/file.md` or a heredoc) — scan the
            # command text itself rather than letting it through unscanned.
            f = pg.scan_text(cmd, patterns, allow, terms, path="Bash")
            code = pg.verdict(f)
            if code:
                return code, _findings_to_reason(f), "Bash"

    return 0, "", name


def main():
    if not team_tier_active():
        return
    if pg is None:
        _out("ask", "privacy gate error: privacy_gate module unavailable")
        return
    payload = json.load(sys.stdin)
    try:
        patterns = pg.load_patterns(PATTERNS_FILE)
        code, reason, target = decide(payload, patterns)
    except Exception as exc:  # fail visible, not open
        _out("ask", f"privacy gate error: {type(exc).__name__}")
        return
    if code == 0:
        return
    decision = "deny" if code == 2 else "ask"
    # The gate decision must reach stdout regardless of whether audit logging
    # succeeds — _audit() swallows all exceptions, so emit _out() first.
    _out(decision, reason)
    _audit({"ts": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "decision": decision, "target": target, "reason": reason})


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        _out("ask", f"privacy gate error: {type(exc).__name__}")
