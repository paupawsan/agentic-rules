# 🔧 Developer Guide - Agentic Rules Framework

## For Engineers & Developers (Advanced Setup)

This guide covers advanced usage, automation, and technical implementation details.

## 🔧 Bootstrap Initialization (Required After Setup)

### **Complete Setup Order for Developers**

1. **First**: Run `setup.html` to generate configuration and rule files
2. **Then**: Initialize bootstrap system through AI agent

### **Framework Bootstrap Process**
After `setup.html` creates the necessary files, the bootstrap initialization is handled by your AI agent:

```bash
# Tell your AI agent to initialize the framework
"Initialize agentic rules system"
# or
"Setup agentic rules bootstrap"
```

**The bootstrap initialization is an interactive process managed by the AI agent, not a programmatic script.**

### **Bootstrap Configuration**
The bootstrap system manages:
- **Framework loading sequence** - Proper initialization order
- **Rule interconnections** - Data flow between components
- **Platform adaptations** - Environment-specific configurations
- **User consent management** - Permission handling

### **Programmatic Integration**
```python
from agentic_bootstrap import BootstrapManager

# Initialize bootstrap context
bootstrap = BootstrapManager()
bootstrap.initialize()

# Check framework status
if bootstrap.is_initialized():
    print("Framework ready for use")

# Load specific rules
bootstrap.load_rule('memory-rules')
bootstrap.load_rule('rag-rules')
```

---

## 🚀 Advanced Setup Options

### Option A: Enhanced Server Mode (Recommended)

**Full file system access with automation:**

```bash
# Launch enhanced server (recommended)
python setup-launcher.py

# Custom port if 8000 is in use
python setup-launcher.py --port 8080

# Basic mode (download dialogs)
python setup-launcher.py --web
```

**Enhanced Mode Benefits:**
- ✅ **Four save options**: Copy, Save (dialog), Download, Direct Create
- ✅ **Direct file creation** - No manual file placement
- ✅ **Automatic cleanup** - Removes conflicting file types
- ✅ **Real-time feedback** - Immediate file operations
- ✅ **Server controls** - Clean shutdown from web interface

### Option B: Command Line Interface

**Full programmatic control:**

```bash
# Interactive setup
python setup.py

# Non-interactive with arguments
python setup.py --lang ja --rules memory,rag --file-type GEMINI.md
```

## 📋 Complete Setup Process

### 1. Launch Interface

**Enhanced Mode (Engineers):**
```bash
python setup-launcher.py
```
Opens http://localhost:8000/setup.html with full file system access.

**Basic Mode (Anyone):**
```bash
open setup.html  # macOS
start setup.html  # Windows
xdg-open setup.html  # Linux
```
Opens setup.html with download/save dialogs.

### 2. Configure Settings

- **Agent Language**: Choose language for generated files (EN/JA/ID core, 15+ extended for plugins)
- **File Type**: AGENTS.md (standard), GEMINI.md (Gemini), or CLAUDE.md (Claude)
- **Rules Selection**: Enable desired AI behaviors

### 3. Generate Files

Click "Generate Configuration Files" to create:
- Root `AGENTS.md`/`GEMINI.md`/`CLAUDE.md`
- Rule-specific files in subdirectories
- `settings.json` files for each enabled rule

### 4. Save Methods

#### 💾 Save (Recommended)
- Opens native file save dialog
- Choose exact save location
- Starts in Documents folder
- Modern browsers: Full file system API
- Legacy browsers: Fallback to download

#### 📥 Download
- Downloads directly to Downloads folder
- Traditional browser download behavior
- Manual file placement required

#### 📋 Copy
- Copies content to clipboard
- Manual paste and save
- Full control over file naming/location

#### 📁 Create (Enhanced Mode Only)
- Direct file creation on server
- Automatic file placement
- No user dialogs required
- Available only in `python setup-launcher.py` mode

## 🔧 Technical Architecture

### File Structure
```
agentic-rules/
├── setup.html              # Main web interface
├── setup.py               # CLI setup script
├── setup-launcher.py      # Enhanced server launcher
├── localization.json      # UI translations
├── bootstrap.json         # Framework configuration
├── CORE-RULES.md         # Framework overview
└── [rule-name]/          # Rule directories
    ├── RULES.md.*        # Rule templates (EN/JA/ID core languages)
    ├── settings.json     # Default settings
    └── setup.json       # Rule configuration
```

### Rule Integration Process

1. **Bootstrap Loading**: `bootstrap.json` defines framework structure
2. **Rule Activation**: User selects which rules to enable
3. **Template Processing**: Rules templates are localized and processed
4. **File Generation**: Creates agent-specific configuration files
5. **Agent Integration**: Files placed in project for agent loading

## 🛠️ API Reference

### setup-launcher.py

**Command Line Options:**
```bash
python setup-launcher.py [OPTIONS]

Options:
  --port PORT    Port to run server on (default: 8000)
  --web         Launch in basic mode (download dialogs)
  --help        Show help message
```

