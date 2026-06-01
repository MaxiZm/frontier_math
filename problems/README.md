# Problems

Each problem lives in its own folder under `problems/<problem_id>/`. The folder
holds the public statement, the protocol scaffolding the agent fills in, the
candidates and experiments it produces, and the final submission. The validator
turns a candidate into a verified result — prose never substitutes for validation
(`docs/00-overview.md`).

`problems/template_problem/` is the canonical layout; copy it to start a new
problem (`docs/10-contribution-guide.md`).

## Folder schema

Authored up front (problem owner):

- `statement.md` — the problem, precisely stated. Public; no answer key.
- `output_format.md` — the exact shape/type the candidate must emit.
- `compliance_rules.md` — which final-answer bans apply
  (`docs/07-final-answer-compliance.md`).
- `task_ladder.md` — the 10-rung ladder (`docs/03-task-ladder-protocol.md`).
- `tool_plan.md` — which tools to route work to (`docs/02-tool-router.md`).
- `problem.yaml` — machine-readable metadata: id, parameters, scoring, budgets,
  compliance flags (schema in `paper_index/schema/problem.schema.json`).
- `validator.py` — the verifier that scores candidates (sandbox-safe, JSON-only,
  deterministic).

Filled in during solving (the agent):

- `retrieved_context.md` — every source consulted
  (`docs/04-retrieval-policy.md`).
- `notes/` — `lemmas.md`, `conjectures.md`, `failed_paths.md`, `attempt_log.md`.
- `experiments/` — numbered experiment scripts + `results/`
  (`docs/06-experiment-protocol.md`).
- `candidates/` — explicit candidate files, each validated.
- `proofs/` — proof sketches / certificates (`docs/05-proof-protocol.md`).
- `final/` — `final_candidate.md`, `verification_report.md`,
  `proof_or_explanation.md` (and the submitted candidate file).

## Integrity
The statement and committed files must never leak an answer key or hidden
verifier output. Keep public statements, generated attempts, and verified final
candidates separate (`docs/11-evaluation-integrity.md`).
