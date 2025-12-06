# Framework Extension Manual

This manual provides comprehensive guidance for extending the agentic rules framework with new rules. The framework now includes automated plugin scaffolding tools for rapid development.

## Quick Start: Automated Plugin Creation

**🎯 Recommended Approach**: Use the automated scaffold generator for instant plugin creation!

### Option 1: Interactive Plugin Creation
```bash
python generate_plugin_scaffold.py
```
**Features:**
- Guided wizard interface
- Automatic file generation
- Multi-language support
- Plugin registration in `plugins.json`

### Option 2: Command-Line Plugin Creation
```bash
# Create from scratch
python generate_plugin_scaffold.py --name my-plugin --description "My awesome plugin"

# Create from existing plugin template (no description needed)
python generate_plugin_scaffold.py --template memory-rules --name my-memory-plugin

# Multi-language plugin (description required)
python generate_plugin_scaffold.py --name my-plugin --description "Multi-language plugin example" --langs en,ja,id,zh

# Advanced: disabled by default
python generate_plugin_scaffold.py --name experimental-plugin --no-enable --description "Experimental features"
```

### What the Scaffold Generator Creates
```
my-plugin/
├── README.md              # Comprehensive plugin documentation
├── RULES.md.en           # English rule algorithms with safety framework
├── RULES.md.ja           # Japanese localized templates (if requested)
├── RULES.md.id           # Indonesian localized templates (if requested)
├── RULES.md.zh           # Chinese localized templates (if requested)
├── settings.json         # Complete configuration with sensible defaults
├── setup.json           # Web interface config with localization
└── [Plugin automatically registered in plugins.json]
```

**✅ Benefits:**
- ⚡ **Instant**: Complete plugin in seconds
- 🎯 **Framework-Ready**: All integration points configured
- 🌍 **Multi-Language**: Templates in all requested languages
- 🔧 **Web-Integrated**: Automatically appears in setup.html
- 📚 **Documented**: Includes usage examples and troubleshooting
- 🛡️ **Safe**: Includes safety precautions and validation

**🔄 For Advanced Localization:**
After scaffold generation, if you need custom localization strings beyond the basic templates:
```bash
# Edit localization.json with your custom strings
# Then update setup.html automatically
python update_localization.py
```

---

## Manual Plugin Development (Advanced)

For advanced users who need full control or want to understand the framework internals, follow these manual steps. We'll use adding RAG rules as our example use case.

## Understanding Plugin Discovery Mechanisms

### CLI vs Web Interface Discovery

The framework has **two different plugin discovery mechanisms**:

#### CLI (`setup.py`) - Dynamic Discovery
- **Automatic**: Scans directories ending with `-rules`
- **Real-time**: Finds plugins by checking for `RULES.md.*` files
- **Flexible**: Works with any language, supports fallback
- **No registration required**: Just create the directory and files

#### Web (`setup.html`) - Static Manifest
- **Manifest-based**: Reads from `plugins.json` file
- **Pre-compiled**: Uses `generate_simple_setup.py` to embed config
- **Structured**: Requires `setup.json` files for each plugin
- **Registration required**: Must add to `plugins.json` and run generator

### Why Two Systems?
- **CLI**: For developers and power users who want immediate plugin discovery
- **Web**: For end users who need a simple double-click experience
- **Both**: Ensure complete compatibility across all usage scenarios

## Understanding Bootstrap Structure

Before extending, understand the bootstrap components:

```json
{
  "entry_points": {
    "global_config": "settings/global-settings.json",
    "rag_config": "rag-rules/settings.json",        // High priority: loads first
    "memory_config": "memory-rules/settings.json",   // Medium priority: loads second
    // Add new rule config here
    "critical_thinking_config": "critical-thinking-rules/settings.json"  // High priority
  },
  "loading_sequence": [
    // Priority-based loading order (lower step numbers = higher priority)
    // 1. User consent and global config (always first)
    // 2. High priority rules (RAG for context optimization)
    // 3. Medium priority rules (Memory enhanced by RAG)
    // 4. High priority rules (Critical Thinking for validation)
  ],
  "rule_interconnections": {
    // How rules communicate with each other
  },
  "platform_adapters": {
    // Platform-specific configurations
  },
  "framework_validation": {
    // File validation requirements
  }
}
```

