# GAP

## What it's for
A system for computational discrete algebra, especially **group theory**: finite
groups, their representations, actions, and symmetric/combinatorial structures.

## When to use it
Per the tool router (`docs/02-tool-router.md`), use GAP for:
- finite groups,
- group actions,
- designs involving symmetry.

Use it when a construction's structure is governed by a group (automorphism
groups, orbits, transitive actions, symmetric designs).

## How to call it
The `gap` interpreter (or via Sage's GAP interface):

```gap
G := SymmetricGroup(5);;
Order(G);                      # 120
cc := ConjugacyClasses(G);;
o := Orbits(G, [1..5]);;       # group action on a set
```

## Install
External binary `gap`. Install from your OS package manager or the GAP
distribution. Verify with `gap --version`.

> **Runner status: STUB.** The harness tool runner for GAP raises
> `ToolUnavailable` until the `gap` binary is installed and on `PATH`.
