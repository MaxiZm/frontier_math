# Benchmarking

The harness is evaluated by an **ablation ladder**: the same agent and problems
are run with progressively more of the harness enabled, so we can attribute gains
to specific components (tools, ladder, retrieval) rather than to the base model
alone.

## The ablation ladder

1. **raw_model** — the base model, no tools, no harness scaffolding. It must emit
   a candidate from reasoning alone.
2. **tools_only** — the tool router and external tools are available
   (`docs/02-tool-router.md`), but no task ladder and no retrieval.
3. **tools_plus_ladder** — adds the 10-rung task ladder protocol
   (`docs/03-task-ladder-protocol.md`).
4. **tools_plus_ladder_plus_retrieval** — adds paper/theorem retrieval under the
   retrieval policy (`docs/04-retrieval-policy.md`).
5. **full_harness** — everything: tools, ladder, retrieval, topic packs,
   experiment memory, candidate search, and the skeptic.

Each level is a subdirectory under `runs/ablations/` (see `runs/README.md`).

## Per-run artifacts

Every run, at every ablation level, saves:

- `run.json` — run metadata: model, ablation level, problem id, seed, time
  budget, tool availability, validator-call count, final score.
- `transcript.md` — the full agent transcript (reasoning + actions).
- `tool_calls.jsonl` — one line per external tool invocation (tool, args,
  outcome, timing).
- `validator_calls.jsonl` — one line per validation (candidate id, verdict,
  score, timing).
- `best_candidate.py` — the best candidate found during the run.
- `best_score.json` — the validator result for the best candidate.
- `failed_paths.md` — dead ends and why they failed.
- `final_report.md` — the agent's final write-up of the submitted answer.

## Reading results

Compare scores level-to-level on the same problem set. The marginal lift from
level *n* to *n*+1 measures the value of the component added at *n*+1. Keep the
problem set, seed, and time budget fixed across levels so comparisons are valid
(`docs/11-evaluation-integrity.md`).
