"""Typed in-process interface for field inventories.

The Inventory module is the central seam: every extractor produces an
Inventory, every consumer (validators, summary reader, OWL projector,
drift register) reads one. The JSON Schema at schema/inventory.schema.json
is the wire serialization; this module is the in-process contract.
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Literal

import yaml
from pydantic import BaseModel, ConfigDict, Field

Cardinality = Literal["required", "optional", "repeating"]
MatchBy = Literal["name", "path"]


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


class TypeEntry(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    extends: str | None = None
    abstract: bool = False
    definition: str = ""
    source_location: str | None = None


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


class Inventory(BaseModel):
    model_config = ConfigDict(extra="forbid")

    standard: str
    module: str
    version: str
    source_artifact: str
    extractor: str
    extracted_at: datetime
    namespace_hint: str | None = None
    types: list[TypeEntry] = Field(default_factory=list)
    fields: list[FieldEntry]

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
        """Check structural invariants beyond JSON Schema. Raises StructuralError.

        Named ``validate_structure`` rather than ``validate`` to avoid shadowing
        pydantic v1's deprecated ``BaseModel.validate`` classmethod, which mypy
        still flags as an override mismatch.
        """
        issues: list[str] = []
        type_names = {t.name for t in self.types}

        for t in self.types:
            if t.extends is not None and t.extends not in type_names:
                issues.append(
                    f"type {t.name!r} extends unknown type {t.extends!r}"
                )

        has_types = bool(self.types)
        for f in self.fields:
            if has_types and f.domain is None:
                issues.append(
                    f"field {f.path!r} missing domain (required when types[] is non-empty)"
                )
            if f.domain is not None and has_types and f.domain not in type_names:
                issues.append(
                    f"field {f.path!r} domain {f.domain!r} not in types[]"
                )
            if f.is_reference and f.range is not None and has_types and f.range not in type_names:
                issues.append(
                    f"field {f.path!r} object reference range {f.range!r} not in types[]"
                )

        if issues:
            raise StructuralError(issues)

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
            types=merged_types,
            fields=merged_fields,
        )


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
