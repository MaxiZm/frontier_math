#!/usr/bin/env python3
"""Bundle a problem's final answer + artifacts into a zip solution pack."""
import argparse
import _bootstrap  # noqa: F401
from math_harness.reporting.final_solution_pack import export_solution_pack


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Export a solution pack.")
    parser.add_argument("--problem", required=True)
    parser.add_argument("--out")
    args = parser.parse_args(argv)
    out = export_solution_pack(args.problem, out_path=args.out)
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
