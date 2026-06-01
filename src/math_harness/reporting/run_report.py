"""Summarize a run directory (run.json + jsonl logs) into markdown."""

from __future__ import annotations

from pathlib import Path

from ..core.run_state import RunState


def summarize_run(run_dir: str | Path) -> str:
    state = RunState.load(run_dir)
    lines = [
        f"# Run report: {state.problem_id}",
        "",
        f"- status: **{state.status}**",
        f"- ladder level: {state.ladder_level}",
        f"- attempts: {len(state.attempts)}",
    ]
    if state.best_result:
        br = state.best_result
        lines += [
            f"- best passed: {br.passed}",
            f"- best objective_value: {br.objective_value}",
            f"- best improved: {br.improved}",
            f"- best candidate: {state.best_candidate_path}",
        ]
    lines.append("")
    lines.append("## Attempts")
    for a in state.attempts:
        lines.append(
            f"- #{a.index} (P{a.level}) passed={a.result.passed} "
            f"obj={a.result.objective_value} :: {a.candidate_path}"
        )
    return "\n".join(lines) + "\n"


def write_run_report(run_dir: str | Path) -> Path:
    run_dir = Path(run_dir)
    report = summarize_run(run_dir)
    out = run_dir / "final_report.md"
    out.write_text(report)
    return out
