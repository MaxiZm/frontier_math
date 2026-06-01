# Benchmark Suite: FrontierMath (Open)

The open subset of FrontierMath-style problems — exceptionally hard,
research-level questions with definite, machine-checkable answers. Because the
**official verifiers are hidden**, this suite ships local **proxy validators**
that approximate the official check; treat scores as proxies, not official
results.

## Layout
- `problems/` — one folder per problem (schema in `problems/README.md`): public
  `statement.md`, `output_format.md`, `compliance_rules.md`, `problem.yaml`.
- `proxy_validators/` — local approximations of the official verifiers. They may
  be weaker; the **skeptic** should probe whether a pass is genuine
  (`agent_instructions/skeptic.md`).
- `metadata/` — per-problem tags: area, difficulty, budgets, compliance flags.
- `runs/` — saved run artifacts (`docs/09-benchmarking.md`).

## Proxy caveat
A proxy validator passing does **not** guarantee the official verifier passes.
Strengthen proxies where possible and clearly label proxy scores as proxy in
reports.

## Integrity
Never commit the official hidden verifiers, expected answers, or any private
FrontierMath material. Keep public statements, generated attempts, and verified
final candidates separated (`docs/11-evaluation-integrity.md`).
