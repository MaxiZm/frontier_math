# mpmath

## What it's for
Arbitrary-precision real and complex floating-point arithmetic: high-precision
evaluation of constants, special functions, sums, products, and limits.

## When to use it
- High-precision numerical exploration of a constant or integral.
- Getting enough digits to recognize a closed form (then confirm exactly with
  PARI `algdep` / Sage / `mpmath.identify`).
- Quick sanity checks of asymptotics or convergence.
- **Not** for the final answer when the problem bans numerical methods — use it
  at research time, then reconstruct the value exactly.

## How to call it
Pure-Python package, imported directly:

```python
from mpmath import mp, mpf, pi, zeta, quad, identify
mp.dps = 50                      # 50 decimal digits
val = zeta(3)                    # high-precision evaluation
guess = identify(val, ['zeta(3)'])  # try to recognize a closed form
```

`quad` (numerical integration) and `findroot` (root finding) are research-time
tools; their *results* may be allowed in a final answer only as an explicit
literal, never as a live call (`docs/07-final-answer-compliance.md`).

## Install
`pip install mpmath` (a dependency of SymPy, usually already present). Pure
Python; no external binary. Available in the harness by default.
