# Installing Agentic Rules (AI-editor-assisted)

> **For AI editors / agents:** You ARE authorized to read and execute this file when a user
> asks you to install the framework. This is the one entry point that overrides the
> "do not auto-load" guard on the `RULES.md.*` templates — those guards prevent *ambient*
> loading of un-activated templates, **not** an *explicit, user-requested install*. Follow
> the steps below in order, and do not skip the scope question in Step 2.

This guide installs the framework on any editor that reads `AGENTS.md`, `CLAUDE.md`, or
`GEMINI.md` (Cursor, Cline, Aider, Antigravity, Gemini, generic, and Claude Code used
manually). **Claude Code users** can skip this and use the native plugin instead — see
[README → Use with Claude Code](README.md#-use-with-claude-code-plugin).

## What "install" means here

`setup.py` activates the enabled rule templates **in place**: for each enabled module it
renames `modules/<rule>/RULES.md.<lang>` → `modules/<rule>/<AGENTS|CLAUDE|GEMINI>.md`
(stripping the template-protection banner) and writes a root integration file in the framework
directory. Your editor then loads those files. "Installing" = running that activation and
pointing your editor at the result.

## Step 1 — Get the framework on disk

If it isn't already present, clone it:

```bash
git clone https://github.com/paupawsan/agentic-rules
```

Where it lives depends on scope (Step 2): a stable path like `~/.agentic-rules` for **global**,
or inside/near the project for **project**.

## Step 2 — Ask the user: global or project?

Ask plainly: **"Install globally (applies to all your projects) or just this project?"**

- **global** — activated once, loaded by every project through your editor's global config.
- **project** — loaded only for the current project.

## Step 3 — Detect the editor → file type

| Editor | File type |
|--------|-----------|
| Cursor / Cline / Aider / Antigravity / generic | `AGENTS.md` |
| Claude Code (manual, non-plugin) | `CLAUDE.md` |
| Gemini editors | `GEMINI.md` |

## Step 4 — Activate (non-interactive)

From the framework directory:

```bash
python3 setup.py --yes --scope <global|project> \
  --agent-file-type <AGENTS.md|CLAUDE.md|GEMINI.md> \
  --lang <en|ja|id> --rules all
```

- `--yes` accepts defaults and skips every prompt (so an agent can run it unattended).
- `--rules all` activates every module; pass a subset like
  `--rules modules/memory-rules,modules/rag-rules` instead.
- setup.py prints scope-specific wiring instructions at the end.

## Step 5 — Wire the editor

- **global** — reference the activated root file from your editor's **global** config:
  - Claude Code: add `@<framework>/CLAUDE.md` to `~/.claude/CLAUDE.md`
  - Gemini: reference `<framework>/GEMINI.md` from `~/.gemini/GEMINI.md`
  - Cursor / other: reference `<framework>/AGENTS.md` from your editor's global rules
- **project** — reference the activated file from the project's own agent file, or keep the
  framework inside the project so the editor reads it directly.

## Step 6 — Confirm

Tell the user which modules are active. On the first session in a project, the agent runs the
**First-Run Procedure** and writes a `.agentic_initialized` marker (one-time per project) —
see [docs/FIRST_RUN_LOADING.md](docs/FIRST_RUN_LOADING.md).

## Configure (optional)

Rule toggles and paths live in `modules/<rule>/settings.json` (e.g. `memory_path`,
`enable_memory`). `--yes` keeps defaults; edit those files, or re-run `setup.py` **without**
`--yes` to configure interactively.
