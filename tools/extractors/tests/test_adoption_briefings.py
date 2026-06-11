"""Tests for the adoption-briefing generator.

Strategy: build a tiny in-memory crosswalk set covering every partition
case (bridge / new / stays-home / both-absent / hazard), exercise the pure
``partition`` helper directly, then stage a fixture repo and run the
generator for the full ordered-pair sweep + determinism.
"""

from __future__ import annotations

import textwrap
from pathlib import Path

from cora_extractors.generator import Generator
from cora_extractors.generators._common import Crosswalk
from cora_extractors.generators.adoption_briefings import (
    AdoptionBriefingGenerator,
    partition,
    render_briefing,
)


def _cw(concept: str, mappings: dict[str, dict[str, object]]) -> Crosswalk:
    return Crosswalk(
        path=Path(f"{concept}.yaml"),
        concept=concept,
        canonical_definition=f"Definition of {concept}.",
        aliases=[],
        boundary=False,
        mappings=mappings,
        maintainer="@coradata/maintainers",
        last_reviewed="2026-06-11",
        references=[],
    )


# One crosswalk per partition case, home=redi adopting=mits.
CROSSWALKS = [
    # present in both, clean -> reconcile (non-hazard)
    _cw("city", {"redi": {"field": "City", "confidence": "exact"},
                 "mits": {"field": "AddressType/City", "confidence": "exact"}}),
    # present in both, divergent on redi -> reconcile (hazard, note surfaced)
    _cw("rent_amount", {"redi": {"field": "Contract_Rent_Qtr", "confidence": "divergent",
                                 "notes": "Quarterly aggregate, not per-lease."},
                        "mits": {"field": "UnitType/UnitRent", "confidence": "close"}}),
    # present in mits, not_present in redi -> new territory
    _cw("move_in_date", {"redi": {"field": None, "confidence": "not_present",
                                  "notes": "REDI is fund-level."},
                         "mits": {"field": "LeaseType/ActualMoveIn", "confidence": "close"}}),
    # present in mits, redi mapping entirely absent -> new territory
    _cw("unit_id", {"mits": {"field": "UnitType/UnitID", "confidence": "close"}}),
    # present in redi, not_present in mits -> stays home
    _cw("discount_rate", {"redi": {"field": "Discount_Rate", "confidence": "exact"},
                          "mits": {"field": None, "confidence": "not_present",
                                   "notes": "MITS is operational."}}),
    # absent from both -> skipped entirely
    _cw("only_ibpdi", {"ibpdi": {"field": "X/Y", "confidence": "exact"}}),
]


def test_partition_classifies_every_case() -> None:
    p = partition("redi", "mits", CROSSWALKS)
    assert [c.concept for c in p.reconcile] == ["city", "rent_amount"]
    assert [c.concept for c in p.new] == ["move_in_date", "unit_id"]
    assert [c.concept for c in p.stays_home] == ["discount_rate"]
    # only_ibpdi appears in no bucket (absent from both redi and mits)
    everywhere = {c.concept for c in p.reconcile + p.new + p.stays_home}
    assert "only_ibpdi" not in everywhere


def test_partition_is_directional() -> None:
    forward = partition("redi", "mits", CROSSWALKS)
    reverse = partition("mits", "redi", CROSSWALKS)
    # reconcile set is symmetric; new and stays-home swap.
    assert {c.concept for c in forward.reconcile} == {c.concept for c in reverse.reconcile}
    assert {c.concept for c in forward.new} == {c.concept for c in reverse.stays_home}
    assert {c.concept for c in forward.stays_home} == {c.concept for c in reverse.new}


def test_render_promotes_hazard_and_surfaces_notes() -> None:
    body = render_briefing("redi", "mits", CROSSWALKS)
    assert "# Adopting MITS when you report in REDI" in body
    # hazard concept is flagged and its note is surfaced
    assert "⚠️ rent_amount" in body
    assert "Quarterly aggregate, not per-lease." in body
    # hazard row precedes the clean reconcile row (city)
    assert body.index("rent_amount") < body.index("| city |")
    # new-territory and stays-home sections present
    assert "## ② New territory (2)" in body
    assert "## ③ Stays home (1)" in body


def _stage_repo(tmp_path: Path) -> Path:
    repo = tmp_path / "repo"
    cw_dir = repo / "crosswalks" / "concepts"
    cw_dir.mkdir(parents=True)
    (cw_dir / "city.yaml").write_text(
        textwrap.dedent(
            """\
            concept: city
            canonical_definition: The city or town of an address.
            maintainer: '@coradata/maintainers'
            last_reviewed: '2026-06-11'
            mappings:
              redi:
                field: City
                confidence: exact
              mits:
                field: AddressType/City
                confidence: exact
            """
        )
    )
    (cw_dir / "move_in_date.yaml").write_text(
        textwrap.dedent(
            """\
            concept: move_in_date
            canonical_definition: Observed occupancy date.
            maintainer: '@coradata/maintainers'
            last_reviewed: '2026-06-11'
            mappings:
              redi:
                field: null
                confidence: not_present
                notes: REDI is fund-level.
              mits:
                field: LeaseType/ActualMoveIn
                confidence: close
            """
        )
    )
    return repo


def test_generator_emits_ordered_pairs_and_index(tmp_path: Path) -> None:
    repo = _stage_repo(tmp_path)
    out = tmp_path / "out"
    paths = AdoptionBriefingGenerator().generate(repo, out)
    names = {str(p) for p in paths}
    # two standards (redi, mits) -> 2 ordered pairs + index
    assert names == {
        "adoption/redi-to-mits.md",
        "adoption/mits-to-redi.md",
        "adoption/README.md",
    }
    index = (out / "adoption" / "README.md").read_text()
    assert "# Adoption briefings" in index
    assert "REDI → MITS" in index


def test_generator_is_a_protocol_member_and_deterministic(tmp_path: Path) -> None:
    gen = AdoptionBriefingGenerator()
    assert isinstance(gen, Generator)
    assert gen.name == "adoption-briefings"
    repo = _stage_repo(tmp_path)
    a, b = tmp_path / "a", tmp_path / "b"
    gen.generate(repo, a)
    gen.generate(repo, b)
    for rel in ["adoption/redi-to-mits.md", "adoption/mits-to-redi.md", "adoption/README.md"]:
        assert (a / rel).read_text() == (b / rel).read_text()


def test_generator_emits_nothing_below_two_standards(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    cw_dir = repo / "crosswalks" / "concepts"
    cw_dir.mkdir(parents=True)
    (cw_dir / "city.yaml").write_text(
        textwrap.dedent(
            """\
            concept: city
            canonical_definition: The city or town of an address.
            maintainer: '@coradata/maintainers'
            last_reviewed: '2026-06-11'
            mappings:
              redi:
                field: City
                confidence: exact
            """
        )
    )
    assert AdoptionBriefingGenerator().generate(repo, tmp_path / "out") == []
