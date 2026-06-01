# MCP Server: openalex_search

Open scholarly metadata search (OpenAlex): works, authors, venues, and concepts.
A broad, open alternative to the other search servers. Serves the retrieval
policy (`docs/04-retrieval-policy.md`).

> **Status: interface stub.** The contract below is defined; the live OpenAlex
> API binding is not wired up yet. Calls return a stub response.

## Tools

### `openalex_search`
- **input**:
  - `query` (string, required).
  - `filter` (object, optional) — e.g. `{ "concept": "graph theory",
    "from_year": 2015 }`.
  - `max_results` (int, optional, default 10).
- **output**: `{ "results": [ { "title", "authors": [string], "year",
  "venue", "concepts": [string], "openalex_id", "doi" } ] }`
  - `doi` / `openalex_id` are `"unknown"` when not confidently known.

### `openalex_get`
- **input**: `{ "openalex_id": string }`.
- **output**: a single work record, or an error if not found.

## Notes
JSON-only I/O. Log every consulted source in `retrieved_context.md`.