## Step-by-Step: Adding RAG Rules (Example Use Case)

### Step 1: Create Rule Directory Structure
```bash
mkdir -p rag-rules
```

### Step 2: Create Rule Algorithm Specification
Create rule algorithm files in all supported languages:

**Main Algorithm File:** [`../rag-rules/RAG-RULES.md`](../rag-rules/RAG-RULES.md) (English - primary reference)

**Localized Rule Files:**
- [`rag-rules/RULES.md.en`](../rag-rules/RULES.md.en) - English version (identical to RAG-RULES.md)
- [`rag-rules/RULES.md.ja`](../rag-rules/RULES.md.ja) - Japanese version
- [`rag-rules/RULES.md.id`](../rag-rules/RULES.md.id) - Indonesian version

**Example structure for localized files:**
```markdown
# RAG Rules Agent Integration (English)
# RAGルールエージェント統合 (Japanese)
# Integrasi Aturan RAG Agen (Indonesian)

**⚠️ SAFETY PRECAUTION**: This is a TEMPLATE file. Agents MUST NOT auto-load this file. Only load when renamed to `AGENTS.md`, `GEMINI.md`, OR `CLAUDE.md` after explicit user activation.

[Algorithm specifications in respective language]
```

```markdown
# RAG Rules

## Overview
Algorithms for efficient information processing...

## Core Algorithms
[Define your algorithms here]
```

### Step 3: Create Rule Settings
Create [`rag-rules/settings.json`](../rag-rules/settings.json):

```json
{
  "rag_rules": {
    "enabled": true,
    "context_window_optimization": {
      "enabled": true,
      "max_context_tokens": 8000
    }
    // Add your rule-specific settings
  }
}
```

### Step 4: Update Global Settings
Add to [`settings/global-settings.json`](../settings/global-settings.json):

```json
"rule_categories": {
  "rag_rules": {
    "path": "../rag-rules",
    "enabled": true,
    "priority": "high",
    "description": "Efficient information processing and context management"
  }
}
```

### Step 5: Update Bootstrap Entry Points
Add to [`bootstrap.json`](../bootstrap.json) entry_points:

```json
"entry_points": {
  "rag_config": "rag-rules/settings.json"
}
```

### Step 6: Add Loading Sequence Step
Insert into [`bootstrap.json`](../bootstrap.json) loading_sequence array:

```json
{
  "step": 4,
  "action": "load_rag_config",
  "file": "rag-rules/settings.json",
  "condition": "global_config.agentic_rules_framework.rule_categories.rag_rules.enabled",
  "priority": "high"
}
```

### Step 7: Define Rule Interconnections
Add to [`bootstrap.json`](../bootstrap.json) rule_interconnections:

```json
"session_memory_to_rag": {
  "source_rule": "memory",
  "source_output": "session_topic_retrieval",
  "target_rule": "rag",
  "target_input": "context_optimization",
  "trigger_condition": "rag_context_request",
  "data_mapping": {
    "session_context": "context_data",
    "topic_history": "context_metadata"
  }
}
```

### Step 8: Update Framework Validation
Add to [`bootstrap.json`](../bootstrap.json) framework_validation:

```json
"required_config_files": [
  "rag-rules/settings.json"
],
"required_rule_files": [
  "rag-rules/RAG-RULES.md"
]
```

### Step 9: Update Platform Adapters (if needed)
For each platform in [`bootstrap.json`](../bootstrap.json) platform_adapters, add rule-specific paths:

```json
"cursor": {
  "rag_cache_path": "${workspace}/.cache/rag",
  "supported_features": ["file_system", "terminal", "editor_tools", "web_search"]
}
```

### Step 10: Update Documentation
Add to [`../README.md`](../README.md) Rule Categories section:

```markdown
### 3. RAG Rules
**Purpose**: Optimize information processing and context management
**Location**: [`rag-rules/RAG-RULES.md`](../rag-rules/RAG-RULES.md)
```

### Step 11: Validate JSON Syntax
```bash
# Validate all JSON files
python3 -m json.tool bootstrap.json
python3 -m json.tool settings/global-settings.json
python3 -m json.tool rag-rules/settings.json
```

