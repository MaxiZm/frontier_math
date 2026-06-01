# Paper Search

Status: documented interface; MCP search servers stubbed in this pass.

## Purpose

Paper search finds methods, constructions, bounds, or theorems across topic cards, paper cards, theorem cards, arXiv, Semantic Scholar, OpenAlex, and the local paper index.

## Use when

- The retrieval policy triggers: unfamiliar term, known-looking pattern, needed theorem, three failed attempts, specialized area, or required known bounds.
- You need a method or construction, not generic background.
- A topic card points to a paper or theorem card.
- OEIS or experiments suggest a named object.

## Do not use when

- The next step is a simple computation or validator run.
- You would dump context without a specific question.
- The source is private/hidden benchmark material.
- A topic pack already contains enough information for the current ladder level.

## Availability check

```bash
find mcp_servers -maxdepth 2 -name README.md -print
```

Expected successful output:

```txt
mcp_servers/.../README.md
```

## Installation notes

The MCP server directories define request/response contracts only. Live search requires future backend wiring and API configuration.

## Minimal smoke test

```python
from math_harness.retrieval.router import retrieval_order

print(retrieval_order())
```

Expected output follows: topic card -> paper card -> theorem card -> relevant paper section -> full paper if necessary.

## Common workflows

### Workflow 1: Policy-ordered retrieval

Goal: avoid context dumping while finding a method.

Steps: check topic pack, then paper card, then theorem card, then relevant section, then full paper only if required.

Code:

```txt
topic card -> paper card -> theorem card -> relevant paper section -> full paper only if necessary
```

Expected output: a small set of relevant facts logged in `retrieved_context.md`.

### Workflow 2: Save a paper card

Goal: preserve a source's actionable method and metadata.

Steps: record title/authors/source quality, capture only the theorem/method needed, and avoid fabricated IDs.

Code:

```yaml
title: unknown
authors: []
source_quality: preprint
usable_method: "TODO: summarize only after reading source"
identifiers:
  arxiv: unknown
```

Expected output: a paper card that is honest about uncertainty.

## Typical mathematical objects

Paper search is good for named constructions, known bounds, theorem statements, proof techniques, survey context, and references connecting computed patterns to literature.

## Agent protocol

When using paper search, the agent must:

1. State the retrieval trigger.
2. Search in policy order: topic card -> paper card -> theorem card -> relevant paper section -> full paper only if necessary.
3. Save source metadata in `retrieved_context.md` or a paper/theorem card.
4. Extract methods, bounds, and theorems rather than dumping context.
5. Label source quality.
6. Never fabricate arXiv IDs, DOIs, theorem names, or citations.

## Pitfalls

- Search results can be irrelevant despite matching keywords.
- Generated summaries may hallucinate identifiers or theorem statements.
- Reading full papers too early wastes context.
- Known bounds may use different normalization or parameters.

## Example integration with the harness

```python
from math_harness.retrieval.query_builder import build_query

query = build_query({"domain": "extremal graph theory", "object": "triangle-free graph"})
print(query)
```

## Final-answer compliance notes

Literature is research-time evidence. Final candidates must include explicit constructions, formulas, or proof dependencies and must not rely on vague paper references or unverified generated summaries.
