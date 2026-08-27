# Team Tiers — Setup and Upgrade Manual

*Applies from Agentic Rules 1.7.0.* Design: [superpowers/specs/2026-08-27-team-tiers-privacy-gate-design.md](superpowers/specs/2026-08-27-team-tiers-privacy-gate-design.md).

Team tiers let one project share knowledge between members while each member's private
memory and knowledge graph stay on their own machine. Nothing changes until you set the new
options; a 1.6.0-style configuration keeps working as before.

| Tier | Markdown memory | Knowledge graph | Where |
|------|-----------------|-----------------|-------|
| private | `memory_path` | `kg_private_mcp_url` (a daemon on `127.0.0.1`) | your machine |
| team | `team_memory_path` (a clone of the team memory repo) | `kg_mcp_url` (shared daemon, per-member URL) | shared host + private git repo |

A **privacy gate** blocks private content from entering the team tier at three points: a
plugin hook, the team daemon, and the team repo's pre-commit / CI check. The plugin hook (L1)
is fast client-side feedback only, and bypassable by anyone with direct shell or git access to
their machine — the team KG daemon and the team repository's pre-commit/CI (L2/L3) are what
actually enforce the boundary when the client isn't this plugin.

---

## 1. Fresh setup (new member)

1. Install the plugin as usual (see [CLAUDE_CODE_PLUGIN.md](CLAUDE_CODE_PLUGIN.md)).
2. Run a **private KG daemon** on your machine, bound to loopback. Any server implementing the
   framework KG contract works; the reference image runs CPU-only and offline:
   ```bash
   docker run -d --name kg-private --restart unless-stopped --init \
     -p 127.0.0.1:8121:8121 -v ~/.claude/memory:/data \
     <kg-server-image> --transport streamable-http --host 0.0.0.0 --port 8121
   ```
   If you work only over SSH on a shared host, you may run this daemon there under your own
   login instead (own port, `chmod 700` on the data dir, a secret segment in the URL path).
   Understand the limit: with a shared root-level container daemon, other members of that
   host can technically read it — private by convention, not enforcement.
3. Clone the **team memory repo** your team gives you and enable its gate hook:
   ```bash
   git clone <team-memory-repo> ~/team-memory
   git -C ~/team-memory config core.hooksPath .githooks
   ```
4. Create your **private terms** file — your usernames, hostnames, family names, one per line —
   at `<memory_path>/private/gate-terms.txt`. It never leaves your machine; the gate uses it to
   flag your own identifiers before they reach the team tier.
5. Configure the plugin:
   ```bash
   claude plugin install agentic-rules@agentic-rules --config '{
     "memory_path": "<private store>",
     "team_memory_path": "<home>/team-memory",
     "kg_mcp_url": "http://<team-host>:<port>/u/<member>/mcp",
     "kg_private_mcp_url": "http://127.0.0.1:8121/mcp"
   }'
   ```
   `<member>` is your short id (`^[a-z0-9][a-z0-9._-]{0,31}$`). Allow the private daemon's
   tools in your settings: `mcp__plugin_agentic-rules_kg-private__kg_*`.

   This `--config` flow is the Claude Code plugin path. On the non-plugin setup path
   (`setup.py` / `setup.html`), there's no wizard prompt yet for the team memory root —
   set `storage.team_base_path` directly in `modules/memory-rules/settings.json` by hand.
6. Restart Claude Code fully, then run the checks in §5.

---

## 2. Upgrade an existing environment (from 1.6.0 or earlier)

Your current single daemon and single store keep working untouched if you stop after step 1.
Steps 2–5 add the team tier. **Copy before you split; split before you share any URL.**

1. **Upgrade the plugin** (`claude plugin update agentic-rules@agentic-rules`). Re-check
   `pluginConfigs` in your settings afterwards — a reinstall does not preserve them.
2. **Private daemon with your full graph.** Copy your existing `kg.db` next to a new loopback
   daemon (§1 step 2). You lose nothing: everything you had stays yours.
3. **Point the plugin** at it with `kg_private_mcp_url`. Leave `kg_mcp_url` as it is for now.
4. **Turn the shared daemon into a team daemon** — *only if you own it*; otherwise your team
   operator does this and hands you a per-member URL:
   - back up the database;
   - export team-eligible scopes into a **new** database through the gate scanner
     (`tools/privacy_gate.py`), read the report, exclude anything flagged;
   - mount the new database; archive the old one unmounted;
   - set `KG_TEAM_GATE=1`, `KG_TEAM_SCOPES=global,project:<id>`, `KG_OWNER_DEFAULT=<you>`,
     `KG_GATE_PATTERNS=<path to privacy-gate.json>`; restart.