### Step 12: Update Plugin Manifest for Web Interface (Manual Process)
**Note**: If you used `generate_plugin_scaffold.py`, this step was done automatically.

**CRITICAL**: The web interface (`setup.html`) uses a different plugin discovery mechanism than the CLI.

Add your new plugin to [`plugins.json`](../plugins.json):
```json
{
  "plugins": [
    "memory-rules",
    "rag-rules",
    "critical-thinking-rules",
    "your-new-rule-rules"
  ]
}
```

### Step 13: Generate Web Configuration (Manual Process)
**Note**: If you used `generate_plugin_scaffold.py`, run `generate_simple_setup.py` to complete web integration.

Run [`generate_simple_setup.py`](../generate_simple_setup.py) to update the web interface:
```bash
python3 generate_simple_setup.py
```

This will:
- Read `plugins.json` to discover plugins
- Load each plugin's `setup.json` configuration
- Embed all plugin data into `setup.html`
- Generate `web-config.json` for standalone operation

### Step 14: Test Integration
1. **CLI Test**: Run `python3 setup.py` to verify CLI plugin discovery
2. **Web Test**: Open `setup.html` to verify web interface includes your plugin
3. **Language Fallback**: Test with different language selections
4. **Rule Activation**: Verify rules activate correctly in both interfaces

## Template-Based Plugin Development

### Using Existing Plugins as Templates

The scaffold generator can create new plugins based on existing ones:

```bash
# Create a memory plugin based on the existing memory-rules
python generate_plugin_scaffold.py --template memory-rules --name my-memory-plugin

# Create a RAG plugin based on rag-rules
python generate_plugin_scaffold.py --template rag-rules --name my-rag-plugin
```

### What Template Creation Does

**Template Mode Benefits:**
- **Instant Structure**: Inherits proven plugin architecture
- **Customizable**: Override names, descriptions, and settings
- **Language Preservation**: Maintains all language templates from source
- **Settings Inheritance**: Gets sensible defaults from template plugin

**Example Template Workflow:**
```bash
# Start with memory rules as foundation
python generate_plugin_scaffold.py --template memory-rules --name session-memory-plugin --description "Session-specific memory management"

# The result inherits:
# - Memory algorithm patterns
# - Category structure (technical, behavioral, etc.)
# - Settings hierarchy
# - But with custom name and purpose
```

### Available Templates
Current framework plugins that can be used as templates:
- `memory-rules` - Comprehensive memory management system
- `rag-rules` - Information processing and context optimization
- `critical-thinking-rules` - Reasoning enhancement and validation

## General Extension Guidelines

### Rule Development Checklist
- [ ] **Algorithm Focus**: Define algorithms, not implementations
- [ ] **Tool Independence**: Rules work with any available tools
- [ ] **Settings Structure**: Include comprehensive configuration options
- [ ] **Interconnection Design**: Define how rule communicates with others
- [ ] **Platform Adaptation**: Consider platform-specific requirements
- [ ] **Localization Support**: Create rule files in all supported languages
- [ ] **Validation**: Ensure JSON syntax and framework integrity

### Naming Conventions
- **Rule Directories**: `rule-name-rules/`
- **Algorithm Files**: `RULE-NAME-RULES.md`
- **Settings Files**: `settings.json`
- **Bootstrap Keys**: `rule_name_config`

### Priority Levels
- **high**: Critical rules (thinking, safety)
- **medium**: Core functionality (memory)
- **low**: Enhancement features

### Common Interconnection Patterns
```json
{
  "source_output": "data_stream_name",
  "target_input": "input_parameter",
  "trigger_condition": "event_or_state",
  "data_mapping": {
    "source_field": "target_field"
  }
}
```

## Localization Support Requirements

### Rule Localization Structure
For each new rule, create localized versions using the framework's template system:

```
rule-name-rules/
├── RULE-NAME-RULES.md      # English primary reference (same as RULES.md.en)
├── RULES.md.en             # English version (core language)
├── RULES.md.ja             # Japanese version (core language)
├── RULES.md.id             # Indonesian version (core language)
├── [RULES.md.{lang}]       # Additional supported languages (see matrix below)
└── settings.json           # Language-neutral configuration
```

### Localization Guidelines

