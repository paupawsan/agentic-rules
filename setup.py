#!/usr/bin/env python3
# Copyright (c) 2025 Paulus Ery Wasito Adhi
#
# Licensed under the MIT License. See LICENSE file for details.
#
# Agentic Rules Framework Setup Script
# ====================================
#
# This script configures the Agentic Rules Framework by:
# - Auto-detecting available rule plugins
# - Activating rule templates to AGENTS.md/GEMINI.md files
# - Supporting bilingual templates (English/Japanese)
# - Providing configuration guidance for each rule

"""
Setup script for configuring agentic-rules framework.

This script helps configure the Agentic Rules Framework by:
- Auto-detecting available rule plugins
- Activating rule templates to AGENTS.md files
- Supporting bilingual templates (English/Japanese)
- Providing configuration guidance for each rule

Features:
- Auto-detection of rule directories (no hardcoding)
- Bilingual support (en/ja) for each rule
- Selective rule activation
- Safety checks to prevent accidental overwrites

Usage:
    python setup.py [--lang en|ja] [--rules memory,rag,critical]

Flow:
    1. Auto-detect available rule plugins
    2. Select language (en/ja) - or use --lang parameter
    3. Choose which rules to activate
    4. Activate selected rule templates to AGENTS.md files
"""

import argparse
import json
import os
import sys
from pathlib import Path

# ============================================================================
# LOAD LOCALIZATION
# ============================================================================
def load_localization():
    """Load localization data from JSON file."""
    loc_file = get_script_directory() / "localization.json"
    if loc_file.exists():
        try:
            with open(loc_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Warning: Could not load localization.json: {e}")

    # Fallback to minimal localization if file not found
    return {
        'en': {
            'cli': {
                'title': 'Agentic Rules Framework Setup',
                'description': 'Configure the Agentic Rules Framework by activating rule templates.',
                'detection_title': 'Rule Plugin Detection',
                'detection_found': 'Found {count} rule plugin(s):',
                'detection_none': 'No rule plugins found in current directory.',
                'lang_title': 'Language Selection',
                'lang_prompt': 'Select language for rule templates:',
                'rules_title': 'Rule Selection',
                'activation_title': 'Rule Activation',
                'processing_title': 'Activating Rules',
                'completion_title': '✓ Setup Complete!',
            }
        },
        'ja': {
            'cli': {
                'title': 'Agentic Rules Framework セットアップ',
                'description': 'ルールテンプレートをアクティブ化してAgentic Rules Frameworkを設定します。',
                'detection_title': 'ルールプラグイン検出',
                'detection_found': '{count}個のルールプラグインが見つかりました：',
                'detection_none': '現在のディレクトリにルールプラグインが見つかりません。',
                'lang_title': '言語選択',
                'lang_prompt': 'ルールテンプレートの言語を選択してください：',
                'rules_title': 'ルール選択',
                'activation_title': 'ルールアクティベーション',
                'processing_title': 'ルールアクティベーション中',
                'completion_title': '✓ セットアップ完了！',
            }
        }
    }

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================
def get_script_directory():
    """Get the directory where this script is located."""
    return Path(__file__).parent.absolute()

LOCALIZATION = load_localization()

def get_available_languages():
    """Get list of available languages from localization data."""
    if LOCALIZATION and '_comment' in LOCALIZATION:
        # Remove metadata key and return language codes
        return [lang for lang in LOCALIZATION.keys() if lang != '_comment']
    return list(LOCALIZATION.keys()) if LOCALIZATION else ['en']

def get_default_language():
    """Get the default language (first available language)."""
    languages = get_available_languages()
    return languages[0] if languages else 'en'

def get_language_display_name(lang_code, ui_lang='en'):
    """Get display name for a language code, with localization support."""
    # Language name mapping with flags
    lang_names = {
        'en': '🇺🇸 English',
        'ja': '🇯🇵 日本語',
        'id': '🇮🇩 Bahasa Indonesia',
        'zh': '🇨🇳 中文',
        'ar': '🇸🇦 العربية',
        'de': '🇩🇪 Deutsch',
        'fr': '🇫🇷 Français',
        'es': '🇪🇸 Español',
        'ko': '🇰🇷 한국어',
        'hi': '🇮🇳 हिन्दी',
        'pt': '🇵🇹 Português',
        'ru': '🇷🇺 Русский',
        'si': '🇱🇰 සිංහල',
        'ta': '🇮🇳 தமிழ்',
        'th': '🇹🇭 ไทย',
        'tr': '🇹🇷 Türkçe',
        'vi': '🇻🇳 Tiếng Việt'
    }

    # Try to get localized name, fall back to flag + code
    display_name = lang_names.get(lang_code, f'{lang_code.upper()} ({lang_code})')
    return display_name

def load_config_file(config_path):
    """Load configuration from a JSON file exported from setup.html."""
    if not config_path:
        return None

    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)

        # Validate the config structure
        if not isinstance(config, dict) or '_metadata' not in config:
            print(f"Warning: Invalid configuration file format: {config_path}")
            return None

        print(f"✅ Loaded configuration from {config_path}")
        if 'exported_from' in config.get('_metadata', {}):
            print(f"   Exported from: {config['_metadata']['exported_from']}")
        if 'export_timestamp' in config.get('_metadata', {}):
            print(f"   Export timestamp: {config['_metadata']['export_timestamp']}")

        return config
    except Exception as e:
        print(f"Warning: Could not load configuration file {config_path}: {e}")
        return None

def detect_rule_plugins(script_dir):
    """Auto-detect rule plugin directories from plugins.json manifest."""
    manifest_file = script_dir / "plugins.json"

    if manifest_file.exists():
        try:
            with open(manifest_file, 'r', encoding='utf-8') as f:
                manifest = json.load(f)
                plugins = manifest.get('plugins', [])
                # Validate that plugin directories exist
                valid_plugins = []
                for plugin in plugins:
                    plugin_dir = script_dir / plugin
                    if plugin_dir.is_dir():
                        # Check for any RULES.md.* template files (supports any language)
                        rules_templates = list(plugin_dir.glob("RULES.md.*"))
                        if rules_templates:
                            valid_plugins.append(plugin)
                return sorted(valid_plugins)
        except Exception as e:
            print(f"Warning: Could not read plugins.json: {e}")

    # Fallback: Original directory scanning logic
    print("Falling back to directory scanning...")
    rule_plugins = []
    for item in script_dir.iterdir():
        if item.is_dir():
            # Check for any RULES.md.* template files (supports any language)
            rules_templates = list(item.glob("RULES.md.*"))
            if rules_templates:
                rule_plugins.append(item.name)

    return sorted(rule_plugins)

