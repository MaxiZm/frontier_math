# SAT Solvers

## Purpose

SAT solvers decide Boolean satisfiability for CNF formulas and are often faster than SMT solvers for pure finite Boolean search.

## Use when

- The problem has a natural Boolean encoding.
- You need raw speed for graph coloring, Ramsey-style search, exact cover, or construction existence.
- You can emit DIMACS CNF and parse a model.
- An `UNSAT` result plus proof artifact would be meaningful for a bounded non-existence claim.

## Do not use when

- Constraints are naturally integer, real, or algebraic; use Z3/ILP/Sage.
- You cannot validate that the CNF encoding matches the math problem.
- You need a human-readable proof of the original theorem.
- The search space is tiny enough for direct Python enumeration.

## Availability check

```bash
command -v kissat && command -v cadical && command -v minisat
```

Expected successful output:

```txt
/path/to/a/sat-solver
```

## Installation notes

This environment has Kissat, CaDiCaL, MiniSat, and Python `python-sat` installed. Glucose CLI is not installed, but PySAT provides `Glucose3` as a Python solver backend.

## Minimal smoke test

```bash
cat > /tmp/smoke.cnf <<'CNF'
p cnf 2 2
1 0
-1 2 0
CNF
kissat /tmp/smoke.cnf
```

Expected output contains `SATISFIABLE` and a model when using Kissat. Substitute another installed solver if needed.

## Common workflows

### Workflow 1: DIMACS construction search

Goal: find a Boolean assignment satisfying a combinatorial encoding.

Steps: map mathematical variables to integer literals, write DIMACS, run solver, decode model into an explicit object.

Code:

```txt
p cnf 2 2
1 0
-1 2 0
```

Expected output: satisfiable model with variable `1` true and variable `2` true or unconstrained by the second clause.

### Workflow 2: Exact-cover style encoding

Goal: enforce exactly-one constraints for choices.

Steps: add one at-least-one clause and pairwise at-most-one clauses, solve, decode selected literals.

Code:

```python
def exactly_one(lits):
    clauses = [list(lits)]
    clauses += [[-a, -b] for i, a in enumerate(lits) for b in lits[i + 1:]]
    return clauses
```

Expected output: CNF clauses enforcing one selected literal.

## Typical mathematical objects

SAT solvers are good for Boolean matrices, graph colorings, exact cover, finite incidence structures, Ramsey searches, packing/covering encodings, and bounded existence questions.

## Agent protocol

When using SAT solvers, the agent must:

1. State the literal mapping and each constraint family.
2. Run a tiny CNF smoke test first.
3. Save encoder code and DIMACS under `experiments/`.
4. Save solver logs/models under `experiments/results/`.
5. Record decoding and validation in `notes/attempt_log.md`.
6. Validate decoded objects with the problem validator, not just solver output.

## Pitfalls

- Wrong encodings produce convincing but irrelevant models.
- DIMACS literal numbering mistakes are common.
- SAT models may leave variables arbitrary; decoding must handle this.
- `UNSAT` without a proof artifact is not always enough for a final mathematical claim.

## Example integration with the harness

```python
from math_harness.tools.sat_runner import available, run

if available():
    run("p cnf 1 1\n1 0\n")
```

## Final-answer compliance notes

SAT solvers are research-time search tools. Final candidates should contain the decoded explicit object or proof artifact requested by the problem, not invoke a SAT solver during scoring unless explicitly allowed.
