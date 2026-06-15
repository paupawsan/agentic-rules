#!/usr/bin/env python3
"""Full-coverage test harness for the Agentic Rules Claude Code plugin.

The plugin is contained in claude-code/; the repo root stays platform-neutral.
This harness is hermetic: every check is read-only or runs the bundled hook in
an isolated subprocess with a hand-built environment. It never reads or writes
the user's real ~/.claude config.

Covers:
  * manifest validity (plugin.json, root marketplace.json, claude-code/.mcp.json,
    hooks.json) and that the plugin root is claude-code/
  * `claude plugin validate` (skipped if the CLI is unavailable)
  * skill + command frontmatter; skill deep-links resolve to real repo files
  * rule text is symlinked (claude-code/modules -> ../modules), never copied, and
    the injector still works as-installed with no sibling repo modules/ (regression)
  * the SessionStart injector across the full settings matrix
  * cross-check that documented settings == manifest settings == what the
    injector actually consumes (no phantom or undocumented settings)

Run:  python tests/test_plugin.py
Exit: 0 if all pass, 1 otherwise.
"""

import json
import os
import re
import shutil
import subprocess
import sys

PLUGIN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # claude-code/
REPO = os.path.dirname(PLUGIN)
HOOK = os.path.join(PLUGIN, "hooks", "session-start.py")

EXPECTED_USER_CONFIG = {
    "language",
    "memory_path",
    "enable_memory",
    "enable_rag",
    "enable_critical_thinking",
    "enable_agent_unit_test",
    "always_on_injection",
    "kg_mcp_url",
}

# module -> authoritative full-rules filename under modules/<module>/
MODULES = {
    "memory-rules": "MEMORY-RULES.md",
    "rag-rules": "RAG-RULES.md",
    "critical-thinking-rules": "CRITICAL-THINKING-RULES.md",
    "agent-interaction-unit-test": "CORE-RULES.md",
}
LANGS = ("en", "ja", "id")

_results = []


def test(fn):
    _results.append(fn)
    return fn


# --- helpers ---------------------------------------------------------------

def load_json(rel):
    with open(os.path.join(REPO, rel), "r", encoding="utf-8") as handle:
        return json.load(handle)


def read(rel):
    with open(os.path.join(REPO, rel), "r", encoding="utf-8") as handle:
        return handle.read()


def frontmatter(text):
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    out = {}
    for line in text[3:end].strip().splitlines():
        if ":" in line and not line.lstrip().startswith("#"):
            key, _, value = line.partition(":")
            out[key.strip()] = value.strip().strip('"').strip("'")
    return out


def run_hook(options, plugin_root=PLUGIN):
    """Run the injector in a sandboxed subprocess; return (stdout, stderr, code)."""
    env = {"PATH": os.environ.get("PATH", "")}
    if plugin_root is not None:
        env["CLAUDE_PLUGIN_ROOT"] = plugin_root
    for key, value in options.items():
        env["CLAUDE_PLUGIN_OPTION_" + key.upper()] = value
    proc = subprocess.run(
        [sys.executable, HOOK], env=env, capture_output=True, text=True, timeout=30
    )
    return proc.stdout.strip(), proc.stderr.strip(), proc.returncode


def injected_context(options, plugin_root=PLUGIN):
    out, err, code = run_hook(options, plugin_root)
    assert code == 0, f"hook exited {code}: {err}"
    if not out:
        return ""
    return json.loads(out)["hookSpecificOutput"]["additionalContext"]


# --- manifests & layout ----------------------------------------------------

@test
def plugin_root_is_contained_in_subdir():
    assert os.path.isfile(os.path.join(PLUGIN, ".claude-plugin", "plugin.json"))
    # Root must NOT carry plugin component dirs (kept platform-neutral).
    for stray in ("skills", "commands", "hooks"):
        assert not os.path.isdir(os.path.join(REPO, stray)), \
            f"plugin dir '{stray}/' leaked to repo root"


@test
def plugin_manifest_valid():
    m = load_json("claude-code/.claude-plugin/plugin.json")
    assert m["name"] == "agentic-rules", m.get("name")
    # Standard locations auto-load; declaring them caused a fatal duplicate /
    # a silently-ignored custom path. They must be ABSENT.
    assert "hooks" not in m, "manifest must not declare hooks (hooks/hooks.json auto-loads)"
    assert "mcpServers" not in m, "manifest must not declare mcpServers (.mcp.json auto-loads)"
    assert set(m["userConfig"].keys()) == EXPECTED_USER_CONFIG, set(m["userConfig"])


