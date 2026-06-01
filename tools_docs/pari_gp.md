# PARI/GP

## What it's for
A fast computer algebra system specialized for number theory: high-speed
arithmetic, algebraic number recognition, modular forms and L-functions.

## When to use it
Per the tool router (`docs/02-tool-router.md`), use PARI/GP for:
- number theory constants,
- algebraic number recognition,
- L-functions,
- high-speed arithmetic.

The go-to for recognizing a numerical value as algebraic (`algdep` / `lindep`)
after you have enough digits from mpmath.

## How to call it
The `gp` interpreter, or the `cypari2` Python binding:

```gp
algdep(1.41421356237309504880, 2)   \\ -> x^2 - 2
lindep([1, Pi, Pi^2])                \\ integer relation search
lfun(1, 2)                           \\ L-function values
```

```python
import cypari2
pari = cypari2.Pari()
pari.algdep(pari('1.4142135623730950488'), 2)
```

## Install
External binary `gp`, or `pip install cypari2` (needs libpari). Verify with
`gp --version`.

> **Runner status: STUB.** The harness tool runner for PARI/GP raises
> `ToolUnavailable` until the `gp` binary (or `cypari2`/libpari) is installed.
