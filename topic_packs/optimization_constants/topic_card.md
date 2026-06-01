# Topic Card: Optimization Constants

## Scope
Best-possible constants in optimization and extremal problems: optimal packing /
covering densities, best constants in functional inequalities, extremal
configurations, and the value of combinatorial or geometric optimization problems
at the limit.

## Key methods & tools
Linear- and semidefinite-programming relaxations and their dual certificates
(LP/SDP duality proves a bound is tight); convexity and symmetry reductions;
high-precision evaluation of conjectured optimal values then exact recognition.
Typical tools: **Z3/SAT/ILP** (finite optimization and feasibility), **Sage** (LP,
exact linear algebra, SDP interfaces), **mpmath/PARI** (precise constants and
recognition). A final answer must return the explicit optimal object or value,
not run the optimizer at scoring time (`docs/07-final-answer-compliance.md`).
