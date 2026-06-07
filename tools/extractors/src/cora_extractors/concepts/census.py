"""Field-level census across every committed inventory.

One row per leaf field. Deterministic sort by ``(standard, module, path)``
so the CSV and Markdown outputs are diff-stable across runs.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from cora_extractors.inventory import Inventory

INVENTORY_GLOB = "standards/*/current/inventory/*.yaml"


@dataclass(frozen=True)
class CensusRow:
    """One row per leaf field in the committed corpus."""

    standard: str
    module: str
    type_name: str
    path: str
    leaf_name: str
    range: str
    cardinality: str
    definition: str


def collect_census(repo_root: Path) -> list[CensusRow]:
    """Walk every committed inventory and emit one row per leaf field."""
    rows: list[CensusRow] = []
    for inv_path in sorted(repo_root.glob(INVENTORY_GLOB)):
        inv = Inventory.from_yaml(inv_path)
        for field in inv.fields:
            rows.append(
                CensusRow(
                    standard=inv.standard,
                    module=inv.module,
                    type_name=field.domain or "",
                    path=field.path,
                    leaf_name=_leaf_name(field.path),
                    range=field.range or "",
                    cardinality=field.cardinality,
                    definition=field.definition or "",
                )
            )
    rows.sort(key=lambda r: (r.standard, r.module, r.path))
    return rows


def _leaf_name(path: str) -> str:
    """The last segment of a CORA inventory path."""
    return path.rsplit("/", 1)[-1]
