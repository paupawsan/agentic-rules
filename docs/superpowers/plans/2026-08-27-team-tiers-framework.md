# Team Tiers — Framework (agentic-rules 1.7.0) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship agentic-rules 1.7.0: a team-shared tier (memory root + team KG) next to the existing member-private tier, a repo-root project identity marker, a fail-closed privacy gate (scanner + plugin PreToolUse hook), and the rules/docs that route knowledge between tiers — with a 1.6.0 configuration behaving byte-for-byte as before.

**Architecture:** One stdlib scanner (`tools/privacy_gate.py` + `settings/privacy-gate.json`) is the single source of truth for "what is private"; the plugin hook, the team KG server (separate plan) and the team memory repo all call it. Plugin options `team_memory_path` / `kg_private_mcp_url` switch the team tier on; hooks read them through `hook_common.py`. Rule text (`RULES.md.{en,ja,id}`) and the injected preamble tell the model how to route; the gate is what enforces it.

**Tech Stack:** Python 3 stdlib only (no third-party packages — `test/dogfood.sh` enforces stock Python), Claude Code plugin hooks (`SessionStart`, `PreToolUse`), JSON settings, Markdown rule text in en/ja/id.

**Spec:** `docs/superpowers/specs/2026-08-27-team-tiers-privacy-gate-design.md`

## Global Constraints

- Python: stdlib only in every shipped script (`tools/`, `claude-code/hooks/`); `bash test/dogfood.sh` runs them on a stock interpreter.
- Backward compatibility: with none of the new options set, `session-start.py` output and `memory-backup.py` behavior are **identical** to 1.6.0 (a test asserts byte equality of the preamble).
- Option names (exact): `team_memory_path`, `kg_private_mcp_url`. Server names (exact): existing `kg-dgx` stays; new `kg-private`.
- Marker file (exact): `.agentic-rules.json` at repo root, JSON `{"project_id": "<id>"}`.
- Team-eligible categories (exact set): `technical`, `contextual`, `topic`, `git_history`, `knowledge_graph`. Never-team: `behavioral`, `personal`, `credentials`, `sensitive`, `session`, `user_interaction`, `backup`, `knowledge_graph_overlay`.
- Scanner exit codes: `0` pass, `2` deny, `3` ask. Scanner never prints matched text — only pattern id, file, line.
- Version: every field `validate.py` checks becomes `1.7.0`; literal `1.6.0` in module rule text becomes `1.7.0`.
- Repo rule: no operator infrastructure names (hosts, IPs, personal repo names) anywhere in this repo.
- Commit convention: Conventional Commits; commit on `feat/team-tiers`; never push without the operator's go-ahead, and only to the internal remote (`origin`).
- Every task ends with `python3 claude-code/tests/test_plugin.py` green.

---

## File map

| File | Responsibility |
|------|----------------|
| `settings/privacy-gate.json` (new) | pattern classes (deny / ask) — the only place regexes live |
| `tools/privacy_gate.py` (new) | scanner library + CLI (`scan`, `staged`, `check-frontmatter`) |
| `tools/tests/test_privacy_gate.py` (new) | scanner unit tests (unittest) |
| `claude-code/hooks/hook_common.py` | shared option reader; **new** `project_id_for()`, `team_root()`, `private_kg_configured()` |
| `claude-code/hooks/memory-backup.py` | uses `hook_common.project_id_for` (marker-aware) |
| `claude-code/hooks/privacy-gate-hook.py` (new) | PreToolUse gate (L1) |
| `claude-code/hooks/hooks.json` | registers the PreToolUse hook |
| `claude-code/hooks/session-start.py` | preamble names team root / private daemon when set |
| `claude-code/.claude-plugin/plugin.json`, `claude-code/.mcp.json` | new options; `kg-private` server |
| `claude-code/tests/test_plugin.py` | hook wiring, gate fixtures, legacy parity |
| `modules/memory-rules/settings.json` | `storage`, `team_eligible`, marker-first identification |
| `modules/memory-rules/{RULES.md.en,ja,id}`, `MEMORY-RULES.md` | tier routing rules + algorithms |
| `modules/rag-rules/{RULES.md.en,ja,id}`, `RAG-RULES.md` | two-daemon recall; team daemon contract |
| `docs/CLAUDE_CODE_PLUGIN.md`, `docs/KG_IMPLEMENTATION_GUIDE.md`, `docs/INDEX.md`, `docs/CHANGELOG.md`, `README.md` | documentation |
| version fields (see Task 9) | 1.7.0 |

---

### Task 0: Open the tracking issue (internal repo)

**Files:** none in-repo.

- [ ] **Step 1: Create the issue on the internal remote** with the spec summary and this plan's task list.

```bash
cd <worktree>
gh issue create --repo "$(git remote get-url origin | sed -E 's#.*github.com[:/]##; s#\.git$##')" \
  --title "v1.7.0 — team tiers (private/team memory + KG), project marker, privacy gate" \
  --body-file docs/superpowers/specs/2026-08-27-team-tiers-privacy-gate-design.md
```

Expected: an issue URL on the **internal** repo. Record the number; every commit message in this plan references it as `#<N>`.

---

### Task 1: Privacy-gate pattern file and scanner library

**Files:**
- Create: `settings/privacy-gate.json`
- Create: `tools/__init__.py` (empty), `tools/privacy_gate.py`
- Test: `tools/tests/__init__.py` (empty), `tools/tests/test_privacy_gate.py`

**Interfaces:**
- Produces:
  - `load_patterns(path: str) -> dict` — `{"version": 1, "deny": [{"id","regex"}], "ask": [...]}` with compiled regexes under key `"_compiled"`: `list[tuple[id, severity, re.Pattern]]`.
  - `load_lines(path: str) -> list[str]` — non-empty, non-comment lines.
  - `scan_text(text, patterns, allowlist=(), private_terms=(), path="<text>") -> list[Finding]`; `Finding` is a `dataclass(pattern_id: str, severity: str, path: str, line: int)`.
  - `verdict(findings) -> int` — `2` if any deny, `3` if any ask, else `0`.
  - `check_team_file(rel_path: str, text: str, team_eligible: frozenset[str]) -> list[str]` — errors for a file inside a team root: missing/incorrect `audience: team` frontmatter; category segment not team-eligible.
  - CLI `python3 tools/privacy_gate.py scan|staged|check-frontmatter …` (Task 2).

- [ ] **Step 1: Write the pattern file**

```json
{
  "version": 1,
  "_comment": "Privacy gate A patterns. deny = definite private content (blocked); ask = heuristic (surfaced for a human decision). Regexes are Python `re`. Extend per team via an allowlist file (pattern ids or literal strings), never by editing this file in a team repo.",
  "deny": [
    {"id": "secret-aws-access-key", "regex": "\\bAKIA[0-9A-Z]{16}\\b"},
    {"id": "secret-github-token", "regex": "\\bgh[pousr]_[A-Za-z0-9]{20,}\\b"},
    {"id": "secret-sk-token", "regex": "\\bsk-[A-Za-z0-9_-]{16,}\\b"},
    {"id": "secret-bearer", "regex": "(?i)\\bbearer\\s+[A-Za-z0-9._~+/=-]{16,}"},
    {"id": "secret-private-key-block", "regex": "-----BEGIN (?:RSA |EC |OPENSSH |DSA |PGP )?PRIVATE KEY(?: BLOCK)?-----"},
    {"id": "net-ipv4-private", "regex": "\\b(?:10\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}|172\\.(?:1[6-9]|2\\d|3[01])\\.\\d{1,3}\\.\\d{1,3}|192\\.168\\.\\d{1,3}\\.\\d{1,3}|100\\.(?:6[4-9]|[7-9]\\d|1[01]\\d|12[0-7])\\.\\d{1,3}\\.\\d{1,3}|169\\.254\\.\\d{1,3}\\.\\d{1,3})\\b"},
    {"id": "net-mesh-vpn-hostname", "regex": "\\b[a-z0-9-]+\\.[a-z0-9-]+\\.ts\\.net\\b"},
    {"id": "path-home-unix", "regex": "(?<![\\w/])/(?:Users|home)/[A-Za-z0-9._-]+/"},
    {"id": "path-home-windows", "regex": "(?i)\\b[A-Z]:\\\\Users\\\\[^\\\\\\s]+"}
  ],
  "ask": [
    {"id": "pii-email", "regex": "\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}\\b"},
    {"id": "pii-phone", "regex": "(?<!\\w)\\+?\\d{1,3}[-.\\s]?\\(?\\d{2,4}\\)?[-.\\s]?\\d{3,4}[-.\\s]?\\d{3,4}(?!\\w)"},
    {"id": "secret-assignment", "regex": "(?i)\\b(?:api[_-]?key|secret|token|password|passwd)\\s*[:=]\\s*[\"']?[A-Za-z0-9._~+/=-]{12,}"}
  ]
}
```

