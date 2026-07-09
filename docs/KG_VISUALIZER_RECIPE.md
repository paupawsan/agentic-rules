# Knowledge Visualizer — Build Recipe

Status: companion to [KG_VISUALIZER_SPEC.md](KG_VISUALIZER_SPEC.md). The spec
defines *what* a conforming visualizer must do; this recipe is the ordered
algorithm for *building* one. It is written contract-style so an AI agent can
execute it phase by phase, and in plain prose so a human can follow it too.

## How to use this recipe

- Execute the phases **in order**. Each phase ends with acceptance checks;
  do not start the next phase until the current checks pass.
- The recipe is **stack-agnostic**. No language, framework, or graph library
  is mandated; everything is expressed as interfaces, data shapes, and
  pseudocode. Where an example helps, it appears as a one-line "any X works"
  note, never a requirement.
- Normative rules (editing discipline, security, parser tolerance) live in
  the spec. This document references them; when in doubt, the spec wins.

## Framework tiers and verification status

The framework's default knowledge store is the **markdown memory store** —
every user has one, with no MCP server and no database. A **runtime knowledge
graph** (a service with its own database and retrieval pipeline) is an
optional tier some deployments add (see
[KG_IMPLEMENTATION_GUIDE.md](KG_IMPLEMENTATION_GUIDE.md)).

This recipe targets the markdown tier first, precisely because it is the tier
every user has — and the one with the least field testing. Be honest about
that in your implementation too: the acceptance checks in Phases 1 and 6 *are*
the test plan for the markdown-only pattern. Run the Phase 1 checks against a
real user store (read-only) before you ever enable editing.

This recipe was itself validated the same way it asks implementers to
validate their build: a clean-room implementer with no context beyond this
document and the spec built a real markdown-tier visualizer from it and
ran every checklist for real. That pass surfaced several gaps now folded
into the phases above (node-id uniqueness, overlay retraction semantics,
the derived-element layering note in Phase 6, and others) — this is not a
theoretical exercise; it produces a working system when followed.

## Phase 0 — Source contract

**Goal:** one small interface that every store adapter implements. This is
the load-bearing decision; every later phase builds against it.

```
interface Source:
  id: string                    # stable key, e.g. "markdown-main"
  kind: string                  # "markdown", "runtime-kg", ...
  capabilities():
      { editable: bool, temporal: bool, reports_stages: bool }
  graph(options): { nodes: [Node], edges: [Edge] }
  node(id): NodeDetail          # full content + metadata for one node
  query(text, options): { matches: [{ id, score }], stages: [StageInfo] }
  # only if capabilities().editable:
  preview_edit(op): { token, diff }
  apply_edit(token): result

Node: { id, title, type, scope, tags: [string], derived: bool, meta: {} }
Edge: { source, target, relation, derived: bool }
```

Notes:

- `derived: true` marks elements with no storage representation (hub nodes,
  grouping/tag edges). They are read-only by spec.
- `stages` is empty for sources that cannot report retrieval stages; the UI
  hides the stages panel in that case (Phase 5).
- Keep the interface this small. Resist adding methods a phase below does
  not need.

**Acceptance checks:**

- [ ] A stub source returning a fixed 3-node, 2-edge graph satisfies the
      interface.
- [ ] `graph()` is deterministic: two calls return identical data.
- [ ] A registry can hold several sources and address each by `id`.

## Phase 1 — Markdown store adapter (read-only)

**Goal:** parse a framework memory store into nodes and edges. Read-only —
editing is Phase 6.

The field mapping (filename stem → id, H1 → title, `## Metadata` → type,
top-level directory → scope, `## Tags` → tags, `[[wiki-links]]` and manifest
tables → edges) is defined in the spec's *Data sources* table. Do not
duplicate it here; implement it from there.

**Algorithm:**