def t(key, locale='en', **kwargs):
    """Get localized string."""
    # Get the locale data with better fallback
    default_lang = get_default_language()
    locale_data = LOCALIZATION.get(locale, LOCALIZATION.get(default_lang, LOCALIZATION.get('en', {})))

    # Try to get from cli section first
    if isinstance(locale_data, dict) and 'cli' in locale_data:
        cli_data = locale_data['cli']
        if isinstance(key, str) and '.' in key:
            # Handle nested keys like 'errors.no_rules'
            parts = key.split('.')
            value = cli_data
            for part in parts:
                if isinstance(value, dict):
                    value = value.get(part, key)
                else:
                    break
            if value != key and isinstance(value, str):
                return value.format(**kwargs)
        else:
            # Direct key lookup
            if key in cli_data:
                value = cli_data[key]
                return value.format(**kwargs) if isinstance(value, str) else str(value)

    # Fall back to main locale data
    if isinstance(key, str) and '.' in key:
        # Handle nested keys like 'errors.no_rules'
        parts = key.split('.')
        value = locale_data
        for part in parts:
            if isinstance(value, dict):
                value = value.get(part, key)
            else:
                return key
        return value.format(**kwargs) if isinstance(value, str) else str(value)
    else:
        return locale_data.get(key, key).format(**kwargs)

# ============================================================================
# LANGUAGE SELECTION
# ============================================================================
def select_ui_language(cli_lang=None):
    """Select UI language for interface."""
    available_langs = get_available_languages()

    if cli_lang and cli_lang.lower() in available_langs:
        return cli_lang.lower()

    print(f"\n{t('ui_lang_title')}")
    print(f"{t('ui_lang_prompt')}")

    # Generate dynamic options based on available languages
    for i, lang in enumerate(available_langs, 1):
        lang_name = t(f'lang_option_{i}')
        if lang_name == f'lang_option_{i}':  # Key not found, use default
            lang_name = f'{i}. {lang.upper()} ({lang})'
        print(f"  {lang_name}")

    valid_choices = [str(i) for i in range(1, len(available_langs) + 1)] + available_langs

    while True:
        choice = input(f'\n{t("enter_choice", choices=", ".join(valid_choices[:5]))}: ').strip().lower()
        if choice in [str(i) for i in range(1, len(available_langs) + 1)]:
            return available_langs[int(choice) - 1]
        elif choice in available_langs:
            return choice
        else:
            print(t('lang_invalid'))

def select_agent_language(cli_lang=None, ui_lang='en'):
    """Select agent language for templates."""
    available_langs = get_available_languages()

    if cli_lang and cli_lang.lower() in available_langs:
        return cli_lang.lower()

    print(f"\n{t('agent_lang_title', locale=ui_lang)}")
    print(f"{t('agent_lang_prompt', locale=ui_lang)}")

    # Generate dynamic options based on available languages
    for i, lang in enumerate(available_langs, 1):
        lang_name = t(f'lang_option_{i}', locale=ui_lang)
        if lang_name == f'lang_option_{i}':  # Key not found, use default
            lang_name = f'{i}. {lang.upper()} ({lang})'
        print(f"  {lang_name}")

    valid_choices = [str(i) for i in range(1, len(available_langs) + 1)] + available_langs

    while True:
        choice = input(f'\n{t("enter_choice", locale=ui_lang, choices=", ".join(valid_choices[:5]))}: ').strip().lower()
        if choice in [str(i) for i in range(1, len(available_langs) + 1)]:
            return available_langs[int(choice) - 1]
        elif choice in available_langs:
            return choice
        else:
            print(t('lang_invalid', locale=ui_lang))

def select_plugin_languages(selected_rules, global_agent_lang, ui_lang='en', script_dir=None):
    """Select language for each selected plugin."""
    plugin_languages = {}

    print(f"\n{t('plugin_lang_title', locale=ui_lang) if 'plugin_lang_title' in LOCALIZATION.get(ui_lang, {}) else 'Plugin Language Selection'}")
    print(f"{t('plugin_lang_description', locale=ui_lang) if 'plugin_lang_description' in LOCALIZATION.get(ui_lang, {}) else 'Choose language for each plugin template:'}")

    for rule in selected_rules:
        print(f"\n  Plugin: {rule}")

        # Check available templates for this plugin
        plugin_dir = Path(script_dir) / rule
        available_templates = []
        if plugin_dir.exists():
            available_templates = [f.suffix[1:] for f in plugin_dir.glob("RULES.md.*")]  # Remove leading dot

        if available_templates:
            available_templates = sorted(set(available_templates))  # Remove duplicates and sort
            print(f"    Available templates: {', '.join(available_templates)}")
        else:
            print("    No templates available")
            continue

        # Default to global language, but allow override
        default_lang = global_agent_lang
        if default_lang not in available_templates:
            default_lang = available_templates[0] if available_templates else 'en'

        while True:
            print(f"    Select language for {rule} (default: {default_lang}):")
            for i, lang in enumerate(available_templates, 1):
                # Try to get localized name, fall back to language code
                lang_name = get_language_display_name(lang, ui_lang)
                marker = " (default)" if lang == default_lang else ""
                print(f"      {i}. {lang_name}{marker}")

            choice = input("    Enter choice (or press Enter for default): ").strip().lower()

            if not choice:  # Empty input = use default
                plugin_languages[rule] = default_lang
                print(f"    ✓ Using default language: {default_lang}")
                break
            elif choice in ['q', 'quit', 'exit']:
                print("Setup cancelled.")
                sys.exit(0)
            elif choice.isdigit() and 1 <= int(choice) <= len(available_templates):
                selected_lang = available_templates[int(choice) - 1]
                plugin_languages[rule] = selected_lang
                print(f"    ✓ Selected: {selected_lang}")
                break
            elif choice in available_templates:
                plugin_languages[rule] = choice
                print(f"    ✓ Selected: {choice}")
                break
            else:
                print("    Invalid choice. Please try again.")

    return plugin_languages

