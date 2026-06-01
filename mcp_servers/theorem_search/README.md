# MCP Server: theorem_search

Search named and formalized theorems (mathlib / formalized corpora and the local
theorem cards) to find the precise statement of a result to cite or to check
formally. Serves the retrieval policy (`docs/04-retrieval-policy.md`) and the
proof protocol (`docs/05-proof-protocol.md`).

> **Status: interface stub.** The contract below is defined; the backing search
> (mathlib index / Loogle-style query + local theorem cards) is not wired up yet.
> Calls return a stub response.

## Tools

### `theorem_search`
- **input**:
  - `query` (string, required) — name, statement fragment, or type signature.
  - `source` (string, optional) — `"mathlib" | "local_cards" | "any"`.
  - `max_results` (int, optional, default 10).
- **output**: `{ "results": [ { "name", "statement", "source",
  "namespace_or_card_id", "url_or_path" } ] }`.

### `theorem_get`
- **input**: `{ "id": string }` — a mathlib name or local theorem-card id.
- **output**: `{ "name", "statement", "hypotheses", "source", "references" }`.

## Notes
JSON-only I/O. A consulted theorem should be recorded as a theorem card
(`paper_index/theorem_cards/`) and logged in `retrieved_context.md`.
