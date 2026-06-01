# Lean / mathlib

Status: documented interface; runner stubbed in this pass.

## Purpose

Lean is a theorem prover, and mathlib is its mathematics library. Use them for theorem lookup, formal proof checking, and small machine-checked lemmas once the informal structure is clear.

## Use when

- You need to verify that a known theorem exists with the expected statement.
- A proof obligation is small and worth machine checking.
- The skeptic requests certainty on a lemma.
- You want theorem-card evidence for a formalized result.

## Do not use when

- You are still doing numeric or construction search.
- The statement is not yet clear enough to formalize.
- A lightweight proof sketch is sufficient for the current ladder level.
- Installation/setup time would dominate the mathematical work.

## Availability check

```bash
lean --version && lake --version
```

Expected successful output:

```txt
Lean ...
Lake ...
```

## Installation notes

Install `elan`, create or enter a Lean project with mathlib, and fetch cached mathlib artifacts with `lake exe cache get`. This can be a large download.

## Minimal smoke test

```lean
import Mathlib
#check Nat.Prime
example : 2 + 2 = 4 := by norm_num
```

Expected output: Lean accepts the file and prints the checked theorem information.

## Common workflows

### Workflow 1: Theorem lookup

Goal: find a known theorem or definition name.

Steps: search mathlib, run `#check`, record exact theorem name/signature in a theorem card.

Code:

```lean
import Mathlib
#check Nat.Coprime
```

Expected output: the signature of `Nat.Coprime`.

### Workflow 2: Formalize a tiny lemma

Goal: machine-check a small arithmetic or algebraic step.

Steps: state the lemma, solve with mathlib tactics if possible, store the Lean snippet.

Code:

```lean
import Mathlib
example : 2 + 2 = 4 := by norm_num
```

Expected output: no errors.

## Typical mathematical objects

Lean/mathlib is good for theorem statements, definitions, formal lemmas, algebraic structures, order facts, number-theory lemmas, topology/analysis theorems, and machine-checked proof dependencies.

## Agent protocol

When using Lean, the agent must:

1. State the exact theorem or lemma being checked.
2. Run a tiny Lean smoke test first.
3. Save `.lean` files under `experiments/`.
4. Save Lean output under `experiments/results/`.
5. Record theorem names and signatures in `notes/attempt_log.md` or a theorem card.
6. Use Lean after the informal structure is clear, not as the first search tool.

## Pitfalls

- Mathlib names may differ from informal theorem names.
- Formalization can be much slower than informal proof checking.
- A `#check` only confirms availability, not that it applies to your hypotheses.
- Version mismatches can break examples.

## Example integration with the harness

```python
from math_harness.tools.lean_search import available, run

if available():
    run("import Mathlib\n#check Nat.Prime")
```

## Final-answer compliance notes

Lean is normally research-time proof support. Final candidates should cite or include the validated theorem/lemma as required by the benchmark, but executable final answers should not depend on Lean unless the problem explicitly requests formal proof artifacts.