# ============================================================================
# FILE TYPE SELECTION
# ============================================================================
def select_agent_file_type(cli_file_type=None, lang='en'):
    """Select agent file type (AGENTS.md, GEMINI.md, or CLAUDE.md)."""
    if cli_file_type:
        return cli_file_type.upper()

    print(f"\n{t('file_type_title', locale=lang)}")
    print(f"{t('file_type_prompt', locale=lang)}")
    print(f"  {t('file_type_option_1', locale=lang)}")
    print(f"  {t('file_type_option_2', locale=lang)}")
    print(f"  {t('file_type_option_3', locale=lang)}")

    while True:
        choice = input('\nEnter choice (1/2/3/agents/gemini/claude): ').strip().lower()
        if choice in ['1', 'agents', 'agents.md']:
            return 'AGENTS.md'
        elif choice in ['2', 'gemini', 'gemini.md']:
            return 'GEMINI.md'
        elif choice in ['3', 'claude', 'claude.md']:
            return 'CLAUDE.md'
        else:
            print(t('file_type_invalid', locale=lang))

# ============================================================================
# RULE SELECTION
# ============================================================================
def select_rules(available_rules, cli_rules=None, lang='en'):
    """Select which rules to activate."""
    if cli_rules:
        if cli_rules.lower() == 'all':
            return available_rules
        selected = [r.strip() for r in cli_rules.split(',') if r.strip()]
        invalid = [r for r in selected if r not in available_rules]
        if invalid:
            print(t('rules_invalid', available=', '.join(available_rules)))
            return []
        return [r for r in selected if r in available_rules]

    print(f"\n{t('rules_title', locale=lang)}")
    print(t('rules_description', locale=lang))
    print(t('rules_available', locale=lang))

    for i, rule in enumerate(available_rules, 1):
        print(f"  {i}. {rule}")

    print(f"\n{t('rules_prompt', locale=lang)}")

    while True:
        choice = input().strip().lower()

        if choice == 'all':
            return available_rules

        if ',' in choice:
            # Comma-separated list
            selected = [r.strip() for r in choice.split(',') if r.strip()]
        else:
            # Check if it's a number
            try:
                index = int(choice) - 1
                if 0 <= index < len(available_rules):
                    selected = [available_rules[index]]
                else:
                    selected = []
            except ValueError:
                # Try to match rule name directly
                selected = [choice] if choice in available_rules else []

        if not selected:
            print(t('rules_invalid', locale=lang, available=', '.join(available_rules)))
            continue

        # Validate all selected rules exist
        invalid = [r for r in selected if r not in available_rules]
        if invalid:
            print(t('rules_invalid', locale=lang, available=', '.join(available_rules)))
            continue

        return list(set(selected))  # Remove duplicates

# ============================================================================
# RULE ACTIVATION
# ============================================================================
def generate_root_file(selected_rules, language, file_type, script_dir, lang='en'):
    """Generate the root integration file (AGENTS.md, GEMINI.md, or CLAUDE.md)."""
    errors = []

    # Define all possible file types to clean up when switching
    all_file_types = ['AGENTS.md', 'GEMINI.md', 'CLAUDE.md']

    # Remove other file types to ensure only one integration file exists
    for old_file_type in all_file_types:
        if old_file_type != file_type:
            # Check for both .md and .MD variants
            for ext_variant in [old_file_type, old_file_type.replace('.md', '.MD')]:
                old_file = script_dir / ext_variant
                if old_file.exists():
                    try:
                        # Create backup before removal
                        backup_file = script_dir / f"{ext_variant}.backup"
                        import shutil
                        shutil.copy2(old_file, backup_file)
                        # Remove the old file
                        old_file.unlink()
                        print(f"    Removed existing {ext_variant} (backed up as {ext_variant}.backup)")
                    except Exception as e:
                        print(f"    Warning: Could not remove {ext_variant}: {e}")

    # Generate root integration content
    enabled_rules = selected_rules

    # Get root template from static config (simulate what setup.html does)
    root_templates = {}
    for lang_code in ['en', 'ja', 'id']:
        root_template_file = script_dir / f"RULES.md.{lang_code}"
        if root_template_file.exists():
            try:
                with open(root_template_file, 'r', encoding='utf-8') as f:
                    root_templates[lang_code] = f.read()
            except Exception as e:
                print(f"Warning: Could not read root template RULES.md.{lang_code}: {e}")

    template_content = root_templates.get(language, root_templates.get('en'))

    # Fallback hardcoded template if no template file found
    if not template_content:
        template_content = f"""# Agentic Rules Framework Integration

**⚠️ SAFETY PRECAUTION**: This is a TEMPLATE file. Agents MUST NOT auto-load this file. Only load when renamed to `{file_type}` after explicit user activation.

**MANDATORY**: Agents must respect the bootstrap configuration in `bootstrap.json` and only load rule files when their corresponding settings are enabled.

## Framework Overview
This framework provides structured AI agent behaviors through modular rules:
- **memory-rules/**: Persistent memory system for context retention
- **rag-rules/**: Retrieval-augmented generation for optimal context usage
- **critical-thinking-rules/**: Intellectual rigor and hallucination prevention

## Bootstrap Compliance
Before loading any rule files, agents MUST:
1. Read `bootstrap.json` to understand the framework configuration
2. Check loading sequence and entry points
3. Validate user consent and settings
4. Only load enabled rule integrations

## Rule Integration Requirements
Each rule provides specific algorithmic implementations that agents must actively execute:

### Memory Rules Integration
**MANDATORY**: If `memory_rules.enabled = true` in settings.json
- Location: `memory-rules/{file_type}`
- Implements: Memory initialization, storage, retrieval, and cleanup processes

### RAG Rules Integration
**MANDATORY**: If `rag_rules.enabled = true` in settings.json
- Location: `rag-rules/{file_type}`
- Implements: Context optimization, relevance scoring, and retrieval algorithms

### Critical Thinking Rules Integration
**MANDATORY**: If `critical_thinking_rules.enabled = true` in settings.json
- Location: `critical-thinking-rules/{file_type}`
- Implements: Error admission, assumption challenge, and verification processes

## Framework Isolation
**CRITICAL**: This framework remains a tool and should never be included in user project codebases. All integrations happen through the rule files in their respective directories.

## Agent Responsibility
Agents using this framework must:
- Respect all user settings and configurations
- Provide clear feedback when rules are disabled
- Maintain framework neutrality in generated content
- Follow bootstrap compliance requirements

**VIOLATION**: Agents that do not respect these integration requirements or user settings.

<!-- METADATA: Root level agent integration template with framework overview -->
<!-- LICENSE: Copyright (c) 2025 Paulus Ery Wasito Adhi - Licensed under the MIT License. See LICENSE file for details. -->"""

    # Generate the root file
    try:
        target_file = script_dir / file_type
        backup_file = script_dir / f"{file_type}.backup"

        print(f"  - Root → {file_type} (using {language} template)")

        # Backup existing file if it exists (preserve user customizations)
        if target_file.exists():
            import shutil
            shutil.copy2(target_file, backup_file)
            print("    Backed up existing file")

        # Write the root file
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(template_content)

        print(f"✓ Successfully generated root {file_type}")
        return True, errors

    except Exception as e:
        error_msg = f"Failed to generate root {file_type}: {str(e)}"
        print(f"✗ {error_msg}")
        errors.append(error_msg)
        return False, errors