```
scan(root):
  for each *.md file under root:
    skip the ENTIRE knowledge_graph/ subtree (not just files literally
      named "manifest") -- base manifest, branch overlays, and
      cross-branch files all describe structure, not knowledge, even
      though several of them have H1/Metadata/Tags sections that look
      like a renderable node
    node.id    = filename stem
    node.title = first "# " heading, else the stem
    node.type  = Metadata "Category" value, else parent directory name
    node.scope = top-level directory (common/, private/, projects/<id>/)
    node.tags  = parsed "## Tags" line "[a, b, c]", else []
    links      = [[stem]] occurrences in "## Related Memories" and
                 "## Cross-References" sections

  node.id is the filename stem ALONE (not the full path). Wiki-links
  resolve against this same bare stem, so ids must be unique across the
  *entire* store scanned by one source, not merely per directory. Warn
  and pick a stable tie-break (e.g. first scanned wins) on collision --
  do not crash, but do not silently merge two different memories either.

resolve_edges(nodes, links, manifests):
  for each link whose target stem exists   -> stored edge
  for each link whose target is missing    -> warn, skip (never crash)
  for each manifest edge row, applied in this order:
      1. base Edge Registry row, both endpoints exist -> stored edge
      2. overlay "Added Edges" row, both endpoints exist -> stored edge
      3. overlay "Removed Edges" row -> retract the matching edge from
         the accumulated set (base or an earlier-applied overlay)
      4. overlay "Modified Edges" row -> replace the matching edge's
         relation/metadata in place, keep the endpoints
      any row (of any kind) naming a missing endpoint, or a Removed/
      Modified row with no matching prior edge -> warn, skip
      whole-file overlay marked stale (e.g. a Status field saying so)
        -> skip the entire file, warn once
```

A manifest-driven source that only ever unions "Added Edges" and ignores
Removed/Modified rows will silently keep edges a later overlay retracted.
Implement all three row kinds, or state plainly which ones you left out.

**Tolerance rules** (normative, from the spec — implement all of them):
`- **Key**: value` bullets *and* loose `**Key**: value` lines inside
`## Metadata`; timestamped and contextual filenames; absent manifests
(wiki-links + directories must suffice); empty or placeholder sections.
When two files disagree about one overlay's status (e.g. a manifest file
and its timestamped companion), the more recently timestamped file wins.

**Runtime-KG variant:** for the optional tier, implement this same `Source`
interface over the service's own data layer — including its temporal
visibility rules (`as_of` reconstruction, expired/superseded filtering).
Never re-parse or re-implement what the service already exposes.

**Acceptance checks — the fixture store:** build a small fixture store
containing, at minimum, one file for each tolerance case:

1. full metadata, tags, and resolvable related links;
2. loose `**Key**: value` metadata lines;
3. no `## Metadata` section at all (type must fall back to directory);
4. a wiki-link to a file that does not exist;
5. an empty placeholder section;
6. a timestamped filename and a contextual filename;
7. one variant with a manifest, one without, one with a stale overlay row.

- [ ] Node count is exact; every id equals its filename stem.
- [ ] No index or manifest file appears as a node.
- [ ] Resolvable links become edges; the dangling link warns and is skipped.
- [ ] Absent manifest and stale overlay produce warnings, never crashes.
- [ ] **Real-store smoke (required):** run the adapter read-only against a
      real user store. Zero crashes; spot-check at least five nodes for
      correct title, type, scope, tags, and edges.

## Phase 2 — Unified graph model and derived elements

**Goal:** merge sources into one model and derive the grouping structure.

**Algorithm:**

```
build_model(sources):
  model = union of graph() from each source,
          node ids namespaced by source id
  for each *fine-grained physical directory*, scoped per source, with
      >= 2 member nodes:
      add hub node (derived=true) + one derived edge per member
      -- group by the actual parent directory a file lives in, not the
      -- coarse top-level scope (common/, private/, projects/<id>/).
      -- Two different sources' same-named subdirectory (e.g. two
      -- projects each with a sessions/ folder) must NOT merge into one
      -- hub -- keep the per-source namespacing from the union step.
  for each tag shared by >= 2 nodes:
      add tag hub node (derived=true) + one derived edge per member
```

