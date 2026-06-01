# Topic Card: Extremal Graph Theory

## Scope
How large or small a graph parameter can be subject to a structural constraint.
The central question (Turán-type): what is the maximum number of edges in an
`n`-vertex graph that contains no copy of a fixed forbidden subgraph `H`? Covers
the **extremal number** `ex(n, H)`, Turán/Zarankiewicz problems, Ramsey-type
existence, and the structure of near-extremal graphs.

## Key methods
Turán's theorem and the Turán graph; the Kővári–Sós–Turán bound for bipartite
forbidden graphs (Zarankiewicz problem); the Erdős–Stone–Simonovits theorem
(chromatic number determines the asymptotics); the Szemerédi regularity lemma
with the removal lemma; the probabilistic **deletion / alteration** method for
lower bounds.

## Typical tools
**NetworkX** for graph prototypes and invariants (`tools_docs/networkx.md`);
**nauty/Traces** for canonical isomorphism and exhaustive generation of small
extremal examples (`tools_docs/nauty_traces.md`); **Z3/SAT/ILP** for finite
existence searches and bounds (`tools_docs/z3.md`); **Sage** for algebraic
constructions over finite fields (e.g. norm/incidence graphs). See
`tool_recommendations.md`.
