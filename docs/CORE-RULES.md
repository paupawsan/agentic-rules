# 🤖 Core Agentic Rules Framework

## Document Purpose

**🎯 Primary Audience**: Framework Integrators, System Architects, and Agent Developers

**📋 Purpose**: This document provides the foundational principles and high-level overview for implementing the agentic rules framework. It serves as a reference for understanding the framework's philosophy, structure, and integration approach before diving into specific rule implementations.

---

## Overview

The Agentic Rules Framework provides a comprehensive, self-contained system for enhancing AI agent behavior through structured, algorithmic rules. The framework is designed to be:

- **🔌 Plug-and-Play**: Enable/disable rules without modifying agent behavior
- **📝 Algorithmic**: Rules expressed as behavioral guidelines, not binary constraints
- **🌐 Multi-Platform**: Works across Cursor, VSCode, CI systems, and custom implementations
- **🛠️ Tool-Agnostic**: Agents use available tools to implement rule algorithms
- **📦 Self-Contained**: Single HTML interface with embedded configuration (works offline)
- **🌍 Multilingual**: Full support for 18+ languages with localized rule templates
- **👀 Transparent**: All rule applications logged in accessible formats

## Framework Architecture

### Core Components

#### 🎯 Web Interface (`setup.html`)
- **Primary Tool**: Double-click to open, no installation required
- **Self-Contained**: Embedded configuration, works offline
- **Multi-Language**: Automatic localization (EN/JA/ID)
- **Configuration Generation**: Copy-paste interface for easy deployment
- **Auto-Re-localization**: Results update when language changes

#### ⚙️ Bootstrap System (`bootstrap.json`)
- **Orchestration Engine**: Machine-readable framework configuration
- **Loading Sequences**: Priority-based rule activation
- **Interconnections**: Data flow between rules
- **Platform Adapters**: Environment-specific adaptations
- **Validation**: Framework integrity checks

#### 📚 Rule Modules
- **Memory Rules**: Persistent context and knowledge storage
- **RAG Rules**: Information processing and context optimization
- **Critical Thinking Rules**: Reasoning verification and error prevention

### Integration Model

#### Distributed Per-Rule Architecture
- **Bootstrap Configuration**: `bootstrap.json` provides orchestration
- **Rule Algorithms**: Individual `AGENTS.md` files contain specific implementations
- **Generated Integration**: Web interface creates `AGENTS.md` files for enabled rules
- **Platform Adaptation**: Automatic environment detection and configuration

## Framework Principles

### 1. 🔌 Plug-and-Play Architecture
Rules can be activated/deactivated through the web interface without modifying core agent behavior. The framework maintains neutrality and doesn't interfere with existing agent operations.

### 2. 📝 Algorithmic Focus
Rules state the reasoning process and behavioral algorithms, not specific implementation details. Agents have freedom in how they execute these algorithms using available tools.

### 3. 🛠️ Tool Independence
Agents implement rule algorithms using their own capabilities and available tools. The framework describes what should be done, not how to do it with specific tools.

### 4. 👀 Transparency
All rule applications, decisions, and processes are logged in accessible markdown formats. Users can review how rules influenced agent behavior.

### 5. 🏗️ Framework Isolation
The framework remains a development tool and is never included in user project codebases. All integrations happen through generated `AGENTS.md` files in rule directories.

## 🎯 AI Rule Categories

### 🧠 Memory Rules (Priority: Medium)
**Algorithm File**: [`memory-rules/MEMORY-RULES.md`](memory-rules/MEMORY-RULES.md)
**Settings**: [`memory-rules/settings.json`](memory-rules/settings.json)
**Generated Integration**: [`memory-rules/AGENTS.md`](memory-rules/AGENTS.md) (created by web interface)

**Capabilities**:
- Structured markdown-based knowledge storage
- Context-aware capture and retrieval systems
- Pattern recognition and categorization
- Adaptive retention policies
- Cross-session memory persistence

**Integration Requirements**:
- Requires valid storage path configuration
- Must implement all memory algorithms when enabled
- Should integrate with RAG rules for enhanced context

### 🔍 RAG Rules (Priority: High)
**Algorithm File**: [`rag-rules/RAG-RULES.md`](rag-rules/RAG-RULES.md)
**Settings**: [`rag-rules/settings.json`](rag-rules/settings.json)
**Generated Integration**: [`rag-rules/AGENTS.md`](rag-rules/AGENTS.md) (created by web interface)

**Capabilities**:
- Hierarchical document reading and analysis
- Relevance-based context optimization
- Multi-language content processing
- Context window management for LLM efficiency
- Pattern recognition across codebases

**Integration Requirements**:
- Critical for optimal context usage
- Should influence memory construction priorities
- Must implement relevance scoring algorithms

### 🤔 Critical Thinking Rules (Priority: High)
**Algorithm File**: [`critical-thinking-rules/CRITICAL-THINKING-RULES.md`](critical-thinking-rules/CRITICAL-THINKING-RULES.md)
**Settings**: [`critical-thinking-rules/settings.json`](critical-thinking-rules/settings.json)
**Generated Integration**: [`critical-thinking-rules/AGENTS.md`](critical-thinking-rules/AGENTS.md) (created by web interface)

**Capabilities**:
- Systematic assumption challenging
- Multi-source verification protocols
- Error admission and correction mechanisms
- Logical consistency validation
- Grounded reasoning safeguards

