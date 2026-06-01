# SAT Solvers

## What it's for
Fast decision of boolean satisfiability (CNF). For purely propositional finite
search and existence/non-existence questions, a dedicated CDCL SAT solver
(MiniSat, Glucose, CaDiCaL, Kissat) often beats a general SMT solver.

## When to use it
Per the tool router (`docs/02-tool-router.md`), use Z3/SAT/ILP for finite
constraint search. Choose a SAT solver when:
- the problem encodes naturally as CNF (graph colorings, Ramsey-type searches,
  combinatorial existence);
- you want maximum raw speed and have an effective encoding;
- an `UNSAT` result (ideally with a DRAT proof) serves as a non-existence
  certificate.

## How to call it
Via the Python `pysat` toolkit, or by emitting DIMACS to a solver binary:

```python
from pysat.solvers import Glucose3
s = Glucose3()
s.add_clause([1, 2]); s.add_clause([-1, 3])
print(s.solve(), s.get_model())
```

DIMACS workflow: write `problem.cnf`, run `cadical problem.cnf`, parse the model.
A **final** answer must emit the found object explicitly, not invoke a solver at
scoring time (`docs/07-final-answer-compliance.md`).

## Install
`pip install python-sat`, or install a solver binary (`cadical`, `kissat`,
`glucose`, `minisat`).

> **Runner status: STUB.** The harness tool runner for SAT solvers raises
> `ToolUnavailable` until a solver (`python-sat` or a solver binary) is
> installed.