@test
def marketplace_points_at_subdir():
    m = load_json(".claude-plugin/marketplace.json")
    assert m["name"] == "agentic-rules"
    assert m["owner"]["name"]
    assert len(m["plugins"]) == 1
    assert m["plugins"][0]["name"] == "agentic-rules"
    assert m["plugins"][0]["source"] == "./claude-code", m["plugins"][0]["source"]


@test
def mcp_config_parameterized():
    m = load_json("claude-code/.mcp.json")
    server = m["mcpServers"]["kg-dgx"]
    assert server["type"] == "http"
    assert server["url"] == "${user_config.kg_mcp_url}", server["url"]


@test
def mcp_no_hardcoded_private_ip():
    assert "100.114" not in read("claude-code/.mcp.json"), \
        "private IP must not ship in the plugin mcp config"
    default = load_json("claude-code/.claude-plugin/plugin.json")["userConfig"]["kg_mcp_url"]["default"]
    assert default == "", f"kg_mcp_url default should be blank, got {default!r}"


@test
def dev_mcp_stays_at_repo_root_only():
    # The repo-root .mcp.json (dev config) must remain and must NOT be inside the plugin.
    assert os.path.isfile(os.path.join(REPO, ".mcp.json"))
    assert "100.114" in read(".mcp.json"), "dev .mcp.json should keep the dev endpoint"


@test
def plugin_mcp_is_not_gitignored():
    """Regression guard: a broad `.mcp.json` ignore once hid the plugin's MCP config."""
    if not shutil.which("git") or not os.path.isdir(os.path.join(REPO, ".git")):
        print("    (skipped: not a git checkout)")
        return
    proc = subprocess.run(
        ["git", "check-ignore", "claude-code/.mcp.json"], cwd=REPO,
        capture_output=True, text=True,
    )
    # check-ignore exits 0 when the path IS ignored — that is the bug we guard against.
    assert proc.returncode != 0, \
        "claude-code/.mcp.json is gitignored — it must ship (add !claude-code/.mcp.json)"


@test
def hooks_config_valid():
    m = load_json("claude-code/hooks/hooks.json")
    cmd = m["hooks"]["SessionStart"][0]["hooks"][0]
    assert cmd["type"] == "command"
    assert "session-start.py" in cmd["command"]
    assert "${CLAUDE_PLUGIN_ROOT}" in cmd["command"]


# --- skills & commands -----------------------------------------------------

@test
def all_skills_present_with_description():
    for module in MODULES:
        fm = frontmatter(read(f"claude-code/skills/{module}/SKILL.md"))
        assert fm.get("description"), f"{module} skill missing description"
        assert len(fm["description"]) > 40, f"{module} skill description too thin"


@test
def unit_test_skill_is_explicit_invoke_only():
    fm = frontmatter(read("claude-code/skills/agent-interaction-unit-test/SKILL.md"))
    assert fm.get("disable-model-invocation") == "true", fm.get("disable-model-invocation")


@test
def skill_references_canonical_modules():
    """Skills must REFERENCE modules/ (no duplicated rule text); canonical files exist."""
    for module in MODULES:
        body = read(f"claude-code/skills/{module}/SKILL.md")
        ref = f"${{CLAUDE_PLUGIN_ROOT}}/modules/{module}/RULES.md.<lang>"
        assert ref in body, f"{module} skill must reference {ref}"
        for lang in LANGS:
            assert os.path.isfile(os.path.join(REPO, "modules", module, f"RULES.md.{lang}")), \
                f"missing canonical modules/{module}/RULES.md.{lang}"


@test
def commands_have_descriptions():
    cmd_dir = os.path.join(PLUGIN, "commands")
    files = [f for f in os.listdir(cmd_dir) if f.endswith(".md")]
    assert {"status.md", "help.md"} <= set(files), files
    for name in files:
        fm = frontmatter(read(f"claude-code/commands/{name}"))
        assert fm.get("description"), f"commands/{name} missing description"


