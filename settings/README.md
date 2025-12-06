# Settings Configuration

## Overview

Settings control the activation and behavior of agentic rules. Each rule category has its own settings file, with a global settings file coordinating overall behavior.

## Configuration Hierarchy

```
global-settings.json (main control)
├── memory-rules/settings.json
├── critical-thinking-rules/settings.json
└── rag-rules/settings.json
```

## Global Settings

### Rule Categories
- **memory_rules**: Controls persistent understanding storage
- **critical_thinking_rules**: Manages verification and reasoning behavior
- **rag_rules**: Handles information processing optimization

### Platform Support
- **cursor_support**: Cursor IDE integration
- **vscode_support**: Visual Studio Code integration
- **ci_systems_support**: CI/CD pipeline integration
- **custom_platforms**: Third-party agentic systems

## Rule-Specific Settings

### Memory Rules Settings
```json
{
  "memory_rules": {
    "enabled": true,
    "storage_path": "./memory",
    "max_entries_per_category": 100,
    "categories": {
      "technical": {"enabled": true},
      "behavioral": {"enabled": true},
      "contextual": {"enabled": true}
    }
  }
}
```

### Critical Thinking Rules Settings
```json
{
  "critical_thinking_rules": {
    "enabled": true,
    "verification_level": "standard",
    "error_admission": {"enabled": true},
    "ground_check": {"enabled": true}
  }
}
```

### RAG Rules Settings
```json
{
  "rag_rules": {
    "enabled": true,
    "context_window_optimization": {"enabled": true},
    "hierarchical_reading": {"enabled": true},
    "log_analysis": {"enabled": true}
  }
}
```

## Usage Instructions

1. **Enable/Disable Rules**: Set `enabled: true/false` in global-settings.json or individual rule settings
2. **Adjust Parameters**: Modify values in respective settings files
3. **Platform Adaptation**: Enable relevant platform support flags
4. **Monitor Performance**: Adjust limits based on system capabilities

## Safety Features

- **Emergency Shutdown**: Automatically disable rules if conflicts detected
- **User Override**: Allow manual control when needed
- **Conflict Resolution**: Priority-based rule conflict handling
- **Backup**: Automatic settings backup before changes

## Logging

All rule applications are logged when `logging_enabled: true`. Logs include:
- Rule activation/deactivation events
- Parameter changes
- Performance metrics
- Error conditions

---

Copyright (c) 2025 Paulus Ery Wasito Adhi. Licensed under the MIT License (see LICENSE file).

