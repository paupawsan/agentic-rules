# 👥 User Guide - Agentic Rules Framework

## For Everyone (No Technical Knowledge Required!)

**Zero technical knowledge required!** This guide will walk you through setting up AI agent rules with simple double-clicks.

## 🚀 Quick Start

Choose the method that works best for you:

### ⚡ **Method 1: Direct Agent Command (Recommended)**
**One-time setup with your AI agent - no downloads required!**

1. **Initialize Framework**: Tell your AI agent to run `initiate agentic rules`
2. **Grant Permission**: When prompted, type `y` to enable the framework
3. **Confirm Settings**: Review and confirm the rule settings (Memory, RAG, Critical Thinking)
4. **Framework Active**: Your agent now has enhanced capabilities automatically!

**Benefits:**
- ✅ **Automatic**: Framework activates immediately with your agent
- ✅ **No Files**: No downloads or file management needed
- ✅ **Persistent**: System remembers setup - no repeated prompts
- ✅ **Smart**: Only asks for permission once, then loads automatically

### 🖱️ **Method 2: Web Interface Setup (Alternative)**
For users who prefer visual configuration:

#### Step 1: Download the Framework
1. Download the `agentic-rules` framework files from GitHub
2. Extract/unzip the downloaded files to any folder on your computer

#### Step 2: Launch the Setup
1. **Double-click** `setup.html` in the extracted folder
2. Your default web browser will open automatically

#### Step 3: Configure Your Rules
1. **Choose Language**: Select from officially supported languages
   - 🇺🇸 **English** (Primary language)
   - 🇯🇵 **日本語** (Japanese)
   - 🇮🇩 **Bahasa Indonesia** (Indonesian)

   > 💡 **For Plugin Developers**: If you want to create custom plugins with additional languages (🇩🇪 Deutsch, 🇫🇷 Français, 🇪🇸 Español, etc.), see the [Extension Manual](EXTENSION-MANUAL.md) for technical details on using `generate_plugin_scaffold.py` with multi-language template support.
2. **Select Rules**: Check the boxes for AI behaviors you want:
   - 🧠 **Memory Rules**: Helps AI remember context across conversations
   - 📚 **RAG Rules**: Improves AI's ability to find and use relevant information
   - 🤔 **Critical Thinking Rules**: Makes AI more careful and accurate

#### Step 4: Generate Configuration
1. Click **"Generate Configuration Files"**
2. The interface will create your personalized AI rules

#### Step 5: Save Your Files
Choose how you want to save the files:

- **💾 Save**: Opens a file browser to choose exactly where to save
- **📥 Download**: Downloads files directly to your Downloads folder
- **📋 Copy**: Copies content to clipboard for manual saving

#### Step 6: Use with Your AI Agent
1. Copy the generated files to your AI project's root directory
2. Configure your AI agent to load the rule files
3. Your AI agent now has enhanced capabilities!

## 📂 File Structure After Setup

Your AI project should look like this:
```
your-ai-project/
├── AGENTS.md              # Main agent configuration
├── modules/               # Plugin modules directory
│   ├── memory-rules/      # Memory system rules
│   │   ├── AGENTS.md     # Memory-specific rules
│   │   └── settings.json # Memory configuration
│   ├── rag-rules/        # RAG system rules
│   │   ├── AGENTS.md     # RAG-specific rules
│   │   └── settings.json # RAG configuration
│   └── critical-thinking-rules/  # Critical thinking rules
│       ├── AGENTS.md     # Thinking-specific rules
│       └── settings.json # Thinking configuration
```

## 🎯 What Each Rule Does

### 🧠 Memory Rules
- Remembers important information across conversations
- Maintains context between sessions
- Helps AI learn from past interactions

### 📚 RAG Rules
- Finds relevant information from your files
- Optimizes how AI reads and processes information
- Improves response accuracy with better context

### 🤔 Critical Thinking Rules
- Makes AI double-check its answers
- Reduces mistakes and "hallucinations"
- Promotes more careful and accurate responses

## 🔧 Troubleshooting

### Setup Won't Open
- Try right-clicking `setup.html` and selecting "Open with" your web browser
- Make sure you're opening the file from the extracted folder, not from within a ZIP archive

### Files Won't Save
- Check that your browser has permission to save files
- Try using the **📥 Download** option first, then move files manually

### Language Not Changing
- Refresh the page after changing the language
- Clear your browser cache if translations don't appear

## 💡 Tips

- **Start Simple**: Begin with just 1-2 rules to understand how they work
- **Test Gradually**: Try your AI agent with the new rules on simple tasks first
- **Backup First**: Save your existing AI configurations before adding new rules
- **Experiment**: Different combinations of rules work better for different types of tasks

## 📞 Need Help?

- Check the [troubleshooting section](#-troubleshooting) above
- Review the [developer guide](DEVELOPER-GUIDE.md) for advanced options
- Open an issue on GitHub for technical problems

---

**🎉 Congratulations!** Your AI agent now has enhanced capabilities through the Agentic Rules Framework.

## Localization / 多言語対応 / Pelokalan

<details>
<summary>🌍 This guide is also available in / このガイドは以下の言語でも利用可能です / Panduan ini juga tersedia dalam</summary>

- **[日本語 (Japanese)](localization/ja/USER-GUIDE.ja.md)** - ユーザーガイド
- **[Bahasa Indonesia (Indonesian)](localization/id/USER-GUIDE.id.md)** - Panduan Pengguna

</details>

---

Copyright (c) 2025 Paulus Ery Wasito Adhi. Licensed under the MIT License (see LICENSE file).