def activate_rule_templates(selected_rules, language, file_type, script_dir, lang='en', config=None, plugin_languages=None):
    """Activate selected rule templates to AGENTS.md files."""
    activated = []
    errors = []

    # Define all possible file types to clean up when switching
    all_file_types = ['AGENTS.md', 'GEMINI.md', 'CLAUDE.md']

    print(f"\n{t('activation_title', locale=lang)}")
    print(t('activation_confirm', locale=lang))

    for rule in selected_rules:
        rule_dir = script_dir / rule

        # Clean up other file types in this rule directory
        for old_file_type in all_file_types:
            if old_file_type != file_type:
                # Check for both .md and .MD variants
                for ext_variant in [old_file_type, old_file_type.replace('.md', '.MD')]:
                    old_file = rule_dir / ext_variant
                    if old_file.exists():
                        try:
                            # Create backup before removal
                            backup_file = rule_dir / f"{ext_variant}.backup"
                            import shutil
                            shutil.copy2(old_file, backup_file)
                            # Remove the old file
                            old_file.unlink()
                            print(f"    Removed existing {rule}/{ext_variant} (backed up as {ext_variant}.backup)")
                        except Exception as e:
                            print(f"    Warning: Could not remove {rule}/{ext_variant}: {e}")

        template_file = rule_dir / f"RULES.md.{language}"

        if template_file.exists():
            print(f"  - {rule} → {file_type} (using {language} template)")
        else:
            # Check for any available templates
            available_templates = list(rule_dir.glob("RULES.md.*"))
            if available_templates:
                available_langs = [t.suffix[1:] for t in available_templates]  # Remove leading dot
                print(f"  - {rule} → {file_type} (fallback to {available_langs[0]} template)")
            else:
                print(f"  - {rule} → {file_type} (no templates available)")

    print(f"\n{t('activation_warning', locale=lang, file_type=file_type)}")
    print(t('activation_backup', locale=lang, file_type=file_type))

    while True:
        confirm = input(f"\n{t('activation_prompt', locale=lang)}").strip().lower()
        if confirm in ['yes', 'y']:
            break
        elif confirm in ['no', 'n']:
            print(f"\n{t('activation_cancelled', locale=lang)}")
            return [], []
        else:
            print(t('activation_invalid', locale=lang))

    print(f"\n{t('processing_title', locale=lang)}")

    for rule in selected_rules:
        print(f"\n{t('processing_rule', locale=lang, rule=rule)}")

        rule_dir = script_dir / rule
        # Check for plugin-specific language setting
        plugin_language = language  # Default to global language
        if plugin_languages and rule in plugin_languages:
            plugin_language = plugin_languages[rule]
            print(f"  📝 {rule} → Using plugin-specific language: {plugin_language}")
        elif config and 'selected_rules' in config and rule in config['selected_rules']:
            plugin_config = config['selected_rules'][rule]
            if isinstance(plugin_config, dict) and 'language' in plugin_config:
                plugin_language = plugin_config['language']
                print(f"  📝 {rule} → Using config language: {plugin_language}")

        template_file = rule_dir / f"RULES.md.{plugin_language}"
        target_file = rule_dir / file_type
        backup_file = rule_dir / f"{file_type}.backup"

        try:
            # Try plugin-specific language first
            if template_file.exists():
                actual_template = template_file
                template_lang = plugin_language
                print(t('processing_template', locale=lang, template=f"RULES.md.{plugin_language}"))
            else:
                # Fallback: Try global language
                global_template = rule_dir / f"RULES.md.{language}"
                if global_template.exists() and plugin_language != language:
                    actual_template = global_template
                    template_lang = language
                    print(f"  ⚠️  {rule} → Plugin language {plugin_language} not available, using global {language} template")
                    print(t('processing_template', locale=lang, template=f"RULES.md.{language}"))
                else:
                    # Final fallback: Look for any available RULES.md.* file
                    available_templates = list(rule_dir.glob("RULES.md.*"))
                    if available_templates:
                        # Use the first available template (could be any language)
                        actual_template = available_templates[0]
                        template_lang = actual_template.suffix[1:]  # Remove the leading dot
                        print(f"  ⚠️  {rule} → Requested {plugin_language}, using available {template_lang} template")
                        print(f"     Note: Plugin uses non-standard language. Consider adding {plugin_language} translation.")
                    else:
                        raise FileNotFoundError(f"No RULES.md.* template files found in {rule_dir}")

            template_file = actual_template

            # Backup existing file if it exists (preserve user customizations)
            if target_file.exists():
                import shutil
                shutil.copy2(target_file, backup_file)
                print(t('processing_backup', locale=lang))

            # Copy template to target
            import shutil
            shutil.copy2(template_file, target_file)

            print(t('processing_success', locale=lang, rule=rule))
            activated.append(rule)

        except Exception as e:
            error_msg = t('processing_error', locale=lang, rule=rule, error=str(e))
            print(error_msg)
            errors.append(f"{rule}: {str(e)}")

    return activated, errors