**Integration Requirements**:
- **MANDATORY** for responsible AI behavior
- Must implement error admission algorithms
- Critical for preventing hallucinations

## ⚙️ Configuration System

### Global Settings
**File**: [`settings/global-settings.json`](settings/global-settings.json)
**Purpose**: Master control for framework components and platform adaptations
**Configuration Method**: Edit manually or use web interface

### Rule-Specific Settings
**Location**: `{rule-name}-rules/settings.json`
**Purpose**: Detailed behavioral configuration for individual rules
**Configuration Method**: Modified by web interface when rules are enabled

### Bootstrap Configuration
**File**: [`bootstrap.json`](bootstrap.json)
**Purpose**: Machine-readable orchestration and rule interconnections
**Audience**: Agent systems implementing the framework
**Modification**: Advanced users only - defines loading sequences and platform adapters

### Web Interface Configuration
**File**: [`setup.html`](setup.html) (embedded)
**Purpose**: User-friendly configuration interface
**Capabilities**: Language selection, rule activation, settings generation
**Output**: Generates `AGENTS.md` files for enabled rules

## 🚀 Implementation Workflow

### For Non-Technical Users (Quick Setup)
1. **Download** the framework files to your computer
2. **Double-click** `setup.html` to open the web interface
3. **Choose** your preferred language (🇺🇸 English / 🇯🇵 日本語 / 🇮🇩 Bahasa Indonesia)
4. **Select** the AI rules you want to enable
5. **Configure** any rule-specific settings
6. **Generate** configuration files using the built-in interface
7. **Copy-paste** the generated files to your AI project
8. **Done!** Your AI agents will now use the enhanced behaviors

### For Framework Integrators
1. **Web Interface**: Use `setup.html` for guided configuration
2. **Review Principles**: Read this document for framework philosophy
3. **Platform Setup**: Configure [`settings/global-settings.json`](settings/global-settings.json) for your environment
4. **Rule Integration**: Load generated `AGENTS.md` files for each enabled rule
5. **Bootstrap Loading**: Read [`bootstrap.json`](bootstrap.json) for orchestration logic
6. **Monitor Operations**: Review generated logs for rule application tracking

### For Agent Developers
1. **Algorithm Study**: Read specific rule documents (MEMORY-RULES.md, etc.) for implementation details
2. **Integration Files**: Load `AGENTS.md` from enabled rule directories
3. **Algorithm Implementation**: Execute rule algorithms using available tools
4. **Transparency Logging**: Log all rule applications and decision processes
5. **Bootstrap Compliance**: Respect [`bootstrap.json`](bootstrap.json) orchestration requirements
6. **Platform Adaptation**: Use platform adapters for environment-specific behavior

### For System Architects
1. **Framework Design**: Understand distributed per-rule integration model
2. **Platform Planning**: Configure platform adapters in `bootstrap.json`
3. **Rule Orchestration**: Design optimal rule interaction patterns
4. **Performance Tuning**: Adjust settings for specific use cases and scale
5. **Monitoring Setup**: Establish logging and compliance monitoring procedures

## 🌍 Multilingual Support

The framework provides complete localization support:

- **🇺🇸 English**: Full interface and documentation
- **🇯🇵 日本語**: Complete Japanese translation
- **🇮🇩 Bahasa Indonesia**: Full Indonesian localization

**Language switching** happens automatically in the web interface and affects all generated content.

## 📚 Documentation Resources

### User Documentation
- **[`README.md`](README.md)**: Complete setup guide and usage instructions
- **[`docs/INDEX.md`](docs/INDEX.md)**: Documentation index and navigation

### Developer Documentation
- **[`docs/EXTENSION-MANUAL.md`](docs/EXTENSION-MANUAL.md)**: Step-by-step guide for adding new rules
- **[`CORE-RULES.md`](CORE-RULES.md)**: This file - framework principles and architecture

### Technical References
- **[`bootstrap.json`](bootstrap.json)**: Machine-readable orchestration configuration
- **[`Bootstrap.md`](Bootstrap.md)**: Detailed algorithmic specifications for agents
- **Rule Algorithm Files**: `{rule-name}-rules/{RULE-NAME}-RULES.md` - specific implementation algorithms

## 🔧 Development Tools

### Web Interface (`setup.html`)
- **Primary Tool**: Self-contained configuration interface
- **Offline Operation**: No network dependencies
- **Multi-language**: Automatic localization
- **File Generation**: Copy-paste deployment workflow

### Python Scripts
- **`generate_simple_setup.py`**: Plugin development tool for web interface updates
- **`update_localization.py`**: Localization management and HTML embedding
- **`setup.py`**: Command-line interface for advanced users

## ⚠️ Critical Integration Notes

### Framework Isolation
**MANDATORY**: The agentic-rules framework is a development tool only. Never include framework files in user project codebases.

### Distributed Integration
**REQUIRED**: Agents must load `AGENTS.md` files from individual rule directories (generated by the web interface) rather than framework files directly.

### Bootstrap Compliance
**CRITICAL**: Agents must respect [`bootstrap.json`](bootstrap.json) configuration and only execute enabled rules.

### Active Implementation
**MANDATORY**: Configuration alone is insufficient. Agents must actually implement and execute all rule algorithms in their runtime environment.

---

<!-- METADATA: Core framework rules and integration guidelines for developers -->
<!-- LICENSE: Copyright (c) 2025 Paulus Ery Wasito Adhi - Licensed under the MIT License. See LICENSE file for details. -->
