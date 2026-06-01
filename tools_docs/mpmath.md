# mpmath

## Purpose

mpmath provides arbitrary-precision real and complex numerical evaluation for constants, special functions, sums, products, limits, and numerical sanity checks.

## Use when

- You need high-precision numerical evidence for a closed-form candidate.
- You need constants or special functions at controlled precision.
- You want to compare a proposed formula against a numeric target.
- You need initial digits before using recognition tools such as PARI/GP or Sage.

## Do not use when

- You need proof; high-precision agreement is evidence, not a theorem.
- The final-answer compliance rules ban numerical search, integration, or root finding.
- Exact algebraic structure is required; prefer SymPy, Sage, or PARI/GP.

## Availability check

```bash
python - <<'PY'
from mpmath import mp
print(mp.dps)
PY
```

Expected successful output:

```txt
15
```

## Installation notes

mpmath is a project dependency. Install the harness with `pip install -e ".[dev]"` or `uv sync`.

## Minimal smoke test

```python
from mpmath import mp

mp.dps = 100
value = mp.zeta(2)
candidate = mp.pi**2 / 6
print(abs(value - candidate))
```

## Common workflows

### Workflow 1: Closed-form numeric check

Goal: test whether a proposed expression matches a target constant.

Steps: set `mp.dps`, evaluate target and candidate, compare absolute error to tolerance.

Code:

```python
from mpmath import mp
mp.dps = 80
print(abs(mp.zeta(2) - mp.pi**2 / 6))
```

Expected output: a tiny value such as `0.0`.

### Workflow 2: Generate digits for recognition

Goal: produce enough digits to feed into PARI/GP `algdep`, OEIS, or a paper search clue.

Steps: raise precision, compute the value, save digits and code under `experiments/`.

Code:

```python
from mpmath import mp
mp.dps = 120
print(mp.nstr(mp.euler, 100))
```

Expected output: 100 significant digits of Euler's constant.

## Typical mathematical objects

mpmath is good for high-precision constants, special functions, integrals, roots, infinite sums/products, asymptotic checks, and numerical comparisons.

## Agent protocol

When using mpmath, the agent must:

1. State the precision and tolerance.
2. Run the smallest numeric check first.
3. Save code under `experiments/`.
4. Save output under `experiments/results/` when it informs a conjecture.
5. Record precision, tolerance, and conclusion in `notes/attempt_log.md`.
6. Never present numerical agreement alone as proof.

## Pitfalls

- Too little precision can create false matches.
- Cancellation can destroy meaningful digits.
- `quad`, `findroot`, and optimization-style loops are research-time tools unless explicitly allowed.
- Matching many digits can still be coincidence or overfitting.

## Example integration with the harness

```python
from math_harness.validators.numeric_closed_form import NumericClosedFormValidator

validator = NumericClosedFormValidator(target="pi**2/6", tol="1e-50")
result = validator.validate("pi**2/6")
assert result.passed
```

## Final-answer compliance notes

mpmath may be used during research to identify or check a candidate. A final candidate may use mpmath constants or functions only when the benchmark permits executable formulas of that style; hidden numerical search, integration, and root finding in final code are normally forbidden.
