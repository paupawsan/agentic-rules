#!/usr/bin/env bash
#
# Clean-room dogfood test for the Agentic Rules Framework.
#
# Verifies, in an isolated environment, the things that break for real users
# before a public push:
#   1. Scripts run on a stock Python 3 with no third-party packages.
#   2. validate.py (the consistency gate) passes.
#   3. Generated artifacts (web-config.json, setup.html) are not stale —
#      regenerating them produces no change vs. what is committed.
#   4. A fresh user can run setup.py non-interactively and get a rule file.
#   5. The v1.4.0 project-local marker model is consistent (no file still
#      instructs the old framework-local marker check).
#   6. The plugin scaffolder's CLI is usable.
#
# Designed to run inside test/Dockerfile, but works on any host with bash +
# python3. Exits non-zero if any check fails. No git required.

set -uo pipefail
FW="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$FW"

fail=0
pass() { printf '  \033[32m✓\033[0m %s\n' "$1"; }
die()  { printf '  \033[31m✗ %s\033[0m\n' "$1"; fail=1; }
hdr()  { printf '\n\033[1m── %s ──\033[0m\n' "$1"; }
# Portable SHA-256 (Linux: sha256sum, macOS: shasum -a 256).
sha() { if command -v sha256sum >/dev/null; then sha256sum "$1"; else shasum -a 256 "$1"; fi | cut -d' ' -f1; }

SCRIPTS="setup.py setup-launcher.py generate_simple_setup.py generate_plugin_scaffold.py update_localization.py validate.py"

hdr "1. Environment (stock Python, no deps)"
python3 --version && pass "python3 present"
if python3 -m py_compile $SCRIPTS 2>/tmp/pyc.log; then
  pass "all scripts compile"
else
  die "py_compile failed"; cat /tmp/pyc.log
fi

hdr "2. Consistency gate (validate.py)"
if python3 validate.py; then pass "validate.py passed"; else die "validate.py failed"; fi

hdr "3. Generated artifacts not stale (regeneration is a no-op)"
before_wc=$(sha web-config.json)
before_html=$(sha setup.html)
python3 generate_simple_setup.py >/tmp/gen.log 2>&1 && pass "generate_simple_setup.py ran" || { die "generator crashed"; cat /tmp/gen.log; }
python3 update_localization.py  >/tmp/loc.log 2>&1 && pass "update_localization.py ran" || { die "localization sync crashed"; cat /tmp/loc.log; }
[ "$before_wc"  = "$(sha web-config.json)" ] \
  && pass "web-config.json matches generator output (not stale)" \
  || die "web-config.json is STALE — commit regenerated output"
[ "$before_html" = "$(sha setup.html)" ] \
  && pass "setup.html matches generator output (not stale)" \
  || die "setup.html is STALE — commit regenerated output"

hdr "4. Clean-room setup (fresh user copy, non-interactive)"
userproj=$(mktemp -d)
cp -a "$FW"/. "$userproj"/
( cd "$userproj" && rm -f CLAUDE.md AGENTS.md GEMINI.md .agentic_initialized
  # Drive the prompts: one Enter per plugin (default language), then 'yes' to
  # activate, 'no' to skip per-rule config. Extra Enters are absorbed by the
  # activation re-prompt, so this tolerates a changing module count.
  printf '\n\n\n\n\n\n\n\nyes\nno\n' | python3 setup.py --lang en --rules all --agent-file-type CLAUDE.md
) >/tmp/setup.log 2>&1
# Exact-name check (grep -x on the listing) works on both case-sensitive and
# case-insensitive filesystems: it compares the stored filename string, so a
# wrong-cased CLAUDE.MD is caught even on macOS where `[ -f CLAUDE.md ]` lies.
if ls -1 "$userproj" | grep -qx 'CLAUDE.md'; then
  pass "setup.py generated exactly CLAUDE.md"
  for needle in "memory-rules" "rag-rules" "critical-thinking-rules" ".agentic_initialized"; do
    grep -q "$needle" "$userproj/CLAUDE.md" && pass "CLAUDE.md contains '$needle'" \
      || die "CLAUDE.md missing expected content: '$needle'"
  done
  # The activated file is the live rule file, not the template — its
  # template-protection block must have been stripped during activation.
  grep -q "SAFETY_PRECAUTION" "$userproj/CLAUDE.md" \
    && die "activated CLAUDE.md still contains the SAFETY_PRECAUTION template block" \
    || pass "template-protection block stripped from activated file"
else
  die "setup.py did not generate a file named exactly CLAUDE.md"; tail -40 /tmp/setup.log
fi
# Regression guard for the wrong-cased extension bug.
ls -1 "$userproj" | grep -qx 'CLAUDE.MD' \
  && die "setup.py produced wrong-cased CLAUDE.MD (would not load on case-sensitive FS)" \
  || pass "no wrong-cased CLAUDE.MD produced"
rm -rf "$userproj"

hdr "5. v1.4.0 project-local marker consistency"
# No file may still hand an agent the OLD framework-local marker command.
hits=$(grep -rn -e "find agentic-rules -name" \
                -e "Path('agentic-rules/.agentic_initialized')" \
                -e '\-Path "agentic-rules"' \
       --include='*.md' --include='*.py' --include='*.json' . 2>/dev/null || true)
if [ -z "$hits" ]; then
  pass "no framework-local marker instructions remain"
else
  die "framework-local marker instruction still present:"; echo "$hits"
fi

hdr "6. Plugin scaffolder CLI"
python3 generate_plugin_scaffold.py --help >/dev/null 2>&1 && pass "scaffold --help works" || die "scaffold --help failed"

printf '\n'
if [ "$fail" -eq 0 ]; then
  printf '\033[1;32m🎉 DOGFOOD PASSED\033[0m\n'
else
  printf '\033[1;31m💥 DOGFOOD FAILED\033[0m\n'
fi
exit "$fail"
