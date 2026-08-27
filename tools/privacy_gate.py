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
