# Topic Card: Combinatorics

## Scope
Counting, existence, and structure of finite discrete objects: subsets,
sequences, set systems, partitions, permutations, and configurations. Includes
enumerative combinatorics (how many?), existence/extremal questions (does one
exist? how large/small can it be?), and the probabilistic and algebraic methods
used to settle them.

## Key methods
Pigeonhole principle; double counting; inclusion–exclusion; bijective proofs;
generating functions (ordinary and exponential); recurrences; the probabilistic
method (first/second moment, Lovász Local Lemma); additive combinatorics
(Cauchy–Davenport); extremal set theory (Sperner, Erdős–Ko–Rado).

## Typical tools
SymPy / generating-function manipulation and `mpmath` for quick counts; **OEIS**
to identify a counted sequence (`tools_docs/oeis.md`); **Sage** for exact
enumeration, combinatorial designs, and species; **Z3/SAT** for finite existence
searches; **GAP** when a group action governs the structure. See
`tool_recommendations.md`.