#### Content Consistency
- **Algorithm specifications** must be identical across all languages
- **Safety precautions** and technical requirements remain the same
- **Only user-facing text** (descriptions, examples) should be localized
- **Code examples** can remain in English unless specifically noted

#### Template-Based Generation
Use the automated scaffold generator for consistent localization:
```bash
python generate_plugin_scaffold.py --name "my-rule" --langs en,ja,id,de,fr
```

#### UI Localization
The setup interface automatically includes localization for all supported languages. No manual additions needed for [`localization.json`](../localization.json) - this is handled by the scaffold generator.

```json
{
  "en": {
    "rules": {
      "new_rule_name": "New Rule Description"
    }
  },
  "ja": {
    "rules": {
      "new_rule_name": "新しいルールの説明"
    }
  },
  "id": {
    "rules": {
      "new_rule_name": "Deskripsi Aturan Baru"
    }
  }
}
```

### Localization Validation Steps

#### 1. Verify File Creation
```bash
ls -la rule-name-rules/
# Should show: RULES.md.en, RULES.md.ja, RULES.md.id (or at minimum one RULES.md.* file)
```

#### 2. Content Consistency Check
- Compare algorithm sections across languages
- Ensure safety precautions are identical
- Verify technical specifications match

#### 3. Localization Testing
- Test setup.py with different language selections
- Verify UI displays correctly in each language
- Confirm rule activation works in all languages

#### 4. Localization Update (Web Interface)
After adding new localization strings to [`localization.json`](../localization.json), update the web interface:

```bash
python update_localization.py
```

This script will:
- Read your updated `localization.json`
- Embed the new strings into `setup.html`
- Update language selection dropdowns
- Automatically commit the changes

**Note**: The scaffold generator handles basic localization automatically, but for custom localization strings, use this script.

### Plugin Language Fallback System

**Important**: The framework supports plugin-level language fallback for maximum extensibility.

#### How Fallback Works
1. **Primary**: Setup requests a specific language (en/ja/id)
2. **Fallback**: If requested language template doesn't exist, uses any available `RULES.md.*` file
3. **Warning**: Shows notification when using non-standard language
4. **Flexibility**: Plugins can have any language as their "default"

#### Example Scenarios

**✅ Recommended**: Plugin with full localization
```
my-rule-rules/
├── RULES.md.en  # English
├── RULES.md.ja  # Japanese
├── RULES.md.id  # Indonesian
```

**✅ Acceptable**: Plugin with single language (fallback enabled)
```
chinese-rule-rules/
├── RULES.md.zh  # Only Chinese available
# Framework will use Chinese template even when user selects English/Japanese/Indonesian
```

**⚠️ Warning Display**: When fallback occurs
```
⚠️ chinese-rule → AGENTS.md (requested en, using available zh template)
Note: Plugin uses non-standard language. Consider adding en translation.
```

#### Benefits of Fallback System
- **Contributor Freedom**: Anyone can contribute plugins in their native language
- **No Translation Barriers**: Reduces barrier to entry for international contributors
- **Graceful Degradation**: System continues to work even with incomplete localization
- **Future Enhancement**: Contributors can add more languages later
- **Plugin Autonomy**: Plugins can establish their own language defaults

#### Best Practices for Contributors
- **Include English**: If possible, always include English version for broadest compatibility
- **Document Language**: Clearly document which language your plugin primarily supports
- **Accept Contributions**: Welcome translation contributions from other language speakers
- **Test Fallback**: Verify your plugin works with the framework's language selection

### Localization Maintenance
- **Keep synchronized**: When updating algorithms, update all language versions
- **Review translations**: Ensure technical accuracy in non-English versions
- **Test regularly**: Include localization testing in development workflow

### Example: Adding Localized Rule Descriptions

**English (RULES.md.en):**
```markdown
## Overview
This rule provides advanced context optimization for information processing.
```

**Japanese (RULES.md.ja):**
```markdown
## 概要
このルールは情報処理のための高度なコンテキスト最適化を提供します。
```

**Indonesian (RULES.md.id):**
```markdown
## Ikhtisar
Aturan ini menyediakan pengoptimalan konteks lanjutan untuk pemrosesan informasi.
```

