# Tool docs

This directory is the practical tool manual for Claude Code / LLM agents working in the math-discovery harness. It lists only local tools that are installed and smoke-tested in this environment. It does not replace official documentation; it records each tool's routing role, smoke tests, harness conventions, pitfalls, and final-answer compliance constraints.

Agent protocol:

1. Read `docs/02-tool-router.md` first.
2. Read the relevant tool card before using a tool.
3. Check availability before running a heavy tool.
4. Run the smallest smoke test before a larger experiment.
5. Save experiment code under the problem's `experiments/` directory.
6. Save outputs under `experiments/results/` when useful.
7. Record conclusions in `notes/attempt_log.md`.
8. Keep `final/proposed_solution.py` compliant with the problem's own compliance rules.

Tools not listed here are not considered available local tooling for this environment. Magma is proprietary/licensed, Glucose CLI is not installed, and live OEIS/paper-search MCP backends are not installed.

## Installed tool cards

- `sage.md` — SageMath for exact algebra, finite fields, number theory, lattices, polynomial rings, and combinatorial designs.
- `sympy.md` — SymPy for lightweight symbolic manipulation and expression testing.
- `mpmath.md` — mpmath for high-precision numerical exploration.
- `pari_gp.md` — PARI/GP for number theory and algebraic recognition.
- `gap.md` — GAP for finite groups, group actions, and symmetry.
- `z3.md` — Z3 for finite SMT constraint search.
- `sat_solvers.md` — installed SAT solvers: Kissat, CaDiCaL, MiniSat, and PySAT/Glucose3.
- `networkx.md` — NetworkX for graph prototypes and property checks.
- `nauty_traces.md` — nauty/Traces for graph isomorphism, canonical labeling, and enumeration.
- `lean_mathlib.md` — Lean/mathlib for theorem lookup and formal checking.
