"""Field inventory extractors for the CORA standards corpus."""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence

__version__ = "0.0.0"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="cora-extract",
        description=(
            "Field inventory extractors for the CORA standards corpus. "
            "Phase 0 scaffold — no extractors implemented yet."
        ),
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"cora-extract {__version__}",
    )
    parser.parse_args(argv)
    return 0


if __name__ == "__main__":
    sys.exit(main())