# --- single source of truth: reference modules/, never duplicate ------------

@test
def rules_are_symlinked_not_copied():
    """No copies of rule text. claude-code/modules is a SYMLINK to the single
    source (../modules), which Claude Code materializes into the plugin cache on
    install — so the plugin ships the rules without duplicating them in the repo."""
    assert not os.path.isdir(os.path.join(PLUGIN, "rules")), \
        "claude-code/rules/ must not exist (no duplicated rule text)"
    assert not os.path.isfile(os.path.join(PLUGIN, "sync_rules.py")), \
        "sync_rules.py must not exist (nothing to sync — modules is symlinked, not copied)"
    link = os.path.join(PLUGIN, "modules")
    assert os.path.islink(link), \
        "claude-code/modules must be a symlink (a real dir would be a duplicated copy)"
    assert os.readlink(link) == "../modules", \
        f"claude-code/modules must point to ../modules, got {os.readlink(link)!r}"
    assert os.path.isfile(os.path.join(link, "memory-rules", "RULES.md.en")), \
        "claude-code/modules symlink must resolve to the canonical rule files"


@test
def injector_works_as_installed_without_sibling_modules():
    """Regression guard for the packaging bug: simulate the install cache — the
    plugin tree only, with the symlink materialized into a real modules/ and NO
    sibling repo modules/ one level up. The injector must still emit content
    (a `../modules` traversal would resolve to nothing here)."""
    import shutil
    import tempfile
    tmp = tempfile.mkdtemp()
    try:
        dst = os.path.join(tmp, "claude-code")
        # symlinks=False dereferences claude-code/modules -> real files under
        # dst/modules, mirroring how Claude Code packages a symlinked subtree.
        shutil.copytree(PLUGIN, dst, symlinks=False)
        assert not os.path.exists(os.path.join(tmp, "modules")), \
            "test setup: there must be no sibling modules/ next to the plugin root"
        out, err, code = run_hook({"always_on_injection": "true"}, plugin_root=dst)
        assert code == 0 and out.strip(), \
            f"as-installed injector emitted nothing (code={code}, err={err[:200]})"
        assert "Agentic Rules Framework (active)" in out
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


# --- injector: gating ------------------------------------------------------

@test
def injector_off_by_default():
    assert injected_context({}) == ""
    assert injected_context({"always_on_injection": "false"}) == ""


@test
def injector_on_emits_valid_json_context():
    ctx = injected_context({"always_on_injection": "true"})
    assert ctx
    assert "Agentic Rules Framework (active)" in ctx


@test
def injector_no_root_is_silent():
    out, err, code = run_hook({"always_on_injection": "true"}, plugin_root=None)
    assert code == 0 and out == "", (code, out)


@test
def injector_bad_root_is_silent():
    out, err, code = run_hook(
        {"always_on_injection": "true"}, plugin_root="/nonexistent-xyz/claude-code"
    )
    assert code == 0 and out == "", (code, out)


@test
def injector_all_modules_disabled_is_silent():
    ctx = injected_context({
        "always_on_injection": "true",
        "enable_memory": "false",
        "enable_rag": "false",
        "enable_critical_thinking": "false",
        "enable_agent_unit_test": "false",
    })
    assert ctx == ""


# --- injector: per-setting effects (the 'settings claimed correct' core) ----
# Module-unique markers (each phrase appears in exactly one module's rule file).
M_MEMORY = "Memory System Architecture"
M_RAG = "RAG System Architecture"
M_CRITICAL = "Hallucination Prevention"
M_UNIT = "Agent Interaction Unit Test Overview"


@test
def setting_default_enables_three_modules_not_unit_test():
    ctx = injected_context({"always_on_injection": "true"})
    assert M_MEMORY in ctx
    assert M_RAG in ctx
    assert M_CRITICAL in ctx
    assert M_UNIT not in ctx, "unit-test module must be absent unless explicitly enabled"


@test
def setting_enable_agent_unit_test_includes_it():
    ctx = injected_context({"always_on_injection": "true", "enable_agent_unit_test": "true"})
    assert M_UNIT in ctx


@test
def setting_enable_memory_false_excludes_memory():
    ctx = injected_context({"always_on_injection": "true", "enable_memory": "false"})
    assert M_MEMORY not in ctx
    assert M_CRITICAL in ctx


