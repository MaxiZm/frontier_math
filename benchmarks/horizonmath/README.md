# Benchmark Suite: HorizonMath

Research-grade mathematical-discovery problems — the harness's primary **hard**
benchmark. Problems span the topic-pack areas and demand explicit, verifier-
checked candidates (constructions, exact values, extremal objects), not prose.

## Layout
- `problems/` — one folder per problem (schema in `problems/README.md`): public
  `statement.md`, `output_format.md`, `compliance_rules.md`, `problem.yaml`.
- `validators/` — the verifiers that score candidates. Some problems use a
  **hidden official verifier**: its internals and expected outputs are **not**
  committed here (`docs/11-evaluation-integrity.md`).
- `metadata/` — per-problem tags: area, difficulty, time/memory budget,
  compliance flags, scoring rule.
- `runs/` — saved run artifacts for this suite (`docs/09-benchmarking.md`).

## Running & scoring
Run the agent per problem at the desired ablation level (`docs/09-benchmarking.md`)
and validate via `verifier_runner` (`mcp_servers/verifier_runner/`). Score is the
validator's verdict/score on the **submitted final candidate**, which must satisfy
the problem's `compliance_rules.md`.

## Integrity
Do not commit hidden verifier outputs, expected answers, or private problems. Keep
public statements, generated attempts, and verified final candidates separate.
