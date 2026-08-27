# Team-shared vs member-private memory and KG, with a privacy gate — design

**Status:** draft for review · **Date:** 2026-08-27 · **Target release:** 1.7.0
**Scope:** framework contract (modules, settings, Claude Code plugin, KG server contract).
Operator procedures (migrating an existing project, standing up hosts, onboarding a member)
live in the operator's own setup repository, not here.

---

## 1. Problem

Today the framework has exactly one memory root (`memory_path`) and one KG endpoint
(`kg_mcp_url`), and no notion of *who* owns a piece of knowledge. That is fine for one
person. It breaks the moment a project has two or more members who want to:

1. **share** project knowledge (decisions, gotchas, procedures, project rules), and
2. keep **member-private** knowledge (preferences, credentials, personal infra, half-formed
   notes) on their own machine — not merely hidden by a filter on a shared host.

Concrete failures observed on a real project with a private internal repo and a public mirror:

| # | Failure | Cause |
|---|---------|-------|
| F1 | The two clones of one project get two different project ids (`<name>-internal` vs `<name>`), so memory and KG scope drift apart. | Project id is derived from the git remote name or directory name; nothing in the repo declares it. |
| F2 | One shared KG host holds personal and project knowledge in the same graph. Handing the URL to a teammate hands them everything, read and write. | KG has `scope` (`global` / `project:<id>`) but no owner or audience. |
| F3 | There is no place a teammate can write shared markdown memory. | Single `memory_path`, per person. |
| F4 | Nothing stops private content (secrets, home paths, private IPs, personal notes) from being copied into a shared space. Rules text is advice, not enforcement. | No gate at the private→team boundary. |
| F5 | Project-level Claude Code config (`.claude/`) is a git worktree of one member's *personal* config repo and is git-ignored by the project. Teammates cannot share it, and personal absolute paths leak into what should be team settings. | Config channel owned by one person instead of the project repo. |

## 2. Goals and non-goals

**Goals**