5. **Team memory repo** — create it (private), seed `index.md` and `projects/<id>/`, vendor
   `tools/privacy_gate.py` + `settings/privacy-gate.json`. This framework does not ship a
   pre-commit hook or CI job itself — the team operator sets those up (see the
   claude-system-setup migration runbook) so `privacy_gate.py scan` runs on changed files at
   commit time and in CI. Clone the repo and set `team_memory_path`.
6. Run §5. Only then invite members.

Rollback: unset `team_memory_path` and `kg_private_mcp_url`, restore the backed-up database.
Private data was only ever copied.

---

## 3. Enable a project

1. Add the identity marker at the repo root and commit it (safe in public repos):
   ```json
   { "project_id": "<id>" }
   ```
   All clones — internal, public, forks — now agree on `projects/<id>/` and `project:<id>`.
2. Make sure `project:<id>` is in the team daemon's `KG_TEAM_SCOPES` and that
   `projects/<id>/` exists in the team memory repo.
3. Keep project-level Claude Code config in the project repo, split by layer:

   | Layer | Files | Git |
   |-------|-------|-----|
   | team | `.claude/CLAUDE.md`, `.claude/settings.json`, `.claude/{skills,commands,agents}/…` | tracked (exclude from public mirrors if the project has one) |
   | private | `.claude/settings.local.json`, `CLAUDE.local.md`, `.claude/{skills,commands,agents}/local-*` | gitignored |

   Machine paths (`additionalDirectories`, `Read(//home/...)`) belong in
   `settings.local.json`. The `local-` prefix keeps private skills from colliding with team ones.
   Suggested `.gitignore` lines:
   ```
   .claude/settings.local.json
   .claude/worktrees/
   .claude/**/local-*
   CLAUDE.local.md
   ```
4. Optional but recommended: run `tools/privacy_gate.py scan .claude` in the project's
   pre-commit so personal paths never enter team config.

---

## 4. Living with the gate

- **Default is private.** Nothing goes to the team tier unless the category is team-eligible
  (`technical`, `contextual`, `topic`, `git_history`, `knowledge_graph`), the content is about
  the project rather than you, and the scanner passes.
- **Never team**, no override: `behavioral`, `personal`, `credentials`, `sensitive`, `session`,
  `user_interaction`, `backup`.
- **Deny vs ask.** Definite matches (keys, tokens, private-key blocks, private IP ranges,
  home directories, mesh-VPN hostnames) are denied. Heuristic matches (emails, phone numbers,
  your private terms) ask you.
- **False positives** go in the team repo's allowlist (pattern id or literal), reviewed like any
  other change.
- The scanner never prints the matched secret — only the pattern id, file and line.

---

## 5. Verify

| # | Do | Expect |
|---|----|--------|
| 1 | `/mcp` | both `kg-dgx` and `kg-private` connected |
| 2 | `kg_context` in a project | results from both; team nodes carry `owner:` |
| 3 | `kg_add` to the team daemon with `AKIA…` and a home path in the content | denied by the hook; with the hook off, denied by the daemon |
| 4 | commit a team-repo file without `audience: team` | pre-commit fails |
| 5 | store a personal preference via memory rules | file under `memory_path`, not `team_memory_path` |
| 6 | end a session | backup manifest under `memory_path/projects/<id>/backup/…`; nothing under the team root |

---

## 6. Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| team writes all rejected | daemon started with the gate on but no pattern file | fail-closed by design — set `KG_GATE_PATTERNS` to a readable file and restart |
| a teammate sees your private nodes | you shared a URL to a daemon that still holds the mixed graph | §2 step 4 first; rotate the host database |
| hook never fires | neither `team_memory_path` nor `kg_private_mcp_url` set | the gate is inactive without a team tier |
| `kg-private` missing from `/mcp` | full restart needed after option change | quit and reopen the IDE/CLI |
| memory dir and KG scope disagree | no `.agentic-rules.json`, heuristic id differs per clone | §3 step 1, then merge the old `projects/<other>/` dir |
