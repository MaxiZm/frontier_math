#!/usr/bin/env python3
"""import_horizonmath: documented stub.

This pipeline is intentionally not implemented in the initial scaffold. It would
import horizonmath using the schemas under paper_index/schema/ and the MCP servers under
mcp_servers/. No private benchmark data is bundled (see docs/11-evaluation-integrity.md).
"""
import sys


def main() -> int:
    print(
        "import_horizonmath is a stub. See docs/ and mcp_servers/ for the intended pipeline. "
        "Implement me before use.",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
