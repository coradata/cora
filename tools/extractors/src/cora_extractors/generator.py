"""Generator seam.

A Generator reads committed inventories + crosswalks and emits browseable
artifacts (Markdown, Mermaid, etc.) into ``output_dir``. Adapters at this
seam are the third pattern alongside ``Extractor`` and ``Validator``:
extractors produce data, validators check it, generators present it.

Output is treated as build product — committed to the repo so reviewers
diff it, but never edited by hand. The CI ``cora docs check`` step
regenerates into a temp dir and fails if the result differs from what's
committed.
"""

from __future__ import annotations

from pathlib import Path
from typing import Protocol, runtime_checkable


@runtime_checkable
class Generator(Protocol):
    """A named docs-output adapter at the Generator seam."""

    name: str

    def generate(self, repo_root: Path, output_dir: Path) -> list[Path]:
        """Read committed artifacts under ``repo_root`` and emit files into
        ``output_dir``. Return the list of paths written (relative to
        ``output_dir``).
        """
        ...
