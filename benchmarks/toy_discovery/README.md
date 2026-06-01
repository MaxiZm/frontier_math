# Benchmark Suite: Toy Discovery

Small, fast discovery problems for **smoke-testing** the harness end to end: the
research loop, candidate validation, the sandbox, and the run-artifact pipeline.
Use this suite for development and CI, not for headline results.

## Layout
- `problems/` — small problems (schema in `problems/README.md`) solvable in
  seconds: tiny constructions, small exact values, simple optimal objects.
- `validators/` — full local validators (these problems have no hidden official
  verifier).
- `runs/` — saved run artifacts (`docs/09-benchmarking.md`).

## Purpose
- Verify the loop works: candidate → sandbox validation → improvement → logs.
- Verify each artifact is written (`run.json`, `transcript.md`,
  `validator_calls.jsonl`, `best_candidate.py`, `best_score.json`, …).
- Provide quick examples for the task-ladder and compliance protocols.

Because cases are tiny, brute-force is often viable at research time; the **final**
candidate must still obey the problem's `compliance_rules.md`
(`docs/07-final-answer-compliance.md`).
