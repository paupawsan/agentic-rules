#!/usr/bin/env python3
# Copyright (c) 2025 Paulus Ery Wasito Adhi
#
# Licensed under the MIT License. See LICENSE file for details.
#
# Agentic Rules Framework - Web Config Generator
# ==============================================
#
# Generates static web-config.json from plugins.json and individual setup.json files.
# This allows setup.html to work completely standalone without requiring Python or web servers.
#
# Usage:
#     python generate_simple_setup.py
#
# Output:
#     web-config.json - Static configuration file for setup.html
#
# Workflow:
# 1. Plugin developers add/modify plugins in plugins.json and setup.json files
# 2. Run this script to generate updated web-config.json
# 3. Commit web-config.json to repository
# 4. End users just double-click setup.html for full setup experience

import json
import os
from pathlib import Path

def load_localization():
    """Load localization data from JSON file."""
    loc_file = Path("localization.json")
    if loc_file.exists():
        try:
            with open(loc_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Warning: Could not load localization.json: {e}")
    return None

def get_available_languages(script_dir=None):
    """Get list of available languages from installed plugin templates."""
    if script_dir is None:
        script_dir = Path('.')

    installed_languages = set()

    try:
        # Check plugins.json for plugin directories
        plugins_manifest = load_json_file('plugins.json')
        if plugins_manifest:
            plugin_names = plugins_manifest.get('plugins', [])
            for plugin_name in plugin_names:
                plugin_dir = script_dir / plugin_name
                if plugin_dir.exists() and plugin_dir.is_dir():
                    # Look for RULES.md.* files
                    for rules_file in plugin_dir.glob('RULES.md.*'):
                        if rules_file.is_file():
                            lang = rules_file.suffix[1:]  # Remove leading dot
                            installed_languages.add(lang)

        # Check for root template files
        for rules_file in script_dir.glob('RULES.md.*'):
            if rules_file.is_file():
                lang = rules_file.suffix[1:]  # Remove leading dot
                installed_languages.add(lang)

    except Exception as e:
        print(f"Warning: Could not scan for installed languages: {e}")

    # Ensure English is always available as fallback
    installed_languages.add('en')

    return sorted(list(installed_languages))

def get_default_language():
    """Get the default language (first available language)."""
    languages = get_available_languages()
    return languages[0] if languages else 'en'

def load_json_file(filepath):
    """Load and parse a JSON file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return None

def generate_web_config():
    """Generate web-config.json from plugins.json and setup.json files."""

    # Load plugin manifest
    plugins_manifest = load_json_file('plugins.json')
    if not plugins_manifest:
        print("❌ Error: plugins.json not found or invalid")
        return None

    plugin_names = plugins_manifest.get('plugins', [])
    if not plugin_names:
        print("❌ Error: No plugins defined in plugins.json")
        return None

    print(f"📦 Found {len(plugin_names)} plugins: {', '.join(plugin_names)}")

    # Initialize web config
    default_lang = get_default_language()
    available_langs = get_available_languages()
    web_config = {
        "version": "1.1.0",
        "description": "Static web configuration generated from setup.json files",
        "availableLanguages": available_langs,
        "uiLanguage": default_lang,
        "agentLanguage": default_lang,
        "plugins": {}
    }

    # Load each plugin's configuration
    loaded_plugins = 0
    for plugin_name in plugin_names:
        plugin_dir = Path(plugin_name)
        setup_file = plugin_dir / 'setup.json'

        if not setup_file.exists():
            print(f"⚠️  Warning: {setup_file} not found, skipping {plugin_name}")
            continue

        setup_data = load_json_file(setup_file)
        if not setup_data:
            print(f"⚠️  Warning: Invalid setup.json for {plugin_name}, skipping")
            continue

        # Extract localization data
        localization = setup_data.get('localization', {})
        available_langs = get_available_languages()

        # Read RULES.md template files for all available languages
        template_content = {}
        template_dir = plugin_dir
        for lang in available_langs:
            template_file = template_dir / f'RULES.md.{lang}'
            if template_file.exists():
                try:
                    with open(template_file, 'r', encoding='utf-8') as f:
                        template_content[lang] = f.read()
                        print(f"✅ Loaded template: {plugin_name}/RULES.md.{lang}")
                except Exception as e:
                    print(f"⚠️  Warning: Could not read {template_file}: {e}")
            else:
                # Template doesn't exist for this language
                print(f"ℹ️  No template for {plugin_name}/RULES.md.{lang}")

        # Read default settings.json template
        default_settings = {}
        settings_file = plugin_dir / 'settings.json'
        if settings_file.exists():
            default_settings_data = load_json_file(settings_file)
            if default_settings_data:
                # Extract the plugin-specific settings (remove metadata and version)
                plugin_key = plugin_name.replace('-', '_')  # Convert kebab-case to snake_case
                if plugin_key in default_settings_data:
                    default_settings = default_settings_data[plugin_key]
                # Also include any root-level settings that might be relevant
                for key, value in default_settings_data.items():
                    if key not in ['_metadata', 'version', plugin_key]:
                        default_settings[key] = value

        # For backward compatibility, ensure en and ja locals are available
        en_local = localization.get('en', {})
        ja_local = localization.get('ja', {})

        # Determine display name and description with fallback to plugin's native language
        display_name = plugin_name
        description = ''

        if en_local.get('plugin_name'):
            # Use English if available
            display_name = en_local['plugin_name']
            description = en_local.get('description', '')
        else:
            # Fall back to plugin's native language
            available_langs = list(localization.keys())
            if available_langs:
                # Use the first available language
                native_local = localization[available_langs[0]]
                display_name = native_local.get('plugin_name', plugin_name)
                description = native_local.get('description', '')

        # Build plugin config for web interface
        plugin_config = {
            "name": plugin_name,
            "display_name": display_name,
            "description": description,
            "localization": localization,
            "mandatory_config": setup_data.get('mandatory_config', []),
            "optional_config": setup_data.get('optional_config', []),
            "default_settings": default_settings,
            "templates": template_content
        }

        web_config["plugins"][plugin_name] = plugin_config
        loaded_plugins += 1
        print(f"✅ Loaded {plugin_name}")

    if loaded_plugins == 0:
        print("❌ Error: No valid plugins could be loaded")
        return None

    # Load root RULES.md templates for all available languages
    root_templates = {}
    available_langs = get_available_languages()
    for lang in available_langs:
        root_template_file = Path(f'RULES.md.{lang}')
        if root_template_file.exists():
            try:
                with open(root_template_file, 'r', encoding='utf-8') as f:
                    root_templates[lang] = f.read()
                print(f"✅ Loaded root template: RULES.md.{lang}")
            except Exception as e:
                print(f"⚠️  Warning: Could not read root template RULES.md.{lang}: {e}")
        else:
            print(f"⚠️  Warning: Root template RULES.md.{lang} not found")

    # Add root templates to web config
    if root_templates:
        web_config["rootTemplates"] = root_templates

    print(f"🎉 Successfully loaded {loaded_plugins} plugins")
    return web_config

def generate_language_options(web_config, supported_langs=None):
    """Generate HTML options for language selectors based on available languages."""
    if supported_langs is None:
        available_langs = web_config.get('availableLanguages', ['en'])
    else:
        available_langs = supported_langs

    localization = load_localization() or {}

    options = []
    for lang in available_langs:
        # Try to get localized name from localization.json
        option_text = None

        # Check for lang_option keys in the localization data
        if lang in localization:
            lang_data = localization[lang]
            # Look for language option keys (lang_option_1, lang_option_2, etc.)
            for i, avail_lang in enumerate(available_langs):
                option_key = f"lang_option_{i + 1}"
                if option_key in lang_data and avail_lang == lang:
                    option_text = lang_data[option_key]
                    break

        # If not found in localization, use language table
        if not option_text:
            from generate_plugin_scaffold import get_language_table
            lang_table = get_language_table()
            if lang in lang_table:
                lang_info = lang_table[lang]
                flag = lang_info.get('flag', '🏳️')
                native = lang_info.get('native', lang.upper())
                option_text = f"{flag} {native}"
            else:
                option_text = lang.upper()

        options.append(f'<option value="{lang}">{option_text}</option>')

    return '\n'.join(options)

def embed_config_in_html(web_config):
    """Embed the web config into setup.html as a JavaScript variable and update language options."""

    # Convert config to JavaScript format
    js_config = f"const staticWebConfig = {json.dumps(web_config, indent=2, ensure_ascii=False)};"

    # Generate root language options (only en/ja/id for agent-language selector)
    root_languages = ['en', 'ja', 'id']
    root_language_options = generate_language_options(web_config, root_languages)

    # Read setup.html
    try:
        with open('setup.html', 'r', encoding='utf-8') as f:
            html_content = f.read()
    except Exception as e:
        print(f"❌ Error reading setup.html: {e}")
        return False

    import re

    # Look for the consolidated AUTO GENERATED STATICWEBCONFIG markers
    start_marker = '  // ---AUTO GENERATED STATICWEBCONFIG START---'
    end_marker = '  // ---AUTO GENERATED STATICWEBCONFIG END---'

    start_pos = html_content.find(start_marker)
    if start_pos == -1:
        print("❌ Error: Could not find staticWebConfig start marker in setup.html")
        return False

    end_pos = html_content.find(end_marker, start_pos)
    if end_pos == -1:
        print("❌ Error: Could not find staticWebConfig end marker in setup.html")
        return False

    # Replace the content between markers
    start_replace_pos = start_pos + len(start_marker) + 1  # +1 for newline
    end_replace_pos = end_pos

    # Create the replacement content (without markers, just the staticWebConfig)
    static_config_only = f'  const staticWebConfig = {json.dumps(web_config, indent=2, ensure_ascii=False)};'

    # Replace staticWebConfig section
    new_html = html_content[:start_replace_pos] + static_config_only + html_content[end_replace_pos:]

    # Replace Agent language selector with only root languages (en/ja/id)
    # Find the agent-language select element and its auto-generated content
    agent_select_pattern = '<select id="agent-language"'
    agent_select_pos = new_html.find(agent_select_pattern)
    if agent_select_pos != -1:
        # Find the auto-generated content within this select
        agent_start_marker = '<!-- AUTO GENERATED CONTENT START -->'
        agent_end_marker = '<!-- AUTO GENERATED CONTENT END -->'

        # Start looking for markers after the select element
        search_start = agent_select_pos + len(agent_select_pattern)
        agent_start_pos = new_html.find(agent_start_marker, search_start)
        if agent_start_pos != -1:
            agent_end_pos = new_html.find(agent_end_marker, agent_start_pos)
            if agent_end_pos != -1:
                agent_start_replace = agent_start_pos + len(agent_start_marker)
                agent_end_replace = agent_end_pos
                new_html = new_html[:agent_start_replace] + f'\n{root_language_options}\n            ' + new_html[agent_end_replace:]


    # Write back to setup.html
    try:
        with open('setup.html', 'w', encoding='utf-8') as f:
            f.write(new_html)

        print("✅ Replaced staticWebConfig in setup.html")
        print(f"✅ Updated language options: {', '.join(root_languages)}")
        return True

    except Exception as e:
        print(f"❌ Error writing setup.html: {e}")
        return False

def main():
    """Main function."""
    print("🤖 Agentic Rules Framework - Web Config Generator")
    print("=" * 50)

    # Check if we're in the right directory
    if not Path('plugins.json').exists():
        print("❌ Error: plugins.json not found. Please run from the agentic-rules root directory.")
        return 1

    # Generate web config
    web_config = generate_web_config()
    if not web_config:
        return 1

    # Write web-config.json
    output_file = 'web-config.json'
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(web_config, f, indent=2, ensure_ascii=False)

        print(f"💾 Generated {output_file}")
        print(f"📊 Contains {len(web_config['plugins'])} plugins")

        # Show summary
        print("\n📋 Plugin Summary:")
        for name, config in web_config['plugins'].items():
            display_name = config.get('display_name', name)
            print(f"   • {display_name} ({name})")

        print(f"\n✅ {output_file} ready for commit!")
        print("📝 Next: git add web-config.json && git commit -m 'Update web config'")

        # Embed config into setup.html
        embed_config_in_html(web_config)

    except Exception as e:
        print(f"❌ Error writing {output_file}: {e}")
        return 1

    return 0

if __name__ == "__main__":
    exit(main())
