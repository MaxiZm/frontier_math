# Final-Answer Compliance

Compliance constrains the **submitted final candidate** — the single Python file
the harness scores as the answer. It does **not** constrain your research code:
experiments, search scripts, and exploratory notebooks may use anything. The
distinction is **research-time exploration vs. final-answer admissibility**.

You may discover the answer with a brute-force optimizer, a SAT solver, a random
search, and a pile of paper retrieval. The *final answer* must then reconstruct
or assert that object under the rules below.

## What is always allowed in a final answer

- Deterministic, finite loops that **construct an explicit object** (build an
  adjacency list, fill a table, assemble a polynomial, enumerate a bounded set).
- Exact arithmetic, integer/rational computation, modular arithmetic.
- Returning a precomputed explicit object (a literal you found offline), as long
  as the construction itself does not violate the rules below.

## What is forbidden in a final answer (when the problem's rules say so)

Each problem's `compliance_rules.md` states which of these apply. Common bans:

- **Hidden numerical search** — scanning parameters until a check passes.
- **Root-finding** — `scipy.optimize`, Newton iterations to locate the answer.
- **Numerical integration** — quadrature to produce the returned value.
- **Randomness** — any RNG influencing the output (`random`, `numpy.random`).
- **Optimization loops** — gradient descent, simulated annealing, LP/ILP solves
  that *are* the answer.
- **Network access** — sockets, HTTP, any I/O off the machine.
- **Subprocesses** — `subprocess`, `os.system`, shelling out to a CAS.
- **File I/O** — reading/writing files to smuggle in precomputed search results
  (returning a literal in-source is fine; loading a results file is not).
- **Forbidden imports** — e.g. `scipy.optimize`, `ortools`, `pulp`, and whatever
  else the problem lists.

## The litmus test

> Could the validator be fooled by a final answer that *searches* until the check
> passes, rather than *constructing* the object?

If yes, that style is forbidden. The final answer should embody the *solution*,
not a process that gropes for it at scoring time. A deterministic finite
construction that builds the object is the canonical compliant shape.

## Workflow

1. Explore freely; find the object however you like.
2. Read the problem's `compliance_rules.md`.
3. Rewrite the final candidate as a compliant deterministic construction (or a
   compliant explicit literal).
4. Have `verifier_runner` confirm it passes, and the skeptic confirm it does not
   secretly violate a ban.
