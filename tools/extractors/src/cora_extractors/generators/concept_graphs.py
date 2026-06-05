"""Concept overview generator.

A single Markdown page (``concept-overview.md``) with one Mermaid graph
showing every committed concept and its mappings across standards.
Edges are labelled with confidence so the at-a-glance view distinguishes
``exact`` from ``partial`` / ``not_present``.
"""

from __future__ import annotations

from pathlib import Path

from cora_extractors.generators._common import (
    DO_NOT_EDIT_FOOTER,
    load_crosswalks,
)

OUTPUT_PATH = Path("concept-overview.md")


class ConceptGraphsGenerator:
    """Generator adapter for the cross-concept overview graph."""

    name = "concept-graphs"

    def generate(self, repo_root: Path, output_dir: Path) -> list[Path]:
        crosswalks = load_crosswalks(repo_root)
        if not crosswalks:
            return []

        lines: list[str] = ["# Concept Overview\n"]
        lines.append(
            f"All {len(crosswalks)} committed concepts and their mappings across "
            "hosted standards. Edge label = mapping confidence.\n"
        )
        lines.append("```mermaid")
        lines.append("flowchart LR")

        standards: set[str] = set()
        for cw in crosswalks:
            standards.update(cw.mappings.keys())
        for std in sorted(standards):
            lines.append(f'  {std}[("{std.upper()}")]')

        for cw in sorted(crosswalks, key=lambda c: c.concept):
            concept_id = _node_id(cw.concept)
            lines.append(f'  {concept_id}["{cw.concept}"]')
            for std in sorted(cw.mappings.keys()):
                confidence = str(cw.mappings[std].get("confidence", "?"))
                lines.append(f"  {concept_id} -- {confidence} --> {std}")

        lines.append("```\n")
        lines.append(DO_NOT_EDIT_FOOTER)

        body = "\n".join(lines)
        out = output_dir / OUTPUT_PATH
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(body)
        return [OUTPUT_PATH]


def _node_id(s: str) -> str:
    return "".join(c if c.isalnum() else "_" for c in s)
