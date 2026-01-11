# 📥 Preload Agentic Rules Command

The **Preload Agentic Rules** command allows you to manually load system rules and configurations from a specified directory into the agent's operational context.

## 🎯 Purpose

This command is useful when:
- Cursor doesn't automatically detect nested agent rules
- You need to load rules from a different directory location
- You want to explicitly load a specific system configuration
- The agent needs to understand a framework or rule set from another project

## 📋 Command Syntax

```
/agentic-rules/preload-agentic-rules [TARGET_DIRECTORY]
```

### Parameters

- **`TARGET_DIRECTORY`** (optional): Path to the directory containing system rule files
  - Can be an absolute path: `/Users/username/Projects/my-agent-rules`
  - Can be a relative path: `../my-agent-rules` or `./subfolder/rules`
  - If omitted, the command will prompt you interactively

## 💡 Usage Examples

### Example 1: Load from Absolute Path
```bash
/agentic-rules/preload-agentic-rules /Users/paupawsan/Library/CloudStorage/GoogleDrive-paupawsan@gmail.com/My Drive/AI/local-as/agentic-rules
```

### Example 2: Load from Relative Path
```bash
# Relative to current workspace
/agentic-rules/preload-agentic-rules ../my-agent-rules

# Relative to current directory
/agentic-rules/preload-agentic-rules ./config/rules
```

### Example 3: Interactive Mode
```bash
# Run without arguments - will prompt for directory
/agentic-rules/preload-agentic-rules
```

## 🔍 What Files Are Loaded?

The command automatically searches for and loads the following system rule files:

- **`AGENTS.md`** - Generic agent configuration and behavior rules
- **`GEMINI.md`** - Google Gemini-specific system configuration
- **`CLAUDE.md`** - Anthropic Claude-specific system configuration

The command searches recursively through the target directory and all subdirectories, excluding backup files (files ending in `.backup`).

## ✅ Expected Output

When files are found:
```
Scanning for system files in: /path/to/directory
Found 3 system file(s):
  - AGENTS.md
  - modules/memory-rules/AGENTS.md
  - modules/rag-rules/AGENTS.md

Loading system files...

=== LOADING: AGENTS.md ===
[File content displayed here]
--- END OF AGENTS.md ---

🎉 System loading complete!
System has been loaded from: /path/to/directory
```

When no files are found:
```
Scanning for system files in: /path/to/directory
No system files found in /path/to/directory

System directories typically contain:
- Agent configuration and behavior files
- Model-specific system configurations
- README.md or documentation files
- Configuration files (.json)
- Rule definition files (.md)
- System specification documents

🎉 System scan complete!
System has been scanned from: /path/to/directory
No system files were found to load.
```

## 🛡️ Safety Features

- **Explicit User Action Required**: Only loads when explicitly requested
- **No Auto-Loading**: Never automatically loads or processes files
- **Backup File Protection**: Automatically excludes `.backup` files
- **Directory Validation**: Verifies directory exists before scanning
- **Read-Only Operation**: Only reads files, never modifies them

## 📝 Requirements

- Target directory must exist
- System files must be named exactly: `AGENTS.md`, `GEMINI.md`, or `CLAUDE.md`
- Agent must have read access to the specified directory
- User must explicitly run the command

## 🔧 Troubleshooting

### Issue: "Directory does not exist"
**Solution**: Verify the path is correct. Use absolute paths if relative paths don't work.

### Issue: "No system files found"
**Possible causes**:
- Files are not named correctly (must be `AGENTS.md`, `GEMINI.md`, or `CLAUDE.md`)
- Files are in a subdirectory that wasn't scanned
- Files have `.backup` extension

**Solution**: 
- Check file names match exactly
- Verify files exist in the target directory
- Remove `.backup` extension if needed

### Issue: Files found but not loading
**Solution**: 
- Check file permissions (agent needs read access)
- Verify files contain valid content
- Try running the command again

## 🔗 Related Documentation

- **[Troubleshooting Guide](TROUBLESHOOTING.md)** - Common issues and manual loading instructions
- **[User Guide](USER-GUIDE.md)** - Complete framework setup and usage
- **[Developer Guide](DEVELOPER-GUIDE.md)** - Advanced configuration and automation

## 📚 Best Practices

1. **Use Absolute Paths**: More reliable than relative paths, especially when working across different directories
2. **Organize Rules**: Keep all rule files in a dedicated directory for easier management
3. **Version Control**: Track rule files in version control to maintain consistency
4. **Test After Loading**: Verify the agent understands the loaded rules by asking a test question

---

**Note**: This command is designed to work seamlessly with the Agentic Rules Framework. After loading, the agent will understand and operate according to the loaded system rules.

<!-- LICENSE: Copyright (c) 2025-2026 Paulus Ery Wasito Adhi - Licensed under the MIT License. See LICENSE file for details. -->
