#!/usr/bin/env python3
# Copyright (c) 2025 Paulus Ery Wasito Adhi
#
# Licensed under the MIT License. See LICENSE file for details.
#
# Plugin Scaffold Generator for Agentic Rules Framework
# ====================================================
#
# This script generates a minimal scaffold for new agentic rules plugins.
# It creates all required files and directory structure for plugin development.
#
# Usage:
#   python generate_plugin_scaffold.py [--name plugin-name] [--langs en,ja,id]
#
# Features:
# - Interactive plugin creation wizard
# - Multi-language support (en/ja/id/zh)
# - Generates all required files (RULES.md.*, settings.json, setup.json, README.md)
# - Optional automatic registration in plugins.json
# - Validation and error checking

import argparse
import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path
import sys
from datetime import datetime

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================
def get_script_directory():
    """Get the directory where this script is located."""
    return Path(__file__).parent.absolute()

def get_current_year():
    """Get the current year for copyright notices."""
    return datetime.now().year

def get_creation_timestamp():
    """Get the current timestamp in ISO format for creation metadata."""
    return datetime.now().isoformat()

def get_scaffold_config():
    """Get scaffold configuration from global settings."""
    try:
        # Read global settings
        script_dir = get_script_directory()
        settings_file = script_dir / "settings" / "global-settings.json"

        if not settings_file.exists():
            # Fallback to default config
            return {
                "template_version": "1.0.0",
                "template_tag_format": "Template_{version}",
                "github_repo": "https://github.com/paupawsan/agentic-rules",
                "prefer_local_templates": True,
                "template_cache_enabled": True
            }

        with open(settings_file, 'r', encoding='utf-8') as f:
            settings = json.load(f)

        scaffold_config = settings.get("agentic_rules_framework", {}).get("scaffold_config", {})

        # Merge with defaults
        defaults = {
            "template_version": "1.0.0",
            "template_tag_format": "Template_{version}",
            "github_repo": "https://github.com/paupawsan/agentic-rules",
            "prefer_local_templates": True,
            "template_cache_enabled": True
        }

        for key, value in defaults.items():
            if key not in scaffold_config:
                scaffold_config[key] = value

        return scaffold_config

    except Exception as e:
        print(f"⚠️  Warning: Could not read scaffold config: {e}")
        return {
            "template_version": "1.0.0",
            "template_tag_format": "Template_{version}",
            "github_repo": "https://github.com/paupawsan/agentic-rules",
            "prefer_local_templates": True,
            "template_cache_enabled": True
        }

def get_template_tag_name(scaffold_config=None):
    """Get the template tag name based on configuration."""
    if scaffold_config is None:
        scaffold_config = get_scaffold_config()

    template_version = scaffold_config["template_version"]
    tag_format = scaffold_config["template_tag_format"]

    return tag_format.format(version=template_version)

def clone_templates_branch():
    """Clone the Template tag to a temporary directory and return the path.
    Falls back to downloading from GitHub if local git access fails."""

    scaffold_config = get_scaffold_config()
    template_tag = get_template_tag_name(scaffold_config)
    prefer_local = scaffold_config.get("prefer_local_templates", True)
    temp_dir = Path(tempfile.mkdtemp(prefix="agentic-templates-"))

    try:
        # First try: Use local git worktree (preferred method) if enabled
        if prefer_local:
            try:
                # Get the current repository root
                repo_root = subprocess.run(
                    ["git", "rev-parse", "--show-toplevel"],
                    capture_output=True, text=True, check=True,
                    cwd=get_script_directory()
                ).stdout.strip()

                # Check if the tag exists locally
                tag_check = subprocess.run(
                    ["git", "tag", "-l", template_tag],
                    capture_output=True, text=True,
                    cwd=repo_root
                )
                if template_tag not in tag_check.stdout.strip():
                    print(f"⚠️  Local tag '{template_tag}' not found, will download from GitHub")
                    raise FileNotFoundError(f"Tag {template_tag} not found locally")

                # Use git worktree to create a temporary worktree for the Template tag
                subprocess.run(
                    ["git", "worktree", "add", "--detach", str(temp_dir), f"tags/{template_tag}"],
                    check=True, capture_output=True,
                    cwd=repo_root
                )

                templates_dir = temp_dir / "templates"
                if not templates_dir.exists():
                    print(f"⚠️  Templates directory not found in worktree for tag '{template_tag}', checking if tag contains templates...")
                    # The tag might exist but the templates directory might not be at the root
                    # Let's check if there are any files in the worktree
                    worktree_files = list(temp_dir.glob("*"))
                    if worktree_files:
                        print(f"Worktree contains: {[f.name for f in worktree_files]}")
                        # If the tag exists but templates dir doesn't exist at root, it might be structured differently
                        raise FileNotFoundError(f"Templates directory not found in {template_tag}: {templates_dir}")
                    else:
                        raise FileNotFoundError(f"Worktree for tag '{template_tag}' appears to be empty")

                print(f"📥 Using local tag '{template_tag}'")
                return temp_dir

            except (subprocess.CalledProcessError, FileNotFoundError):
                # Local git method failed, try downloading from GitHub
                print(f"📥 Local tag '{template_tag}' not available, downloading from GitHub...")

        # Download from GitHub if local is disabled or failed

            # Clean up the failed git worktree attempt
            cleanup_templates_clone(temp_dir)
            temp_dir = Path(tempfile.mkdtemp(prefix="agentic-templates-"))

            # Download from GitHub as zip
            import urllib.request
            import zipfile

            # Get the remote repository URL
            try:
                remote_url = subprocess.run(
                    ["git", "config", "--get", "remote.origin.url"],
                    capture_output=True, text=True, check=True,
                    cwd=repo_root
                ).stdout.strip()

                # Convert SSH URL to HTTPS if needed
                if remote_url.startswith("git@github.com:"):
                    remote_url = remote_url.replace("git@github.com:", "https://github.com/")

                # Remove .git suffix if present
                if remote_url.endswith(".git"):
                    remote_url = remote_url[:-4]

                # Construct zip download URL for Template tag
                zip_url = f"{remote_url}/archive/refs/tags/{template_tag}.zip"
                zip_path = temp_dir / "template.zip"

                print(f"📦 Downloading templates from tag '{template_tag}': {zip_url}")

                # Download the zip file
                with urllib.request.urlopen(zip_url) as response:
                    with open(zip_path, 'wb') as f:
                        f.write(response.read())

                # Extract the zip file
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(temp_dir)

                # Find the extracted directory (GitHub zip includes tag name)
                extracted_dirs = [d for d in temp_dir.iterdir() if d.is_dir() and d.name != "__MACOSX"]
                if not extracted_dirs:
                    raise RuntimeError("No directories found in downloaded zip")

                templates_dir = extracted_dirs[0] / "templates"
                if not templates_dir.exists():
                    raise FileNotFoundError(f"Templates directory not found in downloaded zip: {templates_dir}")

                print("✅ Templates downloaded and extracted successfully")
                return temp_dir

            except Exception as e:
                # Cleanup on failure
                cleanup_templates_clone(temp_dir)
                raise RuntimeError(f"Failed to download templates from GitHub: {e}") from e

    except Exception as e:
        # Cleanup on failure
        cleanup_templates_clone(temp_dir)
        raise e

