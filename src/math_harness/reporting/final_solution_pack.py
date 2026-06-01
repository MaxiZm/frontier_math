"""Bundle a problem's final answer + run artifacts into a zip solution pack."""

from __future__ import annotations

import zipfile
from pathlib import Path

from ..core.problem import Problem


def export_solution_pack(problem_dir: str | Path, out_path: str | Path | None = None) -> Path:
    problem = Problem.load(problem_dir)
    root = problem.root
    out = Path(out_path) if out_path else root / f"{problem.id}.solution_pack.zip"

    include = ["problem.yaml", "statement.md", "output_format.md", "validator.py", "final"]
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        for rel in include:
            path = root / rel
            if path.is_file():
                zf.write(path, arcname=rel)
            elif path.is_dir():
                for f in path.rglob("*"):
                    if f.is_file() and "__pycache__" not in f.parts:
                        zf.write(f, arcname=str(f.relative_to(root)))
    return out
