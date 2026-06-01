# Standard Methods: Combinatorics

## Pigeonhole principle
If `n` items go into `m < n` boxes, some box has at least `ceil(n/m)` items.
Use for existence of a repeat/collision or a large monochromatic structure.

## Double counting
Count the same set of incidences two ways and equate. Proves identities and many
extremal bounds (e.g. counting edges by endpoints).

## Inclusion–exclusion
`|union A_i| = sum |A_i| - sum |A_i ∩ A_j| + ...`. Counts objects avoiding all of
a list of "bad" properties (derangements, surjections, sieve problems).

## Bijective proofs
Establish `|A| = |B|` by an explicit bijection. Strongest form of a counting
identity; often the cleanest route to a closed form.

## Generating functions
Encode `(a_n)` as a power series; translate recurrences and combinatorial
constructions (sum, product, sequence, set) into algebra. Extract coefficients,
asymptotics, and closed forms. SymPy and Sage handle the algebra.

## Recurrences
Set up a recurrence from the combinatorial structure, then solve (characteristic
equation, GF, or guess-and-verify via OEIS).

## Probabilistic method
Show a random object has the desired property with positive probability, so one
exists. Tools: **first moment** (expected count > 0), **second moment**
(concentration), **alteration/deletion** (build then fix), **Lovász Local
Lemma** (rare bad events with limited dependence).

## Extremal set theory
- **Sperner's theorem** — the largest antichain in `2^[n]` has size `C(n, ⌊n/2⌋)`.
- **Erdős–Ko–Rado** — for `n ≥ 2k`, the largest intersecting family of
  `k`-sets has size `C(n-1, k-1)`.

## Additive combinatorics
- **Cauchy–Davenport** — for `A, B ⊆ Z/p` (`p` prime),
  `|A + B| ≥ min(p, |A| + |B| - 1)`.