- [ ] **Step 2: Write the failing tests**

```python
# tools/tests/test_privacy_gate.py
import os, sys, unittest
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, ROOT)
from tools import privacy_gate as pg  # noqa: E402

PATTERNS = pg.load_patterns(os.path.join(ROOT, "settings", "privacy-gate.json"))
ELIGIBLE = frozenset({"technical", "contextual", "topic", "git_history", "knowledge_graph"})


class ScanText(unittest.TestCase):
    def ids(self, text, **kw):
        return sorted(f.pattern_id for f in pg.scan_text(text, PATTERNS, **kw))

    def test_clean_text_passes(self):
        self.assertEqual(self.ids("Run make test before opening a PR."), [])

    def test_aws_key_is_deny(self):
        f = pg.scan_text("key AKIAABCDEFGHIJKLMNOP here", PATTERNS)
        self.assertEqual([(x.pattern_id, x.severity, x.line) for x in f],
                         [("secret-aws-access-key", "deny", 1)])

    def test_private_ip_and_home_path_are_deny(self):
        self.assertEqual(self.ids("host 192.168.1.36 and /Users/alice/x"),
                         ["net-ipv4-private", "path-home-unix"])

    def test_cgnat_range_is_deny(self):
        self.assertEqual(self.ids("100.100.5.7"), ["net-ipv4-private"])

    def test_public_ip_passes(self):
        self.assertEqual(self.ids("8.8.8.8 and 100.128.0.1"), [])

    def test_email_is_ask(self):
        f = pg.scan_text("mail me at a.b@example.org", PATTERNS)
        self.assertEqual([(x.pattern_id, x.severity) for x in f], [("pii-email", "ask")])

    def test_allowlist_by_pattern_id(self):
        self.assertEqual(self.ids("a@example.org", allowlist=["pii-email"]), [])

    def test_allowlist_by_literal(self):
        self.assertEqual(self.ids("see 192.168.1.36", allowlist=["192.168.1.36"]), [])
        self.assertEqual(self.ids("see 192.168.1.37", allowlist=["192.168.1.36"]), ["net-ipv4-private"])

    def test_private_terms_are_ask_case_insensitive(self):
        f = pg.scan_text("Ask PauPawSan about it", PATTERNS, private_terms=["paupawsan"])
        self.assertEqual([(x.pattern_id, x.severity) for x in f], [("private-term", "ask")])

    def test_line_numbers_are_reported(self):
        f = pg.scan_text("ok\nok\nAKIAABCDEFGHIJKLMNOP", PATTERNS)
        self.assertEqual(f[0].line, 3)

    def test_finding_never_carries_matched_text(self):
        f = pg.scan_text("AKIAABCDEFGHIJKLMNOP", PATTERNS)[0]
        self.assertNotIn("AKIA", repr(f))


class Verdict(unittest.TestCase):
    def test_codes(self):
        deny = pg.Finding("x", "deny", "p", 1); ask = pg.Finding("y", "ask", "p", 1)
        self.assertEqual(pg.verdict([]), 0)
        self.assertEqual(pg.verdict([ask]), 3)
        self.assertEqual(pg.verdict([ask, deny]), 2)


class TeamFile(unittest.TestCase):
    def test_requires_audience_team(self):
        errs = pg.check_team_file("projects/p/technical/a.md", "---\naudience: private\n---\nx", ELIGIBLE)
        self.assertEqual(errs, ["projects/p/technical/a.md: frontmatter must declare `audience: team`"])

    def test_missing_frontmatter_is_error(self):
        errs = pg.check_team_file("projects/p/technical/a.md", "no frontmatter", ELIGIBLE)
        self.assertEqual(len(errs), 1)

    def test_ineligible_category_is_error(self):
        errs = pg.check_team_file("projects/p/credentials/a.md", "---\naudience: team\n---\n", ELIGIBLE)
        self.assertEqual(errs, ["projects/p/credentials/a.md: category `credentials` is not team-eligible"])

    def test_common_category_path(self):
        self.assertEqual(pg.check_team_file("common/technical/a.md", "---\naudience: team\n---\n", ELIGIBLE), [])
        self.assertEqual(len(pg.check_team_file("common/behavioral/a.md", "---\naudience: team\n---\n", ELIGIBLE)), 1)

    def test_index_and_readme_exempt(self):
        self.assertEqual(pg.check_team_file("index.md", "# idx", ELIGIBLE), [])
        self.assertEqual(pg.check_team_file("projects/p/README.md", "# r", ELIGIBLE), [])


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 3: Run the tests to verify they fail**

Run: `python3 -m unittest tools.tests.test_privacy_gate -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'tools.privacy_gate'`.

- [ ] **Step 4: Write the library**

```python
#!/usr/bin/env python3
"""Privacy gate A — scanner for the private→team boundary.

Library + CLI. Stdlib only. Finds *shapes* of private content (keys, private
addresses, home paths, PII) plus a member's own private terms. Never prints the
matched text — only pattern id, file and line — so the gate itself can't leak.

Exit codes (CLI): 0 pass, 2 deny, 3 ask.
"""
import argparse
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass

TEAM_ELIGIBLE = frozenset({"technical", "contextual", "topic", "git_history", "knowledge_graph"})
EXEMPT_BASENAMES = frozenset({"index.md", "README.md", "readme.md"})
_FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.DOTALL)


@dataclass(frozen=True)
class Finding:
    pattern_id: str
    severity: str   # "deny" | "ask"
    path: str
    line: int


def load_patterns(path):
    with open(path, "r", encoding="utf-8") as handle:
        data = json.load(handle)
    compiled = []
    for severity in ("deny", "ask"):
        for entry in data.get(severity, []):
            compiled.append((entry["id"], severity, re.compile(entry["regex"])))
    data["_compiled"] = compiled
    return data


def load_lines(path):
    if not path or not os.path.isfile(path):
        return []
    with open(path, "r", encoding="utf-8") as handle:
        return [ln.strip() for ln in handle if ln.strip() and not ln.lstrip().startswith("#")]


def scan_text(text, patterns, allowlist=(), private_terms=(), path="<text>"):
    allow = set(allowlist)
    findings = []
    for lineno, line in enumerate(text.splitlines() or [""], start=1):
        for pid, severity, rx in patterns["_compiled"]:
            if pid in allow:
                continue
            for m in rx.finditer(line):
                if any(lit and lit in m.group(0) for lit in allow):
                    continue
                findings.append(Finding(pid, severity, path, lineno))
                break  # one finding per pattern per line
        low = line.lower()
        for term in private_terms:
            t = term.strip().lower()
            if t and t in low:
                findings.append(Finding("private-term", "ask", path, lineno))
                break
    return findings


def verdict(findings):
    if any(f.severity == "deny" for f in findings):
        return 2
    if findings:
        return 3
    return 0


def _frontmatter(text):
    m = _FRONTMATTER_RE.match(text)
    if not m:
        return None
    out = {}
    for ln in m.group(1).splitlines():
        if ":" in ln and not ln.lstrip().startswith("#"):
            k, _, v = ln.partition(":")
            out[k.strip()] = v.strip().strip("'\"")
    return out


def check_team_file(rel_path, text, team_eligible=TEAM_ELIGIBLE):
    rel = rel_path.replace("\\", "/").lstrip("./")
    if os.path.basename(rel) in EXEMPT_BASENAMES or not rel.endswith(".md"):
        return []
    errors = []
    fm = _frontmatter(text)
    if not fm or fm.get("audience") != "team":
        errors.append(f"{rel_path}: frontmatter must declare `audience: team`")
    parts = rel.split("/")
    category = None
    if parts[0] == "projects" and len(parts) >= 4:
        category = parts[2]
    elif parts[0] == "common" and len(parts) >= 3:
        category = parts[1]
    if category is not None and category not in team_eligible:
        errors.append(f"{rel_path}: category `{category}` is not team-eligible")
    return errors


# --- CLI ----------------------------------------------------------------

def _iter_files(paths):
    for p in paths:
        if os.path.isdir(p):
            for root, _dirs, files in os.walk(p):
                if "/.git" in root or root.endswith("/.git"):
                    continue
                for f in sorted(files):
                    yield os.path.join(root, f)
        elif os.path.isfile(p):
            yield p


