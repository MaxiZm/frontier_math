# Paper Index

The harness's **local, curated knowledge base** of references and theorems. It is
the first stop in the retrieval order (`docs/04-retrieval-policy.md`): the agent
consults cards here before reaching out to live search. Served by the
`local_paper_index` MCP server (`mcp_servers/local_paper_index/`).

## Layout

- `cards/` — **paper cards**: one card per reference, summarizing the method /
  construction / bound it provides and why it matters. Organized by source:
  - `cards/arxiv/`
  - `cards/journals/`
  - `cards/books/`
  - `cards/surveys/`
- `theorem_cards/` — **theorem cards**: precise statements of named theorems
  (hypotheses + conclusion) used in proofs (`docs/05-proof-protocol.md`),
  organized by area:
  - `theorem_cards/combinatorics/`
  - `theorem_cards/geometry/`
  - `theorem_cards/number_theory/`
  - `theorem_cards/special_functions/`
- `citation_graph/` — the directed graph linking cards (cites / cited-by), used
  by `paper_index_citations` to traverse a result's lineage.
- `embeddings/` — vector embeddings of cards backing semantic search
  (`paper_index_search`, `top_k`).

## Schema

Card formats are defined in `paper_index/schema/`:

- `topic_card.schema.json` — topic-pack orientation cards.
- `paper_card.schema.json` — reference cards.
- `theorem_card.schema.json` — theorem cards.
- `problem.schema.json` — the problem-definition schema.

Conform new cards to these schemas. **Honesty rule:** do not fabricate arXiv IDs
or DOIs; mark unknown identifiers `unknown` (`docs/11-evaluation-integrity.md`).

## Relationship to topic packs
Topic packs (`topic_packs/`) are the human-readable, per-area entry point;
the paper index holds the machine-queryable cards those packs reference. The
literature scout (`agent_instructions/literature_scout.md`) keeps both current.