# ============================================================================
# RULE CONFIGURATION
# ============================================================================
def configure_rule_settings(activated_rules, selected_lang, script_dir, lang='en'):
    """Configure settings for activated rules by reading their setup.json files."""
    print(f"\n{t('config_title', locale=lang)}")
    print(t('config_description', locale=lang))

    while True:
        choice = input(f"\n{t('config_prompt', locale=lang)}").strip().lower()
        if choice in ['yes', 'y']:
            break
        elif choice in ['no', 'n']:
            print(f"\n{t('config_skip', locale=lang)}")
            return []
        else:
            print("Please answer 'yes' or 'no'.")

    configured = []

    for rule in activated_rules:
        rule_dir = script_dir / rule
        setup_file = rule_dir / "setup.json"

        if not setup_file.exists():
            print(f"  No setup configuration found for {rule} (setup.json missing)")
            continue

        try:
            with open(setup_file, 'r', encoding='utf-8') as f:
                setup_config = json.load(f)

            configured.extend(configure_plugin_from_setup(rule, setup_config, rule_dir, lang))

        except Exception as e:
            print(f"  Error reading setup config for {rule}: {e}")

    return configured

def configure_plugin_from_setup(rule_name, setup_config, rule_dir, lang='en'):
    """Configure a plugin based on its setup.json configuration."""
    # Get localized plugin name and description from setup.json
    localization = setup_config.get('localization', {})
    lang_data = localization.get(lang, localization.get('en', {}))
    plugin_name = lang_data.get('plugin_name', rule_name)
    plugin_description = lang_data.get('description', '')

    configured = []

    print(f"\n{t('config_rule_title', locale=lang, rule=plugin_name)}")
    if plugin_description:
        print(f"  {plugin_description}")

    # Handle mandatory configuration first
    mandatory_configs = setup_config.get('mandatory_config', [])
    for config in mandatory_configs:
        if not configure_setting(config, rule_dir, lang):
            print(f"  Mandatory configuration failed for {plugin_name}")
            return configured

    # Handle optional configuration
    optional_configs = setup_config.get('optional_config', [])
    if optional_configs:
        print(f"  Available optional configurations:")
        for i, config in enumerate(optional_configs, 1):
            # Get localized title
            localization = config.get('localization', {})
            lang_data = localization.get(lang, localization.get('en', {}))
            title = lang_data.get('title', config.get('title', f"Configuration {i}"))
            print(f"    {i}. {title}")
        print(f"    {len(optional_configs) + 1}. Skip optional configuration")

        while True:
            try:
                choice = int(input(f"  Choose option (1-{len(optional_configs) + 1}): ").strip())
                if choice == len(optional_configs) + 1:
                    break
                elif 1 <= choice <= len(optional_configs):
                    config = optional_configs[choice - 1]
                    if configure_setting(config, rule_dir, lang):
                        configured.append(f"{rule_name}_{config['name']}")
                    break
                else:
                    print(f"  Please choose 1-{len(optional_configs) + 1}")
            except ValueError:
                print("  Please enter a valid number")

    return configured

def configure_setting(config, rule_dir, lang='en'):
    """Configure a single setting based on its configuration."""
    config_type = config.get('type')

    # Get localized strings from config
    localization = config.get('localization', {})
    lang_data = localization.get(lang, localization.get('en', {}))
    title = lang_data.get('title', config.get('title', 'Configuration'))
    description = lang_data.get('description', config.get('description', ''))

    print(f"\n    {title}")
    if description:
        print(f"    {description}")

    if config_type == 'path':
        return configure_path_setting(config, rule_dir, lang)
    elif config_type == 'choice':
        return configure_choice_setting(config, rule_dir, lang)
    else:
        print(f"    Unknown configuration type: {config_type}")
        return False

def configure_path_setting(config, rule_dir, lang='en'):
    """Configure a path setting (like memory path)."""
    # Get localized strings from config
    localization = config.get('localization', {})
    lang_data = localization.get(lang, localization.get('en', {}))
    examples = lang_data.get('examples', config.get('examples', []))
    note = lang_data.get('note', config.get('note', ''))

    if examples:
        print(f"\n    {t('config_memory_path_examples', locale=lang)}")
        for example in examples:
            print(f"      {example}")

    if note:
        print(f"\n    {t('config_memory_path_note', locale=lang)}: {note}")

    while True:
        path_input = input(f"\n    {t('config_memory_path_prompt', locale=lang)}").strip()

        if not path_input:
            print(f"    {t('config_memory_path_error_empty', locale=lang)}")
            continue

        # Expand user path and normalize
        import os
        path_input = os.path.expanduser(path_input)
        path_obj = Path(path_input)

        # Check if path exists
        if not path_obj.exists():
            create = input(f"    {t('config_memory_path_create_prompt', locale=lang)}").strip().lower()
            if create in ['yes', 'y']:
                try:
                    path_obj.mkdir(parents=True, exist_ok=True)
                    print(f"    {t('config_memory_path_create_success', locale=lang, path=path_input)}")
                except Exception as e:
                    print(f"    {t('config_memory_path_create_error', locale=lang, error=e)}")
                    continue
            else:
                continue

        # Confirm path
        normalized_path = str(path_obj.resolve())
        print(f"\n    {t('config_memory_path_confirm_path', locale=lang, path=normalized_path)}")

        if 'structure' in config:
            structure = config.get('confirm_structure', '')
            if structure:
                print(f"    {t('config_memory_path_confirm_structure', locale=lang)}: {structure}")

        confirm = input(f"    {t('config_memory_path_confirm_prompt', locale=lang)}").strip().lower()
        if confirm in ['yes', 'y']:
            # Save to settings
            return save_setting_to_config(config, normalized_path, rule_dir)
        elif confirm in ['no', 'n']:
            print("    Let's try again.")
        else:
            print(f"    {t('config_memory_path_confirm_invalid', locale=lang)}")

