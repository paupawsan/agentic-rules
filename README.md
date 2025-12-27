# 🤖 Agentic Rules Framework

A plug-and-play framework providing structured rules for intelligent AI agent behavior across different platforms.

## 🌍 Localization / 多言語対応 / Pelokalan

<details open>
<summary>📚 Documentation available in multiple languages / ドキュメントが複数の言語で利用可能です / Dokumentasi tersedia dalam berbagai bahasa</summary>

### Japanese (日本語)
<details>
<summary>🇯🇵 Japanese Documentation / 日本語ドキュメント</summary>

- **[メインページ / Main Page](docs/localization/ja/README.ja.md)** - フレームワークの概要とクイックスタート
- **[説明書の目次 / Documentation Index](docs/localization/ja/INDEX.ja.md)** - 説明書の全体像
- **[ユーザーガイド / User Guide](docs/localization/ja/USER-GUIDE.ja.md)** - 初心者向けガイド
- **[開発者ガイド / Developer Guide](docs/localization/ja/DEVELOPER-GUIDE.ja.md)** - 技術者向け詳細
- **[システムの説明 / System Overview](docs/localization/ja/SYSTEM-OVERVIEW.ja.md)** - システムの仕組み
- **[拡張マニュアル / Extension Manual](docs/localization/ja/EXTENSION-MANUAL.ja.md)** - プラグイン開発
- **[トラブルシューティング / Troubleshooting](docs/localization/ja/TROUBLESHOOTING.ja.md)** - 問題解決ガイド

</details>

### Indonesian (Bahasa Indonesia)
<details>
<summary>🇮🇩 Indonesian Documentation / Dokumentasi Bahasa Indonesia</summary>

- **[Halaman Utama / Main Page](docs/localization/id/README.id.md)** - Ikhtisar framework dan mulai cepat
- **[Indeks Dokumentasi / Documentation Index](docs/localization/id/INDEX.id.md)** - Ringkasan dokumentasi
- **[Panduan Pengguna / User Guide](docs/localization/id/USER-GUIDE.id.md)** - Panduan untuk pemula
- **[Panduan Pengembang / Developer Guide](docs/localization/id/DEVELOPER-GUIDE.id.md)** - Detail teknis untuk insinyur
- **[Ikhtisar Sistem / System Overview](docs/localization/id/SYSTEM-OVERVIEW.id.md)** - Detail arsitektur
- **[Manual Ekstensi / Extension Manual](docs/localization/id/EXTENSION-MANUAL.id.md)** - Pengembangan plugin
- **[Panduan Pemecahan Masalah / Troubleshooting](docs/localization/id/TROUBLESHOOTING.id.md)** - Panduan penyelesaian masalah

</details>

</details>

## 🚀 Quick Start - First Time Setup

### ⚠️ **Step 1: Run Setup Interface (IMPORTANT!)**
**Execute `setup.html` first to configure your rules and generate necessary files!**

1. **Download** the framework files from GitHub
2. **Double-click** `setup.html` to launch the web interface
3. **Configure** your preferred rules (Memory, RAG, Critical Thinking)
4. **Generate** configuration files

> 💡 **Why setup.html first?** The web interface creates the required configuration files and rule files that the bootstrap system needs. Without this step, the framework may not initialize properly.
>
> 🔧 **For Engineers/Developers**: Use the enhanced Python launcher for better functionality - it provides direct file creation and server controls. See [Developer Guide](docs/DEVELOPER-GUIDE.md) for setup automation options.

---

### ⚡ **Step 2: Initialize Agentic Rules System**
**After setup.html, complete this ONE-TIME bootstrap initialization!**

1. **Tell your AI agent**: `Initialize the agentic rules system in /path/to/your/agentic-rules folder. I already completed setup.html, so just perform the bootstrap initialization.`
2. **Grant permission** when prompted to enable the framework
3. **Review settings** for Memory, RAG, and Critical Thinking rules
4. **Framework is active** - your agent now has enhanced capabilities!

> 💡 **Why this step?** The framework requires initial bootstrap configuration to ensure proper integration with your AI environment. This one-time setup enables all framework features.

---

## 🎯 Framework Overview

The **Agentic Rules Framework** enhances AI agent capabilities through three specialized rule systems:

### 🧠 **Memory Rules** (Local Memory System)
📖 **[Plugin Details](modules/memory-rules/README.md)** - **Local, human-readable memory** system with 10 specialized categories for persistent context, learning, and personalization across sessions. Full visibility and control over your AI agent's memory data.

### 📚 **RAG Rules**
📖 **[Plugin Details](modules/rag-rules/README.md)** - Advanced information processing with smart reading strategies, context optimization, relevance scoring, and **automatic Knowledge Graph construction** for intelligent project understanding and relationship mapping.

