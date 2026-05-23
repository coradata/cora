"""``cora inventory summary`` reader.

A small reader that consumes the OWL-aware fields of an Inventory and
prints a compact summary. The point isn't the summary itself — it's that
the OWL-aware schema fields (``types[]``, ``domain``, ``range``,
``is_reference``) have a real consumer from day one, so they don't rot
silently before the future OWL derivation phase arrives.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from cora_extractors.inventory import Inventory


@dataclass(frozen=True)
class InventorySummary:
    standard: str
    module: str
    class_count: int
    property_count: int
    datatype_property_count: int
    object_property_count: int
    fields_without_domain: int
    max_inheritance_depth: int

    def render(self) -> str:
        ratio: float | None = None
        if self.property_count:
            ratio = self.datatype_property_count / self.property_count
        ratio_text = "n/a" if ratio is None else f"{ratio:.2f}"
        return (
            f"{self.standard}/{self.module}\n"
            f"  classes:                {self.class_count}\n"
            f"  properties:             {self.property_count} "
            f"(datatype={self.datatype_property_count}, "
            f"object={self.object_property_count}, "
            f"datatype/total={ratio_text})\n"
            f"  fields without domain:  {self.fields_without_domain}\n"
            f"  max inheritance depth:  {self.max_inheritance_depth}"
        )


def summarize(inventory: Inventory) -> InventorySummary:
    object_count = sum(1 for f in inventory.fields if f.is_reference)
    datatype_count = len(inventory.fields) - object_count
    no_domain = sum(1 for f in inventory.fields if f.domain is None)
    return InventorySummary(
        standard=inventory.standard,
        module=inventory.module,
        class_count=len(inventory.types),
        property_count=len(inventory.fields),
        datatype_property_count=datatype_count,
        object_property_count=object_count,
        fields_without_domain=no_domain,
        max_inheritance_depth=_max_inheritance_depth(inventory),
    )


def _max_inheritance_depth(inventory: Inventory) -> int:
    by_name = {t.name: t for t in inventory.types}
    cache: dict[str, int] = {}

    def depth(name: str) -> int:
        if name in cache:
            return cache[name]
        t = by_name.get(name)
        if t is None or t.extends is None or t.extends not in by_name:
            cache[name] = 0
            return 0
        cache[name] = 1 + depth(t.extends)
        return cache[name]

    return max((depth(t.name) for t in inventory.types), default=0)


def summarize_file(path: Path) -> InventorySummary:
    return summarize(Inventory.from_yaml(path))