@test
def setting_enable_rag_false_excludes_rag():
    ctx = injected_context({"always_on_injection": "true", "enable_rag": "false"})
    assert M_RAG not in ctx
    assert M_MEMORY in ctx


@test
def setting_enable_critical_thinking_false_excludes_it():
    ctx = injected_context({"always_on_injection": "true", "enable_critical_thinking": "false"})
    assert M_CRITICAL not in ctx
    assert M_MEMORY in ctx


@test
def setting_language_switches_source():
    en = injected_context({"always_on_injection": "true", "language": "en"})
    ja = injected_context({"always_on_injection": "true", "language": "ja"})
    assert en and ja
    assert en != ja, "language=ja must select different source text than en"
    assert any(ord(c) > 0x3000 for c in ja), "ja injection lacks Japanese characters"
    assert not any(ord(c) > 0x3000 for c in en), "en injection unexpectedly has CJK"


@test
def setting_language_invalid_falls_back_to_en():
    en = injected_context({"always_on_injection": "true", "language": "en"})
    xx = injected_context({"always_on_injection": "true", "language": "zz"})
    assert xx == en, "invalid language must fall back to en"


@test
def setting_language_id_supported():
    assert injected_context({"always_on_injection": "true", "language": "id"})


# --- injector: hygiene -----------------------------------------------------

@test
def injected_text_strips_template_scaffolding():
    ctx = injected_context({"always_on_injection": "true", "enable_agent_unit_test": "true"})
    assert "SAFETY_PRECAUTION" not in ctx, "safety guard block must be stripped"
    assert "<!--" not in ctx, "HTML comments must be stripped"
    assert "First-Run Procedure" not in ctx, "first-run section must be stripped"


# --- consistency: docs == manifest == code ---------------------------------

@test
def hook_consumes_only_declared_settings():
    src = read("claude-code/hooks/session-start.py")
    consumed = set(re.findall(r'opt\("([A-Z_]+)"', src))
    consumed |= {"ENABLE_MEMORY", "ENABLE_RAG",
                 "ENABLE_CRITICAL_THINKING", "ENABLE_AGENT_UNIT_TEST"}
    user_config = {k.upper() for k in EXPECTED_USER_CONFIG}
    undeclared = {c for c in consumed if c not in user_config}
    assert not undeclared, f"hook reads settings not declared in userConfig: {undeclared}"


@test
def docs_settings_table_matches_manifest():
    doc = read("docs/CLAUDE_CODE_PLUGIN.md")
    documented = set(re.findall(r"^\|\s*`([a-z_]+)`\s*\|", doc, flags=re.MULTILINE))
    assert documented == EXPECTED_USER_CONFIG, (
        f"docs/manifest setting mismatch: "
        f"docs-only={documented - EXPECTED_USER_CONFIG}, "
        f"manifest-only={EXPECTED_USER_CONFIG - documented}"
    )


@test
def manifest_defaults_are_sane():
    uc = load_json("claude-code/.claude-plugin/plugin.json")["userConfig"]
    assert uc["enable_memory"]["default"] is True
    assert uc["enable_rag"]["default"] is True
    assert uc["enable_critical_thinking"]["default"] is True
    assert uc["enable_agent_unit_test"]["default"] is False
    assert uc["always_on_injection"]["default"] is False
    assert uc["language"]["default"] == "en"


# --- external validator ----------------------------------------------------

@test
def claude_plugin_validate_passes():
    cli = shutil.which("claude")
    if not cli:
        print("    (skipped: claude CLI not on PATH)")
        return
    proc = subprocess.run(
        [cli, "plugin", "validate", "."], cwd=REPO,
        capture_output=True, text=True, timeout=120,
    )
    assert proc.returncode == 0, f"claude plugin validate failed:\n{proc.stdout}\n{proc.stderr}"


# --- runner ----------------------------------------------------------------

def main():
    passed = failed = 0
    for fn in _results:
        try:
            fn()
            print(f"PASS  {fn.__name__}")
            passed += 1
        except Exception as exc:  # noqa: BLE001
            print(f"FAIL  {fn.__name__}: {exc}")
            failed += 1
    print(f"\n{passed}/{passed + failed} passed, {failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
