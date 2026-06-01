# Attack Patterns: Extremal Graph Theory

A playbook mapping problem shapes to methods and tools. Use these at ladder rungs
P5–P10 (`docs/03-task-ladder-protocol.md`).

- **"Max edges with no `K_{r+1}`"** → **Turán's theorem**; the extremal graph is
  `T(n,r)`. Build it explicitly in NetworkX and validate the edge count.

- **"Max edges with no `K_{s,t}` (bipartite forbidden)"** → upper bound by
  **Kővári–Sós–Turán** (`O(n^{2-1/s})`); for a matching lower bound, try an
  **algebraic construction** (incidence graph of a projective plane for
  `K_{2,2}`, norm graphs for `K_{s,t}`) built over `GF(q)` in Sage.

- **"Asymptotic `ex(n,H)` for general `H`"** → compute `χ(H)` and apply
  **Erdős–Stone–Simonovits**: density is `1 - 1/(χ(H)-1)`. (If `H` bipartite, this
  only gives `o(n^2)` — switch to KST / construction techniques.)

- **"Graph with high girth AND high chromatic number (or no short cycles but
  dense)"** → **probabilistic deletion method**: random graph + delete a witness
  per short cycle.

- **"Does a graph with parameters (n, e, no H, …) exist?"** → finite search.
  Generate candidates with **nauty `geng`** under degree/girth filters
  (`tools_docs/nauty_traces.md`), or encode the constraints in **SAT/Z3**
  (`tools_docs/z3.md`); a model is the construction, `UNSAT` is a non-existence
  proof. Use **nauty** to dedup isomorphic candidates.

- **"Ramsey-type: force a monochromatic `K_s`"** → lower bounds via the
  probabilistic method (random coloring), upper bounds via the standard
  recursion; small exact values via SAT search (a hard, well-studied frontier).

- **"Bound an independence number in a regular graph"** → **spectral** methods:
  Hoffman bound from the least eigenvalue (NetworkX `adjacency_spectrum`).

When 3 attempts on a rung fail, relax one constraint (smaller `n`, weaker forbidden
subgraph, drop regularity) per the *k*−0.5 fallback, extract a lemma or
construction heuristic, and retry. Always convert a search-found graph into an
explicit deterministic final candidate (`docs/07-final-answer-compliance.md`).
