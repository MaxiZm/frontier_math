# Tool Plan

> Template. Decide up front which tools to route work to for this problem
> (`docs/02-tool-router.md`). Update as the approach evolves.

## Area & primary tools
Area: <topic-pack area>. Primary tools: <e.g. NetworkX for prototypes, nauty for
enumeration, Sage for the algebraic construction>.

## Routing by sub-task

| Sub-task / ladder rung | Tool | Why |
|------------------------|------|-----|
| Quick numeric exploration | mpmath | high precision |
| Symbolic checks / identities | SymPy | fast expression testing |
| Exact algebra / finite fields / lattices / designs | Sage | exact structures |
| Number-theory constants / algebraic recognition | PARI/GP | algdep/lindep, L-functions |
| Finite groups / symmetry | GAP | group actions, designs |
| Graph prototypes | NetworkX | quick invariants |
| Graph isomorphism / enumeration | nauty/Traces | canonical labeling, geng |
| Finite constraint / existence search | Z3 / SAT / ILP | model = construction, UNSAT = none |
| Theorem lookup / formal check | Lean/mathlib | precise statements |
| Sequence identification | OEIS | identify counts |
| Method retrieval | paper search | methods, not context dumps |

## Notes
- Research-time tools may be unrestricted; the **final** candidate must obey
  `compliance_rules.md` (`docs/07-final-answer-compliance.md`).
- Heavy tool runners (Sage, PARI, GAP, Z3, SAT, nauty, Lean) are **stubs** until
  installed (`tools_docs/`).
