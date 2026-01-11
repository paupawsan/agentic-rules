# Manual System Rules Loader

This command loads the complete system configuration and rules from a specified directory into the agent's operational context.

## Usage

Run this command to manually load a system when the agent needs to understand and operate within a specific framework or rule set.

### Command Syntax
```
/agentic-rules/preload-agentic-rules [TARGET_DIRECTORY]
```

### Examples
```bash
# Load system from absolute path
/agentic-rules/preload-agentic-rules /Users/username/Projects/my-system

# Load system from relative path (relative to workspace)
/agentic-rules/preload-agentic-rules ../my-system

# Interactive mode (prompts for directory if none provided)
/agentic-rules/preload-agentic-rules
```

## Command Configuration

```bash
# Manual System Rules Loader Command
# This command helps load complete system configurations and rule sets into agent context

# Check if directory argument was provided
if [ $# -eq 1 ]; then
    TARGET_DIR="$1"
    echo "Using specified directory: $TARGET_DIR"
else
    # Prompt user for target project directory if not provided
    read -p "Enter target project directory (relative to workspace): " TARGET_DIR
fi

# Validate target directory exists
if [ ! -d "$TARGET_DIR" ]; then
    echo "Error: Directory '$TARGET_DIR' does not exist"
    exit 1
fi

echo "Scanning for system files in: $TARGET_DIR"

# Function to load system files
load_system_file() {
    local file_path=$1
    local relative_path=${file_path#$TARGET_DIR/}

    if [ -f "$file_path" ]; then
        echo ""
        echo "=== LOADING: $relative_path ==="
        echo ""
        cat "$file_path"
        echo ""
        echo "--- END OF $relative_path ---"
        echo ""
    fi
}

# Find and load all AGENTS.md, GEMINI.md, and CLAUDE.md files (excluding backup files)
FOUND_FILES=$(find "$TARGET_DIR" -type f \( -name "AGENTS.md" -o -name "GEMINI.md" -o -name "CLAUDE.md" \) ! -name "*.backup" | sort)

if [ -z "$FOUND_FILES" ]; then
    echo "No system files found in $TARGET_DIR"
    echo ""
    echo "System directories typically contain:"
    echo "- Agent configuration and behavior files"
    echo "- Model-specific system configurations"
    echo "- README.md or documentation files"
    echo "- Configuration files (.json)"
    echo "- Rule definition files (.md)"
    echo "- System specification documents"
    echo ""
    echo "🎉 System scan complete!"
    echo ""
    echo "System has been scanned from: $TARGET_DIR"
    echo ""
    echo "No system files were found to load."
    exit 0
fi

echo "Found $(echo "$FOUND_FILES" | wc -l) system file(s):"
echo "$FOUND_FILES" | while read -r file; do
    relative_path=${file#$TARGET_DIR/}
    echo "  - $relative_path"
done

echo ""
echo "Loading system..."

# Load each found file
echo "$FOUND_FILES" | while read -r file; do
    load_system_file "$file"
done

echo "🎉 System loading complete!"
echo ""
echo "System has been loaded from: $TARGET_DIR"
```

## Safety Compliance

This command respects system safety precautions:
- Only loads system configurations when explicitly requested by user
- Does not auto-load or auto-process files
- Works with existing system documentation and configuration files only

## Requirements

- Target directory must exist and contain system files
- System files must already be present (typically .md, .txt, or .json files)
- User must explicitly run this command
- Directory path can be provided as command-line argument or entered interactively

## Troubleshooting

If system doesn't load properly:
1. Ensure system files exist in the target directory
2. Check that files have appropriate extensions (.md, .txt, .json)
3. Verify files contain valid system documentation or configuration
4. Ensure the agent has access to read the specified directory

---

<!-- LICENSE: Copyright (c) 2025-2026 Paulus Ery Wasito Adhi - Licensed under the MIT License. See LICENSE file for details. -->