# OEIS

## What it's for
The On-Line Encyclopedia of Integer Sequences: identify an integer (or rational)
sequence from its first terms, and retrieve formulas, references, generating
functions, and cross-links for it.

## When to use it
- After an experiment produces a sequence of counts/values: look it up to
  identify the pattern (ladder rung P6, "infer a reusable pattern").
- To find a closed form or recurrence and the literature behind a sequence.
- As a bridge to papers: an OEIS entry's references often trigger the retrieval
  policy (`docs/04-retrieval-policy.md`).

## How to call it
Via the `oeis_search` MCP server (`mcp_servers/oeis_search/`), or the public
OEIS API:

```
search terms: 1, 1, 2, 5, 14, 42        -> A000108 (Catalan numbers)
```

Provide enough terms (typically 6+) to disambiguate. Record the A-number and any
formula used in `retrieved_context.md`.

## Install
No local install needed for lookups beyond the MCP server / HTTP access. (For
fully offline use, a downloaded `stripped`/`names` OEIS dump can back the search
server.)
