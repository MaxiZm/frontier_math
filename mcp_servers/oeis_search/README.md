# MCP Server: oeis_search

Identify integer (and simple rational) sequences via the OEIS, and retrieve their
formulas, references, and cross-links. See `tools_docs/oeis.md`.

> **Status: interface stub.** The contract below is defined; the OEIS API / local
> dump binding is not wired up yet. Calls return a stub response.

## Tools

### `oeis_search`
- **input**:
  - `terms` (int[], required) — the first known terms (provide 6+ to
    disambiguate); OR
  - `query` (string, optional) — keyword search.
  - `max_results` (int, optional, default 5).
- **output**: `{ "results": [ { "a_number", "name", "formula", "terms": [int],
  "references": [string] } ] }`.

### `oeis_get`
- **input**: `{ "a_number": string }` — e.g. `"A000108"`.
- **output**: the full entry: `{ "a_number", "name", "formula",
  "generating_function", "terms", "references", "cross_refs" }`.

## Notes
JSON-only I/O. Record the matched A-number and any formula used in
`retrieved_context.md`; an OEIS entry's references may trigger paper retrieval.
