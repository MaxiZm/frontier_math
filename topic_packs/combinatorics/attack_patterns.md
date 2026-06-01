# Attack Patterns: Combinatorics

A playbook mapping problem shapes to methods and tools. Use these at ladder rungs
P5–P10 (`docs/03-task-ladder-protocol.md`).

- **"Count the number of …"** → compute small cases by brute force (Sage / plain
  Python), feed the sequence to **OEIS** (`tools_docs/oeis.md`), then prove the
  identified formula via a bijection, recurrence, or generating function.

- **"Show there exists an object with property P"** → try the **probabilistic
  method**: bound the expected number of violations; if `< 1`, a good object
  exists. If violations are rare and weakly dependent, use the **Lovász Local
  Lemma**.

- **"Largest/smallest family avoiding a pattern"** → reach for **extremal set
  theory** (Sperner, Erdős–Ko–Rado) or **double counting**; conjecture the
  extremal family from small cases, then prove the bound and exhibit a matching
  construction.

- **"Some two of these must …"** → **pigeonhole**. Identify the boxes and items.

- **"How many objects avoid all of these bad properties"** → **inclusion–
  exclusion** / sieve.

- **Sumset / `Z/p` size question** → **Cauchy–Davenport** and additive
  combinatorics; test small primes computationally first.

- **Existence of a finite configuration with hard constraints** → encode as
  **SAT / Z3** (`tools_docs/z3.md`); a model is the construction, `UNSAT` is a
  non-existence proof. Convert any found object to an explicit final candidate.

- **Symmetry in the structure** → look for a governing **group action** and use
  **GAP** (`tools_docs/gap.md`); count orbits with Burnside / Pólya.

- **Recurrence suspected but unknown** → fit a linear recurrence to computed
  terms (Sage `guess`, or solve a linear system), then verify and prove.

When 3 attempts on a rung fail, relax one constraint (smaller `n`, drop one
condition) per the *k*−0.5 fallback and extract a lemma before retrying.
