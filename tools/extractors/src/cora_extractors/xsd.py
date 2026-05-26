"""XSD extractor adapter.

Walks any XSD schema tree, resolving ``xs:include`` and ``xs:import``
transitively, and emits a typed Inventory. Generic by construction —
XSD is a standardised format, so no per-source config is required.

Coverage in v1:
- Named ``xs:complexType`` declarations become ``types[]`` entries.
- ``xs:extension base="X"`` becomes ``extends: X`` on the child type.
- ``xs:annotation/xs:documentation`` text becomes the ``definition``.
- Top-level ``xs:element`` children of complex types become ``fields[]``
  rows with ``domain`` set to the containing type and ``path`` set to
  ``<TypeName>/<elementName>``.
- ``xs:attribute`` children of complex types become ``fields[]`` rows
  the same way.
- ``minOccurs``/``maxOccurs`` (or attribute ``use``) drive cardinality.
- Inline ``xs:simpleType/xs:restriction/xs:enumeration`` captures
  enumeration values for the field.
- Anonymous (inline) complex types are not lifted into ``types[]`` in
  v1; the field still appears with a ``range`` of ``None``.
"""

from __future__ import annotations

import sys
from collections.abc import Iterable
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from lxml import etree  # type: ignore[import-untyped]

from cora_extractors import __version__
from cora_extractors.config import ExtractorConfig, XsdConfig
from cora_extractors.inventory import Cardinality, FieldEntry, Inventory, TypeEntry
from cora_extractors.path import build as build_path

EXTRACTOR_ID = f"cora_extractors.xsd@{__version__}"

XS_NS = "http://www.w3.org/2001/XMLSchema"
NS = {"xs": XS_NS}


class XsdExtractor:
    """Extractor adapter for XSD schemas."""

    name = "xsd"

    def extract(
        self,
        source: Path,
        config: ExtractorConfig | None = None,
        *,
        module: str | None = None,
    ) -> Inventory:
        if config is not None and not isinstance(config, XsdConfig):
            raise TypeError("XsdExtractor.extract requires XsdConfig or None")

        xsd_config = config if isinstance(config, XsdConfig) else XsdConfig()
        roots = list(_load_schemas(source, xsd_config))
        types = list(_extract_types(roots))
        fields = list(_extract_fields(roots))

        return Inventory(
            standard=module or source.stem,
            module=module or source.stem,
            version="unknown",
            source_artifact=str(source),
            extractor=EXTRACTOR_ID,
            extracted_at=datetime.now(tz=UTC),
            namespace_hint=xsd_config.namespace_hint,
            source_label="xsd",
            types=types,
            fields=fields,
        )


def _is_remote(schema_location: str) -> bool:
    return schema_location.startswith(("http://", "https://"))


def _resolve_schema_location(
    base_dir: Path, schema_location: str, config: XsdConfig
) -> Path | None:
    """Resolve a schemaLocation to a local path, applying include_remap.

    include_remap is consulted first for every schemaLocation (remote or
    local) so a config can redirect any reference — useful for both NMHC
    URLs that can't be fetched and for bare filenames whose target ships
    elsewhere in the corpus.

    Returns None if the location is a remote URL with no remap entry and
    the config asks us to skip unmapped remote includes; raises if the
    location is a remote URL with no remap entry and skip is disabled.
    Local-but-missing references fall through to ``etree.parse`` which
    raises a clear error.
    """
    remapped = config.include_remap.get(schema_location)
    if remapped is not None:
        candidate = Path(remapped)
        if not candidate.is_absolute():
            candidate = base_dir / candidate
        return candidate.resolve()

    if _is_remote(schema_location):
        if config.skip_unmapped_remote_includes:
            print(
                f"warning: skipping unmapped remote xs:include {schema_location!r}",
                file=sys.stderr,
            )
            return None
        raise ValueError(
            f"remote xs:include {schema_location!r} has no entry in include_remap "
            f"and skip_unmapped_remote_includes is False"
        )

    # Local relative path — let the downstream parser error if it's missing.
    return (base_dir / schema_location).resolve()


def _load_schemas(source: Path, config: XsdConfig) -> Iterable[Any]:
    """Parse the root XSD and every transitively xs:include'd/xs:import'ed schema."""
    visited: set[Path] = set()
    queue: list[Path] = [source.resolve()]
    while queue:
        path = queue.pop(0)
        if path in visited:
            continue
        visited.add(path)
        try:
            tree = etree.parse(str(path))
        except (OSError, etree.XMLSyntaxError) as exc:
            raise ValueError(f"failed to parse XSD at {path}: {exc}") from exc
        root = tree.getroot()
        yield root
        for ref in root.findall("xs:include", NS) + root.findall("xs:import", NS):
            loc = ref.get("schemaLocation")
            if not loc:
                continue
            resolved = _resolve_schema_location(path.parent, loc, config)
            if resolved is not None:
                queue.append(resolved)


