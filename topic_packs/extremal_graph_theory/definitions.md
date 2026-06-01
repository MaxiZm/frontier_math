# Definitions: Extremal Graph Theory

- **Extremal number** `ex(n, H)` — the maximum number of edges in a graph on `n`
  vertices that contains no subgraph isomorphic to `H`.
- **Turán graph** `T(n, r)` — the complete `r`-partite graph on `n` vertices with
  parts as equal as possible. It maximizes edges among `K_{r+1}`-free graphs.
- **Turán density** — the limit `lim_n ex(n,H) / C(n,2)`; equals `1 - 1/(χ(H)-1)`
  by Erdős–Stone–Simonovits, where `χ(H)` is the chromatic number.
- **Zarankiewicz number** `z(m,n; s,t)` — the maximum number of 1s in an `m × n`
  0/1 matrix with no all-1 `s × t` submatrix; equivalently the bipartite analog
  of `ex` for `K_{s,t}`-free bipartite graphs.
- **Girth** — the length of the shortest cycle; high girth = no short cycles.
- **Independence number** `α(G)` / **clique number** `ω(G)` — sizes of the
  largest independent set / clique.
- **Chromatic number** `χ(G)` — fewest colors for a proper vertex coloring.
- **Ramsey number** `R(s,t)` — least `n` such that every 2-coloring of `K_n`'s
  edges contains a red `K_s` or a blue `K_t`.
- **ε-regular pair** — a vertex pair `(A,B)` whose edge densities across all large
  subsets are within `ε` of the overall density (basis of the regularity lemma).
- **Incidence / norm graph** — algebraic graphs over `GF(q)` used to build dense
  `K_{s,t}`-free graphs meeting the Kővári–Sós–Turán bound.
