# MCP Server: experiment_runner

Run an experiment script in the sandbox and capture its JSON result. Supports the
experiment protocol (`docs/06-experiment-protocol.md`): research-time exploration,
not final-answer validation.

> **Status: interface stub.** The contract below is defined; the sandboxed
> executor is not wired up here yet. Calls return a stub response.

## Tools

### `run_experiment`
- **input**:
  - `problem_id` (string, required) — the owning problem.
  - `script_path` (string, required) — e.g. `experiments/003_relaxed_lp_bound.py`;
    OR `code` (string) — inline experiment source.
  - `args` (object, optional) — parameters passed to the experiment.
  - `time_budget_s` (number, optional).
  - `seed` (int, optional) — recorded for reproducibility.
- **output**: `{ "status": "ok" | "timeout" | "error", "result": JSON,
  "stdout": string, "runtime_s": number, "result_path": string }`
  - `result_path` points at the saved `experiments/results/<name>.json`.

## Execution & security
- Runs in the **subprocess sandbox** (`docs/08-sandbox-security.md`): wall-clock
  timeout, best-effort CPU/memory limits, **JSON-only** result I/O, no `pickle`.
- Research-time code may use any installed library; this server does **not**
  enforce final-answer compliance (`docs/07-final-answer-compliance.md`).
- Each call is logged to the run's `tool_calls.jsonl`; the recorded `seed` keeps
  experiments reproducible.
