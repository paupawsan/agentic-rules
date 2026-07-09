# Knowledge Visualizer — Generic Specification

Status: specification only. The framework does not ship a visualizer; this
documents the expected behavior for any implementation that wants to render
and edit Agentic Rules knowledge stores. It complements
[KG_IMPLEMENTATION_GUIDE.md](KG_IMPLEMENTATION_GUIDE.md) and the storage
format defined in [modules/memory-rules/MEMORY-RULES.md](../modules/memory-rules/MEMORY-RULES.md).

## Purpose

A graph view answers two questions the raw stores cannot answer at a glance:

1. **Topology** — what knowledge exists and how it links together.
2. **Retrieval behavior** — which nodes a query actually surfaces, live,
   through the store's own retrieval pipeline (not a reimplementation of it).

The second point is the differentiator over generic note-graph tools: the
visualizer must call the same retrieval code the agent uses, so what you see
highlighted is what the agent would recall.

## Data sources

An implementation should treat "where the knowledge lives" as a pluggable
source behind one small interface (`graph`, `node`, `query`, plus optional
edit previews/applies). Two source kinds matter for this framework:

### 1. Markdown memory store (the framework tier)

The canonical file format (MEMORY-RULES.md; no YAML frontmatter):

| Graph element | Derived from |
|---------------|--------------|
| Node id | filename stem (what `[[wiki-links]]` resolve against) |
| Node title | first `# H1` line |
| Node type | `## Metadata` → `**Category**` bullet, else parent directory name (open set) |
| Node scope | top-level directory (`common/`, `private/`, `projects/<id>/`) |
| Tags | `## Tags` section, single `[a, b, c]` line |
| Edges (stored) | `[[stem]]` wiki-links in `## Related Memories` / `## Cross-References` |
| Edges (stored) | `knowledge_graph/` manifest tables (base Edge Registry + overlay deltas) |
| Edges (derived) | directory grouping and shared tags (rendered as hub nodes) |

Parser requirements: tolerate `- **Key**: value` bullets inside `## Metadata`
*and* loose `**Key**: value` lines; both timestamped and contextual filenames;
absent manifests (wiki-links + directories must suffice); empty or
placeholder sections; stale overlays (skip, warn). Index files and manifest
files are structure, not nodes.

### 2. Runtime knowledge graph (optional tier)

If the deployment uses a runtime KG service (see KG_IMPLEMENTATION_GUIDE.md),
the visualizer should read it through that service's own data layer,
including its temporal-visibility rules (`as_of` reconstruction,
expired/superseded filtering) and its multi-stage retrieval pipeline for the
live query preview. Surface which stages fired for each query.

## Editing discipline (normative)

- **Never auto-apply.** Every mutation is two-step: a *preview* that computes
  and displays a diff without writing, then an explicit per-item *apply* that
  must echo the exact previewed diff (one-time token). No bulk apply.
- **Concurrency guard.** Apply must fail if the underlying data changed since
  preview (content hash for files, state re-check for databases).
- **Derived elements are read-only.** Hub nodes and grouping/tag edges have
  no storage representation; reject edits with a clear message.
- **History is immutable.** In temporal stores, retired/superseded records
  must not be raw-editable — that would corrupt the supersede audit trail.
- **Markdown writes are surgical.** Edit only the lines the diff shows
  (tag line, link line, or whole-content replace); write atomically
  (temp file + rename) to be safe on synced volumes.

## UI expectations

- Multiple selectable layouts (at least one force-directed layout with real
  spacing for hundreds of nodes); animated transitions; optional 3D view.
- Neighborhood focus (N-hop) to cut dense graphs down; hover previews;
  no blocking `prompt()`/`alert()` dialogs.
- Live query box (debounced) highlighting matched nodes and showing the
  retrieval stages that fired; the highlight must survive layout switches
  and reloads.
- A source switcher when several stores are configured; controls that only
  apply to one source kind (temporal filters, priorities, typed relations)
  hide for the others.

## Security (normative)

A visualizer typically ships without authentication. Therefore:

- Bind to loopback or a trusted private overlay network only — never
  `0.0.0.0` on a shared network.
- Runtime retargeting to arbitrary filesystem paths is an arbitrary-file-read
  primitive for anyone who can reach the port. Gate it: allow free paths only
  on loopback binds, or behind an explicit opt-in for trusted networks;
  otherwise restrict switching to a preconfigured allowlist.
- Remember the markdown store may contain a `private/` scope (credentials,
  personal data). Do not expose a store root wider than intended.

## Non-goals

- Not a general markdown editor — only the graph-relevant fields are editable.
- Not a replacement for the retrieval pipeline or the memory rules; it
  visualizes them.
- No collaborative/multi-user editing; the preview tokens assume one operator.