**Acceptance checks:**

- [ ] Every derived element carries `derived: true`.
- [ ] Filtering out derived elements leaves exactly the stored data from
      Phase 1.
- [ ] Directories or tags with a single member produce no hub.

## Phase 3 — Serve (read-only API)

**Goal:** a minimal API the UI can talk to. Any HTTP server works.

Endpoints (names are suggestions; the shapes matter):

- list sources → `[{ id, kind, capabilities }]`
- graph → Phase 2's `build_model`. Distinguish two shapes explicitly,
  since "graph for one source" is otherwise ambiguous between them:
  a **single-source graph** (that one source's own data plus its own
  directory/tag hubs, nothing merged in) and the **full graph** (the
  union across every registered source, per Phase 2). Expose both, by
  whatever route naming you choose — e.g. a required `source` selector
  that switches between "just this one" and "everything."
- node detail → `NodeDetail`
- query → `{ matches, stages }`

Bind to loopback by default from day one — hardening is Phase 7, but the
default must never be `0.0.0.0`.

**Acceptance checks:**

- [ ] All endpoints respond correctly for the fixture store.
- [ ] Unknown source or node id returns a clean not-found, not a crash.
- [ ] A few hundred nodes serve in interactive time (aim well under a
      second).

## Phase 4 — Render

**Goal:** the interactive graph view. Any graph-rendering library works.

