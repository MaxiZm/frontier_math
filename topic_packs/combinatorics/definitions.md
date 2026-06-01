# Definitions: Combinatorics

- **Binomial coefficient** `C(n,k)` — number of `k`-subsets of an `n`-set;
  `C(n,k) = n! / (k!(n-k)!)`. Satisfies Pascal's rule
  `C(n,k) = C(n-1,k-1) + C(n-1,k)`.
- **Falling factorial** `(n)_k = n(n-1)...(n-k+1)` — number of `k`-permutations.
- **Set system / hypergraph** — a family `F` of subsets of a ground set `[n]`.
- **Antichain** — a family in which no set contains another (a Sperner family).
- **Intersecting family** — a family in which every two sets meet.
- **Generating function** — for a sequence `(a_n)`, the ordinary GF
  `A(x) = sum_n a_n x^n`; the exponential GF `sum_n a_n x^n / n!`. Combinatorial
  operations correspond to algebraic operations on GFs.
- **Catalan number** `C_n = C(2n,n)/(n+1)` — counts balanced parentheses,
  triangulations, Dyck paths, binary trees (OEIS A000108).
- **Partition of an integer** `n` — a multiset of positive integers summing to
  `n`; `p(n)` counts them.
- **Stirling numbers** — second kind `S(n,k)` = set partitions of `[n]` into `k`
  blocks; first kind = permutations of `[n]` with `k` cycles.
- **Permanent** of a 0/1 matrix — counts perfect matchings of the corresponding
  bipartite graph.
- **Sumset** `A + B = { a + b : a in A, b in B }` in an abelian group.
- **Probability space on objects** — a distribution over the finite objects,
  used to prove existence by showing a desired property holds with positive
  probability.
