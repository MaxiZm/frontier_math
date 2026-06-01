"""Aggregate best scores across runs into a leaderboard."""

from __future__ import annotations

import json
from pathlib import Path

from ..core.score import is_better


def build_leaderboard(runs_root: str | Path, direction: str = "minimize") -> list[dict]:
    """Scan ``runs_root`` for run.json files and rank by best objective value."""
    rows: list[dict] = []
    for run_json in Path(runs_root).rglob("run.json"):
        try:
            d = json.loads(run_json.read_text())
        except json.JSONDecodeError:
            continue
        best = d.get("best_result") or {}
        rows.append(
            {
                "problem_id": d.get("problem_id"),
                "status": d.get("status"),
                "objective_value": best.get("objective_value"),
                "improved": best.get("improved"),
                "run_dir": str(run_json.parent),
            }
        )

    def sort_key(row: dict):
        v = row.get("objective_value")
        return (v is None, v if v is not None else 0)

    rows.sort(key=sort_key, reverse=(direction == "maximize"))
    return rows
