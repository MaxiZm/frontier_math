# MCP Server: arxiv_search

Search arXiv preprints for methods, constructions, and bounds. Serves the
retrieval policy (`docs/04-retrieval-policy.md`) — for methods, not context dumps.

> **Status: interface stub.** The contract below is defined; the live arXiv API
> binding is not wired up yet. Calls return a stub response until implemented.

## Tools

### `arxiv_search`
- **input**:
  - `query` (string, required) — search terms.
  - `categories` (string[], optional) — e.g. `["math.CO", "math.NT"]`.
  - `max_results` (int, optional, default 10).
  - `sort` (string, optional) — `"relevance"` | `"recent"`.
- **output**: `{ "results": [ { "title", "authors": [string],
  "year", "abstract", "categories": [string], "arxiv_id" } ] }`
  - `arxiv_id` is `"unknown"` if not confidently known (no fabrication).

### `arxiv_get`
- **input**: `{ "arxiv_id": string }`.
- **output**: `{ "title", "authors", "year", "abstract", "arxiv_id" }` or an
  error if not found.

## Notes
JSON-only I/O. Every consulted result is logged to the problem's
`retrieved_context.md`.
