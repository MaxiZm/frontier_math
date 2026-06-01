# Compliance Rules

> Template. State which final-answer restrictions apply. These constrain the
> **submitted final candidate only**, not research code
> (`docs/07-final-answer-compliance.md`).

## Always allowed in the final answer
- Deterministic, finite loops that **construct an explicit object**.
- Exact / integer / rational / modular arithmetic.
- Returning a precomputed explicit literal you found at research time.

## Forbidden in this problem's final answer
Check the boxes that apply.

- [ ] Hidden numerical search (scan-until-pass)
- [ ] Root-finding (e.g. Newton, `scipy.optimize`)
- [ ] Numerical integration (quadrature to produce the value)
- [ ] Randomness (any RNG affecting the output)
- [ ] Optimization loops (gradient descent, annealing, live LP/ILP/SDP solve)
- [ ] Network access
- [ ] Subprocesses (`subprocess`, `os.system`, shelling out to a CAS)
- [ ] File I/O (loading precomputed search results from disk)
- [ ] Forbidden imports: <list, e.g. `scipy.optimize`, `ortools`, `pulp`>

## Allowed imports
<Whitelist: standard library plus any explicitly permitted packages.>

## Budgets
- Wall-clock: <e.g. 10 s>
- Memory: <e.g. 512 MB>

## Litmus test
Could the validator be fooled by a final answer that *searches* until the check
passes, instead of *constructing* the object? If yes, that style is forbidden
here. Prefer an explicit deterministic construction or literal.