def cleanup_templates_clone(temp_dir):
    """Clean up the cloned/downloaded templates directory."""
    if temp_dir and temp_dir.exists():
        try:
            # Try to remove git worktree first (for local git method)
            subprocess.run(
                ["git", "worktree", "remove", str(temp_dir)],
                capture_output=True
            )
        except OSError:
            pass  # git not available
        # Fallback to regular directory removal (for zip download or failed git worktree)
        if temp_dir.exists():
            shutil.rmtree(temp_dir, ignore_errors=True)

def load_template(template_path, variables):
    """Load a template file and substitute variables."""
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Substitute variables
        for key, value in variables.items():
            placeholder = "{{" + key + "}}"
            content = content.replace(placeholder, str(value))

        return content
    except Exception as e:
        raise RuntimeError(f"Failed to load template {template_path}: {e}") from e

def get_existing_plugins():
    """Get list of existing plugin directories."""
    script_dir = get_script_directory()
    plugins = []
    modules_dir = script_dir / "modules"

    if modules_dir.exists():
        for item in modules_dir.iterdir():
            if item.is_dir() and not item.name.startswith('.') and item.name not in ['docs', '__pycache__']:
                # Check if it has the required plugin files
                if (item / "settings.json").exists() and any((item / f"RULES.md.{lang}").exists() for lang in ['en', 'ja', 'id', 'zh']):
                    plugins.append(item.name)

    return sorted(plugins)

