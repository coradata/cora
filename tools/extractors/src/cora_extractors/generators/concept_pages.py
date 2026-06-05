"""Per-concept Markdown pages.

For each ``crosswalks/concepts/*.yaml`` emits ``concepts/<concept>.md``
showing canonical definition, aliases, the mappings table with each
mapped field's definition pulled from the resolved inventory, and a
small Mermaid graph of the concept's mappings.
"""

from __future__ import annotations

from pathlib import Path

from cora_extractors.generators._common import (
    CONFIDENCE_BADGE,
    DO_NOT_EDIT_FOOTER,
    Crosswalk,
    load_crosswalks,
    load_inventories,
    md_table,
    normalize_blanks,
    resolve_field_in_inventories,
)
from cora_extractors.inventory import Inventory


class ConceptPagesGenerator:
    """Generator adapter for per-concept Markdown pages."""

    name = "concept-pages"

    def generate(self, repo_root: Path, output_dir: Path) -> list[Path]:
        crosswalks = load_crosswalks(repo_root)
        inventories = load_inventories(repo_root)
        written: list[Path] = []
        for cw in crosswalks:
            relative = Path("concepts") / f"{cw.concept}.md"
            (output_dir / relative).parent.mkdir(parents=True, exist_ok=True)
            (output_dir / relative).write_text(normalize_blanks(_render(cw, inventories)))
            written.append(relative)
        return sorted(written)


def _render(cw: Crosswalk, inventories: dict[str, list[Inventory]]) -> str:
    parts: list[str] = []
    parts.append(f"# {cw.concept}\n")
    parts.append(_clean(cw.canonical_definition) + "\n")
    if cw.aliases:
        parts.append("**Aliases:** " + ", ".join(f"`{a}`" for a in cw.aliases) + "\n")
    parts.append(
        f"**Maintainer:** `{cw.maintainer}`  •  "
        f"**Last reviewed:** {cw.last_reviewed}\n"
    )
    if cw.boundary:
        parts.append("> ⚠ Boundary crosswalk — links to an adjacent ontology CORA does not host.\n")

    parts.append("## Mappings\n")
    parts.append(_mappings_table(cw, inventories))

    parts.append("\n## Graph\n")
    parts.append(_mermaid(cw))

    if cw.references:
        parts.append("\n## References\n")
        for r in cw.references:
            parts.append(f"- <{r}>")
        parts.append("")

    parts.append("\n" + DO_NOT_EDIT_FOOTER)
    return "\n".join(parts)


def _mappings_table(cw: Crosswalk, inventories: dict[str, list[Inventory]]) -> str:
    headers = ["Standard", "Field", "Confidence", "Definition", "Inventory"]
    rows: list[list[str]] = []
    for std in sorted(cw.mappings.keys()):
        mapping = cw.mappings[std]
        confidence = str(mapping.get("confidence", "?"))
        field = mapping.get("field")
        notes = str(mapping.get("notes") or "")
        if field is None or confidence == "not_present":
            definition = notes or "(not present)"
            rows.append(
                [
                    std.upper(),
                    "—",
                    CONFIDENCE_BADGE.get(confidence, confidence),
                    definition,
                    "—",
                ]
            )
            continue
        found = resolve_field_in_inventories(str(field), inventories.get(std, []))
        if found is None:
            definition = notes or "(field path does not resolve in any inventory)"
            inventory_cell = "—"
        else:
            inv, fe = found
            definition = fe.definition or notes or ""
            inventory_cell = f"[{inv.module}](../inventories/{std}/{inv.module}.md)"
        rows.append(
            [
                std.upper(),
                f"`{field}`",
                CONFIDENCE_BADGE.get(confidence, confidence),
                definition,
                inventory_cell,
            ]
        )
    return md_table(headers, rows)


def _mermaid(cw: Crosswalk) -> str:
    lines: list[str] = ["```mermaid", "flowchart LR"]
    concept_id = _node_id(cw.concept)
    lines.append(f'  {concept_id}["{cw.concept}"]')
    for std in sorted(cw.mappings.keys()):
        mapping = cw.mappings[std]
        confidence = str(mapping.get("confidence", "?"))
        field = mapping.get("field")
        label = field if field else "(not present)"
        target_id = f"{std}_{_node_id(cw.concept)}"
        lines.append(f'  {target_id}["{std.upper()}<br/>{label}"]')
        lines.append(f"  {concept_id} -- {confidence} --> {target_id}")
    lines.append("```")
    return "\n".join(lines) + "\n"


def _node_id(s: str) -> str:
    """Sanitise to a Mermaid-safe identifier."""
    return "".join(c if c.isalnum() else "_" for c in s)


def _clean(text: str) -> str:
    """Collapse whitespace in a YAML block-folded definition."""
    return " ".join(text.split())
