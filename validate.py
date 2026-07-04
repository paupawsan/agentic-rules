#!/usr/bin/env python3
# Copyright (c) 2025-2026 Paulus Ery Wasito Adhi
#
# Licensed under the MIT License. See LICENSE file for details.
#
# Agentic Rules Framework - Consistency Validator
# ================================================
#
# Checks:
#   1. Version strings agree across manifests, module settings, and web-config.json
#   2. Version strings inside module markdown content match the manifests
#   3. plugins.json entries exist on disk and every modules/ directory is listed
#   4. setup-launcher.py fallback plugin list matches plugins.json
#   5. web-config.json and setup.html are not stale relative to RULES.md.* skeletons
#
# Usage:
#     python3 validate.py    # exit 0 = all checks pass, 1 = problems found

import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).parent
errors = []


def fail(msg):
    errors.append(msg)
    print(f"❌ {msg}")


def ok(msg):
    print(f"✅ {msg}")


def load_json(path):
    with open(ROOT / path, encoding='utf-8') as f:
        return json.load(f)


def check_versions():
    versions = {}
    versions['plugins.json'] = load_json('plugins.json').get('version')
    versions['bootstrap.json'] = load_json('bootstrap.json')['agentic_bootstrap'].get('version')
    versions['web-config.json'] = load_json('web-config.json').get('version')
    gs = load_json('settings/global-settings.json')
    versions['global-settings.json:settings_version'] = gs.get('settings_version')
    versions['global-settings.json:framework_version'] = gs.get('agentic_rules_framework', {}).get('framework_version')
    adapter = load_json('settings/cursor-2.0-multi-agent-adapter.json')
    versions['cursor-2.0-multi-agent-adapter.json'] = adapter.get('_metadata', {}).get('version')
    for settings_file in sorted(ROOT.glob('modules/*/settings.json')):
        rel = settings_file.relative_to(ROOT)
        versions[str(rel)] = load_json(rel).get('version')

    # Consumer-facing plugin manifests — the versions Claude Code actually reads at install.
    # (marketplace.json's top-level "version" is the marketplace-format version, not the
    # framework version, so we check the plugin entry's version instead.)
    versions['claude-code/.claude-plugin/plugin.json'] = load_json('claude-code/.claude-plugin/plugin.json').get('version')
    marketplace = load_json('.claude-plugin/marketplace.json')
    mp_plugins = marketplace.get('plugins') or [{}]
    versions['.claude-plugin/marketplace.json:plugins[0]'] = mp_plugins[0].get('version')

    unique = set(versions.values())
    if len(unique) == 1 and None not in unique:
        ok(f"All {len(versions)} version fields agree: {unique.pop()}")
    else:
        # Report only the offenders (entries differing from the majority), not every field.
        present = [v for v in versions.values() if v is not None]
        majority = Counter(present).most_common(1)[0][0] if present else None
        for source, version in sorted(versions.items()):
            if version != majority:
                fail(f"version mismatch or missing: {source} = {version} (expected {majority})")


def check_module_content_versions():
    # Rule text and docs carry literal version strings (First-Run marker JSON,
    # "Agentic Rules vX.Y.Z" report headers, filled-example footers). They are
    # invisible to check_versions() and drift silently on release bumps.
    # "vX.Y.Z+" compatibility floors are deliberate and exempt.
    canonical = load_json('bootstrap.json')['agentic_bootstrap'].get('version')
    patterns = [
        (re.compile(r'\{"version": "(\d+\.\d+\.\d+)"'), 'first-run marker'),
        (re.compile(r'Agentic Rules v(\d+\.\d+\.\d+)(?!\+)'), 'framework reference'),
        (re.compile(r'\*\*Version\*\*: (\d+\.\d+\.\d+)'), 'version footer'),
    ]
    files = sorted(p for p in ROOT.glob('modules/**/*.md*') if p.is_file())
    files.append(ROOT / 'README.md')
    drift = []
    for path in files:
        for lineno, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
            for pattern, label in patterns:
                for match in pattern.finditer(line):
                    if match.group(1) != canonical:
                        drift.append(f"{path.relative_to(ROOT)}:{lineno} "
                                     f"{label} says {match.group(1)} (expected {canonical})")
    if drift:
        for msg in drift:
            fail(f"version drift: {msg}")
    else:
        ok(f"module content version strings all match {canonical}")


