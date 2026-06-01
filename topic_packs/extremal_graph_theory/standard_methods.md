# Standard Methods: Extremal Graph Theory

## Turán's theorem
The maximum number of edges in a `K_{r+1}`-free graph on `n` vertices is attained
**uniquely** by the Turán graph `T(n,r)`, giving roughly `(1 - 1/r) n^2 / 2`
edges. The prototypical extremal result; proofs by induction, weight-shifting, or
Zykov symmetrization.

## Kővári–Sós–Turán theorem
For the bipartite forbidden graph `K_{s,t}` (`s ≤ t`),
`ex(n, K_{s,t}) = O(n^{2 - 1/s})`. Proved by double counting `s`-stars (counting
copies of `K_{s,1}` and bounding shared neighborhoods). Resolves the order of the
**Zarankiewicz problem** for many `(s,t)`; matching constructions are known for
`K_{2,2}`, `K_{3,3}` via algebraic graphs.

## Erdős–Stone–Simonovits
For any fixed `H` with chromatic number `χ(H) = r+1 ≥ 3`,
`ex(n, H) = (1 - 1/r + o(1)) n^2 / 2`. The asymptotic extremal number depends only
on `χ(H)`. (Degenerate `o(n^2)` regime for bipartite `H` is the hard, open part.)

## Szemerédi regularity lemma + removal lemma
Every large graph's vertex set partitions into a bounded number of parts that are
pairwise ε-regular. Combined with a counting lemma, yields the **triangle removal
lemma** and many extremal/property-testing results. Powerful for dense graphs;
the bounds are tower-type.

## Probabilistic deletion (alteration) method
For lower bounds and existence (e.g. graphs of high girth and high chromatic
number): take a random graph `G(n,p)`, compute the expected number of short
cycles, **delete** one vertex/edge per short cycle, and bound what remains. Yields
existence of graphs avoiding many small substructures while staying dense.

## Algebraic / finite-field constructions
Build dense `H`-free graphs explicitly: incidence graphs of projective planes
(for `K_{2,2}`-free), norm graphs and projective norm graphs (for `K_{s,t}`-free),
and Cayley-graph constructions. Often meet the Kővári–Sós–Turán upper bound, so
they certify the true order of `ex`. Use Sage over `GF(q)`.

## Eigenvalue / spectral bounds
Use the adjacency or Laplacian spectrum (Hoffman bound, expander mixing lemma) to
bound independence numbers and edge distributions in regular graphs.
