"""Tests for ``Inventory.enrich`` and the in-place provenance model.

See cora/docs/adr/0001-enrich-vs-merge.md for the design rationale.
"""

from __future__ import annotations

from datetime import UTC, datetime

import pytest

from cora_extractors.inventory import (
    AttributeProvenance,
    FieldEntry,
    Inventory,
    SourceClaim,
)


def _xsd_inventory(*, fields: list[FieldEntry], source_label: str = "xsd") -> Inventory:
    return Inventory(
        standard="mits",
        module="lead-management",
        version="4.0.1",
        source_artifact="lead-management.xsd",
        extractor="cora_extractors.xsd@0.0.0",
        extracted_at=datetime(2026, 5, 24, tzinfo=UTC),
        source_label=source_label,
        fields=fields,
    )


def _excel_inventory(*, fields: list[FieldEntry], source_label: str = "excel") -> Inventory:
    return Inventory(
        standard="mits",
        module="lead-management",
        version="4.0.1",
        source_artifact="lead-management.xls",
        extractor="cora_extractors.excel_multisheet@0.0.0",
        extracted_at=datetime(2026, 5, 24, tzinfo=UTC),
        source_label=source_label,
        fields=fields,
    )


def _xsd_field(**overrides: object) -> FieldEntry:
    base: dict[str, object] = {
        "path": "EventType",
        "domain": "EventType",
        "range": "xs:string",
        "cardinality": "optional",
        "definition": "EventType",  # degenerate placeholder
        "source_location": "lead-management.xsd:146",
    }
    base.update(overrides)
    return FieldEntry(**base)  # type: ignore[arg-type]


def _excel_field(**overrides: object) -> FieldEntry:
    base: dict[str, object] = {
        "path": "EventType/EventType",
        "domain": "EventType",
        "cardinality": "optional",
        "definition": "An event recorded in the lead lifecycle.",
        "source_location": "lead-management.xls!Event Type!4",
    }
    base.update(overrides)
    return FieldEntry(**base)  # type: ignore[arg-type]


# ---------------------------------------------------------------------------
# matching
# ---------------------------------------------------------------------------


def test_match_is_type_scoped_not_leaf_only() -> None:
    """Two fields sharing a leaf name in different domains must not collide."""
    xsd = _xsd_inventory(
        fields=[
            _xsd_field(
                path="PersonType/LastUpdateDate",
                domain="PersonType",
                definition="",
            ),
            _xsd_field(
                path="CompanyType/LastUpdateDate",
                domain="CompanyType",
                definition="",
            ),
        ]
    )
    excel = _excel_inventory(
        fields=[
            _excel_field(
                path="PersonType/LastUpdateDate",
                domain="PersonType",
                definition="When the person was last updated.",
            ),
        ]
    )
    merged = xsd.enrich(excel, attributes={"definition"})

    person = next(f for f in merged.fields if f.domain == "PersonType")
    company = next(f for f in merged.fields if f.domain == "CompanyType")
    assert person.definition == "When the person was last updated."
    assert company.definition == ""


def test_unmatched_other_recorded_not_appended() -> None:
    xsd = _xsd_inventory(fields=[_xsd_field()])
    excel = _excel_inventory(
        fields=[
            _excel_field(),
            _excel_field(
                path="MysteryType/MysteryField",
                domain="MysteryType",
                source_location="lead-management.xls!Mystery!7",
            ),
        ]
    )
    merged = xsd.enrich(excel, attributes={"definition"})

    assert len(merged.fields) == 1
    assert merged.unmatched_enrichments is not None
    assert len(merged.unmatched_enrichments) == 1
    record = merged.unmatched_enrichments[0]
    assert record.source == "excel"
    assert record.domain == "MysteryType"
    assert record.field == "MysteryField"
    assert record.location == "lead-management.xls!Mystery!7"


# ---------------------------------------------------------------------------
# trust list semantics
# ---------------------------------------------------------------------------


def test_trusted_attribute_other_wins() -> None:
    xsd = _xsd_inventory(fields=[_xsd_field(definition="EventType")])
    excel = _excel_inventory(
        fields=[_excel_field(definition="An event recorded in the lead lifecycle.")]
    )
    merged = xsd.enrich(excel, attributes={"definition"})
    assert merged.fields[0].definition == "An event recorded in the lead lifecycle."


def test_untrusted_attribute_self_wins_at_top_level() -> None:
    """range is NOT in the trust list; XSD's value stays, Excel's claim ignored."""
    xsd = _xsd_inventory(fields=[_xsd_field(range="AddressType")])
    excel = _excel_inventory(
        fields=[_excel_field(range="Complex", definition="postal address")]
    )
    merged = xsd.enrich(excel, attributes={"definition"})
    assert merged.fields[0].range == "AddressType"


def test_self_unattested_trusted_attribute_takes_other() -> None:
    xsd = _xsd_inventory(fields=[_xsd_field(definition="")])
    excel = _excel_inventory(fields=[_excel_field(definition="prose from excel")])
    merged = xsd.enrich(excel, attributes={"definition"})
    assert merged.fields[0].definition == "prose from excel"
    # No provenance — single source attested
    assert merged.fields[0].provenance is None


def test_self_unattested_untrusted_attribute_does_not_take_other() -> None:
    """`range` not in trust list — other's attestation is dropped at top level."""
    xsd = _xsd_inventory(fields=[_xsd_field(range=None)])
    excel = _excel_inventory(fields=[_excel_field(range="Complex")])
    merged = xsd.enrich(excel, attributes={"definition"})
    assert merged.fields[0].range is None


# ---------------------------------------------------------------------------
# provenance semantics
# ---------------------------------------------------------------------------


