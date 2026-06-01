# Per-Level Research Loop

Each rung of the task ladder runs the same tight loop. The unit of progress is a
**validated candidate**, not an argument.

```
idea → computation / research → candidate → validation → proof / result → log
```

## 1. Idea

State, in one or two sentences, the hypothesis for this rung: a construction to
try, a bound to test, a pattern to exploit. Write it in `notes/conjectures.md`
or the rung entry in `task_ladder.md`.

## 2. Computation / research

Explore numerically or symbolically before committing. Route to the right tool
(`docs/02-tool-router.md`): mpmath/SymPy for quick tests, Sage/PARI/GAP/Z3 for
exact or combinatorial search, OEIS for sequence identification. Retrieve a
paper **only** if the retrieval policy triggers (`docs/04-retrieval-policy.md`).
Store scratch work under `experiments/` (`docs/06-experiment-protocol.md`).

## 3. Candidate

Turn the idea into an **explicit, runnable Python candidate** that emits the
object in the required output format. No "the answer is approximately…": produce
the object itself (the integer, the adjacency list, the polynomial, the
high-precision decimal string). Save it under `candidates/`.

## 4. Validation

Run the problem validator in the sandbox. Record the result in
`validator_calls.jsonl`. A candidate that does not pass validation does not
count, no matter how convincing the reasoning behind it.

- **Pass + optimal/target met** → promote toward the final answer.
- **Pass but sub-optimal** → keep as current best; try to improve the score.
- **Fail** → log why in `notes/failed_paths.md`; revise the idea or relax a
  constraint (drop to level *k*−0.5).

## 5. Proof / result

If the rung calls for it, write a proof sketch or certificate that **explains why
the candidate is correct or optimal** (`docs/05-proof-protocol.md`). The proof
justifies and generalizes the validated candidate; it never substitutes for
validation.

## 6. Log

Append to the per-problem memory so the loop is resumable and auditable:

- `notes/attempt_log.md` — what was tried, the validator verdict, the score.
- `notes/lemmas.md` — reusable facts established or assumed.
- `notes/failed_paths.md` — dead ends, with the reason, to avoid repeats.
- `retrieved_context.md` — every external source consulted.

Then advance to the next rung, or, if stuck for 3 attempts, invoke the
ladder's *k*−0.5 fallback (`docs/03-task-ladder-protocol.md`).