def configure_choice_setting(config, rule_dir, lang='en'):
    """Configure a choice setting with predefined options."""
    options = config.get('options', [])

    if not options:
        print("    No options available for this setting")
        return False

    print("    Available options:")
    for i, option in enumerate(options, 1):
        # Get localized option description
        option_localization = option.get('localization', {})
        option_lang_data = option_localization.get(lang, option_localization.get('en', {}))
        description = option_lang_data.get('description', option.get('description', option['name']))

        recommended = t('recommended_text', locale=lang) if option.get('recommended', False) else ""
        print(f"      {i}. {option['name']}: {description}{recommended}")

    print(f"      {len(options) + 1}. Skip this configuration")

    while True:
        try:
            choice = int(input(f"    Choose option (1-{len(options) + 1}): ").strip())
            if choice == len(options) + 1:
                print("    Configuration skipped")
                return True
            elif 1 <= choice <= len(options):
                selected_option = options[choice - 1]
                return save_settings_to_config(selected_option.get('settings', {}), rule_dir)
            else:
                print(f"    Please choose 1-{len(options) + 1}")
        except ValueError:
            print("    Please enter a valid number")

def save_setting_to_config(config, value, rule_dir):
    """Save a single setting value to the plugin's settings.json."""
    settings_key = config.get('settings_key')
    if not settings_key:
        print("    No settings key specified for this configuration")
        return False

    settings_file = rule_dir / "settings.json"
    try:
        import json
        if settings_file.exists():
            with open(settings_file, 'r', encoding='utf-8') as f:
                settings = json.load(f)
        else:
            settings = {}

        # Set nested value using dot notation
        keys = settings_key.split('.')
        current = settings
        for key in keys[:-1]:
            if key not in current:
                current[key] = {}
            current = current[key]
        current[keys[-1]] = value

        with open(settings_file, 'w', encoding='utf-8') as f:
            json.dump(settings, f, indent=2, ensure_ascii=False)

        print(f"    ✓ Setting saved: {settings_key} = {value}")
        return True

    except Exception as e:
        print(f"    Error saving setting: {e}")
        return False

def save_settings_to_config(settings_dict, rule_dir):
    """Save multiple settings to the plugin's settings.json."""
    if not settings_dict:
        return True

    settings_file = rule_dir / "settings.json"
    try:
        import json
        if settings_file.exists():
            with open(settings_file, 'r', encoding='utf-8') as f:
                settings = json.load(f)
        else:
            settings = {}

        # Apply each setting
        for key_path, value in settings_dict.items():
            keys = key_path.split('.')
            current = settings
            for key in keys[:-1]:
                if key not in current:
                    current[key] = {}
                current = current[key]
            current[keys[-1]] = value

        with open(settings_file, 'w', encoding='utf-8') as f:
            json.dump(settings, f, indent=2, ensure_ascii=False)

        print(f"    ✓ Settings saved: {len(settings_dict)} configuration(s)")
        return True

    except Exception as e:
        print(f"    Error saving settings: {e}")
        return False

def configure_memory_retention(settings_file, lang):
    """Configure memory retention policies."""
    try:
        import json
        with open(settings_file, 'r', encoding='utf-8') as f:
            settings = json.load(f)

        # Access cleanup_guidance from within memory_rules section
        memory_rules = settings.get('memory_rules', {})
        cleanup = memory_rules.get('cleanup_guidance', {})

        print("    Current retention settings:")
        print(f"      - Notify overdue memories: {cleanup.get('notify_overdue_memories', 'N/A')}")
        print(f"      - Interactive cleanup: {cleanup.get('interactive_cleanup', 'N/A')}")
        print(f"      - Require user consent: {cleanup.get('require_user_consent', 'N/A')}")

        print("\n    Recommended settings for most users:")
        print("      - notify_overdue_memories: true")
        print("      - interactive_cleanup: true")
        print("      - require_user_consent: true")

        apply = input("    Apply recommended retention settings? (yes/no): ").strip().lower()
        if apply in ['yes', 'y']:
            if 'memory_rules' not in settings:
                settings['memory_rules'] = {}
            if 'cleanup_guidance' not in settings['memory_rules']:
                settings['memory_rules']['cleanup_guidance'] = {}
            settings['memory_rules']['cleanup_guidance'].update({
                'notify_overdue_memories': True,
                'interactive_cleanup': True,
                'require_user_consent': True
            })

            with open(settings_file, 'w', encoding='utf-8') as f:
                json.dump(settings, f, indent=2, ensure_ascii=False)
            print("    ✓ Memory retention settings configured")
        else:
            print("    Settings unchanged")

    except Exception as e:
        print(f"    ✗ Error configuring memory retention: {e}")

def configure_memory_git_analysis(settings_file, lang):
    """Configure git analysis settings."""
    try:
        import json
        with open(settings_file, 'r', encoding='utf-8') as f:
            settings = json.load(f)

        print("    Current git analysis settings:")
        git_analysis = settings.get('git_history_analysis', {})
        print(f"      - Enabled: {git_analysis.get('enabled', 'N/A')}")
        print(f"      - Trigger on unknown context: {git_analysis.get('trigger_on_unknown_context', 'N/A')}")
        print(f"      - Max commits to analyze: {git_analysis.get('max_commits_to_analyze', 'N/A')}")

        print("\n    Recommended settings:")
        print("      - enabled: true (enables git analysis)")
        print("      - trigger_on_unknown_context: true (auto-analyze when context unclear)")
        print("      - max_commits_to_analyze: 50 (balance between detail and performance)")

        apply = input("    Apply recommended git analysis settings? (yes/no): ").strip().lower()
        if apply in ['yes', 'y']:
            if 'git_history_analysis' not in settings:
                settings['git_history_analysis'] = {}
            settings['git_history_analysis'].update({
                'enabled': True,
                'trigger_on_unknown_context': True,
                'max_commits_to_analyze': 50
            })

            with open(settings_file, 'w', encoding='utf-8') as f:
                json.dump(settings, f, indent=2, ensure_ascii=False)
            print("    ✓ Git analysis settings configured")
        else:
            print("    Settings unchanged")

    except Exception as e:
        print(f"    ✗ Error configuring git analysis: {e}")

