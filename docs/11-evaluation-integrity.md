# Evaluation Integrity

Benchmark results are only meaningful if there is **no data leakage** and every
run is **auditable**. These rules are mandatory for any run that will be reported.

## No benchmark data leakage

- **Never commit hidden official verifier outputs.** Expected answers, official
  grader internals, and private test vectors must not enter the repo, the
  agent's context, or any logged artifact.
- **Never commit private benchmark material.** If a benchmark ships
  hold-out/private problems, they stay out of the repo and out of training- or
  retrieval-reachable storage.
- **Separate the three kinds of material:**
  1. **Public problem statements** — what the agent is allowed to read.
  2. **Generated attempts** — candidates, experiments, and transcripts the agent
     produces during a run.
  3. **Verified final candidates** — the submitted answers and their validator
     verdicts.
  Keep these in distinct locations; never let expected answers leak into the
  statement or the agent's context.

## Per-run audit log

Every reported run must log, in `run.json` (`docs/09-benchmarking.md`):

- **model** — exact model id / version.
- **prompt** — the prompt template / harness configuration used.
- **tool availability** — which tools and MCP servers were enabled (ties to the
  ablation level).
- **seed** — the random seed for any stochastic component.
- **time budget** — the wall-clock / step budget for the run.
- **number of validator calls** — how many times the validator was invoked
  (guards against brute-forcing the grader).

## Fair comparison

- Fix the problem set, seed, and time budget across ablation levels so
  level-to-level deltas are attributable to the harness component being added.
- The validator is part of the environment, not the agent: an excessive
  validator-call count is itself a reportable signal, not a way to win.
