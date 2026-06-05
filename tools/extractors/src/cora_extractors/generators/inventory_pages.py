"""Per-inventory browse pages.

For each committed ``standards/<std>/current/inventory/<module>.yaml``
emits ``inventories/<std>/<module>.md`` with:

- Metadata (source artifact, version, extractor, source_label, counts).
- A types table (when ``types[]`` is non-empty).
- A fields table sorted by path.

Tables are static Markdown (GitHub renders without JS sort). For large
inventories use browser find.
"""

from __future__ import annotations

from pathlib import Path

from cora_extractors.generators._common import (
    DO_NOT_EDIT_FOOTER,
    load_inventories,
    md_table,
    normalize_blanks,
)
from cora_extractors.inventory import Inventory


class InventoryPagesGenerator:
    """Generator adapter for per-inventory browse pages."""

    name = "inventory-pages"

    def generate(self, repo_root: Path, output_dir: Path) -> list[Path]:
        grouped = load_inventories(repo_root)
        written: list[Path] = []
        for std, invs in grouped.items():
            for inv in invs:
                relative = Path("inventories") / std / f"{inv.module}.md"
                (output_dir / relative).parent.mkdir(parents=True, exist_ok=True)
                (output_dir / relative).write_text(normalize_blanks(_render(inv, std)))
                written.append(relative)
        return sorted(written)


def _render(inv: Inventory, std: str) -> str:
    parts: list[str] = []
    parts.append(f"# {std.upper()} / {inv.module}\n")

    meta_rows: list[list[str]] = [
        ["Source artifact", f"`{inv.source_artifact}`"],
        ["Version", inv.version],
        ["Extractor", f"`{inv.extractor}`"],
    ]
    if inv.source_label:
        meta_rows.append(["Source label", f"`{inv.source_label}`"])
    if inv.namespace_hint:
        meta_rows.append(["Namespace hint", f"`{inv.namespace_hint}`"])
    meta_rows.append(["Types", str(len(inv.types))])
    meta_rows.append(["Fields", str(len(inv.fields))])
    if inv.unmatched_enrichments:
        meta_rows.append(["Unmatched enrichments", str(len(inv.unmatched_enrichments))])

    parts.append(md_table(["Key", "Value"], meta_rows))

    if inv.types:
        parts.append("\n## Types\n")
        parts.append(
            md_table(
                ["Name", "Extends", "Abstract", "Definition"],
                [
                    [
                        t.name,
                        t.extends or "",
                        "✓" if t.abstract else "",
                        (t.definition or "").strip(),
                    ]
                    for t in sorted(inv.types, key=lambda t: t.name)
                ],
            )
        )

    parts.append("\n## Fields\n")
    parts.append(
        md_table(
            ["Path", "Domain", "Range", "Cardinality", "Definition"],
            [
                [
                    f.path,
                    f.domain or "",
                    f.range or "",
                    f.cardinality,
                    (f.definition or "").strip(),
                ]
                for f in sorted(inv.fields, key=lambda f: f.path)
            ],
        )
    )

    parts.append("\n" + DO_NOT_EDIT_FOOTER)
    return "\n".join(parts)
