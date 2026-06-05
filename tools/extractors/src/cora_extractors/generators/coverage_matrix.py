"""Coverage-matrix generator.

Emits a single Markdown file with a concepts × standards table. Each cell
shows the mapping confidence (with an emoji badge for at-a-glance reading).
Sorted alphabetically by concept.
"""

from __future__ import annotations

from pathlib import Path

from cora_extractors.generators._common import (
    CONFIDENCE_BADGE,
    DO_NOT_EDIT_FOOTER,
    load_crosswalks,
    md_table,
    standards_in,
)

OUTPUT_PATH = Path("coverage-matrix.md")


class CoverageMatrixGenerator:
    """Generator adapter for the coverage matrix."""

    name = "coverage-matrix"

    def generate(self, repo_root: Path, output_dir: Path) -> list[Path]:
        crosswalks = load_crosswalks(repo_root)
        if not crosswalks:
            return []
        standards = standards_in(crosswalks)
        headers = ["Concept", *(s.upper() for s in standards)]
        rows: list[list[str]] = []
        for cw in sorted(crosswalks, key=lambda c: c.concept):
            row = [f"[{cw.concept}](concepts/{cw.concept}.md)"]
            for std in standards:
                mapping = cw.mappings.get(std)
                row.append(_cell(mapping))
            rows.append(row)

        body = (
            "# Crosswalk Coverage Matrix\n\n"
            f"{len(crosswalks)} concepts across {len(standards)} hosted "
            f"standards ({', '.join(s.upper() for s in standards)}).\n\n"
            + md_table(headers, rows)
            + "\n"
            + DO_NOT_EDIT_FOOTER
        )

        out = output_dir / OUTPUT_PATH
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(body)
        return [OUTPUT_PATH]


def _cell(mapping: dict[str, object] | None) -> str:
    if mapping is None:
        return "—"
    confidence = str(mapping.get("confidence", "?"))
    return CONFIDENCE_BADGE.get(confidence, confidence)