def test_provenance_recorded_when_multi_source_disagree_trusted() -> None:
    xsd = _xsd_inventory(fields=[_xsd_field(definition="EventType")])
    excel = _excel_inventory(fields=[_excel_field(definition="An event...")])
    merged = xsd.enrich(excel, attributes={"definition"})

    field = merged.fields[0]
    assert field.provenance is not None
    assert len(field.provenance) == 1
    prov = field.provenance[0]
    assert prov.attribute == "definition"
    assert prov.chosen == "excel"
    sources = [c.source for c in prov.claims]
    assert sources == ["xsd", "excel"]


def test_provenance_no_chosen_when_multi_source_agree() -> None:
    xsd = _xsd_inventory(fields=[_xsd_field(definition="Same words.")])
    excel = _excel_inventory(fields=[_excel_field(definition="Same words.")])
    merged = xsd.enrich(excel, attributes={"definition"})

    field = merged.fields[0]
    assert field.provenance is not None
    prov = field.provenance[0]
    assert prov.chosen is None
    assert [c.value for c in prov.claims] == ["Same words.", "Same words."]


def test_provenance_recorded_for_untrusted_disagreement_chosen_is_self() -> None:
    """Untrusted disagreement: provenance still recorded; chosen names self."""
    xsd = _xsd_inventory(fields=[_xsd_field(range="AddressType")])
    excel = _excel_inventory(fields=[_excel_field(range="Complex")])
    merged = xsd.enrich(excel, attributes={"definition"})

    field = merged.fields[0]
    assert field.provenance is not None
    # range provenance recorded because both attested
    range_prov = next(p for p in field.provenance if p.attribute == "range")
    assert range_prov.chosen == "xsd"
    assert [c.value for c in range_prov.claims] == ["AddressType", "Complex"]


def test_provenance_only_when_both_attest() -> None:
    """Single-source attestation = no provenance."""
    xsd = _xsd_inventory(fields=[_xsd_field(definition="", range=None)])
    excel = _excel_inventory(fields=[_excel_field(definition="excel only", range=None)])
    merged = xsd.enrich(excel, attributes={"definition"})

    field = merged.fields[0]
    assert field.provenance is None


def test_existing_provenance_extended_with_new_claim() -> None:
    """A second enrich on already-enriched self extends the claim list."""
    initial_claims = [
        SourceClaim(source="xsd", value="EventType", location="x.xsd:1"),
        SourceClaim(source="excel", value="excel def", location="x.xls!s!1"),
    ]
    seeded = _xsd_field(
        definition="excel def",  # excel won in the prior enrich
        provenance=[
            AttributeProvenance(
                attribute="definition", claims=initial_claims, chosen="excel"
            )
        ],
    )
    xsd = _xsd_inventory(fields=[seeded])
    pdf = _excel_inventory(
        fields=[_excel_field(definition="pdf def", source_location="x.pdf:1")],
        source_label="pdf",
    )

    merged = xsd.enrich(pdf, attributes={"definition"})

    field = merged.fields[0]
    assert field.definition == "pdf def"
    assert field.provenance is not None
    prov = field.provenance[0]
    sources = [c.source for c in prov.claims]
    assert sources == ["xsd", "excel", "pdf"]
    assert prov.chosen == "pdf"


# ---------------------------------------------------------------------------
# source_label discipline
# ---------------------------------------------------------------------------


def test_enrich_requires_source_label_on_both_sides() -> None:
    xsd = _xsd_inventory(fields=[_xsd_field()], source_label=None)  # type: ignore[arg-type]
    excel = _excel_inventory(fields=[_excel_field()])
    with pytest.raises(ValueError, match="source_label"):
        xsd.enrich(excel, attributes={"definition"})


def test_enrich_preserves_self_source_label() -> None:
    xsd = _xsd_inventory(fields=[_xsd_field()])
    excel = _excel_inventory(fields=[_excel_field()])
    merged = xsd.enrich(excel, attributes={"definition"})
    assert merged.source_label == "xsd"


# ---------------------------------------------------------------------------
# attribute discipline
# ---------------------------------------------------------------------------


def test_enrich_rejects_unknown_attributes() -> None:
    xsd = _xsd_inventory(fields=[_xsd_field()])
    excel = _excel_inventory(fields=[_excel_field()])
    with pytest.raises(ValueError, match="unknown enrich attributes"):
        xsd.enrich(excel, attributes={"bogus_attr"})


def test_enrich_rejects_structural_attributes() -> None:
    """`path`, `domain`, `cardinality`, `source_location` are not enrichable."""
    xsd = _xsd_inventory(fields=[_xsd_field()])
    excel = _excel_inventory(fields=[_excel_field()])
    for forbidden in ("path", "domain", "cardinality", "source_location", "is_reference"):
        with pytest.raises(ValueError):
            xsd.enrich(excel, attributes={forbidden})


# ---------------------------------------------------------------------------
# types[] is left untouched
# ---------------------------------------------------------------------------


def test_enrich_does_not_modify_types() -> None:
    from cora_extractors.inventory import TypeEntry

    xsd = Inventory(
        standard="mits",
        module="lead-management",
        version="4.0.1",
        source_artifact="x.xsd",
        extractor="cora_extractors.xsd@0.0.0",
        extracted_at=datetime(2026, 5, 24, tzinfo=UTC),
        source_label="xsd",
        types=[TypeEntry(name="EventType", definition="EventType")],
        fields=[_xsd_field()],
    )
    excel = _excel_inventory(fields=[_excel_field()])
    merged = xsd.enrich(excel, attributes={"definition"})

    assert merged.types == xsd.types