## Simple Memory Commands

### Core Memory Operations

#### 1. Construct Memory for Current Project
**Simple Command:**
```
"Construct memory for current project"
```

**What Agent Does:**
- Creates complete project memory structure
- Analyzes git history and codebase
- Records key patterns, decisions, and context
- Sets up project-specific memory organization

#### 2. Sync Memory for Project
**Simple Command:**
```
"Sync memory for [project-name]"
```

**What Agent Does:**
- Updates existing project memory
- Incorporates recent changes and interactions
- Maintains memory consistency and relevance

#### 3. Check Memory Status
**Simple Command:**
```
"What's in memory for this project?"
```

**Agent Response:**
- Concise summary of stored information
- Key patterns and decisions recorded
- Current memory health status

### Memory Interaction History

**Example Flow:**
```
User: "Construct memory for current project"

Agent: "Understood. I'll construct comprehensive memory for this project. This includes analyzing git history, codebase patterns, and interaction context."

[Agent works...]

Agent: "Memory constructed. Recorded: 15 key patterns, 8 architectural decisions, 23 code examples. Ready for context-aware assistance."
```

**Key Principles:**
- **Simple commands** trigger complex memory operations
- **Agent understands intent** from minimal input
- **Concise responses** focus on results, not process details
- **Token-efficient** interactions prioritize outcomes

## Troubleshooting Extensions

### Common Issues
1. **JSON Syntax Errors**: Use `python3 -m json.tool` to validate
2. **Missing Dependencies**: Check loading sequence order
3. **Interconnection Failures**: Verify data mapping compatibility
4. **Platform Incompatibilities**: Test on target platforms

### Debug Steps
1. Validate all JSON files
2. Check bootstrap loading sequence
3. Verify rule interconnections
4. Test platform-specific configurations
5. Review algorithm implementations

## Advanced Extension Patterns

### Conditional Rule Loading
```json
"condition": "global_config.some_setting.enabled && platform_capabilities.web_search"
```

### Dynamic Interconnections
```json
"trigger_condition": "adaptive",
"data_mapping": "${rule_context}"
```

### Platform-Specific Overrides
```json
"platform_overrides": {
  "cursor": {"max_tokens": 16000},
  "vscode": {"max_tokens": 12000}
}
```

## Example: Complete RAG Rule Integration

After following the steps above, your framework should have:

- ✅ `rag-rules/` directory with algorithm specs and settings
- ✅ Bootstrap integration with loading and interconnections
- ✅ Platform adapters configured
- ✅ Documentation updated
- ✅ All JSON files validated
- ✅ Rule tested and functional

## Scaffold Generator Reference

### Command-Line Options
```bash
generate_plugin_scaffold.py [OPTIONS]

Options:
  --name TEXT           Plugin name in kebab-case (required)
  --display TEXT        Human-readable display name
  --description TEXT    Plugin description (required unless --template used)
  --langs TEXT          Languages (comma-separated codes or names)
  --template TEXT       Use existing plugin as template (makes --description optional)
  --no-enable           Create plugin disabled by default
  --help               Show help message

Note: --description is required when creating plugins from scratch, but optional when using --template.
```

### Language Support
The scaffold generator supports **150+ world languages** with multiple input methods:

**Language Codes (ISO 639-1):**
```bash
--langs en,de,zh,ar,hi,es,fr,ru,pt,ko
```

**Full Language Names:**
```bash
--langs english,german,chinese,arabic,hindi,spanish,french,russian,portuguese,korean
```

**Aliases and Variants:**
```bash
--langs eng,deutsch,mandarin,العربية,hindi,español,français,Русский,português,한국어
```

## 🌍 Language Support Matrix

The framework provides comprehensive multilingual support across three levels:

### 📊 Complete Language Support Table

