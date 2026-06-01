# Tool docs

This directory is the practical tool manual for Claude Code / LLM agents working in the math-discovery harness. It does not replace official documentation; it records each tool's routing role, smoke tests, harness conventions, pitfalls, and final-answer compliance constraints.

Agent protocol:

1. Read `docs/02-tool-router.md` first.
2. Read the relevant tool card before using a tool.
3. Check availability before assuming a heavy tool exists.
4. Run the smallest smoke test before a larger experiment.
5. Save experiment code under the problem's `experiments/` directory.
6. Save outputs under `experiments/results/` when useful.
7. Record conclusions in `notes/attempt_log.md`.
8. Keep `final/proposed_solution.py` compliant with the problem's own compliance rules.

Heavy tools may be unavailable in a fresh environment. Their runners must fail with `ToolUnavailable`, not raw `ImportError` or missing-binary tracebacks.

## Tool cards

- `sage.md` — SageMath for exact algebra, finite fields, number theory, lattices, polynomial rings, and combinatorial designs.
- `sympy.md` — SymPy for lightweight symbolic manipulation and expression testing.
- `mpmath.md` — mpmath for high-precision numerical exploration.
- `pari_gp.md` — PARI/GP for number theory and algebraic recognition.
- `gap.md` — GAP for finite groups, group actions, and symmetry.
- `z3.md` — Z3 for finite SMT constraint search.
- `sat_solvers.md` — SAT solvers for CNF-style finite search.
- `networkx.md` — NetworkX for graph prototypes and property checks.
- `nauty_traces.md` — nauty/Traces for graph isomorphism, canonical labeling, and enumeration.
- `lean_mathlib.md` — Lean/mathlib for theorem lookup and formal checking.
- `oeis.md` — OEIS for sequence recognition.
- `paper_search.md` — Literature retrieval through topic cards, paper cards, theorem cards, and MCP search interfaces.
