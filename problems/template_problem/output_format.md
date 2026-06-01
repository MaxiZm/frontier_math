# Output Format

> Template. Specify the exact, machine-checkable shape the candidate must emit.
> The validator checks this format first (`docs/08-sandbox-security.md`).

## Entry point
<How the validator obtains the output, e.g. a function `solve()` returning a
JSON-serializable value, or a module-level `RESULT` variable.>

```python
def solve():
    """Return the answer in the format below."""
    ...
    return result
```

## Output type & shape
<Exact type and structure. Examples:>
- A single integer.
- A high-precision real as a **decimal string** with at least N significant
  digits (return reals/bignums as strings to avoid JSON precision loss —
  `docs/08-sandbox-security.md`).
- A graph as an edge list: `{"n": int, "edges": [[u, v], ...]}` with
  `0 <= u < v < n`.
- A polynomial as a coefficient list `[a0, a1, ..., ad]`.

## Conventions
- JSON-serializable only; no `pickle`, no objects requiring custom decoding.
- Deterministic output.
- <Indexing base, ordering, normalization, units — state precisely.>

## Worked format example
```json
<a tiny, valid example of the exact output shape (not the real answer)>
```