def configure_memory_storage(settings_file, lang):
    """Configure memory storage settings."""
    try:
        import json
        with open(settings_file, 'r', encoding='utf-8') as f:
            settings = json.load(f)

        print("    Current storage settings:")
        storage = settings.get('storage', {})
        print(f"      - Base path: {storage.get('base_path', 'N/A')}")
        print(f"      - Create directories: {storage.get('create_directories', 'N/A')}")

        print("\n    Note: Base path will be set when copying to your project.")
        print("    This configuration focuses on directory structure.")

        apply = input("    Configure storage structure settings? (yes/no): ").strip().lower()
        if apply in ['yes', 'y']:
            if 'storage' not in settings:
                settings['storage'] = {}
            settings['storage']['create_directories'] = True

            with open(settings_file, 'w', encoding='utf-8') as f:
                json.dump(settings, f, indent=2, ensure_ascii=False)
            print("    ✓ Storage settings configured")
        else:
            print("    Settings unchanged")

    except Exception as e:
        print(f"    ✗ Error configuring storage: {e}")

def configure_rag_context_window(settings_file, lang):
    """Configure RAG context window settings."""
    try:
        import json
        with open(settings_file, 'r', encoding='utf-8') as f:
            settings = json.load(f)

        print("    Current context window settings:")
        context = settings.get('context_optimization', {})
        print(f"      - Max context window: {context.get('max_context_window', 'N/A')}")
        print(f"      - Dynamic adjustment: {context.get('dynamic_adjustment', 'N/A')}")

        print("\n    Recommended settings for most models:")
        print("      - max_context_window: 128000 (tokens, adjust for your model)")
        print("      - dynamic_adjustment: true (adapt to task requirements)")

        apply = input("    Apply recommended context window settings? (yes/no): ").strip().lower()
        if apply in ['yes', 'y']:
            if 'context_optimization' not in settings:
                settings['context_optimization'] = {}
            settings['context_optimization'].update({
                'max_context_window': 128000,
                'dynamic_adjustment': True
            })

            with open(settings_file, 'w', encoding='utf-8') as f:
                json.dump(settings, f, indent=2, ensure_ascii=False)
            print("    ✓ Context window settings configured")
        else:
            print("    Settings unchanged")

    except Exception as e:
        print(f"    ✗ Error configuring context window: {e}")

def configure_rag_relevance(settings_file, lang):
    """Configure RAG relevance thresholds."""
    try:
        import json
        with open(settings_file, 'r', encoding='utf-8') as f:
            settings = json.load(f)

        print("    Current relevance settings:")
        relevance = settings.get('relevance_scoring', {})
        print(f"      - Min relevance score: {relevance.get('min_relevance_score', 'N/A')}")
        print(f"      - Recency weight: {relevance.get('recency_weight', 'N/A')}")

        print("\n    Recommended settings:")
        print("      - min_relevance_score: 0.7 (70% relevance threshold)")
        print("      - recency_weight: 0.3 (30% weight for recent information)")

        apply = input("    Apply recommended relevance settings? (yes/no): ").strip().lower()
        if apply in ['yes', 'y']:
            if 'relevance_scoring' not in settings:
                settings['relevance_scoring'] = {}
            settings['relevance_scoring'].update({
                'min_relevance_score': 0.7,
                'recency_weight': 0.3
            })

            with open(settings_file, 'w', encoding='utf-8') as f:
                json.dump(settings, f, indent=2, ensure_ascii=False)
            print("    ✓ Relevance threshold settings configured")
        else:
            print("    Settings unchanged")

    except Exception as e:
        print(f"    ✗ Error configuring relevance: {e}")

def configure_critical_verification(settings_file, lang):
    """Configure critical thinking verification levels."""
    try:
        import json
        with open(settings_file, 'r', encoding='utf-8') as f:
            settings = json.load(f)

        print("    Current verification settings:")
        verification = settings.get('verification', {})
        print(f"      - Factual claim verification: {verification.get('factual_claim_verification', 'N/A')}")
        print(f"      - Min sources required: {verification.get('min_sources_required', 'N/A')}")

        print("\n    Recommended settings for balanced verification:")
        print("      - factual_claim_verification: true (verify all factual claims)")
        print("      - min_sources_required: 2 (require at least 2 sources for claims)")

        apply = input("    Apply recommended verification settings? (yes/no): ").strip().lower()
        if apply in ['yes', 'y']:
            if 'verification' not in settings:
                settings['verification'] = {}
            settings['verification'].update({
                'factual_claim_verification': True,
                'min_sources_required': 2
            })

            with open(settings_file, 'w', encoding='utf-8') as f:
                json.dump(settings, f, indent=2, ensure_ascii=False)
            print("    ✓ Verification level settings configured")
        else:
            print("    Settings unchanged")

    except Exception as e:
        print(f"    ✗ Error configuring verification: {e}")

def configure_critical_error_handling(settings_file, lang):
    """Configure critical thinking error handling."""
    try:
        import json
        with open(settings_file, 'r', encoding='utf-8') as f:
            settings = json.load(f)

        print("    Current error handling settings:")
        error_handling = settings.get('error_handling', {})
        print(f"      - Immediate error admission: {error_handling.get('immediate_error_admission', 'N/A')}")
        print(f"      - Log corrections: {error_handling.get('log_corrections', 'N/A')}")

        print("\n    Recommended settings:")
        print("      - immediate_error_admission: true (admit errors immediately)")
        print("      - log_corrections: true (store corrections for learning)")

        apply = input("    Apply recommended error handling settings? (yes/no): ").strip().lower()
        if apply in ['yes', 'y']:
            if 'error_handling' not in settings:
                settings['error_handling'] = {}
            settings['error_handling'].update({
                'immediate_error_admission': True,
                'log_corrections': True
            })

            with open(settings_file, 'w', encoding='utf-8') as f:
                json.dump(settings, f, indent=2, ensure_ascii=False)
            print("    ✓ Error handling settings configured")
        else:
            print("    Settings unchanged")

    except Exception as e:
        print(f"    ✗ Error configuring error handling: {e}")