- G1 Two physically separate tiers: **private** (member's machine only) and **team** (shared host / shared repo). Private data never reaches the team tier.
- G2 A **gate** in code — fail-closed — at the private→team boundary, enforced on the destination, not only on the client.
- G3 One **project identity** for all clones of a project.
- G4 **Backward compatibility**: an install that sets none of the new options behaves exactly as 1.6.0.
- G5 A **generic migration** any project can run (procedure lives in the operator repo; the framework supplies the pieces it needs).

**Non-goals**

- Per-user authentication on the team KG (identity is self-declared; network-level trust is assumed). Can be added later without changing the data model.
- Federated retrieval (private daemon querying the team daemon and returning one list). Deferred; see §5.5.
- Multi-tenant KG (many teams on one server). One team per team server.

## 3. Concepts

### 3.1 Three rings, two gates

```
member-private ──gate A──▶ team-shared ──gate B──▶ public
(own machine)              (shared host,          (OSS repo,
                            team repo)             announcements)
```

Gate B (team→public) is the existing internal-first publishing discipline. This design adds
**gate A** (private→team). Same shape, same kind of tooling, different pattern set.

### 3.2 Two tiers

| Tier | Lives on | Memory (markdown) | KG | What goes there |
|------|----------|-------------------|----|-----------------|
| **Private** | the member's machine (or a store only they control) | `memory_path` | a KG daemon bound to loopback (same image, CPU-only, works offline) | everything by default |
| **Team** | a shared host + a shared git repo | `team_memory_path` (a clone of the team memory repo) | a KG daemon on a private network, reachable by members | project knowledge that helps a teammate, after passing gate A |

The default audience of every write is **private**. Team is opt-in per item.

### 3.3 Scope × audience

Two orthogonal axes:

- **scope** — what the knowledge is about: `global` or `project:<id>` (exists today).
- **audience** — who may see it: `private` or `team` (new).

In the KG, audience is not a column: it is *which daemon you wrote to*. The team daemon holds
only team-audience nodes by construction. In the markdown store, audience is which root the
file lives under, mirrored in frontmatter so a misplaced file is detectable.

### 3.4 Project identity marker

A repo-root file, tracked, harmless in public:

```json
// .agentic-rules.json
{ "project_id": "myproject" }
```

The Project Identification Algorithm consults it **first**, then falls back to the current
`git_remote_or_directory_name` heuristic. KG scope for a project is always
`project:<project_id>`. The native-memory backup hook uses the same resolver.

## 4. Memory store (markdown)

### 4.1 Roots

| Option | Tier | Default | Notes |
|--------|------|---------|-------|
| `memory_path` (existing) | private | unset → skill asks | unchanged |
| `team_memory_path` (new) | team | unset → no team tier | must not be inside `memory_path`, and vice versa |

`settings.json`: `memory_rules.storage.team_base_path` (mirror of the plugin option, for
non-plugin platforms).

### 4.2 Team root layout

Same schema as today's store, minus `private/`:

```
<team_memory_path>/
├── index.md
├── common/                # team-wide technical knowledge
│   └── technical/
└── projects/<project_id>/
    ├── contextual/
    ├── technical/
    ├── topic/
    ├── git_history/
    ├── knowledge_graph/
    └── rules/             # team rules (prose); the KG holds their structured form
```

The team root is a git repository. Commits give attribution and history; a pull request gives
review when wanted. The framework does not require a particular hosting service.

### 4.3 Metadata

Every memory file gains one frontmatter key:

```yaml
audience: private | team     # default: private
```

Files written under `memory_path` get `private`; files under `team_memory_path` **must** carry
`team`. A team-root file without `audience: team` is a gate failure (§6).

`settings.json` gains a per-category flag `team_eligible` (default `false`):

| Category | `team_eligible` | Why |
|----------|-----------------|-----|
| technical, contextual, topic, git_history, knowledge_graph | `true` | project knowledge |
| behavioral, personal, credentials, sensitive, session, user_interaction, backup, knowledge_graph_overlay | `false` | about the person or the machine — never team, no override |

### 4.4 Routing

- **Write:** route to `memory_path` unless all of: the category is `team_eligible`; the content
  is about the shared project, not the member; the member asked for it to be shared or the
  rules' audience test says so; gate A passes. Then write under `team_memory_path` with
  `audience: team`.
- **Recall:** read both roots. Order stays as today (loaded index → KG → memory store → broad
  search), with "KG" meaning *both* daemons and "memory store" meaning *both* roots.
- The always-on injected preamble names both roots when both are set.

### 4.5 Backup hook invariant

`memory-backup.py` mirrors native memory into `memory_path` only. The team root is never a
destination — enforced by its existing `_within(projects_root)` check; `team_memory_path`
is simply never read by this hook.

## 5. Knowledge graph

### 5.1 Endpoints and plugin options

| Option | Server name | Tier | Default |
|--------|-------------|------|---------|
| `kg_mcp_url` (existing) | `kg-dgx` (unchanged, so existing permission allowlists keep working) | team — or "the only KG" when no private URL is set | blank → no KG |
| `kg_private_mcp_url` (new) | `kg-private` | private | blank → no private daemon |

Plugin `.mcp.json` registers both servers; a blank URL makes that server unreachable and the
skills degrade as they do today.

Compatibility: a 1.6.0 install has only `kg_mcp_url`; with 1.7.0 nothing changes for it.

Per-member identity on the team daemon rides in the **URL path**, because the plugin can
substitute options into a URL but header substitution is not guaranteed:

```
http://<team-host>:<port>/u/<member>/mcp
```

Each member sets their own `kg_mcp_url`. A URL without `/u/<member>/` is treated as the
daemon's configured default owner (legacy clients).

### 5.2 Team daemon contract

Any server implementing the framework's KG tool contract can be run in team mode. Required
behavior when `KG_TEAM_GATE=1`:

| Item | Contract |
|------|----------|
| owner | `owner` column on nodes (`TEXT DEFAULT ''`; added in place, never by table rebuild). Set from the URL path on every write; reported in results. Existing rows keep `''`, read as `KG_OWNER_DEFAULT`. |
| scope allowlist | `KG_TEAM_SCOPES` — comma list, e.g. `global,project:myproject`. Writes with any other scope are rejected. |
| content gate | every `kg_add` / `kg_link` runs the §6 scanner over id, title, content, tags, source. Deny → reject with the redacted reason. |
| fail-closed | gate enabled but pattern file missing/unreadable → every write rejected. |
| identity | `/u/<member>/mcp` path routing; `<member>` must match `^[a-z0-9][a-z0-9._-]{0,31}$`. |

A private daemon runs with the gate **off** and no owner routing (single user). It may set
`KG_PATH_PREFIX=/t/<secret>` so its MCP endpoint is `…/t/<secret>/mcp` — the only
access control available to a loopback daemon on a shared host (§11).

### 5.3 Tool surface

No signature changes. Choosing the team daemon *is* the audience decision. `kg_query` /
`kg_context` / `kg_list` output gains `owner:<member>` in the compact node line when owner is
non-empty.

### 5.4 Rules text

`RULES.md.{en,ja,id}` for memory-rules and rag-rules, plus the injected preamble:

- recall: query both daemons when both are configured; merge, prefer team for project scope on
  ties.
- write: private daemon by default; team daemon only for `team_eligible` project knowledge
  that passes the audience test; never write personal preferences, credentials, machine paths,
  hostnames, or private addresses to the team daemon.
- `kg_retire` / `supersedes` only within one daemon (no cross-daemon edges).

### 5.5 Deferred: federation

The private daemon could take a team URL, query it itself, and return one ranked list. That
would move the team URL from the plugin into the daemon's config. Not built until the
two-call cost is shown to matter.

## 6. Privacy gate (gate A)

### 6.1 Layers

| Layer | Where | What it checks | On failure |
|-------|-------|----------------|------------|
| **L0 tagging** | file frontmatter / destination daemon | `audience: team` present; category `team_eligible`; KG scope in allowlist | reject |
| **L1 client hook** | plugin `PreToolUse` | team-bound writes only: `kg_add`/`kg_link` on `kg-dgx` when a private daemon is also configured; `Write`/`Edit` under `team_memory_path`; `Bash` copying from `memory_path`, the user config dir, or any `private/` path into `team_memory_path` | `deny` (definite) / `ask` (heuristic) with a redacted reason |
| **L2 team daemon** | server, `KG_TEAM_GATE=1` | §5.2 | reject |
| **L3 team repo** | `pre-commit` + CI on push/PR | L0 + scanner over changed files | commit/CI fails |
| **L4 audit** | `memory_path/private/gate-log/` | every block and override, with pattern id and destination — never the matched text | — |

L1 is convenience (fast feedback). L2 and L3 are the enforcement: they hold even when the
client is not this plugin.

### 6.2 Scanner

One stdlib-only script shipped by the framework (`tools/privacy_gate.py`), vendored by the KG
server and the team repo at a pinned version.

```
privacy_gate.py scan  [--patterns FILE] [--allowlist FILE] [--private-terms FILE] \
                      (--text - | PATH...)          # exit 0 pass · 2 deny · 3 ask
privacy_gate.py staged [same flags]                  # git pre-commit mode
privacy_gate.py check-frontmatter PATH...            # L0 for markdown
```

Pattern file (`settings/privacy-gate.json`, JSON):

```json
{ "version": 1,
  "deny": [ {"id": "secret-generic", "regex": "..."} ],
  "ask":  [ {"id": "email", "regex": "..."} ] }
```

Default classes — **deny**: API-key and token shapes, bearer tokens, private-key blocks;
private IPv4 ranges (10/8, 172.16/12, 192.168/16, 100.64/10) and link-local; mesh-VPN
hostnames; home directories (`/Users/<x>/`, `/home/<x>/`, `C:\Users\<x>\`). **ask**: emails,
phone numbers, terms from the member's private-terms file.

Extension files:

- **team allowlist** (in the team repo): pattern ids or literal strings that are false positives
  for this team (e.g. a public hostname).
- **member private terms** (`memory_path/private/gate-terms.txt`): the member's own
  usernames, hostnames, family names. Local only, by definition.

No override mechanism: a deny/ask decision cannot be bypassed short of fixing the
underlying command or content.

### 6.3 Wiring

- Plugin: `hooks/privacy-gate-hook.py` (PreToolUse; matcher on the tool names above), active
  only when `team_memory_path` or `kg_private_mcp_url` is set.
- Team repo: `.githooks/pre-commit` + a CI workflow calling `privacy_gate.py staged` /
  `scan`. Both installed by the operator migration (§10).
- Project repo (optional but recommended): the same pre-commit over `.claude/` so personal
  paths cannot enter team config (§7).

### 6.4 Invariants (code, not prose)

1. Backup hook never writes outside `memory_path`.
2. Team daemon with gate configured but pattern file unavailable rejects all writes.
3. The scanner never prints matched secret text — only pattern id, file, line.
4. `team_memory_path` and `memory_path` must not nest; the plugin refuses to activate the
   team tier if they do.

## 7. Claude Code project config layering

Use Claude Code's native layers; stop making the project's `.claude/` a worktree of a
personal repo.

| Layer | Files | Owner | Git |
|-------|-------|-------|-----|
| team | `.claude/CLAUDE.md`, `.claude/settings.json`, `.claude/{skills,commands,agents}/…` | the project repo | tracked; excluded from any public mirror by the project's existing publish rules |
| private | `.claude/settings.local.json`, root `CLAUDE.local.md`, `.claude/{skills,commands,agents}/local-*` | each member | ignored by the project (`.gitignore`) |
| global personal | `~/.claude/…` | each member | their own personal config repo |

Native merge rules do the rest: `settings.local.json` > `settings.json` > user settings
(allow lists union, deny wins); `CLAUDE.md` and `CLAUDE.local.md` both load; the `local-`
prefix makes name collisions impossible. Machine paths (`additionalDirectories`,
`Read(//Users/...)`) belong in `settings.local.json`.

The framework's Claude Code docs recommend this layout; the operator's `/settings-init`-style
tooling scaffolds the private files and gitignore lines instead of a worktree.

## 8. Framework changes (file level)

| Area | Change |
|------|--------|
| `modules/memory-rules/settings.json` | `storage.team_base_path`; `categories.*.team_eligible`; `project_identification_method: "marker_then_git_remote_or_directory_name"` |
| `modules/memory-rules/MEMORY-RULES.md` | project marker in the identification algorithm; team root layout; `audience` frontmatter; routing algorithm; gate reference |
| `modules/memory-rules/RULES.md.{en,ja,id}` | tiered recall over both roots/daemons; write routing; never-team list |
| `modules/rag-rules/RULES.md.{en,ja,id}` + `RAG-RULES.md` | two-daemon recall; team daemon contract pointer |
| `settings/privacy-gate.json`, `tools/privacy_gate.py`, `tools/tests/` | scanner + fixtures |
| `claude-code/.claude-plugin/plugin.json` | `team_memory_path`, `kg_private_mcp_url` |
| `claude-code/.mcp.json` | second server `kg-private` |
| `claude-code/hooks/hooks.json`, `privacy-gate-hook.py`, `hook_common.py` | PreToolUse gate; shared option reader |
| `claude-code/hooks/session-start.py` | preamble names both roots/daemons when set |
| `claude-code/hooks/memory-backup.py` | marker-aware `project_id_for()` |
| `claude-code/tests/test_plugin.py` | hook wiring, gate deny/ask/pass fixtures, legacy-config parity |
| `docs/CLAUDE_CODE_PLUGIN.md`, `docs/KG_IMPLEMENTATION_GUIDE.md`, `docs/USER-GUIDE.md`, `docs/CHANGELOG.md`, localized README/docs | document tiers, gate, layering, team daemon contract |
| `bootstrap.json`, `VERSION` strings, `web-config.json`/`setup.html` regen, `validate.py` | 1.7.0; regen check must pass |

## 9. Backward-compatibility matrix

| Install | 1.6.0 behavior | 1.7.0 behavior |
|---------|----------------|----------------|
| no options set | native memory dir is the store; no KG | identical |
| `memory_path` only | private store | identical (`audience: private` added to new files only) |
| `memory_path` + `kg_mcp_url` | one store, one KG | identical; hook inactive; `kg-dgx` name unchanged |
| + `team_memory_path` | — | team root active; gate L1/L3 on |
| + `kg_private_mcp_url` | — | two daemons; `kg_mcp_url` becomes the team one; gate L1 on for it |
| repo without `.agentic-rules.json` | heuristic id | identical |

Legacy KG daemon (no `owner` column, no gate) keeps working as a single-user daemon.

## 10. Generic migration (framework view)

The detailed operator runbook — with hosts, commands, and member onboarding — lives in the
operator's setup repository. The framework-level sequence any project follows:

1. **Identity** — add `.agentic-rules.json`; confirm memory dir and KG scope now agree.
2. **Config layering** — move team config into the project repo; private overlays to
   `local-*` / `settings.local.json`; personal paths out of `settings.json`.
3. **Team memory repo** — create, seed `index.md` + `projects/<id>/`, install pre-commit + CI
   gate, each member clones and sets `team_memory_path`.
4. **KG split** — each member runs a private daemon (loopback) holding their existing graph;
   the team daemon starts from a *scanned, reviewed* export of team-eligible scopes (or empty);
   members set per-member team URLs. The reference server ships an export tool that copies
   selected scopes into a new database, runs the §6.2 scanner on every node, and writes a
   report (`exported` / `denied` / `ask`) for the operator to review before the swap.
5. **Gate on** — plugin options set → L1 active; team daemon `KG_TEAM_GATE=1`; verify a
   planted secret, a home path, and a private IP are all rejected at L1, L2 and L3.
6. **Verify** — recall from both tiers works; a private-only fact never appears in team
   results; backup hook still writes only under `memory_path`.

Rollback at any step: unset the new options → 1.6.0 behavior; team repo and team daemon can be
deleted without touching private data.

## 11. Security and limitations

- Identity on the team daemon is self-declared in the URL. Acceptable for a small trusted
  circle on a private network; tokens can be layered on later.
- Query text sent to the team daemon leaves the member's machine. Recall queries should not
  contain private terms; the rules say so, the gate does not check queries.
- The scanner is pattern-based. It catches shapes (keys, addresses, paths), not meaning. The
  `team_eligible` category wall and the `audience` tag are the deterministic half; the scanner
  is the safety net.
- The team memory repo is only as private as its hosting and membership.
- **Shared multi-login hosts.** A member may run their private daemon on a shared host under
  their own login (own container, own loopback port, `700` data dir, secret URL path). That is
  privacy *by convention*: on a host where members share a root-level container daemon, any of
  them can read the others' container data, and loopback ports are reachable by every local
  user. Enforced privacy on such a host needs rootless containers per user. The default —
  private daemon on the member's own workstation — avoids the question entirely.

## 12. Testing

- `python3 claude-code/tests/test_plugin.py` — hook wiring; gate fixtures (deny, ask, pass;
  allowlist; private terms; fail-closed on missing pattern file); legacy config produces
  byte-identical preamble.
- `tools/tests/test_privacy_gate.py` — pattern classes, frontmatter check, staged mode.
- `python3 validate.py` — version strings, localization parity, regen freshness.
- `bash test/dogfood.sh` — clean-room install with and without team options.
- `plugin-tester` agent — end-to-end across en/ja/id, including a two-daemon sandbox and a
  team root with the pre-commit gate.
- Team daemon contract: reference server tests for owner routing, scope allowlist, gate reject,
  fail-closed.

## 13. Assumptions taken (confirm or change)

1. Definite patterns → hard deny; heuristic patterns → ask.
2. Team repo: pre-commit + CI check; direct push allowed (PRs optional).
3. Members maintain their own private-terms file under `memory_path/private/`.
4. Team KG seeded from a scanned and reviewed export of the project scope, not empty.
5. Member private KG runs on the member's own workstation (loopback) by default. A per-login
   daemon on a shared host is a documented option (member's choice) with the §11 caveat.
6. Team markdown memory is a dedicated private repository, not a directory inside the code repo.
7. First project migrated is the one that surfaced the problem; others follow on demand with
   the same runbook.