def check_module_lists():
    plugin_entries = load_json('plugins.json').get('plugins', [])
    module_entries = {p for p in plugin_entries if p.startswith('modules/')}

    for entry in sorted(plugin_entries):
        if not (ROOT / entry).is_dir():
            fail(f"plugins.json lists '{entry}' but the directory does not exist")
    on_disk = {f"modules/{d.name}" for d in (ROOT / 'modules').iterdir() if d.is_dir()}
    missing = on_disk - module_entries
    for entry in sorted(missing):
        fail(f"directory '{entry}' exists but is not listed in plugins.json")
    if not missing:
        ok(f"plugins.json and modules/ agree on {len(on_disk)} modules")

    launcher = (ROOT / 'setup-launcher.py').read_text(encoding='utf-8')
    match = re.search(r'FALLBACK_PLUGIN_DIRS\s*=\s*\[(.*?)\]', launcher, re.DOTALL)
    if not match:
        fail("setup-launcher.py: FALLBACK_PLUGIN_DIRS not found")
        return
    fallback = set(re.findall(r"'([^']+)'", match.group(1)))
    if fallback == module_entries:
        ok("setup-launcher.py FALLBACK_PLUGIN_DIRS matches plugins.json")
    else:
        fail(f"setup-launcher.py FALLBACK_PLUGIN_DIRS != plugins.json modules: "
             f"only in fallback {sorted(fallback - module_entries)}, "
             f"only in plugins.json {sorted(module_entries - fallback)}")


def check_generated_artifacts():
    web_config = load_json('web-config.json')

    stale = []
    for plugin_dir, plugin in web_config.get('plugins', {}).items():
        for lang, embedded in plugin.get('templates', {}).items():
            skeleton = ROOT / plugin_dir / f'RULES.md.{lang}'
            if not skeleton.exists():
                stale.append(f"{skeleton.relative_to(ROOT)} missing but embedded in web-config.json")
            elif skeleton.read_text(encoding='utf-8') != embedded:
                stale.append(f"web-config.json template for {plugin_dir} ({lang}) != {skeleton.relative_to(ROOT)}")
    for lang, embedded in web_config.get('rootTemplates', {}).items():
        skeleton = ROOT / f'RULES.md.{lang}'
        if not skeleton.exists():
            stale.append(f"RULES.md.{lang} missing but embedded in web-config.json rootTemplates")
        elif skeleton.read_text(encoding='utf-8') != embedded:
            stale.append(f"web-config.json rootTemplate ({lang}) != RULES.md.{lang}")
    if stale:
        for msg in stale:
            fail(f"stale: {msg} — run: python3 generate_simple_setup.py")
    else:
        ok("web-config.json templates match all RULES.md.* skeletons")

    html = (ROOT / 'setup.html').read_text(encoding='utf-8')
    start = html.index('---AUTO GENERATED STATICWEBCONFIG START---')
    end = html.index('---AUTO GENERATED STATICWEBCONFIG END---')
    block = html[start:end]
    embedded_json = block[block.index('=') + 1:]
    embedded_json = embedded_json[:embedded_json.rindex('}') + 1]
    if json.loads(embedded_json) == web_config:
        ok("setup.html embedded staticWebConfig matches web-config.json")
    else:
        fail("setup.html embedded staticWebConfig != web-config.json — run: python3 generate_simple_setup.py")

    version = web_config.get('version')
    if f"Version v{version}" in html:
        ok(f"setup.html displays Version v{version}")
    else:
        fail(f"setup.html does not display 'Version v{version}' — run: python3 generate_simple_setup.py")


def _key_paths(obj, prefix=''):
    paths = set()
    if isinstance(obj, dict):
        for key, value in obj.items():
            here = f"{prefix}.{key}" if prefix else key
            paths.add(here)
            paths |= _key_paths(value, here)
    return paths


def check_localization_parity():
    loc = load_json('localization.json')
    langs = [k for k in loc if k != '_comment']
    if len(langs) < 2:
        ok(f"localization.json has {len(langs)} language(s)")
        return
    reference = langs[0]
    ref_keys = _key_paths(loc[reference])
    consistent = True
    for lang in langs[1:]:
        keys = _key_paths(loc[lang])
        missing = ref_keys - keys
        extra = keys - ref_keys
        if missing:
            fail(f"localization.json[{lang}] missing keys present in [{reference}]: {sorted(missing)}")
            consistent = False
        if extra:
            fail(f"localization.json[{lang}] has keys absent from [{reference}]: {sorted(extra)}")
            consistent = False
    if consistent:
        ok(f"localization.json key sets match across {', '.join(langs)} ({len(ref_keys)} keys)")


def main():
    print("🔎 Agentic Rules Framework - Consistency Validator")
    print("=" * 50)
    check_versions()
    check_module_content_versions()
    check_module_lists()
    check_localization_parity()
    check_generated_artifacts()
    print("=" * 50)
    if errors:
        print(f"💥 {len(errors)} problem(s) found")
        return 1
    print("🎉 All checks passed")
    return 0


if __name__ == '__main__':
    sys.exit(main())