def generate_web_config(activated_rules, ui_lang, script_dir, ui_lang_param, agent_lang):
    """Generate configuration file for the web interface."""
    try:
        web_config = {
            'uiLanguage': ui_lang,
            'agentLanguage': agent_lang,
            'plugins': {}
        }

        # Read setup.json from each activated rule
        for rule in activated_rules:
            rule_dir = script_dir / rule
            setup_file = rule_dir / "setup.json"

            if setup_file.exists():
                with open(setup_file, 'r', encoding='utf-8') as f:
                    setup_data = json.load(f)

                # Extract web-relevant data
                localization = setup_data.get('localization', {})
                lang_data = localization.get(ui_lang, localization.get('en', {}))

                web_config['plugins'][rule] = {
                    'name': rule,
                    'display_name': lang_data.get('plugin_name', rule),
                    'description': lang_data.get('description', ''),
                    'mandatory_config': setup_data.get('mandatory_config', []),
                    'optional_config': setup_data.get('optional_config', [])
                }

        # Write web config file
        web_config_file = script_dir / "web-config.json"
        with open(web_config_file, 'w', encoding='utf-8') as f:
            json.dump(web_config, f, indent=2, ensure_ascii=False)

        print(f"✓ Generated web interface configuration: {web_config_file.name}")

    except Exception as e:
        print(f"Warning: Could not generate web config: {e}")

# ============================================================================
# MAIN FUNCTION
# ============================================================================
def main():
    """Main setup function."""
    parser = argparse.ArgumentParser(description='Setup script for agentic-rules framework')
    available_langs = get_available_languages()
    parser.add_argument('--ui-lang', choices=available_langs, help=f'Interface language ({", ".join(available_langs)})')
    parser.add_argument('--agent-lang', choices=available_langs, help=f'Agent template language ({", ".join(available_langs)})')
    parser.add_argument('--agent-file-type', choices=['AGENTS.md', 'GEMINI.md', 'CLAUDE.md'], help='Agent file type to generate (AGENTS.md/GEMINI.md/CLAUDE.md)')
    parser.add_argument('--lang', choices=available_langs, help=f'Set both UI and agent language ({", ".join(available_langs)})')
    parser.add_argument('--rules', help='Comma-separated list of rules to activate, or "all"')
    parser.add_argument('--config', help='Path to configuration file exported from setup.html')
    args = parser.parse_args()

    script_dir = get_script_directory()

    print("="*70)
    print(t('title'))
    print("="*70)
    print(t('description'))

    # Step 1: Auto-detect rule plugins
    print(f"\n{t('detection_title')}")
    available_rules = detect_rule_plugins(script_dir)

    if not available_rules:
        print(t('detection_none'))
        return

    print(t('detection_found', count=len(available_rules)))
    for rule in available_rules:
        print(f"  - {rule}")

    # Load configuration file if specified
    config = None
    if args.config:
        config = load_config_file(args.config)
        if config:
            # Override settings with config file values
            if 'ui_language' in config:
                args.ui_lang = config['ui_language']
            if 'agent_language' in config:
                args.agent_lang = config['agent_language']
            if 'agent_file_type' in config:
                args.agent_file_type = config['agent_file_type']

    # Step 2: Select languages
    # Handle backward compatibility with --lang
    if args.lang and not (args.ui_lang or args.agent_lang):
        ui_lang = args.lang
        agent_lang = args.lang
    else:
        ui_lang = select_ui_language(args.ui_lang) if not args.ui_lang else args.ui_lang
        agent_lang = select_agent_language(args.agent_lang, ui_lang) if not args.agent_lang else args.agent_lang

    print(f"\n{t('ui_lang_selected', locale=ui_lang, lang=ui_lang.upper())}")
    print(f"{t('agent_lang_selected', locale=ui_lang, lang=agent_lang.upper())}")

    # Step 3: Select agent file type
    agent_file_type = select_agent_file_type(args.agent_file_type, ui_lang)

    print(f"{t('file_type_selected', locale=ui_lang, type=agent_file_type)}")

    # Step 4: Select rules to activate
    selected_rules = select_rules(available_rules, args.rules, ui_lang)

    if not selected_rules:
        print(f"\n{t('rules_none_selected', locale=ui_lang)}")
        return

    print(f"\n{t('rules_selected', locale=ui_lang, rules=', '.join(selected_rules))}")

    # Step 4: Select plugin languages (if not using config file)
    plugin_languages = {}
    if not config:
        plugin_languages = select_plugin_languages(selected_rules, agent_lang, ui_lang, script_dir)
    else:
        # Extract plugin languages from config
        if 'selected_rules' in config:
            for rule, rule_config in config['selected_rules'].items():
                if isinstance(rule_config, dict) and 'language' in rule_config:
                    plugin_languages[rule] = rule_config['language']

    # Step 5: Generate root integration file
    if selected_rules:
        root_file_activated, root_errors = generate_root_file(selected_rules, agent_lang, agent_file_type, script_dir, ui_lang)
        activated = selected_rules if root_file_activated else []
        errors = root_errors
    else:
        activated = []
        errors = []

    # Step 5: Activate rule templates
    if activated:
        rule_activated, rule_errors = activate_rule_templates(selected_rules, agent_lang, agent_file_type, script_dir, ui_lang, config, plugin_languages)
        # Keep activated list as is, but collect errors
        errors.extend(rule_errors)

    # Step 5: Configure rule settings (optional)
    if activated:
        configured = configure_rule_settings(activated, ui_lang, script_dir, ui_lang)

    # Step 6: Generate web interface config (if web interface exists)
    if activated:
        generate_web_config(activated, ui_lang, script_dir, ui_lang, agent_lang)

    # Step 7: Show results
    print(f"\n{t('completion_title', locale=ui_lang)}")

    if activated:
        print(f"\n{t('completion_summary', locale=ui_lang, count=len(activated))}")
        for rule in activated:
            print(f"  ✓ {rule}")

    if errors:
        print(f"\nErrors encountered:")
        for error in errors:
            print(f"  ✗ {error}")

    if activated:
        print(f"\n{t('completion_next_steps', locale=ui_lang)}")
        print(t('completion_step_1', locale=ui_lang))
        print(t('completion_step_2', locale=ui_lang))
        print(t('completion_step_3', locale=ui_lang))
        print(t('completion_step_4', locale=ui_lang))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\nSetup cancelled by user.")
        sys.exit(1)
