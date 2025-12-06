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

def get_available_languages():
    """Get list of available languages from localization data."""
    localization = load_localization()
    if localization and '_comment' in localization:
        # Remove metadata key and return language codes
        return [lang for lang in localization.keys() if lang != '_comment']
    return list(localization.keys()) if localization else ['en']

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
    web_config = {
        "version": "0.1.0",
        "description": "Static web configuration generated from setup.json files",
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
                except Exception as e:
                    print(f"⚠️  Warning: Could not read {template_file}: {e}")

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

def embed_config_in_html(web_config):
    """Embed the web config into setup.html as a JavaScript variable."""

    # Convert config to JavaScript format
    js_config = f"const staticWebConfig = {json.dumps(web_config, indent=2, ensure_ascii=False)};"

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

    # Write back to setup.html
    try:
        with open('setup.html', 'w', encoding='utf-8') as f:
            f.write(new_html)

        print("✅ Replaced staticWebConfig in setup.html")
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
