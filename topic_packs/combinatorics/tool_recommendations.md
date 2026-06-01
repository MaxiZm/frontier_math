# Tool Recommendations: Combinatorics

Per the tool router (`docs/02-tool-router.md`):

- **OEIS** (`tools_docs/oeis.md`) — first stop after computing a sequence of
  counts. Identifies the sequence and surfaces formulas/recurrences/references.

- **Sage** (`tools_docs/sage.md`) — exact enumeration, combinatorial species,
  partitions, designs, and `guess`-style recurrence fitting. The workhorse for
  exact counting beyond small hand cases.

- **SymPy** (`tools_docs/sympy.md`) — generating-function algebra, coefficient
  extraction, binomial identities, quick symbolic checks.

- **Z3 / SAT** (`tools_docs/z3.md`, `tools_docs/sat_solvers.md`) — finite
  existence and constraint search: find a configuration (a model) or prove none
  exists (`UNSAT`). Encode set systems / colorings as constraints.

- **GAP** (`tools_docs/gap.md`) — when a group action governs the objects: orbit
  counting (Burnside/Pólya), automorphisms, symmetric designs.

- **mpmath** (`tools_docs/mpmath.md`) — high-precision evaluation when an
  asymptotic count or a probabilistic bound needs many digits.

## Workflow
1. Brute-force small cases (Sage / Python) → sequence.
2. Identify with OEIS; conjecture a formula/recurrence.
3. Prove via bijection / GF / induction (SymPy for the algebra).
4. For existence problems, push to Z3/SAT; for symmetry, to GAP.
5. Validate every candidate; convert solver outputs to explicit final candidates
   (`docs/07-final-answer-compliance.md`).