| Language | Code | Native Name | Rules Template | README Template | Setup UI | Status |
|----------|------|-------------|----------------|-----------------|----------|--------|
| **English** | `en` | English | ✅ Full | ✅ Full | ✅ Complete | **Core** |
| **Japanese** | `ja` | 日本語 | ✅ Full | ❌ N/A | ✅ Complete | **Core** |
| **Indonesian** | `id` | Bahasa Indonesia | ✅ Full | ❌ N/A | ✅ Complete | **Core** |
| **German** | `de` | Deutsch | ✅ Full | ✅ Full | ✅ Complete | **Major** |
| **French** | `fr` | Français | ✅ Full | ✅ Full | ✅ Complete | **Major** |
| **Spanish** | `es` | Español | ✅ Full | ✅ Full | ✅ Complete | **Major** |
| **Arabic** | `ar` | العربية | ✅ Full | ✅ Full | ✅ Complete | **Major** |
| **Chinese** | `zh` | 中文 | ✅ Full | ❌ N/A | ❌ N/A | **Major** |
| **Korean** | `ko` | 한국어 | ✅ Full | ❌ N/A | ✅ Complete | **Major** |
| **Hindi** | `hi` | हिन्दी | ✅ Full | ❌ N/A | ✅ Complete | **Major** |
| **Portuguese** | `pt` | Português | ✅ Full | ❌ N/A | ✅ Complete | **Major** |
| **Russian** | `ru` | Русский | ✅ Full | ❌ N/A | ✅ Complete | **Major** |
| **Turkish** | `tr` | Türkçe | ✅ Full | ❌ N/A | ✅ Complete | **Major** |
| **Vietnamese** | `vi` | Tiếng Việt | ✅ Full | ❌ N/A | ✅ Complete | **Major** |
| **Thai** | `th` | ภาษาไทย | ✅ Full | ❌ N/A | ✅ Complete | **Major** |
| **Javanese** | `jv` | Basa Jawa | ✅ Full | ❌ N/A | ✅ Complete | **Major** |
| **Sinhala** | `si` | සිංහල | ✅ Full | ❌ N/A | ✅ Complete | **Major** |
| **Tamil** | `ta` | தமிழ் | ✅ Full | ❌ N/A | ✅ Complete | **Major** |

### 🎯 Support Level Definitions

#### **Rules Template** - Algorithm Content
- ✅ **Full**: Complete rule algorithms in native language
- ❌ **N/A**: Not available (uses generic English template)

#### **README Template** - Documentation
- ✅ **Full**: Localized plugin documentation
- ❌ **N/A**: English documentation only

#### **Setup UI** - Web Interface
- ✅ **Complete**: Full UI localization (titles, descriptions, options)
- ❌ **N/A**: English interface only

#### **Status Categories**
- **Core**: Original framework languages with complete support
- **Major**: Extended languages with comprehensive support

**All World Languages (150+ ISO codes supported):**
- 🌍 **African**: Arabic, Amharic, Hausa, Swahili, Yoruba, Zulu, Afrikaans...
- 🇪🇺 **European**: German, French, Spanish, Italian, Russian, Polish, Dutch, Swedish...
- 🌏 **Asian**: Hindi, Korean, Thai, Vietnamese, Turkish, Persian, Hebrew, Greek...
- 🌎 **American**: Portuguese, Dutch, Swedish, Norwegian...

**Language Validation:**
- Invalid language entries show clear error messages with available options
- Interactive mode provides retry mechanism with comprehensive language table
- Command-line mode exits with helpful error information
- Supports language aliases in native scripts (العربية, Русский, 한국어, etc.)

### Template Sources
Available plugins for `--template`:
- `memory-rules` - Memory management with categories, retention, search
- `rag-rules` - Context optimization, relevance scoring, information processing
- `critical-thinking-rules` - Reasoning validation, error prevention, verification

### Language Support Details
**Template Languages**: Only EN, JA, ID, ZH have actual rule templates
**Input Languages**: 150+ world languages accepted for future template creation
**Validation**: Comprehensive ISO 639-1 code validation with aliases
**Display**: Interactive mode shows supported languages with native names and flags

### Generated File Structure
```
plugin-name/
├── README.md              # Comprehensive documentation
├── RULES.md.en           # English rule algorithms
├── RULES.md.ja           # Japanese translations (if requested)
├── RULES.md.id           # Indonesian translations (if requested)
├── RULES.md.zh           # Chinese translations (if requested)
├── settings.json         # Configuration with sensible defaults
└── setup.json           # Web interface configuration
```

