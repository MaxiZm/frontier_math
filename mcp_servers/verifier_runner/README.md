# MCP Server: verifier_runner

Run a candidate against a problem's validator in the sandbox and return the
verdict and score. This is the harness's ground truth — the verifier_runner role
card (`agent_instructions/verifier_runner.md`) uses this server.

> **Status: interface stub.** The contract below is defined; the sandboxed
> executor is not wired up here yet. Calls return a stub response.

## Tools

### `validate_candidate`
- **input**:
  - `problem_id` (string, required) — which problem's `validator.py` to use.
  - `candidate_code` (string, required) — the candidate's Python source; OR
  - `candidate_output` (JSON, optional) — a precomputed candidate output to check.
  - `time_budget_s` (number, optional) — overrides the problem default.
- **output**: `{ "verdict": "pass" | "fail" | "timeout" | "error",
  "score": number | null, "diagnostics": string, "runtime_s": number,
  "memory_mb": number }`.

## Execution & security
- Runs in the **subprocess sandbox** (`docs/08-sandbox-security.md`): wall-clock
  timeout, best-effort CPU/memory limits, **JSON-only** I/O, no `pickle`, no
  `eval` of candidate output.
- Treats candidate output as adversarial; validates shape before scoring.
- Each call appends a line to the run's `validator_calls.jsonl` and increments the
  validator-call count logged in `run.json`
  (`docs/11-evaluation-integrity.md`).
