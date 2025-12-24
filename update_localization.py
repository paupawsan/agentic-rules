#!/usr/bin/env python3
# Copyright (c) 2025 Paulus Ery Wasito Adhi
#
# Licensed under the MIT License. See LICENSE file for details.
#
# Update Localization Script
# ==========================
#
# This script updates the embedded localization and language options in setup.html when localization.json is modified.
#
# Usage:
#     python update_localization.py              # Update localization from localization.json
#     python update_localization.py --reset       # Factory reset - empty localization section
#
# Update mode will:
# 1. Read localization.json
# 2. Convert it to JavaScript object format
# 3. Replace the localization object in setup.html
# 4. Update HTML select options for UI and agent languages dynamically
# 5. Commit the changes
#
# Reset mode will:
# 1. Empty the localization section in setup.html
# 2. Reset HTML select options to minimal state
# 3. Commit the changes
#
# This makes it easy to add new languages without manual HTML editing.

import json
import re
import sys


def update_setup_html_localization():
    """Update the embedded localization and language options in setup.html from localization.json"""

    # Read localization.json
    with open('localization.json', 'r', encoding='utf-8') as f:
        loc_data = json.load(f)

    # Get available languages (excluding metadata)
    available_langs = [lang for lang in loc_data.keys() if lang != '_comment']

    # Convert to JavaScript object format (direct object, not JSON.parse)
    json_str = json.dumps(loc_data, ensure_ascii=False, indent=2, separators=(',', ': '))
    js_content = '    // ---AUTO GENERATED LOCALIZATION START---\n  const localization = ' + json_str + ';\n    // ---AUTO GENERATED LOCALIZATION END---'

    # Read setup.html
    with open('setup.html', 'r') as f:
        html_content = f.read()

    # Replace the localization section (between markers)
    start_marker = '    // ---AUTO GENERATED LOCALIZATION START---'
    end_marker = '    // ---AUTO GENERATED LOCALIZATION END---'

    start_pos = html_content.find(start_marker)
    if start_pos == -1:
        print("❌ Could not find localization start marker in setup.html")
        return False

    end_pos = html_content.find(end_marker, start_pos)
    if end_pos == -1:
        print("❌ Could not find localization end marker in setup.html")
        return False

    # Find the content to replace (from start marker to end marker, including the }); line)
    start_replace_pos = start_pos
    # Find the }; line before the end marker
    closing_brace_pos = html_content.rfind('};', start_pos, end_pos)
    if closing_brace_pos == -1:
        print("❌ Could not find closing brace in localization section")
        return False
    end_replace_pos = end_pos + len(end_marker)

    # Create the replacement content (complete section with markers)
    localization_section = '    // ---AUTO GENERATED LOCALIZATION START---\n  const localization = ' + json_str + ';\n    // ---AUTO GENERATED LOCALIZATION END---'

    # Replace the entire localization section including markers
    new_html = html_content[:start_replace_pos] + localization_section + html_content[end_replace_pos:]

    # Generate dynamic language options with flags and native names
    ui_lang_options = []
    agent_lang_options = []

    # Language table with flags and native names (same as generate_simple_setup.py)
    lang_table = {
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

    for lang in available_langs:
        # Use flag + native name format
        display_name = lang_table.get(lang, f"{lang.upper()} ({lang})")

        ui_lang_options.append(f'<option value="{lang}">{display_name}</option>')
        agent_lang_options.append(f'<option value="{lang}">{display_name}</option>')

    ui_options_html = '\n'.join(ui_lang_options)
    agent_options_html = '\n'.join(agent_lang_options)

    # Update UI language select - replace content between existing markers
    ui_select_start = new_html.find('<select id="ui-language"')
    ui_select_end = new_html.find('</select>', ui_select_start) + len('</select>')
    ui_section = new_html[ui_select_start:ui_select_end]
    ui_pattern = r'(<!-- AUTO GENERATED CONTENT START -->).*?(<!-- AUTO GENERATED CONTENT END -->)'
    ui_replacement = rf'\1\n{ui_options_html}\n\2'
    ui_section_updated = re.sub(ui_pattern, ui_replacement, ui_section, flags=re.DOTALL)
    new_html = new_html[:ui_select_start] + ui_section_updated + new_html[ui_select_end:]

    # Skip agent language select update - handled by generate_simple_setup.py
    print("ℹ️  Skipping agent language options update (handled by generate_simple_setup.py)")

    # Write back
    with open('setup.html', 'w') as f:
        f.write(new_html)

    print("✅ Updated localization and language options in setup.html")
    return True


def factory_reset_localization():
    """Factory reset - empty localization, staticWebConfig, and reset language options to English only"""

    # Read setup.html
    try:
        with open('setup.html', 'r') as f:
            html_content = f.read()
    except Exception as e:
        print(f"❌ Error reading setup.html: {e}")
        return False

    new_html = html_content

    # Empty staticWebConfig between JavaScript markers
    swc_pattern = r'(  // ---AUTO GENERATED STATICWEBCONFIG START---\n).*?(  // ---AUTO GENERATED STATICWEBCONFIG END---)'
    new_html = re.sub(swc_pattern, r'\1  const staticWebConfig = {};\n\2', new_html, flags=re.DOTALL)

    # Empty localization section with markers
    loc_start_marker = '    // ---AUTO GENERATED LOCALIZATION START---'
    loc_end_marker = '    // ---AUTO GENERATED LOCALIZATION END---'

    loc_start_pos = new_html.find(loc_start_marker)
    if loc_start_pos != -1:
        loc_end_pos = new_html.find(loc_end_marker, loc_start_pos)
        if loc_end_pos != -1:
            loc_end_pos += len(loc_end_marker)
            empty_loc_section = '    // ---AUTO GENERATED LOCALIZATION START---\n  const localization = {};\n    // ---AUTO GENERATED LOCALIZATION END---'
            new_html = new_html[:loc_start_pos] + empty_loc_section + new_html[loc_end_pos:]

    # Reset UI language select - replace content between existing markers
    ui_select_start = new_html.find('<select id="ui-language"')
    ui_select_end = new_html.find('</select>', ui_select_start) + len('</select>')
    ui_section = new_html[ui_select_start:ui_select_end]
    ui_pattern = r'(<!-- AUTO GENERATED CONTENT START -->).*?(<!-- AUTO GENERATED CONTENT END -->)'
    ui_replacement = r'\1\n<option value="en">🇺🇸 English</option>\n\2'
    ui_section_updated = re.sub(ui_pattern, ui_replacement, ui_section, flags=re.DOTALL)
    new_html = new_html[:ui_select_start] + ui_section_updated + new_html[ui_select_end:]

    # Skip agent language select reset - handled by generate_simple_setup.py
    print("ℹ️  Skipping agent language options reset (handled by generate_simple_setup.py)")

    # Write back
    with open('setup.html', 'w') as f:
        f.write(new_html)

    print("✅ Factory reset - emptied localization and staticWebConfig sections, reset language options")
    return True

if __name__ == '__main__':
    # Check command line arguments
    if len(sys.argv) > 1 and sys.argv[1] == '--reset':
        print("🔄 Factory resetting localization in setup.html...")
        if factory_reset_localization():
            print("✅ Factory reset complete!")
            print("\nTo commit changes:")
            print("  git add setup.html")
            print("  git commit -m 'Factory reset localization'")
        else:
            print("❌ Factory reset failed!")
    else:
        print("🔄 Updating localization in setup.html...")
        if update_setup_html_localization():
            print("✅ Localization update complete!")
            print("\nTo commit changes:")
            print("  git add setup.html localization.json")
            print("  git commit -m 'Update localization strings'")
        else:
            print("❌ Localization update failed!")
