"""Validator for the Basel constant example.

Convention: expose ``validate(output) -> dict``. The harness runs the candidate
entrypoint in the sandbox and passes its return value here.
"""

from __future__ import annotations

import mpmath
from sympy import sympify

TARGET_EXPR = "pi**2/6"  # zeta(2) = sum 1/n^2
DPS = 50
TOL = mpmath.mpf("1e-30")
BASELINE = 1e-6


def validate(output) -> dict:
    mpmath.mp.dps = DPS
    target = mpmath.mpf(sympify(TARGET_EXPR).evalf(DPS))
    try:
        value = mpmath.mpf(sympify(str(output)).evalf(DPS))
    except Exception as exc:  # noqa: BLE001
        return {
            "passed": False,
            "score": 0.0,
            "messages": [f"could not parse candidate output {output!r}: {exc}"],
            "details": {"output": str(output)},
        }

    err = abs(value - target)
    passed = err <= TOL
    return {
        "passed": bool(passed),
        "score": 1.0 if passed else 0.0,
        "objective_value": float(err),
        "baseline": BASELINE,
        "improved": bool(err < mpmath.mpf(BASELINE)),
        "messages": [] if passed else [f"abs_error {err} exceeds tolerance {TOL}"],
        "details": {"target": TARGET_EXPR, "value": str(value), "abs_error": str(err)},
    }
