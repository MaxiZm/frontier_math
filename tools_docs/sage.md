# Sage (SageMath)

## What it's for
A large open-source CAS unifying many libraries (PARI, GAP, Singular, NetworkX,
and more) behind one Python-based interface. The workhorse for **exact**
mathematics.

## When to use it
Per the tool router (`docs/02-tool-router.md`), use Sage for:
- exact algebra,
- finite fields,
- number theory,
- lattices,
- polynomial rings,
- combinatorial designs.

Reach for Sage when SymPy/mpmath are not exact or expressive enough and you need
genuine structures (rings, fields, lattices, designs).

## How to call it
Via the Sage interpreter / `sage -python`:

```python
F = GF(2^8)                       # finite field
R.<x> = PolynomialRing(F)         # polynomial ring
L = IntegerLattice(matrix([[2,0],[1,2]]))
factor(2^67 - 1)                  # exact number theory
```

## Install
External binary, **large**. Install from your OS package manager or a conda/
binary distribution (`sagemath`). Verify with `sage --version`.

> **Runner status: STUB.** The harness tool runner for Sage raises
> `ToolUnavailable` until the `sage` binary is installed and on `PATH`. Install
> Sage to enable it.