def _read(path):
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as handle:
            return handle.read()
    except OSError:
        return ""


def _staged_files():
    out = subprocess.run(["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR"],
                         capture_output=True, text=True, check=False)
    return [ln for ln in out.stdout.splitlines() if ln.strip()]


def main(argv=None):
    ap = argparse.ArgumentParser(description="Privacy gate A scanner")
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("scan", "staged", "check-frontmatter"):
        s = sub.add_parser(name)
        s.add_argument("--patterns", default=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "settings", "privacy-gate.json"))
        s.add_argument("--allowlist", default="")
        s.add_argument("--private-terms", default="")
        s.add_argument("--json", action="store_true", help="machine-readable output")
        s.add_argument("--text", action="store_true", help="scan stdin text instead of paths (scan only)")
        s.add_argument("paths", nargs="*")
    args = ap.parse_args(argv)

    patterns = load_patterns(args.patterns)
    allow = load_lines(args.allowlist)
    terms = load_lines(args.private_terms)
    findings, errors = [], []

    if args.cmd == "scan" and args.text:
        findings = scan_text(sys.stdin.read(), patterns, allow, terms, path="<stdin>")
    else:
        files = _staged_files() if args.cmd == "staged" else list(_iter_files(args.paths))
        for f in files:
            text = _read(f)
            if args.cmd in ("scan", "staged"):
                findings.extend(scan_text(text, patterns, allow, terms, path=f))
            if args.cmd in ("check-frontmatter", "staged"):
                errors.extend(check_team_file(f, text))

    code = verdict(findings)
    if errors:
        code = 2
    if args.json:
        print(json.dumps({"exit": code, "findings": [f.__dict__ for f in findings], "errors": errors}))
    else:
        for f in findings:
            print(f"{f.severity.upper():4} {f.pattern_id:28} {f.path}:{f.line}")
        for e in errors:
            print(f"DENY frontmatter/category          {e}")
        if code == 0:
            print("privacy-gate: pass")
    return code


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 5: Run the tests to verify they pass**

Run: `python3 -m unittest tools.tests.test_privacy_gate -v`
Expected: all tests `ok`.

- [ ] **Step 6: Commit**

```bash
git add settings/privacy-gate.json tools/__init__.py tools/privacy_gate.py tools/tests/__init__.py tools/tests/test_privacy_gate.py
git commit -m "feat(gate): privacy-gate scanner library + pattern classes (#<N>)"
```

---

### Task 2: Scanner CLI behavior (scan / staged / check-frontmatter)

**Files:**
- Modify: `tools/privacy_gate.py` (CLI already present from Task 1 — this task tests it)
- Test: `tools/tests/test_privacy_gate.py`

**Interfaces:**
- Consumes: Task 1 library.
- Produces: exit-code contract `0/2/3`; `--json` shape `{"exit": int, "findings": [{"pattern_id","severity","path","line"}], "errors": [str]}`; `staged` = scan + frontmatter/category checks over `git diff --cached` files.

- [ ] **Step 1: Write the failing tests**

```python
class Cli(unittest.TestCase):
    SCRIPT = os.path.join(ROOT, "tools", "privacy_gate.py")

    def run_cli(self, *args, stdin=""):
        import subprocess
        return subprocess.run([sys.executable, self.SCRIPT, *args], input=stdin,
                              capture_output=True, text=True)

    def test_scan_text_deny_exit_2_and_no_secret_echo(self):
        p = self.run_cli("scan", "--text", stdin="token AKIAABCDEFGHIJKLMNOP")
        self.assertEqual(p.returncode, 2)
        self.assertIn("secret-aws-access-key", p.stdout)
        self.assertNotIn("AKIAABCDEFGHIJKLMNOP", p.stdout + p.stderr)

    def test_scan_text_ask_exit_3(self):
        self.assertEqual(self.run_cli("scan", "--text", stdin="a@example.org").returncode, 3)

    def test_scan_clean_exit_0(self):
        p = self.run_cli("scan", "--text", stdin="all good")
        self.assertEqual(p.returncode, 0); self.assertIn("privacy-gate: pass", p.stdout)

    def test_json_output(self):
        import json
        p = self.run_cli("scan", "--text", "--json", stdin="AKIAABCDEFGHIJKLMNOP")
        data = json.loads(p.stdout)
        self.assertEqual(data["exit"], 2)
        self.assertEqual(data["findings"][0]["pattern_id"], "secret-aws-access-key")

    def test_staged_checks_frontmatter_in_team_repo(self):
        import subprocess, tempfile
        with tempfile.TemporaryDirectory() as d:
            subprocess.run(["git", "init", "-q", d], check=True)
            os.makedirs(os.path.join(d, "projects", "p", "technical"))
            f = os.path.join(d, "projects", "p", "technical", "a.md")
            with open(f, "w") as h: h.write("---\naudience: private\n---\nclean\n")
            subprocess.run(["git", "-C", d, "add", "."], check=True)
            p = subprocess.run([sys.executable, self.SCRIPT, "staged"], cwd=d, capture_output=True, text=True)
            self.assertEqual(p.returncode, 2)
            self.assertIn("audience: team", p.stdout)
```