### 🤔 **Critical Thinking Rules**
📖 **[Plugin Details](modules/critical-thinking-rules/README.md)** - Systematic reasoning enhancement with error prevention, assumption validation, and evidence-based decision making.

**Key Benefits:**
- **🔌 Plug-and-Play**: Enable/disable rules without modifying agent behavior
- **🌍 Multi-Platform**: Works with Cursor, VSCode, and custom agentic systems
- **📦 Self-Contained**: Single HTML file with embedded configuration
- **🛠️ Tool Agnostic**: Agents use available tools to implement rule requirements
- **🌐 Generic**: Applicable to any AI agent capable of following structured guidelines
- **🌍 Multi-Language**: 18+ languages supported with localized rule templates

## 🧠 **Knowledge Graph Integration**
**✅ ENABLED BY DEFAULT** - Automatic KG construction and usage for intelligent project understanding.

### **What It Does**
- **🔍 Automatic Discovery**: Scans conversations and codebases to build knowledge graphs
- **🧷 Smart Linking**: Connects related concepts, files, and ideas automatically
- **💬 Proactive Usage**: Uses KG insights in conversations without manual activation
- **📈 Learning Evolution**: KGs grow smarter with continued usage

### **For Users**
- **Zero Configuration**: Works out-of-the-box with standard setup
- **Enhanced Conversations**: Responses include relevant historical context
- **Relationship Understanding**: System knows how project components connect
- **Progressive Intelligence**: Gets smarter with each interaction

### **For Agent Developers**
📖 **[KG Implementation Guide](docs/KG_IMPLEMENTATION_GUIDE.md)** - Logical algorithms and pseudocode for KG functionality
📖 **[User KG Integration](docs/README_KG_INTEGRATION.md)** - End-user KG experience and benefits

## 🚀 Quick Start

### ⚡ **First-Time Setup** (One-Time Only)
1. **Initialize Framework**: Run `initiate agentic rules` in your AI agent
2. **Grant Consent**: Approve framework activation when prompted
3. **Framework Ready**: System remembers initialization - no repeated prompts needed

**After initialization, the framework activates automatically with your agent.**

### 📋 **Choose Your Experience Level**

#### 👥 **For Everyone** (No Technical Knowledge)
📖 **[User Guide](docs/USER-GUIDE.md)** - Double-click setup with step-by-step instructions

#### 🔧 **For Engineers & Developers**
📖 **[Developer Guide](docs/DEVELOPER-GUIDE.md)** - Server setup, automation, and API usage

#### 🛠️ **For Plugin Developers**
📖 **[Extension Manual](docs/EXTENSION-MANUAL.md)** - Plugin development and framework extension

#### 📚 **System Architecture & Technical Deep Dive**
📖 **[System Overview](docs/SYSTEM-OVERVIEW.md)** - Complete technical architecture and design principles

#### 🐛 **Troubleshooting & FAQ**
📖 **[Troubleshooting Guide](docs/TROUBLESHOOTING.md)** - Solutions for common issues and manual loading instructions
🛠️ **Quick Scaffold**: `python generate_plugin_scaffold.py --help` - Generate plugin templates instantly

### 🔄 **Framework Lifecycle**
- **Initialization**: One-time setup with user consent
- **Automatic Activation**: Framework loads automatically after first setup
- **Configuration**: Modify settings in `settings/global-settings.json`
- **Reset**: Delete `.agentic_initialized` file to force re-initialization

## 🤝 Contributing

**We welcome contributions!** This project thrives on community input and collaboration.

- 📝 **Report Issues**: Found a bug? Have a suggestion? [Open an issue](https://github.com/paupawsan/agentic-rules/issues)
- 🔧 **Submit Pull Requests**: Help improve the framework
- 💬 **Discussions**: Join conversations about agentic systems and AI behavior
- 📖 **Documentation**: Help improve guides and documentation

## ⚠️ Important Disclaimers

**Personal Project**: This framework is designed and developed using personal time and resources. I am not affiliated with any company, and this is not an official product or service.

**Maintenance Notice**: I cannot guarantee active updates or timely maintenance. While I strive to keep the framework functional and secure, updates depend on available time and resources.

**Community Support**: Your contributions, feedback, and participation mean a lot to the continued development and improvement of this framework. Community involvement helps ensure the project remains useful and relevant.

**Use at Your Own Risk**: This framework is provided as-is. Users should evaluate its suitability for their specific use cases and implement appropriate security measures.

---

Copyright (c) 2025 Paulus Ery Wasito Adhi. Licensed under the MIT License (see LICENSE file).