### Automatic Integration
✅ **Plugin Registration**: Added to `plugins.json` automatically
✅ **Web Interface**: Ready for `generate_simple_setup.py`
✅ **CLI Discovery**: Framework detects via directory scanning
✅ **Localization**: Templates in requested languages

### Related Tools
- [`generate_simple_setup.py`](../generate_simple_setup.py) - Generate web configuration from plugins
- [`update_localization.py`](../update_localization.py) - Update web interface with new localization strings
- [`setup.py`](../setup.py) - CLI interface for rule activation

## Manual Development Reference

### File Structure for Manual Rules
```
rule-name-rules/
├── RULE-NAME-RULES.md    # English primary algorithm specifications
├── RULES.md.en           # English localized version
├── RULES.md.ja           # Japanese localized version
├── RULES.md.id           # Indonesian localized version
└── settings.json         # Language-neutral configuration options
```

### Bootstrap Integration Points (Manual)
1. `entry_points` - Add config file reference
2. `loading_sequence` - Add loading step with conditions
3. `rule_interconnections` - Define data flow between rules
4. `framework_validation` - Add required files
5. `platform_adapters` - Add platform-specific settings

### Validation Checklist (Manual Development)
- [ ] JSON syntax valid in all files
- [ ] Loading sequence dependencies satisfied
- [ ] Rule interconnections properly mapped
- [ ] Platform adapters configured
- [ ] Documentation updated
- [ ] Rule algorithms defined in all languages (en, ja, id)
- [ ] Localization entries added to localization.json
- [ ] Plugin added to plugins.json manifest
- [ ] Web config generated with generate_simple_setup.py
- [ ] Settings comprehensively configured
- [ ] CLI plugin discovery working
- [ ] Web interface includes new plugin
- [ ] Localization testing completed for all languages

## Development Workflow Comparison

### Automated Development (Recommended)
```bash
# 5-minute plugin creation
python generate_plugin_scaffold.py --name my-plugin --description "My feature"
# → Complete plugin ready for testing
```

**Pros:**
- ⚡ **Fast**: Complete plugin in minutes
- 🎯 **Reliable**: Framework-compliant structure
- 🔧 **Integrated**: Automatic web interface registration
- 🌍 **Multi-language**: Templates in all supported languages
- 📚 **Documented**: Includes README and examples

**Cons:**
- 📝 **Less Control**: Fixed structure and conventions
- 🔄 **Standardized**: May not fit highly specialized needs

### Manual Development (Advanced)
```bash
# 2-3 hour comprehensive development
mkdir my-plugin-rules/
# Create 15+ files manually...
# Configure bootstrap, settings, localization...
```

**Pros:**
- 🎨 **Full Control**: Custom structure and architecture
- 🔧 **Specialized**: Can implement unique patterns
- 📖 **Educational**: Deep understanding of framework internals

**Cons:**
- ⏰ **Time-Intensive**: Hours of careful configuration
- 🐛 **Error-Prone**: Easy to miss integration points
- 🔄 **Maintenance**: More complex to maintain and update

## When to Use Each Approach

### Use Automated Development For:
- **New Contributors**: Quick start without learning all internals
- **Standard Plugins**: Rules that fit common patterns
- **Prototyping**: Rapid testing of rule concepts
- **Feature Extensions**: Adding variations of existing rule types

### Use Manual Development For:
- **Framework Extensions**: Adding new rule categories or patterns
- **Complex Integrations**: Rules with unusual bootstrap requirements
- **Research Rules**: Experimental algorithms needing custom loading
- **Platform Specialists**: Rules requiring deep platform-specific integration

## Migration: Manual to Automated

If you have manually created plugins, you can still benefit from automation:

### Option 1: Create New Version
```bash
# Create automated version alongside manual one
python generate_plugin_scaffold.py --name my-plugin-v2 --template memory-rules
# Compare and migrate customizations
```

### Option 2: Use as Template Source
```bash
# Use your custom plugin as template for variations
python generate_plugin_scaffold.py --template my-custom-plugin --name my-variant-plugin
```

### Option 3: Validate Manual Structure
```bash
# Test your manual plugin against automated standards
python setup.py  # CLI discovery
python generate_simple_setup.py  # Web integration
```

---

Copyright (c) 2025 Paulus Ery Wasito Adhi. Licensed under the MIT License (see LICENSE file).

