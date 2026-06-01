#!/usr/bin/env python3
"""Evaluate a candidate against a problem. Thin wrapper over run_problem.main."""
import _bootstrap  # noqa: F401
from math_harness.runners.run_problem import main

if __name__ == "__main__":
    raise SystemExit(main())
