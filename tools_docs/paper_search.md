# Paper Search

## What it's for
Finding the *method, construction, bound, or theorem* needed to make progress —
across arXiv, Semantic Scholar, OpenAlex, and the local paper index. Search for
methods, **not** for dumping context (`docs/02-tool-router.md`).

## When to use it
Only when the retrieval policy triggers (`docs/04-retrieval-policy.md`):
unfamiliar term, a pattern that smells like known literature, a needed external
theorem, three failed attempts, a clearly specialized area, or known
constructions/bounds required. Otherwise, do not read papers.

Search in policy order: **topic card → paper card → theorem card → relevant paper
section → full paper only if necessary.**

## How to call it
Via the search MCP servers (`mcp_servers/`):
- `arxiv_search` — preprints by query/author/category.
- `semantic_scholar_search` — citation-aware search and references.
- `openalex_search` — open scholarly metadata.
- `local_paper_index` — the curated `paper_index/` cards (check this first).
- `theorem_search` — named theorems (mathlib / formalized corpora).
- `oeis_search` — integer-sequence identification (`tools_docs/oeis.md`).

## Logging & honesty
- Log **every** source consulted in the problem's `retrieved_context.md`.
- Capture the usable method/theorem, not the whole paper.
- Do not fabricate arXiv IDs or DOIs; mark uncertain identifiers `unknown`
  (`docs/11-evaluation-integrity.md`).

## Install
The search MCP servers are interface stubs (`mcp_servers/README.md`); they need
their backing APIs / local index wired up before live search works.