- [ ] **Step 2: Run to verify they fail or pass** — `python3 -m unittest tools.tests.test_privacy_gate.Cli -v`. Expected: `test_staged_checks_frontmatter_in_team_repo` FAILS if `staged` is not wired for frontmatter (it is in Task 1's code — then all pass; if any fails, fix `main()` until they pass).

- [ ] **Step 3: Run the whole scanner suite** — `python3 -m unittest tools.tests.test_privacy_gate -v` → all `ok`.

- [ ] **Step 4: Commit**

```bash
git add tools/tests/test_privacy_gate.py tools/privacy_gate.py
git commit -m "test(gate): CLI exit codes, JSON output, staged frontmatter check (#<N>)"
```

---

### Task 3: Project identity marker in `hook_common` + backup hook

**Files:**
- Modify: `claude-code/hooks/hook_common.py`
- Modify: `claude-code/hooks/memory-backup.py:52-70` (remove local `project_id_for`, import from `hook_common`)
- Test: `claude-code/tests/test_plugin.py`

**Interfaces:**
- Produces in `hook_common.py`:
  - `MARKER_FILE = ".agentic-rules.json"`
  - `project_id_for(cwd) -> str` — marker first (walks up from `cwd` to the git top-level or filesystem root), then git remote name, then directory name. Marker value must match `^[A-Za-z0-9][A-Za-z0-9._-]{0,63}$`, else ignored.
  - `team_root() -> str` — `team_memory_path` option, expanded; `""` if unset **or** nested with `memory_path` (either direction).
  - `private_kg_configured() -> bool` — `kg_private_mcp_url` option non-empty.
  - `team_tier_active() -> bool` — `team_root() != "" or private_kg_configured()`.

- [ ] **Step 1: Write the failing tests** (append to `test_plugin.py`)

```python
@test
def backup_uses_marker_project_id_over_git_remote():
    """A repo-root .agentic-rules.json wins over the git remote name."""
    with tempfile.TemporaryDirectory() as tmp:
        repo = os.path.join(tmp, "myproj-internal"); os.makedirs(repo)
        subprocess.run(["git", "init", "-q", repo], check=True)
        subprocess.run(["git", "-C", repo, "remote", "add", "origin",
                        "git@example.com:org/myproj-internal.git"], check=True)
        with open(os.path.join(repo, ".agentic-rules.json"), "w") as h:
            json.dump({"project_id": "myproj"}, h)
        sub = os.path.join(repo, "src"); os.makedirs(sub)
        store = os.path.join(tmp, "store")
        native = os.path.join(tmp, "native", "slug"); os.makedirs(os.path.join(native, "memory"))
        with open(os.path.join(native, "memory", "MEMORY.md"), "w") as h: h.write("x")
        run_backup({"memory_path": store},
                   {"transcript_path": os.path.join(native, "s.jsonl"), "cwd": sub})
        assert os.path.isdir(os.path.join(store, "projects", "myproj", "backup", "claude-code-native", "slug")), \
            os.listdir(os.path.join(store, "projects"))


@test
def backup_ignores_invalid_marker_project_id():
    with tempfile.TemporaryDirectory() as tmp:
        repo = os.path.join(tmp, "dirname"); os.makedirs(repo)
        with open(os.path.join(repo, ".agentic-rules.json"), "w") as h:
            json.dump({"project_id": "../escape"}, h)
        store = os.path.join(tmp, "store")
        native = os.path.join(tmp, "native", "slug"); os.makedirs(os.path.join(native, "memory"))
        with open(os.path.join(native, "memory", "MEMORY.md"), "w") as h: h.write("x")
        run_backup({"memory_path": store}, {"transcript_path": os.path.join(native, "s.jsonl"), "cwd": repo})
        assert os.path.isdir(os.path.join(store, "projects", "dirname")), "fell back to directory name"
        assert not os.path.exists(os.path.join(tmp, "escape"))


@test
def hook_common_team_root_refuses_nesting():
    src = read("claude-code/hooks/hook_common.py")
    assert "def team_root" in src and "def private_kg_configured" in src
    env = dict(os.environ)
    with tempfile.TemporaryDirectory() as tmp:
        code = ("import hook_common as h, sys; print(h.team_root())")
        for mp, tp, expect in [
            (tmp, os.path.join(tmp, "team"), ""),          # team inside private → refused
            (os.path.join(tmp, "p"), tmp, ""),             # private inside team → refused
            (os.path.join(tmp, "p"), os.path.join(tmp, "t"), os.path.join(tmp, "t")),
        ]:
            env["CLAUDE_PLUGIN_OPTION_MEMORY_PATH"] = mp
            env["CLAUDE_PLUGIN_OPTION_TEAM_MEMORY_PATH"] = tp
            out = subprocess.run([sys.executable, "-c", code], cwd=os.path.join(PLUGIN, "hooks"),
                                 env=env, capture_output=True, text=True).stdout.strip()
            assert out == expect, (mp, tp, out)
```

- [ ] **Step 2: Run to verify they fail** — `python3 claude-code/tests/test_plugin.py` → the three new tests FAIL (`AssertionError` / missing functions).

- [ ] **Step 3: Implement in `hook_common.py`** (append)

```python
import json
import re
import subprocess

MARKER_FILE = ".agentic-rules.json"
_PROJECT_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,63}$")


def _marker_project_id(cwd):
    """Walk up from cwd looking for .agentic-rules.json; stop at the git
    top-level (if any) or the filesystem root. Invalid ids are ignored."""
    top = None
    try:
        proc = subprocess.run(["git", "-C", cwd, "rev-parse", "--show-toplevel"],
                              capture_output=True, text=True, timeout=3)
        if proc.returncode == 0:
            top = os.path.realpath(proc.stdout.strip())
    except Exception:
        pass
    here = os.path.realpath(cwd)
    while True:
        candidate = os.path.join(here, MARKER_FILE)
        if os.path.isfile(candidate):
            try:
                with open(candidate, "r", encoding="utf-8") as handle:
                    pid = str(json.load(handle).get("project_id", "")).strip()
                if _PROJECT_ID_RE.match(pid):
                    return pid
            except (OSError, ValueError):
                pass
            return ""
        if here == top or os.path.dirname(here) == here:
            return ""
        here = os.path.dirname(here)


def project_id_for(cwd):
    """Project identifier: repo marker, else git remote name, else directory
    name. Mirrors the Project Identification Algorithm in MEMORY-RULES.md."""
    pid = _marker_project_id(cwd)
    if pid:
        return pid
    try:
        remote = subprocess.run(["git", "-C", cwd, "remote", "get-url", "origin"],
                                capture_output=True, text=True, timeout=3)
        if remote.returncode == 0 and remote.stdout.strip():
            name = remote.stdout.strip().rstrip("/").rsplit("/", 1)[-1]
            if name.endswith(".git"):
                name = name[:-4]
            if name:
                return name
    except Exception:
        pass
    return os.path.basename(os.path.normpath(cwd)) or "default-project"


def _nested(a, b):
    a, b = os.path.realpath(a), os.path.realpath(b)
    try:
        return os.path.commonpath([a, b]) in (a, b)
    except ValueError:
        return False


def team_root():
    """team_memory_path, or "" when unset or nested with memory_path."""
    team = os.path.expanduser((opt("TEAM_MEMORY_PATH") or "").strip())
    if not team:
        return ""
    private = os.path.expanduser((opt("MEMORY_PATH") or "").strip())
    if private and _nested(private, team):
        return ""
    return team


def private_kg_configured():
    return bool((opt("KG_PRIVATE_MCP_URL") or "").strip())


def team_tier_active():
    return bool(team_root()) or private_kg_configured()
```

Then in `memory-backup.py`: delete the local `project_id_for` (lines 52–70) and change the import to `from hook_common import is_true, opt, project_id_for`.

- [ ] **Step 4: Run tests** — `python3 claude-code/tests/test_plugin.py` → all pass (existing backup tests still green: git-remote and directory fallbacks unchanged).

- [ ] **Step 5: Commit**

```bash
git add claude-code/hooks/hook_common.py claude-code/hooks/memory-backup.py claude-code/tests/test_plugin.py
git commit -m "feat(plugin): .agentic-rules.json project marker; team_root/private_kg helpers (#<N>)"
```

---

### Task 4: Plugin options and the `kg-private` MCP server

**Files:**
- Modify: `claude-code/.claude-plugin/plugin.json` (userConfig)
- Modify: `claude-code/.mcp.json`
- Modify: `claude-code/tests/test_plugin.py` (`EXPECTED_USER_CONFIG`, new tests)
- Modify: `docs/CLAUDE_CODE_PLUGIN.md` "Settings reference" table (the test `docs_settings_table_matches_manifest` requires it)

**Interfaces:**
- Produces: options `team_memory_path` (type `directory`), `kg_private_mcp_url` (type `string`, default `""`); server `kg-private` with `url: ${user_config.kg_private_mcp_url}`.

- [ ] **Step 1: Write the failing tests**

```python
@test
def manifest_declares_team_tier_options():
    uc = load_json("claude-code/.claude-plugin/plugin.json")["userConfig"]
    assert uc["team_memory_path"]["type"] == "directory"
    assert uc["team_memory_path"].get("required") is False
    assert uc["kg_private_mcp_url"]["type"] == "string" and uc["kg_private_mcp_url"]["default"] == ""


@test
def mcp_config_declares_private_server():
    servers = load_json("claude-code/.mcp.json")["mcpServers"]
    assert servers["kg-dgx"]["url"] == "${user_config.kg_mcp_url}"
    assert servers["kg-private"] == {"type": "http", "url": "${user_config.kg_private_mcp_url}"}
```

Add `"team_memory_path"` and `"kg_private_mcp_url"` to `EXPECTED_USER_CONFIG`.

- [ ] **Step 2: Run to verify they fail** — `python3 claude-code/tests/test_plugin.py` → `manifest_declares_team_tier_options`, `mcp_config_declares_private_server`, and `hook_consumes_only_declared_settings`/`docs_settings_table_matches_manifest` fail.

- [ ] **Step 3: Edit `plugin.json`** — insert after `kg_mcp_url`:

```json
    "kg_private_mcp_url": {
      "type": "string",
      "title": "Private Knowledge Graph MCP endpoint",
      "description": "HTTP URL of a KG daemon that stays on your own machine (e.g. http://127.0.0.1:8121/mcp). When set, kg_mcp_url is treated as the TEAM graph and the privacy gate guards writes to it. Leave blank for a single-graph setup.",
      "default": ""
    },
    "team_memory_path": {
      "type": "directory",
      "title": "Team memory root path",
      "description": "Root of the team-shared memory store (typically a clone of your team's memory repo). Recall reads it alongside memory_path; only team-eligible project knowledge with `audience: team` may be written there — the privacy gate enforces this. Leave blank for no team tier.",
      "required": false
    }
```

Edit `.mcp.json`:

```json
{
  "_comment": "The plugin's standard MCP config (plugin root is claude-code/, so this auto-loads). URLs are supplied at enable time via the kg_mcp_url / kg_private_mcp_url userConfig options; a blank URL makes that server unreachable and the memory/RAG skills run without it, by design. kg-dgx keeps its historical name so existing permission allowlists keep working; when kg_private_mcp_url is also set, kg-dgx is the TEAM graph and kg-private the member's own. This is NOT the repo-root .mcp.json (that one is internal dev config and never ships with the plugin).",
  "mcpServers": {
    "kg-dgx": { "type": "http", "url": "${user_config.kg_mcp_url}" },
    "kg-private": { "type": "http", "url": "${user_config.kg_private_mcp_url}" }
  }
}
```

Add two rows to the Settings reference table in `docs/CLAUDE_CODE_PLUGIN.md` (same column layout as the existing rows):

```
| `kg_private_mcp_url` | string | `""` | URL of a KG daemon on your own machine. When set, `kg_mcp_url` is the team graph and the privacy gate guards writes to it. |
| `team_memory_path` | directory | unset | Team-shared memory root (a clone of the team memory repo). Read alongside `memory_path`; writes are gated. |
```

- [ ] **Step 4: Run tests** — all pass. Also `claude plugin validate claude-code` if the CLI is present (test does this).

- [ ] **Step 5: Commit**

```bash
git add claude-code/.claude-plugin/plugin.json claude-code/.mcp.json claude-code/tests/test_plugin.py docs/CLAUDE_CODE_PLUGIN.md
git commit -m "feat(plugin): team_memory_path + kg_private_mcp_url options; kg-private MCP server (#<N>)"
```

---

### Task 5: Session-start preamble for the team tier (legacy output byte-identical)

**Files:**
- Modify: `claude-code/hooks/session-start.py:97-109,188-189`
- Test: `claude-code/tests/test_plugin.py`

**Interfaces:**
- Consumes: `hook_common.team_root()`, `private_kg_configured()`.
- Produces: `activation_preamble(kg_configured, memory_path="", team_root="", private_kg=False)`; new paragraphs `_PREAMBLE_TEAM_ROOT(team)`, `_PREAMBLE_TWO_KGS`, `_PREAMBLE_TEAM_DISABLED_NESTED`.

- [ ] **Step 1: Write the failing tests**

```python
@test
def preamble_legacy_config_is_byte_identical_to_1_6_0():
    """No team option set → preamble must not change at all."""
    base = injected_context({"memory_path": "/tmp/store", "kg_mcp_url": "http://x/mcp"})
    assert "Team tier" not in base and "kg-private" not in base
    again = injected_context({"memory_path": "/tmp/store", "kg_mcp_url": "http://x/mcp",
                              "team_memory_path": "", "kg_private_mcp_url": ""})
    assert base == again


@test
def preamble_names_team_root_and_routing():
    ctx = injected_context({"memory_path": "/tmp/p", "team_memory_path": "/tmp/t"})
    assert "**Team tier.**" in ctx and "`/tmp/t`" in ctx
    assert "audience: team" in ctx and "never" in ctx.lower()


@test
def preamble_two_graphs_when_private_kg_set():
    ctx = injected_context({"kg_mcp_url": "http://team/u/me/mcp", "kg_private_mcp_url": "http://127.0.0.1:8121/mcp"})
    assert "**Two knowledge graphs.**" in ctx
    assert "kg-private" in ctx and "kg-dgx" in ctx


@test
def preamble_warns_when_roots_nest():
    ctx = injected_context({"memory_path": "/tmp/p", "team_memory_path": "/tmp/p/team"})
    assert "**Team tier disabled**" in ctx and "nest" in ctx
```

- [ ] **Step 2: Run to verify they fail** — `python3 claude-code/tests/test_plugin.py` → the three team tests fail; the legacy test passes (nothing changed yet).

- [ ] **Step 3: Implement** — add after `_PREAMBLE_KG_OPTIONAL`:

```python
def _preamble_team_root(team):
    return (
        f"**Team tier.** A team memory root is configured (`{team}`), shared with "
        "teammates through git. *Recall* reads both roots. *Write* there only "
        "team-eligible project knowledge — categories technical, contextual, topic, "
        "git_history, knowledge_graph — with `audience: team` in the frontmatter, and "
        "only when it is about the shared project rather than the user. Never write "
        "preferences, credentials, sessions, interaction logs, machine paths, hostnames "
        "or private addresses there; a privacy gate blocks such writes. Everything else "
        "stays in the private root by default.\n\n"
    )


_PREAMBLE_TEAM_DISABLED_NESTED = (
    "**Team tier disabled:** `team_memory_path` and `memory_path` nest inside each "
    "other, which the framework refuses. Treat the team root as unset until the "
    "configuration is fixed.\n\n"
)

_PREAMBLE_TWO_KGS = (
    "**Two knowledge graphs.** `kg-private` is your own graph; `kg-dgx` is the team "
    "graph. Before non-trivial work call `kg_context` on both. Write to `kg-private` "
    "by default; write to the team graph only project knowledge a teammate would need, "
    "never personal or machine-specific facts — the team daemon rejects private "
    "patterns and out-of-scope nodes, and never link nodes across the two graphs.\n\n"
)


def activation_preamble(kg_configured, memory_path="", team_root="", private_kg=False,
                        team_nested=False):
    mp = (memory_path or "").strip()
    store = (
        f"the configured memory root `{mp}`" if mp
        else "your configured memory root, or — if none is configured — Claude "
             "Code's project memory directory, structured per the rules below"
    )
    kg = _PREAMBLE_KG_CONFIGURED if kg_configured else _PREAMBLE_KG_OPTIONAL
    extra = ""
    if team_nested:
        extra += _PREAMBLE_TEAM_DISABLED_NESTED
    elif team_root:
        extra += _preamble_team_root(team_root)
    if private_kg and kg_configured:
        extra += _PREAMBLE_TWO_KGS
    return _preamble_head(store) + kg + extra + "---\n\n"
```

and in `main()` replace the `context = …` line with:

```python
    team = team_root()
    raw_team = (opt("TEAM_MEMORY_PATH") or "").strip()
    context = activation_preamble(
        kg_configured, opt("MEMORY_PATH"),
        team_root=team, private_kg=private_kg_configured(),
        team_nested=bool(raw_team) and not team,
    ) + "\n\n---\n\n".join(sections)
```

with the import line `from hook_common import is_true, opt, private_kg_configured, team_root`.

- [ ] **Step 4: Run tests** — all pass, including `preamble_legacy_config_is_byte_identical_to_1_6_0`.

- [ ] **Step 5: Commit**

```bash
git add claude-code/hooks/session-start.py claude-code/tests/test_plugin.py
git commit -m "feat(plugin): preamble routes between private and team tiers when configured (#<N>)"
```

---

### Task 6: PreToolUse privacy-gate hook (L1)

**Files:**
- Create: `claude-code/hooks/privacy-gate-hook.py`
- Modify: `claude-code/hooks/hooks.json` (add `PreToolUse`)
- Test: `claude-code/tests/test_plugin.py`

**Interfaces:**
- Consumes: `tools/privacy_gate.py` via `${CLAUDE_PLUGIN_ROOT}/tools` — **ship it**: add a symlink `claude-code/tools -> ../tools` (same pattern as `claude-code/modules -> ../modules`, which the injector already relies on) and a symlink `claude-code/settings -> ../settings`? No — keep one: the hook loads patterns from `${CLAUDE_PLUGIN_ROOT}/tools/../settings/privacy-gate.json` only if that resolves; the symlinked `tools` dir resolves to the repo `tools/`, whose parent is the repo root, so `settings/privacy-gate.json` resolves in-repo. In the installed plugin cache the symlinked tree is materialized under `claude-code/tools/`, whose parent is the plugin root — so also add `claude-code/settings -> ../settings`. Two symlinks, both materialized on install.
- Produces: stdout JSON `{"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "allow"|"deny"|"ask", "permissionDecisionReason": "<redacted reason>"}}`; audit lines appended to `<memory_path>/private/gate-log/YYYY-MM-DD.jsonl` on deny/ask.

- [ ] **Step 1: Create the symlinks**

```bash
cd claude-code && ln -s ../tools tools && ln -s ../settings settings && cd ..
git add claude-code/tools claude-code/settings
```

- [ ] **Step 2: Write the failing tests**

```python
GATE_HOOK = os.path.join(PLUGIN, "hooks", "privacy-gate-hook.py")

def run_gate(options, payload, plugin_root=PLUGIN):
    env = {k: v for k, v in os.environ.items() if not k.startswith("CLAUDE_PLUGIN_")}
    env["CLAUDE_PLUGIN_ROOT"] = plugin_root
    for key, value in options.items():
        env["CLAUDE_PLUGIN_OPTION_" + key.upper()] = value
    proc = subprocess.run([sys.executable, GATE_HOOK], input=json.dumps(payload), env=env,
                          capture_output=True, text=True, timeout=30)
    assert proc.returncode == 0, proc.stderr
    return json.loads(proc.stdout)["hookSpecificOutput"] if proc.stdout.strip() else None

TEAM = {"memory_path": "/tmp/p", "team_memory_path": "/tmp/t",
        "kg_mcp_url": "http://team/u/me/mcp", "kg_private_mcp_url": "http://127.0.0.1:8121/mcp"}
KG_ADD = "mcp__plugin_agentic-rules_kg-dgx__kg_add"

@test
def gate_inactive_without_team_tier():
    out = run_gate({"memory_path": "/tmp/p", "kg_mcp_url": "http://x/mcp"},
                   {"tool_name": KG_ADD, "tool_input": {"id": "a", "type": "fact", "title": "t", "content": "AKIAABCDEFGHIJKLMNOP"}})
    assert out is None  # no output → Claude Code proceeds normally

@test
def gate_denies_secret_to_team_kg():
    out = run_gate(TEAM, {"tool_name": KG_ADD, "tool_input": {"id": "a", "type": "fact", "title": "t",
                          "content": "key AKIAABCDEFGHIJKLMNOP", "scope": "project:x"}})
    assert out["permissionDecision"] == "deny"
    assert "secret-aws-access-key" in out["permissionDecisionReason"]
    assert "AKIAABCDEFGHIJKLMNOP" not in out["permissionDecisionReason"]

@test
def gate_asks_on_heuristic_to_team_kg():
    out = run_gate(TEAM, {"tool_name": KG_ADD, "tool_input": {"id": "a", "type": "fact", "title": "t", "content": "ping a@example.org"}})
    assert out["permissionDecision"] == "ask"

@test
def gate_allows_clean_team_write_silently():
    out = run_gate(TEAM, {"tool_name": KG_ADD, "tool_input": {"id": "a", "type": "fact", "title": "t", "content": "run make test first"}})
    assert out is None

@test
def gate_ignores_private_kg_writes():
    out = run_gate(TEAM, {"tool_name": "mcp__plugin_agentic-rules_kg-private__kg_add",
                          "tool_input": {"id": "a", "type": "fact", "title": "t", "content": "AKIAABCDEFGHIJKLMNOP"}})
    assert out is None

@test
def gate_denies_team_file_without_audience_and_secret_content():
    out = run_gate(TEAM, {"tool_name": "Write", "tool_input": {"file_path": "/tmp/t/projects/x/technical/a.md",
                          "content": "---\naudience: private\n---\nnote"}})
    assert out["permissionDecision"] == "deny" and "audience: team" in out["permissionDecisionReason"]
    out = run_gate(TEAM, {"tool_name": "Write", "tool_input": {"file_path": "/tmp/t/projects/x/technical/a.md",
                          "content": "---\naudience: team\n---\nsee /Users/alice/x"}})
    assert out["permissionDecision"] == "deny" and "path-home-unix" in out["permissionDecisionReason"]

@test
def gate_denies_ineligible_category_in_team_root():
    out = run_gate(TEAM, {"tool_name": "Write", "tool_input": {"file_path": "/tmp/t/projects/x/credentials/a.md",
                          "content": "---\naudience: team\n---\nx"}})
    assert out["permissionDecision"] == "deny" and "not team-eligible" in out["permissionDecisionReason"]

@test
def gate_ignores_writes_outside_team_root():
    out = run_gate(TEAM, {"tool_name": "Write", "tool_input": {"file_path": "/tmp/p/private/x.md", "content": "AKIAABCDEFGHIJKLMNOP"}})
    assert out is None

@test
def gate_denies_bash_copy_from_private_into_team_root():
    for cmd in ["cp /tmp/p/private/notes.md /tmp/t/projects/x/technical/",
                "rsync -a /tmp/p/ /tmp/t/",
                "cat ~/.claude/CLAUDE.md > /tmp/t/rules/global.md"]:
        out = run_gate(TEAM, {"tool_name": "Bash", "tool_input": {"command": cmd}})
        assert out and out["permissionDecision"] == "deny", cmd
    out = run_gate(TEAM, {"tool_name": "Bash", "tool_input": {"command": "ls /tmp/t"}})
    assert out is None

@test
def gate_writes_audit_line_without_matched_text():
    with tempfile.TemporaryDirectory() as tmp:
        opts = dict(TEAM, memory_path=tmp)
        run_gate(opts, {"tool_name": KG_ADD, "tool_input": {"id": "a", "type": "fact", "title": "t", "content": "AKIAABCDEFGHIJKLMNOP"}})
        logs = os.listdir(os.path.join(tmp, "private", "gate-log"))
        assert len(logs) == 1
        with open(os.path.join(tmp, "private", "gate-log", logs[0]), encoding="utf-8") as h:
            body = h.read()
        assert "secret-aws-access-key" in body and "AKIAABCDEFGHIJKLMNOP" not in body

@test
def gate_hook_registered_for_pretooluse():
    hooks = load_json("claude-code/hooks/hooks.json")["hooks"]
    entry = hooks["PreToolUse"][0]
    assert "privacy-gate-hook.py" in entry["hooks"][0]["command"]
    assert re.search(r"kg_add|Write|Bash", entry["matcher"])

@test
def gate_reports_ask_on_internal_error():
    out = run_gate(TEAM, {"tool_name": KG_ADD, "tool_input": "not-a-dict"})
    assert out["permissionDecision"] == "ask" and "gate error" in out["permissionDecisionReason"]
```

- [ ] **Step 3: Run to verify they fail** — `python3 claude-code/tests/test_plugin.py` → all `gate_*` tests fail (hook missing).

- [ ] **Step 4: Write the hook**

```python
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
FILE_TOOLS = {"Write", "Edit", "MultiEdit"}
COPY_VERB_RE = re.compile(r"\b(cp|rsync|mv|tee|install|git\s+add)\b|>\s*\S")
PRIVATE_SRC_MARKERS = ("/private/", "/.claude/", "~/.claude")


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
    except OSError:
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
        text = "\n".join(str(inp.get(k, "")) for k in ("id", "title", "content", "tags", "source", "source_id", "target_id"))
        f = pg.scan_text(text, patterns, allow, terms, path=name)
        return pg.verdict(f), _findings_to_reason(f), name

    if name in FILE_TOOLS and team:
        path = str(inp.get("file_path", ""))
        if path and _within(team, path):
            text = str(inp.get("content", inp.get("new_string", "")))
            rel = os.path.relpath(os.path.realpath(os.path.expanduser(path)), os.path.realpath(team))
            errors = pg.check_team_file(rel, text) if name == "Write" else []
            f = pg.scan_text(text, patterns, allow, terms, path=rel)
            code = pg.verdict(f)
            if errors:
                code = 2
            return code, _findings_to_reason(f, errors), rel

    if name == "Bash" and team:
        cmd = str(inp.get("command", ""))
        team_hit = team in cmd or os.path.realpath(team) in cmd
        src_hit = (mp and mp in cmd) or any(m in cmd for m in PRIVATE_SRC_MARKERS)
        if team_hit and src_hit and COPY_VERB_RE.search(cmd):
            return 2, "privacy gate: copying from a private location into the team root is blocked", "Bash"

    return 0, "", name


def main():
    if not team_tier_active() or pg is None:
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
    _audit({"ts": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "decision": decision, "target": target, "reason": reason})
    _out(decision, reason)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        _out("ask", f"privacy gate error: {type(exc).__name__}")
```

Note for the `gate_reports_ask_on_internal_error` test: `decide()` raises on a non-dict `tool_input`, which `main()` converts to `ask` — the test payload is an intentionally bad shape.

Register in `hooks.json` (add a top-level key next to `SessionStart`):

```json
    "PreToolUse": [
      {
        "matcher": "mcp__.*kg-dgx__kg_(add|link)|Write|Edit|MultiEdit|Bash",
        "hooks": [
          {
            "type": "command",
            "command": "sh -c 't=\"${CLAUDE_PLUGIN_OPTION_TEAM_MEMORY_PATH:-${CLAUDE_PLUGIN_OPTION_team_memory_path:-}}\"; k=\"${CLAUDE_PLUGIN_OPTION_KG_PRIVATE_MCP_URL:-${CLAUDE_PLUGIN_OPTION_kg_private_mcp_url:-}}\"; [ -z \"$t\" ] && [ -z \"$k\" ] && exit 0; exec python3 \"${CLAUDE_PLUGIN_ROOT}/hooks/privacy-gate-hook.py\"'"
          }
        ]
      }
    ],
```

and extend the `_comment` with one sentence: "PreToolUse runs privacy-gate-hook.py only when a team tier is configured (team_memory_path or kg_private_mcp_url) — the shell guard keeps single-tier installs at zero cost."

- [ ] **Step 5: Run tests** — `python3 claude-code/tests/test_plugin.py` → all pass, including `hooks_config_valid` (adjust its expected event set if it enumerates events) and `hook_consumes_only_declared_settings` (the hook reads only declared options).

- [ ] **Step 6: Commit**

```bash
git add claude-code/hooks/privacy-gate-hook.py claude-code/hooks/hooks.json claude-code/tools claude-code/settings claude-code/tests/test_plugin.py
git commit -m "feat(plugin): PreToolUse privacy gate for team-bound writes (#<N>)"
```

---

### Task 7: Settings schema — `team_eligible`, `storage`, marker-first identification

**Files:**
- Modify: `modules/memory-rules/settings.json`
- Regenerate: `web-config.json`, `setup.html` (via `generate_simple_setup.py`, `update_localization.py`)
- Test: `validate.py`, `test/dogfood.sh`

**Interfaces:**
- Produces: `memory_rules.storage = {"base_path": "", "team_base_path": ""}`; `memory_rules.categories.<c>.team_eligible: bool`; `memory_rules.project_support.project_identification_method = "marker_then_git_remote_or_directory_name"`.

- [ ] **Step 1: Edit `settings.json`** with a script (keeps ordering deterministic):

```bash
python3 - <<'PY'
import json, collections
p='modules/memory-rules/settings.json'
d=json.load(open(p), object_pairs_hook=collections.OrderedDict)
m=d['memory_rules']
m['project_support']['project_identification_method']='marker_then_git_remote_or_directory_name'
m['project_support']['project_marker_file']='.agentic-rules.json'
elig={'technical','contextual','topic','git_history','knowledge_graph'}
for name,cat in m['categories'].items():
    cat['team_eligible']= name in elig
storage=collections.OrderedDict([('base_path',''),('team_base_path','')])
# insert storage right after 'categories' to keep the file readable
items=list(m.items()); out=collections.OrderedDict()
for k,v in items:
    out[k]=v
    if k=='categories': out['storage']=storage
d['memory_rules']=out
json.dump(d,open(p,'w'),indent=2,ensure_ascii=False); open(p,'a').write('\n')
PY
```

- [ ] **Step 2: Regenerate and validate**

```bash
python3 generate_simple_setup.py && python3 update_localization.py && python3 validate.py
```

Expected: `validate.py` reports all OK (version fields still agree at 1.6.0 for now; generated artifacts fresh).

- [ ] **Step 3: Run the clean-room check** — `bash test/dogfood.sh` → all checks pass (regeneration is a no-op).

- [ ] **Step 4: Commit**

```bash
git add modules/memory-rules/settings.json web-config.json setup.html
git commit -m "feat(memory-rules): team_eligible categories, storage.team_base_path, marker-first project id (#<N>)"
```

---

### Task 8: Rule text — memory-rules and rag-rules (en/ja/id) + deep docs

**Files:**
- Modify: `modules/memory-rules/RULES.md.en`, `RULES.md.ja`, `RULES.md.id`
- Modify: `modules/rag-rules/RULES.md.en`, `RULES.md.ja`, `RULES.md.id`
- Modify: `modules/memory-rules/MEMORY-RULES.md` (§Project Identification Algorithm, §Memory Routing Algorithm, new §Team Tier and Audience, new §Privacy Gate)
- Modify: `modules/rag-rules/RAG-RULES.md` (new §Team KG daemon contract)
- Regenerate: `web-config.json`, `setup.html`

**Interfaces:** none (text). The ja/id files mirror the en structure with bilingual headings (`### アルゴリズム: X / Algorithm: X`), matching the existing convention.

- [ ] **Step 1: memory-rules `RULES.md.en`** — after `## Memory System Architecture` add the team root line, and after `Memory_Retrieval_Process` add two algorithms:

```markdown
## Memory System Architecture
- **common/**: Shared knowledge across projects
- **private/**: Personal/sensitive data (credentials, preferences)
- **project/**: Project-specific memory and context
- **team root** (optional, `storage.team_base_path`): a second root shared with teammates through git — `common/` and `projects/<id>/` only, never `private/`. Every file there carries `audience: team`.

### Algorithm: Team_Memory_Routing
**WHEN**: storage.team_base_path is set and a memory is about to be stored

**Steps**:
1. Default audience is **private** — route to the private root unless every check below passes
2. Category must be team-eligible (`categories.<name>.team_eligible = true`: technical, contextual, topic, git_history, knowledge_graph); behavioral, personal, credentials, sensitive, session, user_interaction, backup are never team
3. Content must be about the shared project, not the user; contain no credentials, machine paths, hostnames, private addresses, or personal identifiers
4. The user asked for it to be shared, or the content is a project decision/gotcha/procedure a teammate needs
5. Write under the team root at `projects/<project-id>/<category>/` (or `common/technical/`) with frontmatter `audience: team`; a privacy gate blocks writes that fail steps 2–3
6. Recall reads both roots; on conflict prefer the team root for project facts and the private root for user facts

### Algorithm: Project_Identification
**WHEN**: a project id is needed for routing or KG scope

**Steps**:
1. If `.agentic-rules.json` exists at the repository root, use its `project_id` — all clones of a project (internal, public, forks) must agree
2. Else derive from the git remote name, else the directory name
3. KG scope is always `project:<project_id>`
```

Update the First-Run marker version in step 5 to `1.7.0` (Task 9 does the sweep; do it here too so the file is consistent when committed).

- [ ] **Step 2: memory-rules `RULES.md.ja` / `RULES.md.id`** — add the same three blocks, bilingual headings, e.g. `### アルゴリズム: Team_Memory_Routing / Algorithm: Team_Memory_Routing` and `### Algoritma: Team_Memory_Routing / Algorithm: Team_Memory_Routing`, translating the step text and keeping identifiers (`audience: team`, category names, file names) verbatim.

- [ ] **Step 3: rag-rules `RULES.md.{en,ja,id}`** — in `Knowledge_Graph_Query_Enhancement` add step `1b.` and in `Runtime_Knowledge_Graph_Generation` add a step after 6:

```markdown
1b. If two KG servers are configured (a private one and a team one), query both and merge; prefer the team graph for project-scoped facts and the private graph for user facts
```

```markdown
7. Write new nodes to the private KG by default; write to the team KG only project knowledge a teammate would need (a team daemon enforces a scope allowlist and a privacy gate and rejects other writes); never create edges between the two graphs
```

- [ ] **Step 4: `MEMORY-RULES.md`** — replace the Project Identification Algorithm with:

```markdown
### Project Identification Algorithm
1. **Marker Check**: If `.agentic-rules.json` exists at the repository root and contains a valid `project_id` (`^[A-Za-z0-9][A-Za-z0-9._-]{0,63}$`), use it — this is what keeps internal and public clones of one project on the same id
2. **Git Remote Check**: Else extract the project identifier from the git remote URL (last path segment, `.git` stripped)
3. **Directory Name Fallback**: Else use the current directory name
4. **Validation**: Reject ids containing path separators or `..`
5. **Registration**: Register the project in the global memory index; KG scope is `project:<project_id>`
```

Add to the Memory Routing Algorithm step 5 a bullet: `- If storage.team_base_path is set and the category has team_eligible: true and the content passes the Team Memory Routing checks: route to [storage.team_base_path]/projects/[project-id]/[category]/ with frontmatter audience: team`. Add a new section before `## Settings Configuration`:

```markdown
## Team Tier, Audience Metadata and the Privacy Gate

Two tiers may exist: the member-private store (`storage.base_path`) and an optional team store (`storage.team_base_path`, a git clone shared by the team). Every memory file carries `audience: private | team` in its frontmatter (default `private`); files under the team root must carry `audience: team`, and only categories with `team_eligible: true` may appear there.

A privacy gate enforces the boundary in code (`tools/privacy_gate.py`, patterns in `settings/privacy-gate.json`): definite private shapes (keys, tokens, private-key blocks, private IPv4 ranges, mesh-VPN hostnames, home directories) are denied; heuristics (emails, phone numbers, the member's own private terms from `private/gate-terms.txt`) ask. The gate runs as a platform hook before team-bound writes, as a pre-commit and CI check in the team repository, and inside a team KG daemon. It never prints matched text. False positives go in the team repository's `settings/allowlist.txt` (pattern id or literal). Blocks and overrides are logged to `private/gate-log/` in the private store.
```

- [ ] **Step 5: `RAG-RULES.md`** — add before the last section:

```markdown
## Team Knowledge Graph Daemon Contract

Any KG server implementing this framework's seven tools may run as a *team* daemon. In that mode it must: (1) record an `owner` per node, taken from the member segment of the request path `/u/<member>/mcp` (or a configured default for legacy clients); (2) reject writes whose `scope` is outside a configured allowlist; (3) run the framework privacy-gate scanner over every `kg_add`/`kg_link` payload and reject on a deny finding, returning pattern ids only; (4) reject **all** writes if the gate is configured but its pattern file is unavailable (fail closed). Members run their own private daemon (no gate, no owner routing) on their own machine; a private daemon may protect its endpoint with a secret path prefix.
```

- [ ] **Step 6: Regenerate, validate, test**

```bash
python3 generate_simple_setup.py && python3 update_localization.py && python3 validate.py && python3 claude-code/tests/test_plugin.py && bash test/dogfood.sh
```

Expected: all green. `injected_text_strips_template_scaffolding` still passes; `setting_language_switches_source` still passes (ja/id files have distinct headings).

- [ ] **Step 7: Commit**

```bash
git add modules/memory-rules modules/rag-rules web-config.json setup.html
git commit -m "docs(rules): team tier routing, marker-first project id, two-graph recall, gate + team daemon contract (en/ja/id) (#<N>)"
```

---

### Task 9: Version 1.7.0, CHANGELOG, docs index, user docs

**Files:**
- Modify: `plugins.json`, `bootstrap.json`, `web-config.json` (regen), `settings/global-settings.json` (2 fields), `settings/cursor-2.0-multi-agent-adapter.json`, `modules/*/settings.json` (4), `claude-code/.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`
- Modify: literal `1.6.0` in `modules/*/RULES.md.{en,ja,id}` First-Run marker JSON and in `README.md` example / `MEMORY-RULES.md` example (`check_module_content_versions`)
- Modify: `docs/CHANGELOG.md`, `docs/INDEX.md`, `docs/CLAUDE_CODE_PLUGIN.md` (§Memory store and Knowledge Graph), `docs/KG_IMPLEMENTATION_GUIDE.md` (link to the team daemon contract), `README.md` (one paragraph under the memory section pointing at `docs/TEAM_TIERS_SETUP.md`)

- [ ] **Step 1: Sweep the version**

```bash
grep -rl --exclude-dir=.git --exclude-dir=__pycache__ '1\.6\.0' . | grep -v -E 'CHANGELOG|superpowers' 
# review the list, then:
grep -rl --exclude-dir=.git --exclude-dir=__pycache__ '1\.6\.0' . | grep -v -E 'CHANGELOG|superpowers' | xargs sed -i '' 's/1\.6\.0/1.7.0/g'
python3 generate_simple_setup.py && python3 update_localization.py && python3 validate.py
```

Expected: `validate.py` → "All N version fields agree: 1.7.0" and module content versions OK.

- [ ] **Step 2: CHANGELOG entry** (top of `docs/CHANGELOG.md`):

```markdown
## [1.7.0] - <date>

### Added

- **Team tier.** Optional `team_memory_path` (a git-shared memory root with `common/` and `projects/<id>/`, every file tagged `audience: team`) and `kg_private_mcp_url` (a second, member-private KG daemon; when set, `kg_mcp_url` is the team graph). A 1.6.0 configuration is unaffected — the injected preamble is byte-identical when neither option is set. Design: `docs/superpowers/specs/2026-08-27-team-tiers-privacy-gate-design.md`; manual: `docs/TEAM_TIERS_SETUP.md`.
- **Privacy gate.** `tools/privacy_gate.py` + `settings/privacy-gate.json` — a stdlib scanner (deny: keys/tokens/private-key blocks, private IPv4 ranges, mesh-VPN hostnames, home directories; ask: emails, phones, the member's private terms) wired as a `PreToolUse` hook for team-bound writes, and reusable as a pre-commit/CI check for team repositories and inside a team KG daemon (contract in `RAG-RULES.md`). Never prints matched text.
- **Project identity marker.** `.agentic-rules.json` `{"project_id": …}` at the repo root now wins over the git-remote/directory heuristic, so internal and public clones of one project share memory dir and KG scope. The native-memory backup hook honors it.
- `team_eligible` per memory category; `storage.team_base_path`; new memory-rules algorithms `Team_Memory_Routing` and `Project_Identification`; two-graph recall in rag-rules.

### Changed

- Claude Code project config guidance: keep the team layer (`.claude/CLAUDE.md`, `settings.json`, skills/commands/agents) in the project repo and the private layer (`settings.local.json`, `CLAUDE.local.md`, `local-*` prefixed skills/commands/agents) gitignored — see `docs/TEAM_TIERS_SETUP.md` §3.
```

- [ ] **Step 3: Docs** — `docs/INDEX.md`: add `- **[TEAM_TIERS_SETUP.md](TEAM_TIERS_SETUP.md)** - Team-shared vs member-private memory/KG: setup, upgrade, gate` under User Guides. `docs/CLAUDE_CODE_PLUGIN.md` §Memory store and Knowledge Graph: add a short "Team tier" subsection (options, two server names, gate hook, link to the manual). `docs/KG_IMPLEMENTATION_GUIDE.md`: add a "Team daemon" pointer to `RAG-RULES.md` contract. `README.md`: one paragraph.

- [ ] **Step 4: Full verification**

```bash
python3 tools/tests/test_privacy_gate.py && python3 claude-code/tests/test_plugin.py && python3 validate.py && bash test/dogfood.sh
```

Expected: all green.

- [ ] **Step 5: Commit**

```bash
git add -A -- plugins.json bootstrap.json web-config.json setup.html settings modules claude-code/.claude-plugin/plugin.json .claude-plugin/marketplace.json README.md docs
git commit -m "chore(release): 1.7.0 — team tiers, privacy gate, project marker (#<N>)"
```

---

### Task 10: End-to-end plugin test and issue report

**Files:** none (verification).

- [ ] **Step 1: Sandbox install from this worktree** (interactive session; approve the scoped probes when asked): dispatch the `plugin-tester` agent per `.claude/CLAUDE.md`. It installs from committed `HEAD` of the worktree in an isolated `CLAUDE_CONFIG_DIR`. Add to its brief: "also configure `team_memory_path` to a temp git repo with the pre-commit gate installed and `kg_private_mcp_url`/`kg_mcp_url` to two local daemons (see runbook Part B) and exercise: gate deny on a planted key, ask on an email, allow on clean; recall from both roots; en/ja/id."

Expected: pass matrix with no regressions on the 1.6.0 cases.

- [ ] **Step 2: Legacy parity** — in the sandbox, install with only `memory_path` + `kg_mcp_url` and diff the injected context against a 1.6.0 install of the same options: identical.

- [ ] **Step 3: Update the issue** with the implementation report (what shipped, files, tests, verification evidence) and self-reflection (deviations from this plan), per the issue-driven rule. Do not close until the operator has reviewed.

- [ ] **Step 4: Stop.** Pushing `feat/team-tiers` to the internal remote and opening the internal PR needs the operator's explicit go-ahead; the public release goes through `/publish` later.

---

## Self-review

- **Spec coverage:** §3.4 marker → Task 3/7/8; §4 roots/layout/metadata/routing → Tasks 4/5/7/8; §4.5 backup invariant → unchanged code + Task 3 tests; §5.1 options/servers → Task 4; §5.2 team daemon contract → Task 8 (`RAG-RULES.md`) + separate server plan; §5.4 rules text → Task 8; §6.1 L1 → Task 6; §6.2 scanner → Tasks 1–2; §6.3 pre-commit/CI wiring → scanner `staged` mode (Task 2) + operator runbook; §6.4 invariants 1 (backup), 3 (no matched text), 4 (nesting) → Tasks 3/1/5–6; invariant 2 (daemon fail-closed) → server plan; §7 layering → docs (Task 9) + operator runbook; §8 file list → Tasks 4–9; §9 compat → Task 5 byte-identical test + Task 6 inactive test; §12 tests → Tasks 1–10.
- **Placeholders:** none; every code step has code. `#<N>` is the issue number from Task 0.
- **Type consistency:** `Finding(pattern_id, severity, path, line)` used identically in Tasks 1, 2, 6; `team_root()` / `private_kg_configured()` / `team_tier_active()` names identical in Tasks 3, 5, 6; option env names `CLAUDE_PLUGIN_OPTION_TEAM_MEMORY_PATH` / `_KG_PRIVATE_MCP_URL` identical in Tasks 3–6.
