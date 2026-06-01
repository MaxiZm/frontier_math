# Topic Packs

A **topic pack** is a per-area knowledge module the agent consults *before*
reading any paper. Packs are the first stop in the retrieval order
(`docs/04-retrieval-policy.md`): they hold the definitions, methods, attack
patterns, key references, and tool advice for a research area, so the agent can
orient and choose an approach without dumping a paper into context.

Each fully-populated pack lives in `topic_packs/<area>/` and contains **7 files**:

1. **topic_card.md** — one-screen orientation: scope of the area, the handful of
   key methods, and the typical tools to reach for.
2. **definitions.md** — the core objects and definitions, stated precisely.
3. **standard_methods.md** — the standard techniques/theorems of the area and
   when each applies.
4. **attack_patterns.md** — concrete "if the problem looks like X, try Y"
   playbook entries that map problem shapes to methods and tools.
5. **canonical_papers.yaml** — a small list of foundational references. Fields:
   `title`, `authors`, `year`, `venue`, `why_relevant`. Do **not** fabricate
   arXiv IDs or DOIs — omit identifiers you are unsure of, or mark them
   `unknown`.
6. **recent_papers.yaml** — a small list of more recent / advanced references,
   same fields and the same honesty rule.
7. **tool_recommendations.md** — which tools from the tool router
   (`docs/02-tool-router.md`) fit this area, and how to use them here.

## Populated vs. stub packs

- **Fully populated** (all 7 files): `combinatorics/`, `extremal_graph_theory/`.
- **Stub** (a short `topic_card.md` only): `coding_theory/`,
  `discrete_geometry/`, `number_theory/`, `lattice_models/`,
  `integrals_and_special_functions/`, `mathematical_constants/`,
  `continuum_physics/`, `algebra/`, `optimization_constants/`. Flesh these out
  per `docs/10-contribution-guide.md` as problems demand.
