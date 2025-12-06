# 🐛 Troubleshooting Guide

## Common Issues and Solutions

### 🔄 **Editor Won't Load AGENTS.md Automatically**

**Problem**: Cursor, VSCode, or other editors sometimes fail to automatically load `AGENTS.md`, `GEMINI.md`, or `CLAUDE.md` into the agent's context, preventing the rules from taking effect.

**Symptoms**:
- Agent behaves as if no rules are active
- Memory, RAG, or critical thinking features don't work
- Agent forgets project context between sessions

**Solution**: Manually load the rules file into your prompt.

#### Quick Manual Loading Prompts

**Option 1: Paste File Content**
```
Please follow these structured rules for our interaction. Load and apply all rules from this AGENTS.md file:

[PASTE THE ENTIRE CONTENT OF YOUR AGENTS.md FILE HERE]

Apply these rules immediately and maintain them throughout our conversation. Confirm you understand and will follow these guidelines.
```

**Option 2: Provide File Path**
```
Please follow these structured rules for our interaction. Load and apply all rules from the file at this path:

[path/to/your/project/]AGENTS.md

Apply these rules immediately and maintain them throughout our conversation. Confirm you understand and will follow these guidelines.
```

**Alternative: Cursor @ Reference**
```
Please follow these structured rules for our interaction. Load and apply all rules from this file:

@AGENTS.md

Apply these rules immediately and maintain them throughout our conversation. Confirm you understand and will follow these guidelines.
```

**💡 Tip:** Use `@filename` in Cursor - it automatically resolves to the correct file path!

**For GEMINI.md (Gemini-Specific)**:
```
Please follow these Gemini-optimized rules for our interaction. Load and apply all rules from this GEMINI.md file:

[PASTE THE ENTIRE CONTENT OF YOUR GEMINI.md FILE HERE]

Apply these rules immediately and maintain them throughout our conversation. Confirm you understand and will follow these guidelines.
```

**Alternative: File Path Only**
```
Please follow these Gemini-optimized rules for our interaction. Load and apply all rules from the file at this path:

[path/to/your/project/]GEMINI.md

Apply these rules immediately and maintain them throughout our conversation. Confirm you understand and will follow these guidelines.
```

**Or use Cursor @ Reference**
```
Please follow these Gemini-optimized rules for our interaction. Load and apply all rules from this file:

@GEMINI.md

Apply these rules immediately and maintain them throughout our conversation. Confirm you understand and will follow these guidelines.
```

**For CLAUDE.md (Claude-Specific)**:
```
Please follow these Claude-optimized rules for our interaction. Load and apply all rules from this CLAUDE.md file:

[PASTE THE ENTIRE CONTENT OF YOUR CLAUDE.md FILE HERE]

Apply these rules immediately and maintain them throughout our conversation. Confirm you understand and will follow these guidelines.
```

**Alternative: File Path Only**
```
Please follow these Claude-optimized rules for our interaction. Load and apply all rules from the file at this path:

[path/to/your/project/]CLAUDE.md

Apply these rules immediately and maintain them throughout our conversation. Confirm you understand and will follow these guidelines.
```

**Or use Cursor @ Reference**
```
Please follow these Claude-optimized rules for our interaction. Load and apply all rules from this file:

@CLAUDE.md

Apply these rules immediately and maintain them throughout our conversation. Confirm you understand and will follow these guidelines.
```

#### Step-by-Step Manual Loading Process

**Option A: Full Content Loading**
1. **Open your rules file** in your editor
2. **Copy the entire content** (Ctrl+A, Ctrl+C)
3. **Start a new chat/conversation**
4. **Paste the appropriate prompt above**
5. **Replace `[PASTE THE ENTIRE CONTENT...]` with your actual file content**
6. **Send the message**

**Option B: File Path Loading**
1. **Ensure your rules file is accessible** to the AI agent
2. **Start a new chat/conversation**
3. **Use one of these approaches:**
   - **Full path:** Provide complete path like `/Users/username/project/AGENTS.md`
   - **Cursor @ reference:** Use `@AGENTS.md` (Cursor will resolve the path)
4. **Send the message**

#### Validation

