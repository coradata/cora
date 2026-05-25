"""Typed in-process interface for field inventories.

The Inventory module is the central seam: every extractor produces an
Inventory, every consumer (validators, summary reader, OWL projector,
drift register) reads one. The JSON Schema at schema/inventory.schema.json
is the wire serialization; this module is the in-process contract.
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any, Literal

import yaml
from pydantic import BaseModel, ConfigDict, Field

Cardinality = Literal["required", "optional", "repeating"]
MatchBy = Literal["name", "path"]

# Attributes that `Inventory.enrich` can flow from `other` into `self`.
# Excluded: `path` (immutable key), `domain` (match-key prefix; agreement is
# structural so provenance would be tautological noise), `source_location`
# (per-source by definition — each source has its own; the SourceClaim's own
# `location` field captures it), `cardinality` and `is_reference` (always
# attested, defaulted; would clutter provenance on every field). See
# cora/docs/adr/0001-enrich-vs-merge.md.
ENRICHABLE_ATTRIBUTES: frozenset[str] = frozenset(
    {"definition", "enumeration", "range", "concept_id"}
)


class StructuralError(ValueError):
    """Inventory.validate() raises this when structural invariants are violated."""

    def __init__(self, issues: list[str]) -> None:
        self.issues = issues
        super().__init__("; ".join(issues))


class MergeConflict(ValueError):
    """Inventory.merge() raises this when two fields disagree on an attested value."""

    def __init__(self, conflicts: list[str]) -> None:
        self.conflicts = conflicts
        super().__init__("; ".join(conflicts))


class SourceClaim(BaseModel):
    """A single source's attestation of an attribute value."""

    model_config = ConfigDict(extra="forbid")

    source: str
    value: Any
    location: str | None = None


class AttributeProvenance(BaseModel):
    """Multi-source provenance for one attribute on one field/type.

    Present whenever ≥2 sources attest a value. ``chosen`` names the source
    whose value lives at the top level; absent when all claims agree.
    """

    model_config = ConfigDict(extra="forbid")

    attribute: str
    claims: list[SourceClaim] = Field(min_length=2)
    chosen: str | None = None


class UnmatchedEnrichment(BaseModel):
    """A row from `other` that found no match during enrich."""

    model_config = ConfigDict(extra="forbid")

    source: str
    domain: str | None = None
    field: str
    location: str | None = None