def _annotation_text(node: Any) -> str:
    doc = node.find("xs:annotation/xs:documentation", NS)
    if doc is None or doc.text is None:
        return ""
    return " ".join(doc.text.split())


def _extract_types(roots: list[Any]) -> Iterable[TypeEntry]:
    for root in roots:
        for ct in root.findall("xs:complexType", NS):
            name = ct.get("name")
            if not name:
                continue
            extends = None
            ext = ct.find("xs:complexContent/xs:extension", NS)
            if ext is not None:
                base = ext.get("base")
                if isinstance(base, str):
                    extends = _strip_xs_prefix(base) if base.startswith("xs:") else base
            abstract = ct.get("abstract") == "true"
            yield TypeEntry(
                name=name,
                extends=extends,
                abstract=abstract,
                definition=_annotation_text(ct),
                source_location=_source_location(root, ct),
            )


def _extract_fields(roots: list[Any]) -> Iterable[FieldEntry]:
    known_type_names: set[str] = set()
    for root in roots:
        for ct in root.findall("xs:complexType", NS):
            n = ct.get("name")
            if n:
                known_type_names.add(n)

    for root in roots:
        for ct in root.findall("xs:complexType", NS):
            type_name = ct.get("name")
            if not type_name:
                continue
            yield from _fields_of_complex_type(ct, type_name, known_type_names, root)


def _fields_of_complex_type(
    ct: Any, type_name: str, known_types: set[str], root: Any
) -> Iterable[FieldEntry]:
    # Sequence and attributes can sit directly under <xs:complexType> or
    # inside <xs:complexContent>/<xs:extension> for inheriting types.
    extension = ct.find("xs:complexContent/xs:extension", NS)
    container = extension if extension is not None else ct

    for el in container.findall("xs:sequence/xs:element", NS) + container.findall(
        "xs:sequence/xs:choice/xs:element", NS
    ):
        yield _field_from_element(el, type_name, known_types, root)

    for attr in container.findall("xs:attribute", NS):
        yield _field_from_attribute(attr, type_name, known_types, root)


def _field_from_element(
    el: Any, type_name: str, known_types: set[str], root: Any
) -> FieldEntry:
    name = el.get("name") or "anonymous"
    type_ref = el.get("type")
    range_value, is_reference = _classify_range(type_ref, known_types)
    min_occurs = el.get("minOccurs", "1")
    max_occurs = el.get("maxOccurs", "1")
    enumeration = _inline_enumeration(el)

    return FieldEntry(
        path=build_path([type_name, name]),
        domain=type_name,
        range=range_value,
        is_reference=is_reference,
        cardinality=_cardinality_from_occurs(min_occurs, max_occurs),
        definition=_annotation_text(el),
        source_location=_source_location(root, el),
        enumeration=enumeration,
    )


def _field_from_attribute(
    attr: Any, type_name: str, known_types: set[str], root: Any
) -> FieldEntry:
    name = attr.get("name") or "anonymous"
    type_ref = attr.get("type")
    range_value, is_reference = _classify_range(type_ref, known_types)
    use = attr.get("use", "optional")
    cardinality: Cardinality = "required" if use == "required" else "optional"

    return FieldEntry(
        path=build_path([type_name, name]),
        domain=type_name,
        range=range_value,
        is_reference=is_reference,
        cardinality=cardinality,
        definition=_annotation_text(attr),
        source_location=_source_location(root, attr),
        enumeration=_inline_enumeration(attr),
    )


def _classify_range(
    type_ref: str | None, known_types: set[str]
) -> tuple[str | None, bool]:
    if not type_ref:
        return None, False
    if type_ref.startswith("xs:"):
        return type_ref, False
    return type_ref, type_ref in known_types


def _inline_enumeration(node: Any) -> list[str] | None:
    enums = node.findall("xs:simpleType/xs:restriction/xs:enumeration", NS)
    if not enums:
        return None
    values = [e.get("value") for e in enums if e.get("value") is not None]
    return [v for v in values if isinstance(v, str)] or None


def _cardinality_from_occurs(min_occurs: str, max_occurs: str) -> Cardinality:
    if max_occurs == "unbounded" or _safe_int(max_occurs, 1) > 1:
        return "repeating"
    if _safe_int(min_occurs, 1) == 0:
        return "optional"
    return "required"


def _safe_int(value: str, default: int) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def _strip_xs_prefix(value: str) -> str:
    return value.removeprefix("xs:")


def _source_location(root: Any, node: Any) -> str | None:
    """Best-effort 'file:line' string for a node."""
    base = root.base or ""
    short = Path(base).name if base else ""
    line = getattr(node, "sourceline", None)
    if not short and line is None:
        return None
    if not short:
        return f"line {line}"
    if line is None:
        return short
    return f"{short}:{line}"