Requirements (from the spec's *UI expectations*):

- Multiple selectable layouts; at least one force-directed layout that keeps
  real spacing at hundreds of nodes; animated transitions; 3D optional.
- Neighborhood focus: pick a node, show only its N-hop neighborhood.

  ```
  focus(node, n): BFS n hops over visible edges; hide the rest;
                  show an exit control back to the full graph
  ```

- Hover previews for nodes; no blocking `prompt()`/`alert()` dialogs.
- A source switcher when several sources are registered; controls that only
  apply to one source kind (temporal filters, typed relations) hide for the
  others.

**Acceptance checks:**

- [ ] A ~300-node fixture renders without collapsing into an unreadable
      clump.
- [ ] Switching layouts preserves the current selection and runs animated.
- [ ] Focus mode enters and exits cleanly at N = 1 and N = 2.
- [ ] Inapplicable controls disappear when switching source kinds.

## Phase 5 — Live query overlay

**Goal:** the differentiator (spec, *Purpose*): show what the store's own
retrieval would recall — never a second, cleverer pipeline that diverges
from what the agent actually sees.

- Runtime-KG sources: call the service's retrieval pipeline and display the
  stages it reports.
- Markdown sources: the memory rules describe recall only loosely ("scan
  the index," "apply similarity algorithms to rank memories") without
  naming a concrete algorithm. Do not assume that vague description
  already pins down a specific procedure. Instead: **choose and document**
  a concrete signal set (e.g. id, filename, title, tag, and content
  matching, weighted) and treat that documented choice — not an
  unspecified "what the memory rules already do" — as the thing Phase 5's
  fidelity rule holds you to. The rule is: query what you documented,
  faithfully; do not silently layer on extra cleverness later.

**Algorithm:**

```
on query input (debounced ~300 ms):
  res = active_source.query(text)
  highlight nodes in res.matches (scale by score if provided)
  if res.stages non-empty: show which stages fired, else hide the panel
persist the query text (not the match list) in client state:
  on layout switch or reload, re-run the query against the live source
  and re-apply the highlight from the fresh result
  -- re-running beats caching the old matches: Phase 6 allows the
  -- underlying store to change at any time, so a cached match list can
  -- go stale the moment an edit lands.
```

**Acceptance checks:**

- [ ] One query fires per typing pause, not per keystroke.
- [ ] Matched nodes highlight; clearing the box clears the highlight.
- [ ] The highlight survives a layout switch and a page reload.
- [ ] The stages panel appears only for sources that report stages.

## Phase 6 — Editing (preview → apply)

**Goal:** guarded mutations for editable sources. The editing discipline is
normative in the spec; this is the algorithm that satisfies it.

Editable fields only — the tags line, related-memory links, or a
whole-content replace. This is not a general markdown editor.

**Layering note (architectural — get this wrong and the derived-element
rejection silently doesn't work):** "derived" is a Phase 2 concept — a
bare `Source` (Phase 0) only ever sees the ids it created itself and has
no idea a hub id even exists, let alone that it's derived. If you put the
derived-element check inside a `Source`'s own `preview_edit`, a request
naming a hub id never matches anything there and falls through to a
generic not-found error — not the friendly "this element is derived, it
has no storage representation" the spec requires. Do the derived/hub
check at the layer that holds the Phase 2 model (typically the API layer
of Phase 3), *before* the request ever reaches a `Source`. A `Source`
rejecting an id it doesn't recognize is fine as a second line of defense;
it must not be the only one.

**Algorithm:**

```
preview(op):
  current = read(op.path)
  new     = apply surgical line edit (tag line / link line / full replace)
  diff    = unified diff(current, new)
  token   = random one-time token
  pending[token] = { path: op.path, hash: sha256(current), new, expires }
  return { token, diff }

apply(token):
  entry = pending.pop(token)          # single use: absent -> reject
  if sha256(read(entry.path)) != entry.hash:
      reject "file changed since preview"
  write entry.new to temp file, then atomic rename over entry.path
```

Rejections that must be explicit and friendly:

- edits to `derived` elements ("this element is derived; it has no storage
  representation");
- in temporal stores, raw edits to retired/superseded records (they are the
  audit trail). A markdown-only source has no real bi-temporal mechanism
  to check this against — stand in with a plain metadata marker (e.g. a
  `Status: retired` field) so the rejection path is still exercised and
  the checklist below still means something; do not skip the check just
  because the tier lacks a "real" retirement concept, and do not present
  the marker as equivalent to actual temporal storage;
- bulk apply — apply is per item, always.

**Acceptance checks:**

- [ ] Apply without a prior preview is impossible; a token works only once.
- [ ] Editing the file externally between preview and apply causes a clean
      rejection.
- [ ] The diff shown equals the bytes written, exactly.
- [ ] Derived-element and retired-record edits are rejected with clear
      messages.
- [ ] All of the above run against **copies** of the fixture store; only
      after they pass, one real-store trial on a backed-up copy.

## Phase 7 — Hardening and final acceptance

**Goal:** make the spec's security section true. A visualizer usually ships
without authentication, so the network boundary and the filesystem boundary
are the whole defense.

- Bind to loopback or a trusted private overlay network only.
- Runtime source loading (pointing the visualizer at a new path while it
  runs) is an arbitrary-file-read primitive. Gate it exactly as the spec
  says: free paths only on loopback binds or behind explicit opt-in;
  otherwise a preconfigured allowlist of roots.
- Resolve symlinks on **both** sides before comparing:

  ```
  allowed(path, roots):
    real = realpath(path)
    return any( real is under realpath(root) for root in roots )
  ```

- Remember `private/` scope may hold credentials and personal data; never
  expose a store root wider than intended.

**Final end-to-end acceptance:**

- [ ] Fresh checkout → configure a store path → browse, query, focus, and
      one edit round-trip on the fixture store, following only this recipe.
- [ ] Real-store read-only smoke (Phase 1's last check) re-run on the
      finished build.
- [ ] Path-traversal and symlink escape attempts against the source-loading
      endpoint are rejected.
- [ ] The server is unreachable from another machine on a shared network
      with default settings.

## Non-goals

Unchanged from the spec: not a general markdown editor, not a replacement
for the retrieval pipeline or the memory rules, no multi-user editing.