class TypeEntry(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    extends: str | None = None
    abstract: bool = False
    definition: str = ""
    source_location: str | None = None
    provenance: list[AttributeProvenance] | None = None


class FieldEntry(BaseModel):
    model_config = ConfigDict(extra="forbid")

    path: str
    concept_id: str | None = None
    domain: str | None = None
    range: str | None = None
    is_reference: bool = False
    cardinality: Cardinality
    definition: str = ""
    source_location: str | None = None
    enumeration: list[str] | None = None
    provenance: list[AttributeProvenance] | None = None


class Inventory(BaseModel):
    model_config = ConfigDict(extra="forbid")

    standard: str
    module: str
    version: str
    source_artifact: str
    extractor: str
    extracted_at: datetime
    namespace_hint: str | None = None
    source_label: str | None = None
    types: list[TypeEntry] = Field(default_factory=list)
    fields: list[FieldEntry]
    unmatched_enrichments: list[UnmatchedEnrichment] | None = None

    @classmethod
    def from_yaml(cls, path: Path) -> Inventory:
        with path.open() as f:
            data = yaml.safe_load(f)
        return cls.model_validate(data)

    def to_yaml(self, path: Path) -> None:
        data = self.model_dump(mode="json", exclude_none=True)
        with path.open("w") as f:
            yaml.safe_dump(
                data,
                f,
                sort_keys=False,
                default_flow_style=False,
                allow_unicode=True,
            )

    def validate_structure(self) -> None:
        """Check hard structural invariants. Raises StructuralError.

        Only checks invariants that must hold WITHIN a single inventory:

        - When ``types[]`` is non-empty, every field must declare a ``domain``.
        - A field's ``domain`` must reference a type defined in this inventory.

        Cross-inventory references (``type.extends`` or object-reference
        ``field.range`` pointing at a type defined in another standard or
        module) are *not* errors — inventories are per-module, and shared
        Core-Data types live elsewhere by design. ``external_references()``
        surfaces such pointers for informational reporting.

        Named ``validate_structure`` rather than ``validate`` to avoid shadowing
        pydantic v1's deprecated ``BaseModel.validate`` classmethod, which mypy
        still flags as an override mismatch.
        """
        issues: list[str] = []
        type_names = {t.name for t in self.types}
        has_types = bool(self.types)

        for f in self.fields:
            if has_types and f.domain is None:
                issues.append(
                    f"field {f.path!r} missing domain (required when types[] is non-empty)"
                )
            if f.domain is not None and has_types and f.domain not in type_names:
                issues.append(
                    f"field {f.path!r} domain {f.domain!r} not in this inventory's types[]"
                )

        if issues:
            raise StructuralError(issues)

    def external_references(self) -> list[str]:
        """Return human-readable descriptions of cross-inventory references.

        These are *not* errors — Core-Data types referenced by other MITS
        modules, for example. Useful for reporting and for the future drift
        register; the validator may surface them as warnings.
        """
        out: list[str] = []
        type_names = {t.name for t in self.types}

        for t in self.types:
            if t.extends is not None and t.extends not in type_names:
                out.append(
                    f"type {t.name!r} extends external type {t.extends!r}"
                )
        for f in self.fields:
            if f.is_reference and f.range is not None and f.range not in type_names:
                out.append(
                    f"field {f.path!r} references external type {f.range!r}"
                )
        return out

    def merge(self, other: Inventory, *, match_by: MatchBy) -> Inventory:
        """Structural merge: definitions/metadata from `other` enrich `self`.

        Conflicts on attested values raise MergeConflict. Fields in `other`
        with no match in `self` are appended.
        """
        conflicts: list[str] = []

        def field_key(f: FieldEntry) -> str:
            if match_by == "path":
                return f.path
            return f.path.split("/")[-1]

        self_by_key: dict[str, FieldEntry] = {field_key(f): f for f in self.fields}
        merged_fields: list[FieldEntry] = []

        for s in self.fields:
            other_match = next(
                (o for o in other.fields if field_key(o) == field_key(s)),
                None,
            )
            if other_match is None:
                merged_fields.append(s)
                continue
            merged, field_conflicts = _merge_field(s, other_match)
            conflicts.extend(field_conflicts)
            merged_fields.append(merged)

        for o in other.fields:
            if field_key(o) not in self_by_key:
                merged_fields.append(o)

        merged_types, type_conflicts = _merge_types(self.types, other.types)
        conflicts.extend(type_conflicts)

        if conflicts:
            raise MergeConflict(conflicts)

        return Inventory(
            standard=self.standard,
            module=self.module,
            version=self.version,
            source_artifact=self.source_artifact,
            extractor=self.extractor,
            extracted_at=self.extracted_at,
            namespace_hint=self.namespace_hint,
            source_label=self.source_label,
            types=merged_types,
            fields=merged_fields,
            unmatched_enrichments=self.unmatched_enrichments,
        )

    def enrich(self, other: Inventory, *, attributes: set[str]) -> Inventory:
        """Asymmetric type-scoped fill-in from ``other`` into ``self``.

        Match key: ``(field.domain, field.path.split("/")[-1])``. For attributes
        in ``attributes`` (the trust list), ``other`` wins at the top level if
        attested. Untrusted attributes are left as-is on ``self``. Provenance
        is recorded on every field where ≥2 sources attest an attribute, even
        for untrusted attributes — the inventory becomes the full lineage record.

        Unmatched ``other.fields`` rows are recorded in the returned
        inventory's ``unmatched_enrichments`` list rather than appended to
        ``fields``. ``types[]`` is left untouched on ``self`` (future
        deepening for PDF-style type-level enrichment).

        Never raises a conflict. See ADR-0001 for the design rationale.
        """
        unknown = attributes - ENRICHABLE_ATTRIBUTES
        if unknown:
            raise ValueError(
                f"unknown enrich attributes: {sorted(unknown)}; "
                f"valid: {sorted(ENRICHABLE_ATTRIBUTES)}"
            )
        if self.source_label is None or other.source_label is None:
            raise ValueError(
                "enrich requires source_label set on both inventories"
            )

        self_label = self.source_label
        other_label = other.source_label

        def field_key(f: FieldEntry) -> tuple[str | None, str]:
            return (f.domain, f.path.split("/")[-1])

        other_by_key: dict[tuple[str | None, str], FieldEntry] = {
            field_key(f): f for f in other.fields
        }
        matched_keys: set[tuple[str | None, str]] = set()

        new_fields: list[FieldEntry] = []
        for s in self.fields:
            k = field_key(s)
            o = other_by_key.get(k)
            if o is None:
                new_fields.append(s)
                continue
            matched_keys.add(k)
            new_fields.append(_enrich_field(s, o, attributes, self_label, other_label))

        new_unmatched: list[UnmatchedEnrichment] = []
        for o in other.fields:
            if field_key(o) not in matched_keys:
                new_unmatched.append(
                    UnmatchedEnrichment(
                        source=other_label,
                        domain=o.domain,
                        field=o.path.split("/")[-1],
                        location=o.source_location,
                    )
                )

        combined_unmatched = [*(self.unmatched_enrichments or []), *new_unmatched]
        return Inventory(
            standard=self.standard,
            module=self.module,
            version=self.version,
            source_artifact=self.source_artifact,
            extractor=self.extractor,
            extracted_at=self.extracted_at,
            namespace_hint=self.namespace_hint,
            source_label=self.source_label,
            types=self.types,
            fields=new_fields,
            unmatched_enrichments=combined_unmatched or None,
        )


def _is_attested(value: Any) -> bool:
    """Return True if a value counts as an attested attribute."""
    if value is None:
        return False
    if isinstance(value, str) and value == "":
        return False
    if isinstance(value, list) and not value:
        return False
    return True


def _enrich_field(
    s: FieldEntry,
    o: FieldEntry,
    attributes: set[str],
    self_label: str,
    other_label: str,
) -> FieldEntry:
    """Apply enrichment from one matched ``other`` field onto a ``self`` field."""
    updates: dict[str, Any] = {}
    provenance_by_attr: dict[str, AttributeProvenance] = {
        p.attribute: p for p in (s.provenance or [])
    }

    for attr in ENRICHABLE_ATTRIBUTES:
        self_val = getattr(s, attr)
        other_val = getattr(o, attr)
        self_attested = _is_attested(self_val)
        other_attested = _is_attested(other_val)

        if not other_attested:
            continue

        if attr in attributes:
            updates[attr] = other_val

        if not self_attested:
            continue

        existing = provenance_by_attr.get(attr)
        other_claim = SourceClaim(
            source=other_label, value=other_val, location=o.source_location
        )
        if existing is None:
            self_claim = SourceClaim(
                source=self_label, value=self_val, location=s.source_location
            )
            claims = [self_claim, other_claim]
        else:
            claims = [*existing.claims, other_claim]

        values = [c.value for c in claims]
        all_equal = all(v == values[0] for v in values[1:])
        chosen: str | None
        if all_equal:
            chosen = None
        else:
            chosen = other_label if attr in attributes else self_label

        provenance_by_attr[attr] = AttributeProvenance(
            attribute=attr, claims=claims, chosen=chosen
        )

    new_values = s.model_dump()
    new_values.update(updates)
    sorted_provenance = [
        provenance_by_attr[k] for k in sorted(provenance_by_attr.keys())
    ]
    new_values["provenance"] = sorted_provenance or None
    return FieldEntry(**new_values)


def _merge_field(s: FieldEntry, o: FieldEntry) -> tuple[FieldEntry, list[str]]:
    """Field-level merge with conflict accumulation."""
    conflicts: list[str] = []
    key = s.path

    def pick_str(attr: str, sv: str | None, ov: str | None) -> str | None:
        if sv and ov and sv != ov:
            conflicts.append(f"field {key!r} {attr}: {sv!r} vs {ov!r}")
            return sv
        return sv or ov

    merged_definition = pick_str("definition", s.definition or None, o.definition or None) or ""
    merged_source_location = pick_str("source_location", s.source_location, o.source_location)
    merged_concept_id = pick_str("concept_id", s.concept_id, o.concept_id)
    merged_domain = pick_str("domain", s.domain, o.domain)
    merged_range = pick_str("range", s.range, o.range)

    if s.cardinality != o.cardinality:
        conflicts.append(f"field {key!r} cardinality: {s.cardinality} vs {o.cardinality}")

    if s.is_reference != o.is_reference:
        conflicts.append(
            f"field {key!r} is_reference: {s.is_reference} vs {o.is_reference}"
        )

    merged_enumeration: list[str] | None
    if s.enumeration is None:
        merged_enumeration = o.enumeration
    elif o.enumeration is None:
        merged_enumeration = s.enumeration
    elif s.enumeration != o.enumeration:
        conflicts.append(f"field {key!r} enumeration: {s.enumeration} vs {o.enumeration}")
        merged_enumeration = s.enumeration
    else:
        merged_enumeration = s.enumeration

    return (
        FieldEntry(
            path=s.path,
            concept_id=merged_concept_id,
            domain=merged_domain,
            range=merged_range,
            is_reference=s.is_reference,
            cardinality=s.cardinality,
            definition=merged_definition,
            source_location=merged_source_location,
            enumeration=merged_enumeration,
        ),
        conflicts,
    )


def _merge_types(
    self_types: list[TypeEntry], other_types: list[TypeEntry]
) -> tuple[list[TypeEntry], list[str]]:
    """Type-level merge with conflict accumulation."""
    conflicts: list[str] = []
    by_name = {t.name: t for t in self_types}
    merged: list[TypeEntry] = []

    for s in self_types:
        match = next((t for t in other_types if t.name == s.name), None)
        if match is None:
            merged.append(s)
            continue

        merged_t, type_conflicts = _merge_one_type(s, match)
        conflicts.extend(type_conflicts)
        merged.append(merged_t)

    for o in other_types:
        if o.name not in by_name:
            merged.append(o)

    return merged, conflicts


def _merge_one_type(s: TypeEntry, o: TypeEntry) -> tuple[TypeEntry, list[str]]:
    """Type-pair merge with conflict accumulation."""
    conflicts: list[str] = []

    def pick_str(attr: str, sv: str | None, ov: str | None) -> str | None:
        if sv and ov and sv != ov:
            conflicts.append(f"type {s.name!r} {attr}: {sv!r} vs {ov!r}")
            return sv
        return sv or ov

    if s.extends and o.extends and s.extends != o.extends:
        conflicts.append(f"type {s.name!r} extends: {s.extends!r} vs {o.extends!r}")
    if s.abstract != o.abstract:
        conflicts.append(f"type {s.name!r} abstract: {s.abstract} vs {o.abstract}")

    return (
        TypeEntry(
            name=s.name,
            extends=s.extends or o.extends,
            abstract=s.abstract,
            definition=pick_str("definition", s.definition or None, o.definition or None) or "",
            source_location=pick_str("source_location", s.source_location, o.source_location),
        ),
        conflicts,
    )