def copy_from_template(template_plugin, new_plugin_name, new_display_name, new_description, templates_dir=None):
    """Copy files from an existing plugin as template."""
    script_dir = get_script_directory()
    template_dir = script_dir / "modules" / template_plugin
    new_plugin_dir = script_dir / "modules" / new_plugin_name
    current_year = get_current_year()

    if not template_dir.exists():
        raise ValueError(f"Template plugin '{template_plugin}' does not exist")

    print(f"📋 Using '{template_plugin}' as template...")

    # Copy all files from template
    import shutil

    # Get template plugin info
    setup_file = template_dir / "setup.json"
    template_display_name = new_display_name
    template_description = new_description

    if setup_file.exists():
        try:
            with open(setup_file, 'r', encoding='utf-8') as f:
                setup_data = json.load(f)
                localization = setup_data.get('localization', {})
                en_local = localization.get('en', {})
                if not template_display_name:
                    template_display_name = en_local.get('plugin_name', new_plugin_name)
                if not template_description:
                    template_description = en_local.get('description', '')
        except Exception as e:
            print(f"⚠️  Could not read template setup.json: {e}")

    # Copy all relevant files
    for item in template_dir.iterdir():
        if item.is_file() and item.suffix not in ['.backup']:
            dest_file = new_plugin_dir / item.name

            if item.name.startswith('RULES.md.'):
                # Copy and modify rule templates
                lang = item.suffix[1:]  # Remove leading dot
                content = generate_rules_template(new_plugin_name, template_display_name, template_description, lang, current_year, templates_dir)
                with open(dest_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✓ Generated {item.name} (modified from template)")

            elif item.name == 'settings.json':
                # Copy and modify settings
                content = generate_settings_json(new_plugin_name, template_display_name, True, current_year, templates_dir)
                with open(dest_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✓ Generated settings.json (modified from template)")

            elif item.name == 'setup.json':
                # Copy and modify setup config
                available_langs = []
                for rules_file in template_dir.glob("RULES.md.*"):
                    lang = rules_file.suffix[1:]
                    if lang in ['en', 'ja', 'id', 'zh']:
                        available_langs.append(lang)

                if not available_langs:
                    available_langs = ['en']

                content = generate_setup_json(new_plugin_name, template_display_name, template_description, available_langs, current_year, templates_dir)
                with open(dest_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✓ Generated setup.json (modified from template)")

            elif item.name == 'README.md':
                # Generate new README
                content = generate_readme(new_plugin_name, template_display_name, template_description, current_year, templates_dir)
                with open(dest_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✓ Generated README.md (new)")

            else:
                # Copy other files as-is
                shutil.copy2(item, dest_file)
                print(f"✓ Copied {item.name}")

    return template_display_name, template_description

def kebab_to_title_case(kebab_name):
    """Convert kebab-case to Title Case."""
    return ' '.join(word.capitalize() for word in kebab_name.split('-'))

def kebab_to_pascal_case(kebab_name):
    """Convert kebab-case to PascalCase."""
    return ''.join(word.capitalize() for word in kebab_name.split('-'))

def get_available_languages():
    """Get all available language codes from the comprehensive table."""
    return list(get_language_table().keys())

def get_language_table():
    """Get comprehensive language table with full information for all ISO 639-1 codes."""
    return {
        # Core framework languages (with templates)
        'en': {'name': 'English', 'native': 'English', 'flag': '🇺🇸', 'supported': True},
        'ja': {'name': 'Japanese', 'native': '日本語', 'flag': '🇯🇵', 'supported': True},
        'id': {'name': 'Indonesian', 'native': 'Bahasa Indonesia', 'flag': '🇮🇩', 'supported': True},
        'zh': {'name': 'Chinese', 'native': '中文', 'flag': '🇨🇳', 'supported': False},

        # European Languages
        'af': {'name': 'Afrikaans', 'native': 'Afrikaans', 'flag': '🇿🇦', 'supported': False},
        'sq': {'name': 'Albanian', 'native': 'Shqip', 'flag': '🇦🇱', 'supported': False},
        'am': {'name': 'Amharic', 'native': 'አማርኛ', 'flag': '🇪🇹', 'supported': False},
        'ar': {'name': 'Arabic', 'native': 'العربية', 'flag': '🇸🇦', 'supported': False},
        'hy': {'name': 'Armenian', 'native': 'Հայերեն', 'flag': '🇦🇲', 'supported': False},
        'az': {'name': 'Azerbaijani', 'native': 'Azərbaycan dili', 'flag': '🇦🇿', 'supported': False},
        'eu': {'name': 'Basque', 'native': 'Euskera', 'flag': '🇪🇸', 'supported': False},
        'be': {'name': 'Belarusian', 'native': 'Беларуская', 'flag': '🇧🇾', 'supported': False},
        'bn': {'name': 'Bengali', 'native': 'বাংলা', 'flag': '🇧🇩', 'supported': False},
        'bs': {'name': 'Bosnian', 'native': 'Bosanski', 'flag': '🇧🇦', 'supported': False},
        'bg': {'name': 'Bulgarian', 'native': 'Български', 'flag': '🇧🇬', 'supported': False},
        'ca': {'name': 'Catalan', 'native': 'Català', 'flag': '🇪🇸', 'supported': False},
        'ceb': {'name': 'Cebuano', 'native': 'Cebuano', 'flag': '🇵🇭', 'supported': False},
        'ny': {'name': 'Chichewa', 'native': 'Chichewa', 'flag': '🇲🇼', 'supported': False},
        'co': {'name': 'Corsican', 'native': 'Corsu', 'flag': '🇫🇷', 'supported': False},
        'hr': {'name': 'Croatian', 'native': 'Hrvatski', 'flag': '🇭🇷', 'supported': False},
        'cs': {'name': 'Czech', 'native': 'Čeština', 'flag': '🇨🇿', 'supported': False},
        'da': {'name': 'Danish', 'native': 'Dansk', 'flag': '🇩🇰', 'supported': False},
        'nl': {'name': 'Dutch', 'native': 'Nederlands', 'flag': '🇳🇱', 'supported': False},
        'eo': {'name': 'Esperanto', 'native': 'Esperanto', 'flag': '🏴‍☠️', 'supported': False},
        'et': {'name': 'Estonian', 'native': 'Eesti', 'flag': '🇪🇪', 'supported': False},
        'tl': {'name': 'Filipino', 'native': 'Filipino', 'flag': '🇵🇭', 'supported': False},
        'fi': {'name': 'Finnish', 'native': 'Suomi', 'flag': '🇫🇮', 'supported': False},
        'fr': {'name': 'French', 'native': 'Français', 'flag': '🇫🇷', 'supported': False},
        'fy': {'name': 'Frisian', 'native': 'Frysk', 'flag': '🇳🇱', 'supported': False},
        'gl': {'name': 'Galician', 'native': 'Galego', 'flag': '🇪🇸', 'supported': False},
        'ka': {'name': 'Georgian', 'native': 'ქართული', 'flag': '🇬🇪', 'supported': False},
        'de': {'name': 'German', 'native': 'Deutsch', 'flag': '🇩🇪', 'supported': False},
        'el': {'name': 'Greek', 'native': 'Ελληνικά', 'flag': '🇬🇷', 'supported': False},
        'gu': {'name': 'Gujarati', 'native': 'ગુજરાતી', 'flag': '🇮🇳', 'supported': False},
        'ht': {'name': 'Haitian Creole', 'native': 'Kreyòl ayisyen', 'flag': '🇭🇹', 'supported': False},
        'ha': {'name': 'Hausa', 'native': 'Hausa', 'flag': '🇳🇬', 'supported': False},
        'haw': {'name': 'Hawaiian', 'native': 'ʻŌlelo Hawaiʻi', 'flag': '🇺🇸', 'supported': False},
        'iw': {'name': 'Hebrew', 'native': 'עברית', 'flag': '🇮🇱', 'supported': False},
        'hi': {'name': 'Hindi', 'native': 'हिन्दी', 'flag': '🇮🇳', 'supported': False},
        'hmn': {'name': 'Hmong', 'native': 'Hmong', 'flag': '🇨🇳', 'supported': False},
        'hu': {'name': 'Hungarian', 'native': 'Magyar', 'flag': '🇭🇺', 'supported': False},
        'is': {'name': 'Icelandic', 'native': 'Íslenska', 'flag': '🇮🇸', 'supported': False},
        'ig': {'name': 'Igbo', 'native': 'Igbo', 'flag': '🇳🇬', 'supported': False},
        'ga': {'name': 'Irish', 'native': 'Gaeilge', 'flag': '🇮🇪', 'supported': False},
        'it': {'name': 'Italian', 'native': 'Italiano', 'flag': '🇮🇹', 'supported': False},
        'jv': {'name': 'Javanese', 'native': 'Basa Jawa', 'flag': '🇮🇩', 'supported': False},
        'kn': {'name': 'Kannada', 'native': 'ಕನ್ನಡ', 'flag': '🇮🇳', 'supported': False},
        'kk': {'name': 'Kazakh', 'native': 'Қазақ тілі', 'flag': '🇰🇿', 'supported': False},
        'km': {'name': 'Khmer', 'native': 'ខ្មែរ', 'flag': '🇰🇭', 'supported': False},
        'ko': {'name': 'Korean', 'native': '한국어', 'flag': '🇰🇷', 'supported': False},
        'ku': {'name': 'Kurdish (Kurmanji)', 'native': 'Kurdî', 'flag': '🇹🇷', 'supported': False},
        'ky': {'name': 'Kyrgyz', 'native': 'Кыргызча', 'flag': '🇰🇬', 'supported': False},
        'lo': {'name': 'Lao', 'native': 'ລາວ', 'flag': '🇱🇦', 'supported': False},
        'la': {'name': 'Latin', 'native': 'Latina', 'flag': '🏛️', 'supported': False},
        'lv': {'name': 'Latvian', 'native': 'Latviešu', 'flag': '🇱🇻', 'supported': False},
        'lt': {'name': 'Lithuanian', 'native': 'Lietuvių', 'flag': '🇱🇹', 'supported': False},
        'lb': {'name': 'Luxembourgish', 'native': 'Lëtzebuergesch', 'flag': '🇱🇺', 'supported': False},
        'mk': {'name': 'Macedonian', 'native': 'Македонски', 'flag': '🇲🇰', 'supported': False},
        'mg': {'name': 'Malagasy', 'native': 'Malagasy', 'flag': '🇲🇬', 'supported': False},
        'ms': {'name': 'Malay', 'native': 'Bahasa Melayu', 'flag': '🇲🇾', 'supported': False},
        'ml': {'name': 'Malayalam', 'native': 'മലയാളം', 'flag': '🇮🇳', 'supported': False},
        'mt': {'name': 'Maltese', 'native': 'Malti', 'flag': '🇲🇹', 'supported': False},
        'mi': {'name': 'Maori', 'native': 'Māori', 'flag': '🇳🇿', 'supported': False},
        'mr': {'name': 'Marathi', 'native': 'मराठी', 'flag': '🇮🇳', 'supported': False},
        'mn': {'name': 'Mongolian', 'native': 'Монгол', 'flag': '🇲🇳', 'supported': False},
        'my': {'name': 'Myanmar (Burmese)', 'native': 'မြန်မာစာ', 'flag': '🇲🇲', 'supported': False},
        'ne': {'name': 'Nepali', 'native': 'नेपाली', 'flag': '🇳🇵', 'supported': False},
        'no': {'name': 'Norwegian', 'native': 'Norsk', 'flag': '🇳🇴', 'supported': False},
        'ps': {'name': 'Pashto', 'native': 'پښتو', 'flag': '🇦🇫', 'supported': False},
        'fa': {'name': 'Persian', 'native': 'فارسی', 'flag': '🇮🇷', 'supported': False},
        'pl': {'name': 'Polish', 'native': 'Polski', 'flag': '🇵🇱', 'supported': False},
        'pt': {'name': 'Portuguese', 'native': 'Português', 'flag': '🇵🇹', 'supported': False},
        'pa': {'name': 'Punjabi', 'native': 'ਪੰਜਾਬੀ', 'flag': '🇮🇳', 'supported': False},
        'ro': {'name': 'Romanian', 'native': 'Română', 'flag': '🇷🇴', 'supported': False},
        'ru': {'name': 'Russian', 'native': 'Русский', 'flag': '🇷🇺', 'supported': False},
        'sm': {'name': 'Samoan', 'native': 'Gagana Samoa', 'flag': '🇼🇸', 'supported': False},
        'gd': {'name': 'Scots Gaelic', 'native': 'Gàidhlig', 'flag': '🇬🇧', 'supported': False},
        'sr': {'name': 'Serbian', 'native': 'Српски', 'flag': '🇷🇸', 'supported': False},
        'st': {'name': 'Sesotho', 'native': 'Sesotho', 'flag': '🇱🇸', 'supported': False},
        'sn': {'name': 'Shona', 'native': 'Shona', 'flag': '🇿🇼', 'supported': False},
        'sd': {'name': 'Sindhi', 'native': 'سنڌي', 'flag': '🇵🇰', 'supported': False},
        'si': {'name': 'Sinhala', 'native': 'සිංහල', 'flag': '🇱🇰', 'supported': False},
        'sk': {'name': 'Slovak', 'native': 'Slovenčina', 'flag': '🇸🇰', 'supported': False},
        'sl': {'name': 'Slovenian', 'native': 'Slovenščina', 'flag': '🇸🇮', 'supported': False},
        'so': {'name': 'Somali', 'native': 'Soomaali', 'flag': '🇸🇴', 'supported': False},
        'es': {'name': 'Spanish', 'native': 'Español', 'flag': '🇪🇸', 'supported': False},
        'su': {'name': 'Sundanese', 'native': 'Basa Sunda', 'flag': '🇮🇩', 'supported': False},
        'sw': {'name': 'Swahili', 'native': 'Kiswahili', 'flag': '🇹🇿', 'supported': False},
        'sv': {'name': 'Swedish', 'native': 'Svenska', 'flag': '🇸🇪', 'supported': False},
        'tg': {'name': 'Tajik', 'native': 'Тоҷикӣ', 'flag': '🇹🇯', 'supported': False},
        'ta': {'name': 'Tamil', 'native': 'தமிழ்', 'flag': '🇮🇳', 'supported': False},
        'te': {'name': 'Telugu', 'native': 'తెలుగు', 'flag': '🇮🇳', 'supported': False},
        'th': {'name': 'Thai', 'native': 'ไทย', 'flag': '🇹🇭', 'supported': False},
        'tr': {'name': 'Turkish', 'native': 'Türkçe', 'flag': '🇹🇷', 'supported': False},
        'uk': {'name': 'Ukrainian', 'native': 'Українська', 'flag': '🇺🇦', 'supported': False},
        'ur': {'name': 'Urdu', 'native': 'اردو', 'flag': '🇵🇰', 'supported': False},
        'uz': {'name': 'Uzbek', 'native': 'Oʻzbekcha', 'flag': '🇺🇿', 'supported': False},
        'vi': {'name': 'Vietnamese', 'native': 'Tiếng Việt', 'flag': '🇻🇳', 'supported': False},
        'cy': {'name': 'Welsh', 'native': 'Cymraeg', 'flag': '🇬🇧', 'supported': False},
        'xh': {'name': 'Xhosa', 'native': 'isiXhosa', 'flag': '🇿🇦', 'supported': False},
        'yi': {'name': 'Yiddish', 'native': 'ייִדיש', 'flag': '🇮🇱', 'supported': False},
        'yo': {'name': 'Yoruba', 'native': 'Yorùbá', 'flag': '🇳🇬', 'supported': False},
        'zu': {'name': 'Zulu', 'native': 'isiZulu', 'flag': '🇿🇦', 'supported': False}
    }

def get_language_aliases():
    """Get comprehensive language aliases for user-friendly input."""
    return {
        # Core supported languages (with templates)
        'english': 'en', 'eng': 'en', 'us': 'en', 'american': 'en', 'british': 'en',
        'japanese': 'ja', 'japan': 'ja', 'jp': 'ja', 'nihongo': 'ja',
        'indonesian': 'id', 'indonesia': 'id', 'indo': 'id', 'bahasa': 'id',

        # Other languages (validation only, no templates)
        'chinese': 'zh', 'china': 'zh', 'mandarin': 'zh', 'cn': 'zh', 'simplified': 'zh', '中文': 'zh',

        # European Languages
        'afrikaans': 'af', 'african': 'af',
        'albanian': 'sq', 'shqip': 'sq',
        'amharic': 'am', 'amhara': 'am',
        'arabic': 'ar', 'العربية': 'ar', 'عربي': 'ar',
        'armenian': 'hy', 'Հայերեն': 'hy', 'հայերեն': 'hy',
        'azerbaijani': 'az', 'azeri': 'az',
        'basque': 'eu', 'euskera': 'eu',
        'belarusian': 'be', 'Беларуская': 'be', 'беларуская': 'be',
        'bengali': 'bn', 'বাংলা': 'bn', 'bangla': 'bn',
        'bosnian': 'bs', 'bosanski': 'bs',
        'bulgarian': 'bg', 'Български': 'bg', 'български': 'bg',
        'catalan': 'ca', 'català': 'ca',
        'cebuano': 'ceb',
        'chichewa': 'ny',
        'corsican': 'co', 'corsu': 'co',
        'croatian': 'hr', 'hrvatski': 'hr',
        'czech': 'cs', 'čeština': 'cs',
        'danish': 'da', 'dansk': 'da',
        'dutch': 'nl', 'nederlands': 'nl',
        'esperanto': 'eo',
        'estonian': 'et', 'eesti': 'et',
        'filipino': 'tl',
        'finnish': 'fi', 'suomi': 'fi',
        'french': 'fr', 'français': 'fr',
        'frisian': 'fy', 'frysk': 'fy',
        'galician': 'gl', 'galego': 'gl',
        'georgian': 'ka', 'ქართული': 'ka',
        'german': 'de', 'deutsch': 'de',
        'greek': 'el', 'Ελληνικά': 'el',
        'gujarati': 'gu', 'ગુજરાતી': 'gu',
        'haitian': 'ht', 'creole': 'ht', 'kreyòl': 'ht',
        'hausa': 'ha',
        'hawaiian': 'haw', 'ʻŌlelo': 'haw',
        'hebrew': 'iw', 'עברית': 'iw',
        'hindi': 'hi', 'हिन्दी': 'hi', 'हिंदी': 'hi',
        'hmong': 'hmn',
        'hungarian': 'hu', 'magyar': 'hu',
        'icelandic': 'is', 'íslenska': 'is',
        'igbo': 'ig',
        'irish': 'ga', 'gaeilge': 'ga',
        'italian': 'it', 'italiano': 'it',
        'javanese': 'jv', 'jawa': 'jv', 'jv': 'jv',
        'kannada': 'kn', 'ಕನ್ನಡ': 'kn',
        'kazakh': 'kk', 'Қазақ': 'kk',
        'khmer': 'km', 'ខ្មែរ': 'km',
        'korean': 'ko', '한국어': 'ko', '조선말': 'ko',
        'kurdish': 'ku', 'kurmanji': 'ku', 'kurdî': 'ku',
        'kyrgyz': 'ky', 'Кыргызча': 'ky', 'кыргызча': 'ky',
        'lao': 'lo', 'ລາວ': 'lo', 'ພາສາລາວ': 'lo',
        'latin': 'la', 'latina': 'la',
        'latvian': 'lv', 'latviešu': 'lv',
        'lithuanian': 'lt', 'lietuvių': 'lt',
        'luxembourgish': 'lb', 'lëtzebuergesch': 'lb',
        'macedonian': 'mk', 'Македонски': 'mk',
        'malagasy': 'mg',
        'malay': 'ms', 'bahasa_melayu': 'ms',
        'malayalam': 'ml', 'മലയാളം': 'ml',
        'maltese': 'mt', 'malti': 'mt',
        'maori': 'mi', 'māori': 'mi',
        'marathi': 'mr', 'मराठी': 'mr',
        'mongolian': 'mn', 'Монгол': 'mn',
        'myanmar': 'my', 'burmese': 'my', 'မြန်မာစာ': 'my',
        'nepali': 'ne', 'नेपाली': 'ne',
        'norwegian': 'no', 'norsk': 'no',
        'pashto': 'ps', 'پښتو': 'ps',
        'persian': 'fa', 'farsi': 'fa', 'فارسی': 'fa',
        'polish': 'pl', 'polski': 'pl',
        'portuguese': 'pt', 'português': 'pt',
        'punjabi': 'pa', 'ਪੰਜਾਬੀ': 'pa',
        'romanian': 'ro', 'română': 'ro',
        'russian': 'ru', 'Русский': 'ru', 'русский': 'ru',
        'samoan': 'sm',
        'scots': 'gd', 'gaelic': 'gd', 'gàidhlig': 'gd',
        'serbian': 'sr', 'Српски': 'sr',
        'sesotho': 'st',
        'shona': 'sn',
        'sindhi': 'sd', 'سنڌي': 'sd',
        'sinhala': 'si', 'සිංහල': 'si',
        'slovak': 'sk', 'slovenčina': 'sk',
        'slovenian': 'sl', 'slovenščina': 'sl',
        'somali': 'so', 'soomaali': 'so',
        'spanish': 'es', 'español': 'es',
        'sundanese': 'su', 'sunda': 'su',
        'swahili': 'sw', 'kiswahili': 'sw',
        'swedish': 'sv', 'svenska': 'sv',
        'tajik': 'tg', 'Тоҷикӣ': 'tg',
        'tamil': 'ta', 'தமிழ்': 'ta',
        'telugu': 'te', 'తెలుగు': 'te',
        'thai': 'th', 'ไทย': 'th',
        'turkish': 'tr', 'türkçe': 'tr',
        'ukrainian': 'uk', 'Українська': 'uk',
        'urdu': 'ur', 'اردو': 'ur',
        'uzbek': 'uz', 'oʻzbekcha': 'uz',
        'vietnamese': 'vi', 'tiếng_việt': 'vi',
        'welsh': 'cy', 'cymraeg': 'cy',
        'xhosa': 'xh', 'isixhosa': 'xh',
        'yiddish': 'yi', 'ייִדיש': 'yi',
        'yoruba': 'yo', 'yorùbá': 'yo',
        'zulu': 'zu', 'isizulu': 'zu'
    }

def validate_and_normalize_languages(lang_input):
    """Validate and normalize language input. Returns (valid_languages, invalid_entries, available_info)"""
    if not lang_input:
        return ['en'], [], ""

    # Split and clean input
    lang_entries = [lang.strip().lower() for lang in lang_input.split(',') if lang.strip()]

    available_langs = get_available_languages()
    lang_table = get_language_table()
    aliases = get_language_aliases()

    valid_languages = []
    invalid_entries = []

    for entry in lang_entries:
        # Check if it's a direct language code
        if entry in available_langs:
            if entry not in valid_languages:  # Avoid duplicates
                valid_languages.append(entry)
        # Check if it's an alias
        elif entry in aliases:
            lang_code = aliases[entry]
            if lang_code not in valid_languages:  # Avoid duplicates
                valid_languages.append(lang_code)
        else:
            invalid_entries.append(entry)

    # Create available languages info
    available_info = "\n".join([
        f"  {lang_table[code]['flag']} {code.upper()}: {lang_table[code]['name']} ({lang_table[code]['native']})"
        for code in available_langs
    ])

    return valid_languages, invalid_entries, available_info

def validate_plugin_name(name):
    """Validate plugin name format."""
    if not name:
        return False, "Plugin name cannot be empty"

    # Must be kebab-case (lowercase, hyphens, no spaces)
    if not all(c.islower() or c == '-' for c in name):
        return False, "Plugin name must be kebab-case (lowercase letters and hyphens only)"

    if name.startswith('-') or name.endswith('-'):
        return False, "Plugin name cannot start or end with hyphen"

    if '--' in name:
        return False, "Plugin name cannot contain consecutive hyphens"

    # Check if plugin already exists
    script_dir = get_script_directory()
    plugin_dir = script_dir / "modules" / name
    if plugin_dir.exists():
        return False, f"Plugin directory 'modules/{name}' already exists"

    return True, ""

# ============================================================================
# TEMPLATE GENERATORS
# ============================================================================
def generate_rules_template(plugin_name, display_name, description, lang='en', current_year=None, templates_dir=None):
    """Generate a RULES.md template for the specified language using template files."""

    if current_year is None:
        current_year = get_current_year()

    # Use the comprehensive language table to get the proper language name
    lang_table = get_language_table()
    lang_info = lang_table.get(lang, {})

    # For supported languages, use the native name; for others, use English name
    if lang_info:
        lang_name = lang_info['name']
    else:
        # Fallback for any language not in our table (shouldn't happen but safety)
        lang_name = f"Language ({lang.upper()})"

    # Determine which template file to use
    if templates_dir:
        # Try language-specific template first
        lang_template = templates_dir / "rules" / f"RULES.md.{lang}"
        if lang_template.exists():
            template_path = lang_template
        else:
            # Fall back to generic template
            generic_template = templates_dir / "rules" / "RULES.md.template"
            if generic_template.exists():
                template_path = generic_template
            else:
                raise FileNotFoundError(f"No template found for language {lang} in {templates_dir}")
    else:
        raise ValueError("Templates directory not provided")

    # Load and substitute template
    variables = {
        'plugin_name': plugin_name,
        'plugin_key': plugin_name.replace('-', '_'),
        'plugin_name_kebab': plugin_name.replace('-', ' '),
        'display_name': display_name,
        'description': description,
        'language_name': lang_name,
        'pascal_case_name': kebab_to_pascal_case(plugin_name),
        'author_name': '{author_name}',  # Keep as placeholder
        'current_year': current_year
    }

    return load_template(template_path, variables)

def generate_settings_json(plugin_name, display_name, enabled_by_default=True, current_year=None, templates_dir=None):
    """Generate a basic settings.json file using template."""

    if current_year is None:
        current_year = get_current_year()

    creation_timestamp = get_creation_timestamp()

    if templates_dir:
        template_path = templates_dir / "scaffold" / "settings.json.template"
        if template_path.exists():
            variables = {
                'plugin_name': plugin_name,
                'plugin_key': plugin_name.replace('-', '_'),
                'display_name': display_name,
                'author_name': '{author_name}',  # Keep as placeholder
                'current_year': current_year,
                'creation_timestamp': creation_timestamp
            }
            content = load_template(template_path, variables)
            return content
        else:
            print(f"⚠️  Settings template not found, using fallback generation")

    # Fallback generation
    settings = {
        "_metadata": {
            "license": "MIT",
            "copyright": f"Copyright (c) {current_year} {{author_name}}",
            "license_file": "LICENSE",
            "created": creation_timestamp,
            "last_modified": creation_timestamp
        },
        "version": "1.0.0",
        f"{plugin_name.replace('-', '_')}": {
            "enabled": enabled_by_default,
            "config": {
                "example_setting": "example_value",
                "max_entries": 100,
                "cleanup_days": 90
            },
            "advanced": {
                "debug_mode": False,
                "performance_mode": "balanced"
            }
        }
    }

    return json.dumps(settings, indent=2, ensure_ascii=False)

def generate_setup_json(plugin_name, display_name, description, languages, current_year=None, templates_dir=None):
    """Generate a setup.json file for web interface configuration using template."""

    if current_year is None:
        current_year = get_current_year()

    if templates_dir:
        template_path = templates_dir / "scaffold" / "setup.json.template"
        if template_path.exists():
            # Generate localization for all requested languages
            localization = {}
            lang_table = get_language_table()

            for lang in languages:
                lang_info = lang_table.get(lang, {})
                native_name = lang_info.get('native', 'English')
                localization[lang] = {
                    "plugin_name": display_name if lang == 'en' else f"{display_name} ({native_name})",
                    "description": description
                }

            variables = {
                'plugin_name': plugin_name,
                'plugin_key': plugin_name.replace('-', '_'),
                'display_name': display_name,
                'description': description,
                'author_name': '{author_name}',  # Keep as placeholder
                'current_year': current_year,
                'localization': json.dumps(localization, indent=2, ensure_ascii=False)
            }
            content = load_template(template_path, variables)
            return content
        else:
            print(f"⚠️  Setup template not found, using fallback generation")

    # Fallback generation
    # Generate localization for all requested languages
    localization = {}
    lang_table = get_language_table()

    for lang in languages:
        lang_info = lang_table.get(lang, {})
        native_name = lang_info.get('native', 'English')
        localization[lang] = {
            "plugin_name": display_name if lang == 'en' else f"{display_name} ({native_name})",
            "description": description
        }

    setup_config = {
        "_comment": f"Copyright (c) {current_year} {{author_name}} - Licensed under the MIT License. See LICENSE file for details.",
        "localization": localization,
        "mandatory_config": [
            {
                "name": f"{plugin_name}_enable",
                "type": "choice",
                "localization": {
                    lang: {
                        "title": f"Enable {display_name}",
                        "description": f"Enable or disable {display_name} functionality"
                    } for lang in languages
                },
                "options": [
                    {
                        "name": "enable",
                        "localization": {
                            lang: {
                                "description": f"Enable {display_name}"
                            } for lang in languages
                        },
                        "recommended": True,
                        "settings": {
                            f"{plugin_name.replace('-', '_')}.enabled": True
                        }
                    },
                    {
                        "name": "disable",
                        "localization": {
                            lang: {
                                "description": f"Disable {display_name}"
                            } for lang in languages
                        },
                        "settings": {
                            f"{plugin_name.replace('-', '_')}.enabled": False
                        }
                    }
                ],
                "settings_key": f"{plugin_name.replace('-', '_')}.enabled",
                "required": True
            }
        ],
        "optional_config": [
            {
                "name": "performance_mode",
                "type": "choice",
                "localization": {
                    lang: {
                        "title": "Performance Mode",
                        "description": "Choose performance optimization mode"
                    } for lang in languages
                },
                "options": [
                    {
                        "name": "balanced",
                        "localization": {
                            lang: {
                                "description": "Balanced performance and features"
                            } for lang in languages
                        },
                        "recommended": True,
                        "settings": {
                            f"{plugin_name.replace('-', '_')}.advanced.performance_mode": "balanced"
                        }
                    },
                    {
                        "name": "fast",
                        "localization": {
                            lang: {
                                "description": "Optimized for speed"
                            } for lang in languages
                        },
                        "settings": {
                            f"{plugin_name.replace('-', '_')}.advanced.performance_mode": "fast"
                        }
                    }
                ]
            }
        ]
    }

    return json.dumps(setup_config, indent=2, ensure_ascii=False)

def generate_readme(plugin_name, display_name, description, current_year=None, templates_dir=None, primary_lang='en'):
    """Generate a README.md file for the plugin using template."""

    if current_year is None:
        current_year = get_current_year()

    if templates_dir:
        # Try language-specific README template first
        lang_readme = templates_dir / "scaffold" / f"README.{primary_lang}.md"
        if lang_readme.exists():
            template_path = lang_readme
        else:
            # Fall back to generic README template
            generic_readme = templates_dir / "scaffold" / "README.md.template"
            if generic_readme.exists():
                template_path = generic_readme
            else:
                print(f"⚠️  README template not found for {primary_lang}, using fallback generation")
                template_path = None

        if template_path:
            variables = {
                'plugin_name': plugin_name,
                'plugin_key': plugin_name.replace('-', '_'),
                'plugin_name_kebab': plugin_name.replace('-', ' '),
                'display_name': display_name,
                'description': description,
                'pascal_case_name': kebab_to_pascal_case(plugin_name),
                'author_name': '{author_name}',  # Keep as placeholder
                'current_year': current_year
            }
            content = load_template(template_path, variables)
            return content

    # Fallback generation
    readme = f"""# {display_name}

{description}

## Overview

This is a custom plugin for the Agentic Rules Framework that provides {plugin_name.replace('-', ' ')} functionality for AI agents.

## Features

- **Algorithm Implementation**: Provides structured algorithms for {plugin_name.replace('-', ' ')} operations
- **Configuration Management**: Flexible settings through `settings.json`
- **Multi-language Support**: Templates available in multiple languages
- **Framework Integration**: Seamless integration with the Agentic Rules Framework

## Installation

1. Copy this plugin directory to the `modules/` folder in your agentic-rules framework
2. The script automatically adds `modules/{plugin_name}` to `plugins.json`
3. Run `python generate_simple_setup.py` to update web configuration
4. Activate the plugin using `python setup.py`

## Configuration

### Basic Settings (`settings.json`)

```json
{{
  "{plugin_name.replace('-', '_')}": {{
    "enabled": true,
    "config": {{
      "example_setting": "example_value",
      "max_entries": 100,
      "cleanup_days": 90
    }},
    "advanced": {{
      "debug_mode": false,
      "performance_mode": "balanced"
    }}
  }}
}}
```

### Settings Description

- `enabled`: Enable/disable the plugin
- `config.max_entries`: Maximum number of entries to maintain
- `config.cleanup_days`: Days to retain data before cleanup
- `advanced.debug_mode`: Enable debug logging
- `advanced.performance_mode`: Performance optimization mode

## Usage

1. **Enable the Plugin**: Set `enabled: true` in `settings.json`
2. **Activate Rules**: Use `python setup.py` to generate rule files
3. **Integration**: Copy the generated rule file (e.g., `AGENTS.md`) to your project
4. **Configuration**: Customize settings in `{plugin_name}/settings.json`

## Rule Algorithms

This plugin implements the following algorithms:

### {kebab_to_pascal_case(plugin_name)} Initialization Process
- Initializes the {plugin_name.replace('-', ' ')} system
- Validates configuration
- Sets up required data structures

### {kebab_to_pascal_case(plugin_name)} Main Process
- Processes user interactions
- Applies {plugin_name.replace('-', ' ')} logic
- Returns processed results

### {kebab_to_pascal_case(plugin_name)} Cleanup Process
- Performs periodic cleanup
- Requires user consent
- Maintains data integrity

## File Structure

```
{plugin_name}/
├── README.md              # This documentation
├── RULES.md.en           # English rule template
├── settings.json         # Default settings
└── setup.json           # Web interface configuration
```

## Development

### Adding New Languages

1. Create `RULES.md.{{language_code}}` with translated template
2. Add localization to `setup.json`
3. Update `settings.json` if needed

### Customizing Algorithms

Edit the `RULES.md.*` files to modify the algorithms and behavior.

### Testing

1. Enable the plugin in settings
2. Run setup.py to generate rule files
3. Test the generated rules in your AI agent

## Troubleshooting

### Plugin Not Detected
- Ensure the plugin directory exists
- Check that at least one `RULES.md.*` file exists
- Verify `plugins.json` includes `modules/{plugin_name}` (for web interface)

### Configuration Errors
- Check `settings.json` syntax
- Verify all required settings are present
- Ensure file permissions are correct

### Rule Activation Fails
- Check that the plugin is enabled in settings
- Verify `setup.py` completed successfully
- Ensure generated rule files are properly copied

## License

Copyright (c) {current_year} {{author_name}}

Licensed under the MIT License. See LICENSE file for details.

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

For major changes, please open an issue first to discuss the proposed changes.
"""

    return readme

# ============================================================================
# MAIN SCAFFOLD GENERATION
# ============================================================================
def create_plugin_scaffold(plugin_name, display_name, description, languages, enabled_by_default=True, template_plugin=None):
    """Create a complete plugin scaffold using templates from Template branch."""

    script_dir = get_script_directory()
    plugin_dir = script_dir / "modules" / plugin_name
    current_year = get_current_year()
    templates_temp_dir = None

    if template_plugin:
        print(f"\n🔧 Creating plugin scaffold for '{plugin_name}' from template '{template_plugin}'...")
    else:
        print(f"\n🔧 Creating plugin scaffold for '{plugin_name}'...")
    print(f"📁 Plugin directory: {plugin_dir}")

    try:
        # Clone Template branch to get the latest templates
        print("📥 Cloning Template branch for latest templates...")
        templates_temp_dir = clone_templates_branch()
        templates_dir = templates_temp_dir / "templates"
        print("✅ Templates loaded successfully")

        # Create plugin directory
        plugin_dir.mkdir(parents=True, exist_ok=True)

        if template_plugin:
            # Copy from template
            actual_display_name, actual_description = copy_from_template(template_plugin, plugin_name, display_name, description, templates_dir)
            if not display_name:
                display_name = actual_display_name
            if not description:
                description = actual_description
        else:
            # Generate from scratch
            # Generate rule templates for each language
            for lang in languages:
                template_file = plugin_dir / f"RULES.md.{lang}"
                template_content = generate_rules_template(plugin_name, display_name, description, lang, current_year, templates_dir)

                with open(template_file, 'w', encoding='utf-8') as f:
                    f.write(template_content)

                print(f"✓ Generated {template_file.name}")

            # Generate settings.json
            settings_file = plugin_dir / "settings.json"
            settings_content = generate_settings_json(plugin_name, display_name, enabled_by_default, current_year, templates_dir)

            with open(settings_file, 'w', encoding='utf-8') as f:
                f.write(settings_content)

            print(f"✓ Generated settings.json")

            # Generate setup.json
            setup_file = plugin_dir / "setup.json"
            setup_content = generate_setup_json(plugin_name, display_name, description, languages, current_year, templates_dir)

            with open(setup_file, 'w', encoding='utf-8') as f:
                f.write(setup_content)

            print(f"✓ Generated setup.json")

        # Generate README.md (use first language as primary)
        readme_file = plugin_dir / "README.md"
        primary_lang = languages[0] if languages else 'en'
        readme_content = generate_readme(plugin_name, display_name, description, current_year, templates_dir, primary_lang)

        with open(readme_file, 'w', encoding='utf-8') as f:
            f.write(readme_content)

        print(f"✓ Generated README.md")

        # Always add to plugins.json
        plugins_file = script_dir / "plugins.json"

        # Ensure plugins.json exists with proper structure
        if not plugins_file.exists():
            # Create plugins.json if it doesn't exist
            plugins_config = {
                "_comment": f"Copyright (c) {current_year} Paulus Ery Wasito Adhi - Licensed under the MIT License. See LICENSE file for details.",
                "version": "1.0.0",
                "plugins": [],
                "description": "Manifest of available agentic-rules plugins"
            }
            try:
                with open(plugins_file, 'w', encoding='utf-8') as f:
                    json.dump(plugins_config, f, indent=2, ensure_ascii=False)
                print(f"✓ Created plugins.json")
            except Exception as e:
                print(f"⚠️  Could not create plugins.json: {e}")

        # Now update plugins.json
        try:
            with open(plugins_file, 'r', encoding='utf-8') as f:
                plugins_config = json.load(f)

            # Ensure plugins array exists
            if 'plugins' not in plugins_config:
                plugins_config['plugins'] = []

            # Add plugin if not already present
            plugin_full_name = f"modules/{plugin_name}"
            if plugin_full_name not in plugins_config['plugins']:
                plugins_config['plugins'].append(plugin_full_name)
                plugins_config['plugins'].sort()  # Keep sorted

                with open(plugins_file, 'w', encoding='utf-8') as f:
                    json.dump(plugins_config, f, indent=2, ensure_ascii=False)

                print(f"✓ Added '{plugin_full_name}' to plugins.json")
            else:
                print(f"⚠️  '{plugin_full_name}' already in plugins.json")

        except Exception as e:
            print(f"⚠️  Could not update plugins.json: {e}")

        print("\n🎉 Plugin scaffold created successfully!")
        print(f"📂 Location: {plugin_dir}")
        print(f"📋 Languages: {', '.join(languages).upper()}")
        print(f"⚙️  Default enabled: {enabled_by_default}")

        print("\n🚀 Next steps:")
        print(f"  1. Customize the algorithms in RULES.md.* files")
        print(f"  2. Modify settings in settings.json")
        print(f"  3. Update localization in setup.json if needed")
        print(f"  4. Run 'python generate_simple_setup.py' to update web config")
        print(f"  5. Test with 'python setup.py'")

        return True

    except Exception as e:
        print(f"❌ Error creating plugin scaffold: {e}")
        # Clean up partially created plugin directory on failure
        if plugin_dir.exists():
            shutil.rmtree(plugin_dir, ignore_errors=True)
        return False

    finally:
        # Always clean up the cloned templates
        if templates_temp_dir:
            cleanup_templates_clone(templates_temp_dir)
            print("🧹 Cleaned up temporary templates")

# ============================================================================
# INTERACTIVE WIZARD
# ============================================================================
def interactive_wizard():
    """Run an interactive plugin creation wizard."""

    print("🎯 Agentic Rules Framework - Plugin Scaffold Generator")
    print("=" * 60)

    # Get plugin name
    while True:
        plugin_name = input("\n📝 Enter plugin name (kebab-case, e.g., 'my-awesome-plugin'): ").strip()

        valid, error_msg = validate_plugin_name(plugin_name)
        if valid:
            break
        print(f"❌ {error_msg}")

    # Get display name
    default_display = kebab_to_title_case(plugin_name)
    display_name = input(f"📋 Enter display name (default: '{default_display}'): ").strip()
    if not display_name:
        display_name = default_display

    # Get description
    description = input("📖 Enter plugin description: ").strip()
    while not description:
        print("❌ Description cannot be empty")
        description = input("📖 Enter plugin description: ").strip()

    # Get languages
    lang_table = get_language_table()
    print("\n🌐 Language Support:")
    print("  📝 Full Templates Available (18 languages):")
    # Show languages that have full rule templates
    template_langs = ['en', 'ja', 'id', 'de', 'fr', 'es', 'ar', 'zh', 'ko', 'hi', 'pt', 'ru', 'tr', 'vi', 'th', 'jv', 'si', 'ta']
    for code in template_langs:
        if code in lang_table:
            info = lang_table[code]
            status = "⭐ Core" if code in ['en', 'ja', 'id'] else "✅ Full"
            print(f"    {info['flag']} {code.upper()}: {info['name']} ({info['native']}) - {status}")

    print("\n  🌍 All World Languages (150+ ISO codes supported for validation):")
    print("    🇪🇺 European: German, French, Spanish, Italian, Russian, Polish, Dutch, Swedish...")
    print("    🌏 Asian: Korean, Hindi, Arabic, Thai, Vietnamese, Turkish, Persian, Hebrew...")
    print("    🌍 African: Swahili, Hausa, Yoruba, Zulu, Amharic, Afrikaans...")
    print("    🌎 American: Portuguese, Dutch, Swedish, Norwegian, Haitian Creole...")
    print("\n💡 Usage: language codes (en, de, zh), names (english, german, chinese), or native script (العربية, 한국어, 中文)")

    lang_input = input("🔤 Enter languages (comma-separated, default: 'en'): ").strip()
    languages, invalid_entries, available_info = validate_and_normalize_languages(lang_input)

    if invalid_entries:
        print(f"❌ Invalid language entries: {', '.join(invalid_entries)}")
        print("📚 Available languages:")
        print(available_info)
        print("\n💡 Retrying language input...")

        # Allow retry
        lang_input = input("🔤 Enter languages (comma-separated, default: 'en'): ").strip()
        languages, invalid_entries, _ = validate_and_normalize_languages(lang_input)

        if invalid_entries:
            print(f"⚠️  Still invalid entries ignored: {', '.join(invalid_entries)}")
            if not languages:
                print("⚠️  No valid languages specified, using English")
                languages = ['en']

    # Get enabled by default
    enabled_input = input("⚙️  Enable by default? (y/n, default: y): ").strip().lower()
    enabled_by_default = enabled_input not in ['n', 'no', 'false']

    # Confirm
    print(f"\n📋 Plugin Summary:")
    print(f"  Name: {plugin_name}")
    print(f"  Display: {display_name}")
    print(f"  Description: {description}")
    print(f"  Languages: {', '.join(languages).upper()}")
    print(f"  Enabled by default: {enabled_by_default}")
    print(f"  Auto-added to plugins.json: Yes")

    confirm = input("\n✅ Create plugin scaffold? (y/n): ").strip().lower()
    if confirm not in ['y', 'yes', 'true']:
        print("❌ Plugin creation cancelled")
        return False

    # Create the scaffold
    return create_plugin_scaffold(plugin_name, display_name, description, languages, enabled_by_default)

# ============================================================================
# MAIN FUNCTION
# ============================================================================
def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description='Generate plugin scaffold for Agentic Rules Framework',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python generate_plugin_scaffold.py                                    # Interactive mode
  python generate_plugin_scaffold.py --name my-plugin --description "My plugin"  # Quick create
  python generate_plugin_scaffold.py --name my-plugin --description "Plugin" --langs en,de,zh   # European + Asian
  python generate_plugin_scaffold.py --name my-plugin --langs english,german,chinese  # Using names
  python generate_plugin_scaffold.py --name my-plugin --langs eng,deutsch,mandarin  # Using aliases
  python generate_plugin_scaffold.py --template memory-rules --name my-memory-plugin  # From template

Core Framework Languages (Full Templates):
  🇺🇸 EN: English (English)
  🇯🇵 JA: Japanese (日本語)
  🇮🇩 ID: Indonesian (Bahasa Indonesia)

Extended Languages (Full Templates):
  🇩🇪 DE: German (Deutsch)
  🇫🇷 FR: French (Français)
  🇪🇸 ES: Spanish (Español)
  🇸🇦 AR: Arabic (العربية)
  🇰🇷 KO: Korean (한국어)
  🇨🇳 ZH: Chinese (中文)
  🇮🇳 HI: Hindi (हिन्दी)
  🇵🇹 PT: Portuguese (Português)
  🇷🇺 RU: Russian (Русский)
  🇹🇷 TR: Turkish (Türkçe)
  🇻🇳 VI: Vietnamese (Tiếng Việt)
  🇹🇭 TH: Thai (ภาษาไทย)
  🇮🇩 JV: Javanese (Basa Jawa)
  🇱🇰 SI: Sinhala (සිංහල)
  🇱🇰 TA: Tamil (தமிழ்)

All World Languages Supported (150+ ISO codes): Validation available for any ISO 639-1 code
        """
    )

    parser.add_argument('--name', help='Plugin name in kebab-case (e.g., my-awesome-plugin)')
    parser.add_argument('--display', help='Human-readable display name')
    parser.add_argument('--description', help='Plugin description')
    parser.add_argument('--langs', help='Comma-separated language codes, names, or aliases (en,de,zh or english,german,chinese)')
    parser.add_argument('--template', help='Use existing plugin as template (e.g., memory-rules)')
    parser.add_argument('--no-enable', action='store_true', help='Do not enable by default')

    args = parser.parse_args()

    # Check if running in interactive mode
    if not any([args.name, args.display, args.description, args.langs, args.template]):
        # Interactive mode
        success = interactive_wizard()
    else:
        # Command-line mode
        plugin_name = args.name
        if not plugin_name:
            print("❌ --name is required for command-line mode")
            return 1

        # Validate plugin name
        valid, error_msg = validate_plugin_name(plugin_name)
        if not valid:
            print(f"❌ {error_msg}")
            return 1

        # Check template
        template_plugin = args.template
        if template_plugin:
            existing_plugins = get_existing_plugins()
            if template_plugin not in existing_plugins:
                print(f"❌ Template plugin '{template_plugin}' not found. Available: {', '.join(existing_plugins)}")
                return 1
            print(f"📋 Using '{template_plugin}' as template")

        # Get display name
        display_name = args.display or kebab_to_title_case(plugin_name)

        # Get description
        description = args.description
        if not description and not template_plugin:
            print("❌ --description is required (unless using --template)")
            return 1

        # Get languages
        if args.langs:
            languages, invalid_entries, available_info = validate_and_normalize_languages(args.langs)
            if invalid_entries:
                print(f"❌ Invalid language entries: {', '.join(invalid_entries)}")
                print("📚 Available languages:")
                print(available_info)
                return 1
        else:
            languages = ['en']

        enabled_by_default = not args.no_enable

        success = create_plugin_scaffold(plugin_name, display_name, description, languages, enabled_by_default, template_plugin)

    return 0 if success else 1

if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\n❌ Plugin scaffold generation cancelled by user.")
        sys.exit(1)
