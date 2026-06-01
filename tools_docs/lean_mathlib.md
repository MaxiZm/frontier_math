# Lean / mathlib

## What it's for
The Lean theorem prover and its mathematics library `mathlib`: machine-checked
formal proofs and a vast searchable corpus of formalized theorems and
definitions.

## When to use it
Per the tool router (`docs/02-tool-router.md`), use Lean/mathlib for theorem
lookup or formal checking:
- **lookup** — find the precise statement / name of a known theorem to cite in a
  proof sketch (create a theorem card from it);
- **formal checking** — discharge a proof obligation with a machine-checked term,
  or `#check` that a theorem you rely on exists with the signature you assume.

Most often you use it for **lookup**; full formalization is reserved for steps
where the skeptic demands certainty (`docs/05-proof-protocol.md`).

## How to call it
The `lean` toolchain (via `elan`/`lake`) over a project depending on `mathlib`:

```lean
import Mathlib
#check @Nat.Coprime              -- inspect a definition/theorem
example : 2 + 2 = 4 := by norm_num
```

Search mathlib via Loogle / Moogle / the theorem_search MCP server
(`mcp_servers/theorem_search/`).

## Install
Install `elan` (Lean toolchain manager), then `lake exe cache get` for a mathlib
project. Large download. Verify with `lean --version`.

> **Runner status: STUB.** The harness tool runner for Lean/mathlib raises
> `ToolUnavailable` until the Lean toolchain and a mathlib project are installed.
