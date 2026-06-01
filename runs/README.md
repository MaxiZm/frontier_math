# Runs

Saved artifacts from harness runs. Each run is one agent attempt at one problem at
one ablation level; this directory is the audit trail and the data behind any
reported benchmark numbers (`docs/09-benchmarking.md`,
`docs/11-evaluation-integrity.md`).

## Layout

- `ablations/` — runs organized by ablation level (`docs/09-benchmarking.md`):
  `raw_model`, `tools_only`, `tools_plus_ladder`,
  `tools_plus_ladder_plus_retrieval`, `full_harness`. Compare the same problem
  set across levels to attribute gains to harness components.
- `horizonmath/` — runs against the HorizonMath suite.
- `frontiermath_open/` — runs against the FrontierMath (open) suite (proxy
  scores).
- `local/` — ad-hoc local / development runs (e.g. toy_discovery, custom).

A typical run directory is `<area>/<problem_id>/<timestamp_or_id>/`.

## Stored per run

- `run.json` — model, ablation level, problem id, **seed**, **time budget**,
  **tool availability**, **number of validator calls**, final score (the audit
  record from `docs/11-evaluation-integrity.md`).
- `transcript.md` — full agent transcript (reasoning + actions).
- `tool_calls.jsonl` — one line per external tool invocation.
- `validator_calls.jsonl` — one line per validation (candidate, verdict, score).
- `best_candidate.py` — the best candidate found.
- `best_score.json` — its validator result.
- `failed_paths.md` — dead ends and why they failed.
- `final_report.md` — the submitted-answer write-up.

## Integrity
Runs hold **generated attempts** and **verified final candidates** only — never
hidden official verifier outputs, expected answers, or private benchmark material
(`docs/11-evaluation-integrity.md`).
