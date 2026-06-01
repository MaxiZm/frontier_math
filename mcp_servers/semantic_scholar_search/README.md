# MCP Server: semantic_scholar_search

Citation-aware scholarly search (Semantic Scholar): find papers and traverse
their references and citations. Serves the retrieval policy
(`docs/04-retrieval-policy.md`).

> **Status: interface stub.** The contract below is defined; the live Semantic
> Scholar API binding is not wired up yet. Calls return a stub response.

## Tools

### `semantic_scholar_search`
- **input**:
  - `query` (string, required).
  - `max_results` (int, optional, default 10).
  - `year_from` / `year_to` (int, optional).
- **output**: `{ "results": [ { "title", "authors": [string], "year",
  "venue", "abstract", "citation_count", "paper_id", "doi" } ] }`
  - `doi` / `paper_id` are `"unknown"` when not confidently known.

### `semantic_scholar_references`
- **input**: `{ "paper_id": string, "direction": "references" | "citations" }`.
- **output**: `{ "papers": [ { "title", "authors", "year", "paper_id" } ] }`.

## Notes
JSON-only I/O. Use to find the methodological lineage of a result; log every
consulted source in `retrieved_context.md`.