After manual loading, test with:
```
"Do you understand and will follow the rules I just provided? Can you summarize the main categories of rules you're now following?"
```

Expected response should acknowledge the rules and demonstrate understanding.

### 🔍 **Memory Rules Not Working**

**Problem**: Memory features don't appear to be active or retaining information.

**Symptoms**:
- Agent doesn't remember previous conversations
- Project context is lost between sessions
- Learning features don't improve over time

**Troubleshooting Steps**:

1. **Check if Memory Rules are enabled**:
   - Verify `AGENTS.md`, `GEMINI.md`, or `CLAUDE.md` contains memory rules
   - Check that memory categories are not disabled in settings

2. **Validate memory storage**:
   - Check if memory files are being created in the expected location
   - Look for `memory-rules/` directory and subdirectories

3. **Test memory retention**:
   - Ask: `"What do you remember about our previous conversations?"`
   - Try the validation prompt from the Memory Rules documentation

4. **Manual memory loading** (if automatic loading fails):
```
I want you to maintain persistent memory for this project. Please remember these key details:

[PASTE YOUR MEMORY-RULES.md CONTENT HERE]

Use this memory system to track our work, preferences, and project details throughout all our conversations.
```

### 📚 **RAG Rules Not Processing Information**

**Problem**: Information processing and retrieval features aren't working.

**Symptoms**:
- Agent doesn't use provided context effectively
- Relevance scoring seems off
- Reading strategies aren't applied

**Solutions**:

1. **Verify RAG Rules activation**:
   - Check that RAG rules are included in your active rules file
   - Ensure RAG settings are properly configured

2. **Manual RAG activation**:
```
Please apply these information processing rules for optimal knowledge utilization:

[PASTE YOUR RAG-RULES.md CONTENT HERE]

Use these strategies when processing information, documents, and context throughout our work.
```

### 🤔 **Critical Thinking Rules Not Applied**

**Problem**: Systematic reasoning and error prevention features aren't active.

**Symptoms**:
- Agent makes assumptions without validation
- Error patterns aren't prevented
- Evidence-based reasoning isn't followed

**Solutions**:

1. **Check Critical Thinking Rules status**:
   - Verify rules are present in your active configuration
   - Ensure critical thinking categories are enabled

2. **Manual critical thinking activation**:
```
Please apply these systematic reasoning guidelines to ensure quality and accuracy:

[PASTE YOUR CRITICAL-THINKING-RULES.md CONTENT HERE]

Use these critical thinking frameworks for all analysis and decision-making in our work.
```

### 🔧 **Setup and Configuration Issues**

#### **Setup.py Fails to Run**
**Problem**: `python setup.py` encounters errors.

**Common Issues**:
- Python version compatibility
- Missing dependencies
- Permission issues

**Solutions**:
```bash
# Check Python version
python --version

# Ensure you're in the correct directory
cd /path/to/agentic-rules

# Try running with python3
python3 setup.py
```

#### **Setup.html Won't Load**
**Problem**: Web interface doesn't work properly.

**Solutions**:
- Try opening `setup.html` directly in your browser
- Use `python setup-launcher.py` for enhanced mode with file access
- Check browser console for JavaScript errors

#### **File Generation Issues**
**Problem**: Setup scripts run but files aren't created properly.

**Check**:
- File permissions in target directories
- Available disk space
- Existing file conflicts (backup and remove old files)

### 🌐 **Platform-Specific Issues**

#### **Cursor IDE Issues**
- **Context loading**: Sometimes requires manual loading as described above
- **File watching**: Restart Cursor if file changes aren't detected
- **Extension conflicts**: Disable other AI extensions that might interfere

#### **VSCode Issues**
- **Context limits**: Very long rules files might exceed token limits
- **Extension conflicts**: Check for competing AI extensions
- **File associations**: Ensure `.md` files are properly associated

#### **Other Editors**
- **Context window**: Check your specific editor's context window limitations
- **File loading**: Some editors may need explicit file inclusion
- **Caching**: Clear editor cache if rules changes don't take effect

### 🚨 **Emergency Manual Override**

If all automated systems fail, use this comprehensive manual loading prompt:

