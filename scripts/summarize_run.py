#!/usr/bin/env python3
"""Summarize a run directory into final_report.md and print it."""
import argparse
import _bootstrap  # noqa: F401
from math_harness.reporting.run_report import summarize_run, write_run_report


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Summarize a run directory.")
    parser.add_argument("--run", required=True, help="Path to a run directory")
    args = parser.parse_args(argv)
    print(summarize_run(args.run))
    out = write_run_report(args.run)
    print(f"\nWrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
