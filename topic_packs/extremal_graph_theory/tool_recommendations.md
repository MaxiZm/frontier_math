# Tool Recommendations: Extremal Graph Theory

Per the tool router (`docs/02-tool-router.md`):

- **NetworkX** (`tools_docs/networkx.md`) — build candidate graphs and the Turán
  graph `T(n,r)`; compute edge counts, degrees, girth, cliques, and the
  adjacency/Laplacian spectrum for spectral bounds. The first prototype tool.

- **nauty / Traces** (`tools_docs/nauty_traces.md`) — exhaustively generate all
  non-isomorphic graphs on small `n` (`geng`, with `-d`/girth filters) for
  extremal searches, and canonically label to dedup candidates and test
  isomorphism.

- **Z3 / SAT / ILP** (`tools_docs/z3.md`, `tools_docs/sat_solvers.md`) — encode
  "does a graph with these parameters and no `H` exist?" as constraints. A model
  is the construction; `UNSAT` certifies non-existence (useful for small Ramsey /
  Zarankiewicz values).

- **Sage** (`tools_docs/sage.md`) — algebraic constructions over `GF(q)`:
  incidence graphs of projective planes (`K_{2,2}`-free), norm / projective norm
  graphs (`K_{s,t}`-free), Cayley graphs. These give tight lower bounds matching
  KST.

- **mpmath / SymPy** — evaluate and simplify the asymptotic edge-count
  expressions (`(1 - 1/r) n^2/2`, `O(n^{2-1/s})`) and check ratios numerically.

## Workflow
1. Prototype small extremal graphs in NetworkX; compute the parameter.
2. For exact small cases, enumerate with nauty or search with SAT/Z3.
3. For asymptotic constructions, build algebraic graphs in Sage and verify the
   forbidden subgraph is absent.
4. Pair every lower-bound construction with the matching upper-bound theorem
   (Turán / KST / Erdős–Stone) to certify optimality.
5. Validate candidates and convert searched graphs into explicit deterministic
   final candidates (`docs/07-final-answer-compliance.md`).
