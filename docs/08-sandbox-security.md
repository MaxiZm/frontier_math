# Sandbox & Security

Candidate code is **untrusted**. The harness never imports or `exec`s a candidate
in its own process. Every candidate and validator runs in an **isolated
subprocess sandbox**.

## Execution model

- **Subprocess isolation.** The candidate runs in a fresh child process. A crash,
  hang, or memory blow-up takes down only the child.
- **Wall-clock timeout.** Each run has a hard wall-clock limit. On timeout the
  child is killed and the result is recorded as a timeout failure.
- **Best-effort POSIX resource limits.** Where the platform supports it
  (`resource.setrlimit`), the child gets CPU-time and address-space (memory)
  caps, plus limits on file size / open files. These are best-effort: on
  platforms without `setrlimit` only the wall-clock timeout applies.
- **JSON-only I/O.** Inputs go to the child and results come back as **JSON**
  over a pipe / temp channel. **No `pickle`** — never unpickle untrusted output.
  Candidates must emit JSON-serializable results.
- **Docker (optional).** For stronger isolation, the runner can execute the child
  inside a container with no network and a read-only mount. This is optional and
  off by default; the subprocess + rlimits path is the baseline.

## Implications for candidate authors

- Return JSON-serializable objects (ints, strings, lists, dicts, nested
  combinations). For big integers or high-precision reals, return them as
  strings to avoid precision loss in JSON.
- Stay within the time and memory budget; a correct-but-too-slow candidate scores
  as a failure.
- No network, no subprocesses, no file I/O in the final answer (this also helps
  it pass compliance — see `docs/07-final-answer-compliance.md`).

## Implications for validator authors

- Validators also run sandboxed and communicate via JSON.
- Validate the **shape** of candidate output before trusting it; assume it may be
  malformed, oversized, or adversarial.
- Never `pickle.loads` candidate output and never `eval` candidate strings.
