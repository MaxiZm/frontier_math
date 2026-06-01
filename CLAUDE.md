# Math Discovery Harness

You are working inside a verifier-driven mathematical discovery environment.
Your goal is not to write convincing prose.
Your goal is to produce explicit candidates that pass validators or improve scores.

For every problem, follow this loop:

1. Parse the exact statement.
2. Identify the output type.
3. Inspect the validator.
4. Build a 10-level task ladder.
5. Start with the easiest level.
6. For each level:
   idea -> computation/research -> candidate -> validation -> proof/result -> log.
7. If stuck, create an easier intermediate level.
8. Retrieve papers only when needed.
9. Never claim success without running the validator.
10. Save every useful failed path.

Final answers must be explicit, reproducible, and validator-clean.

## Where things live

- `CLAUDE.md` — this constitution (read automatically).
- `docs/` — the protocols you must follow. Start with `docs/00-overview.md`, then
  `docs/01-research-loop.md`, `docs/03-task-ladder-protocol.md`, `docs/04-retrieval-policy.md`,
  `docs/02-tool-router.md`, `docs/07-final-answer-compliance.md`, `docs/08-sandbox-security.md`.
- `agent_instructions/` — role cards (researcher, skeptic, optimizer, literature_scout,
  proof_checker, verifier_runner, final_writer).
- `tools_docs/` — when and how to use each math tool.
- `topic_packs/` — domain knowledge packs (definitions, methods, attack patterns, papers).
- `src/math_harness/` — the deterministic harness: problem loading, validators, sandbox,
  run bookkeeping. **The harness never thinks for you** — it loads your problem, runs your
  candidate in a sandbox, runs the validator, and records the result.
- `problems/` and `benchmarks/` — problem folders. Each has `problem.yaml`, `statement.md`,
  `validator.py`, a task ladder, and a `final/proposed_solution.py` you write.
- `runs/` — per-run artifacts (run.json, transcript.md, *.jsonl, best candidate, reports).

## Hard rules

- A candidate is only "solved" once `python scripts/evaluate_candidate.py` prints a green result.
- The final answer is executed in a subprocess sandbox with a timeout — it must be self-contained.
- Compliance is about the *submitted* candidate: deterministic finite loops that construct an
  explicit object are fine; hidden numerical search / optimization / randomness in the final answer
  are not, unless the problem explicitly allows them. See `docs/07-final-answer-compliance.md`.
- Any stochastic search you run must take and log a `seed`.
- Log every source you read in the problem's `retrieved_context.md`, and every dead end in
  `notes/failed_paths.md`.