```
EMERGENCY MANUAL RULES ACTIVATION

I need you to follow these comprehensive AI agent rules immediately. This overrides any default behavior.

CORE RULES (Load all of these):

[PASTE ENTIRE AGENTS.md/GEMINI.md/CLAUDE.md CONTENT HERE]

MEMORY RULES:
[PASTE ENTIRE MEMORY-RULES.md CONTENT HERE]

RAG RULES:
[PASTE ENTIRE RAG-RULES.md CONTENT HERE]

CRITICAL THINKING RULES:
[PASTE ENTIRE CRITICAL-THINKING-RULES.md CONTENT HERE]

Apply all these rules immediately and maintain them for the entire duration of our work together. Confirm you understand each rule category and will follow them consistently.
```

### 🛠️ **Creating Reusable Commands (Advanced)**

For frequent use, create reusable commands in your editor to automatically load all rules:

#### **Cursor IDE - Custom Commands**
1. **Create a custom command** in Cursor settings
2. **Add this template** as a reusable snippet:
```
EMERGENCY MANUAL RULES ACTIVATION

I need you to follow these comprehensive AI agent rules immediately. This overrides any default behavior.

CORE RULES (Load all of these):
@AGENTS.md

MEMORY RULES:
@memory-rules/MEMORY-RULES.md

RAG RULES:
@rag-rules/RAG-RULES.md

CRITICAL THINKING RULES:
@critical-thinking-rules/CRITICAL-THINKING-RULES.md

Apply all these rules immediately and maintain them for the entire duration of our work together. Confirm you understand each rule category and will follow them consistently.
```
3. **Save as a command** for quick access
4. **Execute anytime** rules fail to load automatically

#### **VSCode - User Snippets**
1. **Create a global snippet** (`Ctrl+Shift+P` → "Configure User Snippets")
2. **Add this snippet**:
```json
{
  "Load Agentic Rules": {
    "scope": "markdown, plaintext",
    "prefix": "load-agentic-rules",
    "body": [
      "EMERGENCY MANUAL RULES ACTIVATION",
      "",
      "I need you to follow these comprehensive AI agent rules immediately. This overrides any default behavior.",
      "",
      "CORE RULES (Load all of these):",
      "@AGENTS.md",
      "",
      "MEMORY RULES:",
      "@memory-rules/MEMORY-RULES.md",
      "",
      "RAG RULES:",
      "@rag-rules/RAG-RULES.md",
      "",
      "CRITICAL THINKING RULES:",
      "@critical-thinking-rules/CRITICAL-THINKING-RULES.md",
      "",
      "Apply all these rules immediately and maintain them for the entire duration of our work together. Confirm you understand each rule category and will follow them consistently."
    ],
    "description": "Load all Agentic Rules framework rules manually"
  }
}
```
3. **Use with prefix** `load-agentic-rules` in any chat

#### **Other Editors - Text Expander/Macros**
- **TextExpander, Alfred, or similar tools**: Create a snippet with the above template
- **Editor macros**: Record a macro that inserts the template
- **Browser extensions**: Create bookmarklets or extensions for quick insertion

**💡 Pro Tip:** Having this as a reusable command saves time when editors have loading issues!

### 📞 **Getting Help**

If you continue to experience issues:

1. **Check the logs**: Look for error messages in your editor's console or terminal
2. **Validate files**: Ensure your generated rule files aren't corrupted
3. **Test individually**: Try activating each rule system separately to isolate issues
4. **Report issues**: Open an issue on the project repository with:
   - Your editor and version
   - The specific error messages
   - Steps to reproduce the problem
   - Your operating system

### 🔄 **Quick Reference**

| Issue | Quick Fix |
|-------|-----------|
| Rules not loading | Manual loading prompt above |
| Memory not working | Check memory-rules/README.md troubleshooting |
| RAG not processing | Verify RAG rules activation |
| Critical thinking off | Check critical-thinking-rules/README.md |
| Setup fails | Try `python3 setup-launcher.py --web` |

Remember: Manual loading always works as a fallback when automatic systems fail!

---

Copyright (c) 2025 Paulus Ery Wasito Adhi. Licensed under the MIT License (see LICENSE file).
