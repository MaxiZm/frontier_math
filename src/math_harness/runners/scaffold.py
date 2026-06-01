"""Scaffold a new problem directory from the template.

Generates new problem folders, so it lives outside the read-only verification
path. ``create_problem`` copies ``problems/template_problem`` and rewrites the
``id``/``benchmark`` in the generated ``problem.yaml``.
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[3]
_TEMPLATE = _REPO_ROOT / "problems" / "template_problem"

_MINIMAL_PROBLEM_YAML = """\
id: {id}
benchmark: {benchmark}
domain:
  - uncategorized
output_type: constant
evaluation_mode: ground_truth_computable
compliance_style: closed_form
difficulty:
  level: 1
  description: TODO
objective:
  direction: minimize
  metric: abs_error
  baseline: null
entrypoint:
  function_name: solve
  file: final/proposed_solution.py
validator:
  file: validator.py
  timeout_seconds: 30
  deterministic: true
compliance:
  allow_floats: true
  allow_search_inside_final_solution: false
  allow_hardcoded_candidate: true
  require_deterministic: true
  forbidden_imports: []
  forbidden_calls: []
retrieval:
  enabled: true
  default_policy: trigger_based
tools:
  recommended:
    - python
    - sympy
    - mpmath
"""

_MINIMAL_VALIDATOR = '''\
"""Validator for {id}. Expose `validate(output) -> dict`."""


def validate(output) -> dict:
    # TODO: replace with a real check of the candidate output.
    return {{
        "passed": False,
        "messages": ["validator not implemented yet"],
        "details": {{"output": str(output)}},
    }}
'''

_MINIMAL_SOLUTION = '''\
"""Final candidate for {id}. Must be self-contained and validator-clean."""


def solve():
    # TODO: return the explicit answer.
    raise NotImplementedError
'''


def create_problem(benchmark: str, problem_id: str, base_dir: str | Path | None = None) -> Path:
    """Create ``<base>/<benchmark>/problems/<id>`` and return its path."""
    base = Path(base_dir) if base_dir else _REPO_ROOT / "benchmarks"
    target = base / benchmark / "problems" / problem_id
    if target.exists():
        raise FileExistsError(f"Problem already exists: {target}")

    if _TEMPLATE.is_dir():
        shutil.copytree(_TEMPLATE, target)
    else:  # pragma: no cover - template ships with the repo
        target.mkdir(parents=True)

    for sub in ("experiments", "candidates", "proofs", "notes", "final"):
        (target / sub).mkdir(parents=True, exist_ok=True)

    (target / "problem.yaml").write_text(
        _MINIMAL_PROBLEM_YAML.format(id=problem_id, benchmark=benchmark)
    )
    (target / "validator.py").write_text(_MINIMAL_VALIDATOR.format(id=problem_id))
    (target / "final" / "proposed_solution.py").write_text(
        _MINIMAL_SOLUTION.format(id=problem_id)
    )
    return target


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Scaffold a new problem from the template.")
    parser.add_argument("--benchmark", required=True)
    parser.add_argument("--id", required=True, dest="problem_id")
    parser.add_argument("--base-dir")
    args = parser.parse_args(argv)
    target = create_problem(args.benchmark, args.problem_id, base_dir=args.base_dir)
    print(f"Created {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
