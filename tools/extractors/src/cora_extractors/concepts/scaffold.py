"""Generate a draft ``crosswalks/concepts/<name>.yaml`` from a cluster.

The editorial pass that turns a Phase 6a string-match cluster or Phase 6c
semantic-match cluster into a committed crosswalk involves three classes
of decision:

1. **Mechanical**: the per-standard ``field:`` paths, the standard
   versions, the source-url links. These come straight from the cluster.
2. **Editorial**: the canonical name, the canonical_definition, the
   confidence label per mapping, narrative notes for ``divergent`` /
   ``not_present`` / ``partial``.
3. **Reviewer-supplied**: any aliases the reviewer knows about.

This module handles (1) — emits a YAML file with the mechanical pieces
filled in and the editorial fields marked ``TODO`` so the maintainer can
fill them in by hand. The output validates against the JSON Schema only
after the TODOs are resolved.
"""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Sequence
from datetime import date
from pathlib import Path

from cora_extractors.concepts.census import CensusRow

CROSSWALK_DIR = Path("crosswalks/concepts")
INVENTORY_REPO_BASE = (
    "https://github.com/coradata/cora/blob/main/standards/{standard}/current/inventory/{module}.yaml"
)


def scaffold_crosswalk(
    name: str,
    rows: Sequence[CensusRow],
    *,
    standards_present: Sequence[str],
    all_standards: Sequence[str],
    today: date | None = None,
) -> str:
    """Render a draft crosswalk YAML for a cluster.

    Args:
        name: canonical concept name (lowercase snake_case).
        rows: every CensusRow in the cluster (typically across two or
            three standards, multiple modules per standard).
        standards_present: which standards have a path to map (e.g.,
            ``("ibpdi", "mits")``).
        all_standards: every participating standard in the corpus (e.g.,
            ``("ibpdi", "mits", "redi")``). Standards in this set but
            not in ``standards_present`` are scaffolded as ``not_present``
            with a TODO note.
        today: override for the ``last_reviewed`` date (test seam).
    """
    today_str = (today or date.today()).isoformat()

    by_standard: dict[str, list[CensusRow]] = defaultdict(list)
    for r in rows:
        by_standard[r.standard].append(r)

    lines: list[str] = []
    lines.append(f"concept: {name}")
    lines.append("canonical_definition: >-")
    lines.append("  TODO — write the canonical definition. One or two sentences naming")
    lines.append("  what the concept IS and how a consumer should read it.")
    lines.append("aliases: []  # TODO — add any alternative names this concept is known by")
    lines.append("maintainer: '@coradata/maintainers'")
    lines.append(f"last_reviewed: '{today_str}'")
    lines.append("mappings:")
    for standard in all_standards:
        present_rows = by_standard.get(standard, [])
        if present_rows:
            chosen = _pick_canonical_row(present_rows)
            lines.append(f"  {standard}:")
            lines.append(f"    field: {chosen.path}")
            lines.append(f"    version: 'TODO  # confirm against {chosen.module}.yaml'")
            lines.append("    confidence: TODO  # exact | close | partial | divergent")
            lines.append(
                "    source_url: "
                + INVENTORY_REPO_BASE.format(standard=standard, module=chosen.module)
            )
            if len(present_rows) > 1:
                others = [r for r in present_rows if r is not chosen]
                extra_paths = ", ".join(
                    sorted({f"{r.module}:{r.path}" for r in others})
                )
                lines.append(
                    f"    notes: >-  # TODO — see also {extra_paths}"
                )
        else:
            lines.append(f"  {standard}:")
            lines.append("    field: null")
            lines.append("    version: '1.0'")
            lines.append("    confidence: not_present")
            lines.append("    notes: >-")
            lines.append(
                f"      TODO — narrative explaining why {standard.upper()} does not "
                f"carry this concept."
            )
    return "\n".join(lines) + "\n"


def write_scaffold(
    name: str,
    rows: Sequence[CensusRow],
    *,
    standards_present: Sequence[str],
    all_standards: Sequence[str],
    repo_root: Path,
    today: date | None = None,
) -> Path:
    """Write the scaffolded YAML to ``crosswalks/concepts/<name>.yaml``.

    Raises FileExistsError if the file already exists — scaffolding over
    a committed crosswalk would silently lose the editorial work.
    """
    out = repo_root / CROSSWALK_DIR / f"{name}.yaml"
    if out.exists():
        raise FileExistsError(
            f"{out} already exists. Pick a new concept name or remove the existing file."
        )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(
        scaffold_crosswalk(
            name,
            rows,
            standards_present=standards_present,
            all_standards=all_standards,
            today=today,
        )
    )
    return out


def _pick_canonical_row(rows: Sequence[CensusRow]) -> CensusRow:
    """When a standard has multiple paths in the same cluster, pick the
    one with the longest non-empty definition (likely the most informative
    source); tie-break by module name alphabetically."""
    sorted_rows = sorted(
        rows,
        key=lambda r: (-len(r.definition or ""), r.module, r.path),
    )
    return sorted_rows[0]