**Server Endpoints (Enhanced Mode):**
- `GET /` - Serve static files
- `POST /api/create-file` - Create file directly
- `POST /api/cleanup-files` - Remove conflicting files
- `POST /api/shutdown` - Shutdown server gracefully

### setup.py

**Command Line Options:**
```bash
python setup.py [OPTIONS]

Options:
  --ui-lang {en,ja,id}        Interface language (en, ja, id)
  --agent-lang {en,ja,id}     Agent template language (en, ja, id)
  --agent-file-type {AGENTS.md,GEMINI.md,CLAUDE.md}
                               Agent file type to generate
  --lang {en,ja,id}           Set both UI and agent language (en, ja, id)
  --rules RULES               Comma-separated list of rules to activate, or "all"
  --help                      Show help message
```

**Note:** `setup.py` currently supports the core 3 languages. For full 18+ language support, use the web interface (`setup.html`) or the scaffold generator (`generate_plugin_scaffold.py`).

## 🔌 Integration Examples

### Cursor Integration
```javascript
// In your Cursor configuration
{
  "agentic-rules": {
    "enabled": true,
    "rules": ["memory", "rag"],
    "language": "en"
  }
}
```

### VSCode Extension
```json
// settings.json
{
  "agenticRules.enabled": true,
  "agenticRules.rules": ["memory", "critical-thinking"],
  "agenticRules.fileType": "AGENTS.md"
}
```

### Custom Agent Integration
```python
# Load agentic rules
import json

# Load bootstrap configuration
with open('bootstrap.json', 'r') as f:
    bootstrap = json.load(f)

# Load enabled rules
enabled_rules = ['memory-rules', 'rag-rules']
for rule in enabled_rules:
    rule_file = f"{rule}/AGENTS.md"
    settings_file = f"{rule}/settings.json"

    # Load and apply rule configurations
    with open(rule_file, 'r') as f:
        rule_content = f.read()

    with open(settings_file, 'r') as f:
        rule_settings = json.load(f)
```

## 🔍 Debugging & Troubleshooting

### Server Won't Start
```bash
# Check if port is available
lsof -i :8000

# Try different port
python setup-launcher.py --port 8081
```

### Files Not Generating
```bash
# Check file permissions
ls -la setup.html setup.py

# Verify Python installation
python --version
python -c "import json; print('JSON working')"
```

### Browser Issues
```bash
# Clear browser cache
# Try incognito/private mode
# Check browser console for errors
```

### Rule Conflicts
- Each agent file type (AGENTS.md/GEMINI.md/CLAUDE.md) is mutually exclusive
- Enhanced mode automatically cleans up conflicting files
- Manual cleanup may be required in basic mode

## 🚀 Advanced Usage

### Custom Rule Development
- See [Extension Manual](EXTENSION-MANUAL.md)
- Create new rule directories
- Define settings.json and template files
- Add to bootstrap.json configuration

### Automated Deployment
```bash
#!/bin/bash
# Automated setup script
python setup-launcher.py --port 9000 &
sleep 2
curl -X POST http://localhost:9000/api/shutdown
```

### CI/CD Integration
```yaml
# GitHub Actions example
- name: Setup Agentic Rules
  run: |
    python setup.py --lang en --rules memory,rag --file-type AGENTS.md
    cp -r generated-files/* ./ai-project/
```

## 📊 Performance Considerations

### Memory Usage
- Rule templates are loaded into memory during generation
- Large rule sets may require more RAM
- Consider rule selection based on use case

### File System Operations
- Enhanced mode performs direct file writes
- Ensure proper permissions for target directories
- Backup files are created automatically

### Browser Compatibility
- Modern browsers: Full File System API support
- Legacy browsers: Fallback to download dialogs
- Mobile browsers: Limited functionality

## 🔐 Security Notes

- Framework runs client-side when using `setup.html`
- Enhanced mode requires local server (user trust required)
- No data is transmitted externally
- All file operations are local to user system

## 📞 Support & Contributing

- **Issues**: [GitHub Issues](https://github.com/your-repo/issues)
- **Discussions**: Framework design and implementation
- **Contributing**: See main README for contribution guidelines

---

**🔧 Advanced users**: This framework provides maximum flexibility for integrating structured AI behaviors into any agentic system.

## Localization / 多言語対応 / Pelokalan

<details>
<summary>🌍 This guide is also available in / このガイドは以下の言語でも利用可能です / Panduan ini juga tersedia dalam</summary>

- **[日本語 (Japanese)](localization/ja/DEVELOPER-GUIDE.ja.md)** - 開発者ガイド
- **[Bahasa Indonesia (Indonesian)](localization/id/DEVELOPER-GUIDE.id.md)** - Panduan Pengembang

</details>

---

Copyright (c) 2025 Paulus Ery Wasito Adhi. Licensed under the MIT License (see LICENSE file).
