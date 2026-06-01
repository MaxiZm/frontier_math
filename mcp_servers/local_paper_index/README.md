# MCP Server: local_paper_index

Query the curated local paper index (`paper_index/`): topic cards, paper cards,
theorem cards, the citation graph, and embeddings. This is the **first** stop in
the retrieval order (`docs/04-retrieval-policy.md`) — check here before any live
web search.

> **Status: interface stub.** The contract below is defined; the index backend
> (card store + embeddings + citation graph) is not wired up yet. Calls return a
> stub response.

## Tools

### `paper_index_search`
- **input**:
  - `query` (string, required).
  - `card_type` (string, optional) — `"topic" | "paper" | "theorem"`.
  - `top_k` (int, optional, default 5) — semantic search over embeddings.
- **output**: `{ "results": [ { "card_id", "card_type", "title", "summary",
  "path", "score" } ] }`.

### `paper_index_get`
- **input**: `{ "card_id": string }`.
- **output**: the full card contents (per `paper_index/schema/`).

### `paper_index_citations`
- **input**: `{ "card_id": string, "direction": "cited_by" | "cites" }`.
- **output**: `{ "neighbors": [ { "card_id", "title" } ] }`.

## Notes
JSON-only I/O. Card schemas live under `paper_index/schema/`. Log consulted cards
in `retrieved_context.md`.
