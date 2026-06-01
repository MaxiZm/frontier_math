"""Render an ablation_report.json into a comparison table."""

from __future__ import annotations

import json
from pathlib import Path


def render_ablation(report_path: str | Path) -> str:
    data = json.loads(Path(report_path).read_text())
    lines = ["# Ablation report", "", "| arm | passed | objective | improved |", "|---|---|---|---|"]
    for arm, result in data.items():
        lines.append(
            f"| {arm} | {result.get('passed')} | "
            f"{result.get('objective_value')} | {result.get('improved')} |"
        )
    return "\n".join(lines) + "\n"
