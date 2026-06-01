#!/usr/bin/env python3
"""build_embeddings: documented stub.

This pipeline is intentionally not implemented in the initial scaffold. It would
build embeddings using the schemas under paper_index/schema/ and the MCP servers under
mcp_servers/. No private benchmark data is bundled (see docs/11-evaluation-integrity.md).
"""
import sys


def main() -> int:
    print(
        "build_embeddings is a stub. See docs/ and mcp_servers/ for the intended pipeline. "
        "Implement me before use.",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
