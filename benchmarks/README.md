# Benchmarks

The benchmark suites the harness is evaluated on. Each suite is a collection of
problems with validators; the harness runs an agent against them and scores the
submitted final candidates. Evaluation uses the ablation ladder and per-run
artifacts described in `docs/09-benchmarking.md`, under the integrity rules in
`docs/11-evaluation-integrity.md`.

## The four suites

- **`horizonmath/`** — research-grade problems with hidden official verifiers;
  the primary hard benchmark. (`problems/`, `validators/`, `metadata/`, `runs/`.)
- **`frontiermath_open/`** — the open subset of FrontierMath-style problems, run
  through local **proxy** validators (the official hidden verifiers are not
  shipped). (`problems/`, `proxy_validators/`, `metadata/`, `runs/`.)
- **`toy_discovery/`** — small, fast discovery problems for smoke-testing the
  loop, validators, and sandbox end to end. (`problems/`, `validators/`,
  `runs/`.)
- **`custom/`** — your own problems and validators for local experiments.
  (`problems/`, `validators/`, `runs/`.)

## Run artifacts

Every run, at every ablation level, writes the standard artifact set
(`docs/09-benchmarking.md`):

- `run.json` — model, ablation level, problem id, seed, time budget, tool
  availability, validator-call count, final score.
- `transcript.md` — full agent transcript.
- `tool_calls.jsonl` — one line per external tool call.
- `validator_calls.jsonl` — one line per validation.
- `best_candidate.py` — best candidate found.
- `best_score.json` — its validator result.
- `failed_paths.md` — dead ends and why.
- `final_report.md` — the submitted-answer write-up.

## Integrity

Never commit hidden official verifier outputs or private benchmark material. Keep
public statements, generated attempts, and verified final candidates separated
(`docs/11-evaluation-integrity.md`).
