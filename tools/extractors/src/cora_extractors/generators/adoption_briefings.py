"""Adoption-briefing generator.

For every *ordered* pair of hosted standards (home → adopting), emits a
Markdown briefing for a consumer who already reports in ``home`` and is
taking on ``adopting``. The briefing is a pure projection of the committed
crosswalks — it partitions concepts into:

- **Recognise but reconcile** — present in both standards. Rows where either
  side is ``partial``/``divergent`` are promoted to the top with the mapping
  ``notes`` surfaced, because "looks equal but isn't" is the costly case.
- **New territory** — present in ``adopting`` but absent from ``home``.
- **Stays home** — present in ``home`` but absent from ``adopting``.

Direction matters: home→adopting and adopting→home share the reconcile set
but swap the new/stays-home partitions.

Output: ``adoption/<home>-to-<adopting>.md`` per ordered pair, plus an
``adoption/README.md`` index. Committed build product like the rest of
``docs/generated/``; drift-gated by ``cora docs check``.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations
from pathlib import Path

from cora_extractors.generators._common import (
    CONFIDENCE_BADGE,
    DO_NOT_EDIT_FOOTER,
    Crosswalk,
    load_crosswalks,
    md_table,
    normalize_blanks,
    standards_in,
)

OUTPUT_DIR = Path("adoption")

# Confidence values that mean "this standard does not usefully carry the
# concept" — i.e. not part of either side of a bridge.
_ABSENT = {None, "not_present"}

# Confidence values where the concept exists on both sides but the mapping
# carries a meaningful caveat the adopter must reconcile.
_HAZARD = {"partial", "divergent"}

# Stable cross-tree links (the generated tree and the authored site live in
# different directories, so absolute blob URLs are more robust than relative
# paths across that boundary).
_SUGGESTIONS_URL = (
    "https://github.com/coradata/cora/blob/main/docs/concepts-analysis/suggestions.md"
)
_REQUEST_URL = (
    "https://github.com/coradata/cora/blob/main/docs/site/docs/requesting-a-crosswalk.md"
)


def _confidence(cw: Crosswalk, std: str) -> str | None:
    mapping = cw.mappings.get(std)
    if not mapping:
        return None
    conf = mapping.get("confidence")
    return str(conf) if conf is not None else None


def _present(cw: Crosswalk, std: str) -> bool:
    return _confidence(cw, std) not in _ABSENT


def _is_hazard(cw: Crosswalk, home: str, adopting: str) -> bool:
    return _confidence(cw, home) in _HAZARD or _confidence(cw, adopting) in _HAZARD


@dataclass(frozen=True)
class Partition:
    """The three buckets for one ordered (home → adopting) pair."""

    reconcile: list[Crosswalk]
    new: list[Crosswalk]
    stays_home: list[Crosswalk]


def partition(home: str, adopting: str, crosswalks: list[Crosswalk]) -> Partition:
    """Classify each crosswalk for an ordered (home → adopting) adoption.

    - reconcile: present in both
    - new: present in adopting, absent from home
    - stays_home: present in home, absent from adopting
    (absent from both is skipped)
    """
    reconcile: list[Crosswalk] = []
    new: list[Crosswalk] = []
    stays_home: list[Crosswalk] = []
    for cw in sorted(crosswalks, key=lambda c: c.concept):
        in_home = _present(cw, home)
        in_adopting = _present(cw, adopting)
        if in_home and in_adopting:
            reconcile.append(cw)
        elif in_adopting and not in_home:
            new.append(cw)
        elif in_home and not in_adopting:
            stays_home.append(cw)
    return Partition(reconcile, new, stays_home)


def _field_cell(cw: Crosswalk, std: str) -> str:
    mapping = cw.mappings.get(std) or {}
    field = mapping.get("field") or "—"
    conf = str(mapping.get("confidence", "?"))
    badge = CONFIDENCE_BADGE.get(conf, conf)
    return f"`{field}` · {badge}"


def _hazard_note(cw: Crosswalk, home: str, adopting: str) -> str:
    notes: list[str] = []
    for std in (home, adopting):
        mapping = cw.mappings.get(std) or {}
        if mapping.get("confidence") in _HAZARD and mapping.get("notes"):
            notes.append(f"**{std.upper()}:** {mapping['notes']}")
    return " ".join(notes)


def render_briefing(home: str, adopting: str, crosswalks: list[Crosswalk]) -> str:
    """Render one ordered-pair briefing to Markdown (also used by the CLI)."""
    p = partition(home, adopting, crosswalks)
    H, A = home.upper(), adopting.upper()

    parts: list[str] = [
        f"# Adopting {A} when you report in {H}\n",
        (
            f"You already report in **{H}**. You're taking on **{A}**. "
            "This briefing is generated from CORA's crosswalks: what you'll "
            "recognise, what's genuinely new, and — most importantly — where "
            f"the two standards look equal but aren't.\n"
        ),
        (
            f"- **{len(p.reconcile)}** concepts appear in both — recognise, "
            "but reconcile the caveats.\n"
            f"- **{len(p.new)}** are new territory {A} carries that {H} never modelled.\n"
            f"- **{len(p.stays_home)}** stay home — {H} concepts {A} won't carry.\n"
        ),
    ]

    # ① Recognise but reconcile — hazard rows first.
    parts.append(f"## ① Recognise, but reconcile ({len(p.reconcile)})\n")
    if p.reconcile:
        parts.append(
            "Concepts both standards model. Rows flagged ⚠️ carry a "
            "`partial`/`divergent` mapping — the values look comparable but "
            "differ in scope or grain. Read the note before joining them.\n"
        )
        ordered = sorted(
            p.reconcile,
            key=lambda c: (not _is_hazard(c, home, adopting), c.concept),
        )
        rows: list[list[str]] = []
        for cw in ordered:
            hazard = _is_hazard(cw, home, adopting)
            concept = f"⚠️ {cw.concept}" if hazard else cw.concept
            rows.append(
                [
                    concept,
                    _field_cell(cw, home),
                    _field_cell(cw, adopting),
                    _hazard_note(cw, home, adopting) if hazard else "",
                ]
            )
        parts.append(md_table(["Concept", H, A, "Watch out"], rows))
    else:
        parts.append("_No concepts are mapped in both standards yet._\n")

    # ② New territory.
    parts.append(f"## ② New territory ({len(p.new)})\n")
    if p.new:
        parts.append(
            f"Concepts {A} carries that {H} never modelled — data you'll be "
            "handling for the first time.\n"
        )
        rows = [
            [cw.concept, _field_cell(cw, adopting), cw.canonical_definition]
            for cw in p.new
        ]
        parts.append(md_table(["Concept", A, "What it means"], rows))
    else:
        parts.append(f"_{A} introduces no concepts {H} lacks (in the current corpus)._\n")

    # ③ Stays home.
    parts.append(f"## ③ Stays home ({len(p.stays_home)})\n")
    if p.stays_home:
        parts.append(f"Your {H} concepts {A} won't carry — they remain yours to report.\n")
        for cw in p.stays_home:
            parts.append(f"- {cw.concept} (`{(cw.mappings.get(home) or {}).get('field') or '—'}`)")
        parts.append("")
    else:
        parts.append(f"_Every {H} concept also appears in {A} (in the current corpus)._\n")

    # ④ Coverage honesty.
    parts.append("## ④ Coverage and what's missing\n")
    parts.append(
        f"CORA maps **{len(p.reconcile)}** concept(s) across both {H} and {A} "
        "today. Coverage is partial and grows with the editorial corpus — this "
        "briefing reflects only what's mapped, not everything the journey needs. "
        f"For candidate concepts not yet covered, see the "
        f"[suggestions report]({_SUGGESTIONS_URL}); to ask for one, "
        f"[request a crosswalk]({_REQUEST_URL}).\n"
    )

    parts.append(DO_NOT_EDIT_FOOTER)
    return normalize_blanks("\n".join(parts))


class AdoptionBriefingGenerator:
    """Generator adapter for per-ordered-pair adoption briefings."""

    name = "adoption-briefings"

    def generate(self, repo_root: Path, output_dir: Path) -> list[Path]:
        crosswalks = load_crosswalks(repo_root)
        if not crosswalks:
            return []
        standards = standards_in(crosswalks)
        if len(standards) < 2:
            return []

        out_dir = output_dir / OUTPUT_DIR
        out_dir.mkdir(parents=True, exist_ok=True)
        written: list[Path] = []

        index_rows: list[list[str]] = []
        for home, adopting in permutations(standards, 2):
            p = partition(home, adopting, crosswalks)
            rel = OUTPUT_DIR / f"{home}-to-{adopting}.md"
            (output_dir / rel).write_text(render_briefing(home, adopting, crosswalks))
            written.append(rel)
            index_rows.append(
                [
                    f"[{home.upper()} → {adopting.upper()}]({home}-to-{adopting}.md)",
                    str(len(p.reconcile)),
                    str(len(p.new)),
                    str(len(p.stays_home)),
                ]
            )

        index_body = normalize_blanks(
            "# Adoption briefings\n\n"
            "Directional guides for a consumer who already reports in one hosted "
            "standard and is adopting another. Each briefing partitions concepts "
            "into recognise-but-reconcile, new territory, and stays-home — "
            "generated from the crosswalk corpus.\n\n"
            + md_table(
                ["Adoption path", "Reconcile", "New", "Stays home"],
                index_rows,
            )
            + "\n"
            + DO_NOT_EDIT_FOOTER
        )
        index_rel = OUTPUT_DIR / "README.md"
        (output_dir / index_rel).write_text(index_body)
        written.append(index_rel)

        return written
