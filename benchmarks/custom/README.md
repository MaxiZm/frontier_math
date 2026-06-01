# Benchmark Suite: Custom

Your own problems and validators for local experiments — a scratch suite for
trying new problem ideas, new validators, or new topic packs before promoting
them to a standard suite.

## Layout
- `problems/` — your problem folders (schema in `problems/README.md`). Start from
  `problems/template_problem/`.
- `validators/` — your local validators (see the validator guidance in
  `docs/10-contribution-guide.md`).
- `runs/` — saved run artifacts (`docs/09-benchmarking.md`).

## Adding a custom problem
1. Copy `problems/template_problem/` into `problems/`.
2. Fill in `statement.md`, `output_format.md`, `compliance_rules.md`,
   `task_ladder.md`, `tool_plan.md`, `problem.yaml`.
3. Write a validator in `validators/` (sandbox-safe, JSON-only, deterministic).
4. Add tests and run `pytest` (`docs/10-contribution-guide.md`).

## Integrity
Even for local work, keep public statements, generated attempts, and verified
final candidates separated, and never commit answer keys into statements
(`docs/11-evaluation-integrity.md`).
