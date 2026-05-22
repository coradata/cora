"""Path grammar for inventory field references.

The path value is the canonical, format-agnostic reference that crosswalks
use to point at fields. Extractors construct paths through this module
(never by string concatenation) so the grammar stays consistent across
XSD, JSON, Excel, and future formats.

Grammar v1:
  - Segments are separated by SEPARATOR ("/").
  - Each segment is a local identifier — no separator character inside.
  - Empty paths and empty segments are invalid.
  - Cardinality (repeating, optional) is captured on FieldEntry, not in
    the path string. A path like "Property/tenants" is single regardless
    of whether tenants is a single or repeating field.
  - Namespaces are normalised away by the extractor before path
    construction. If preserving namespace prefixes ever becomes
    necessary, the grammar will extend here.
  - Flat-table sources (Excel data dictionaries) produce single-segment
    paths (e.g. "tenant_email"). That's a valid path.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from cora_extractors.inventory import FieldEntry, Inventory

SEPARATOR = "/"


class InvalidPathError(ValueError):
    """Raised when a path or path segment violates the grammar."""


def build(parts: Sequence[str]) -> str:
    """Construct a canonical path string from segments."""
    if not parts:
        raise InvalidPathError("path must have at least one segment")
    for part in parts:
        if not part:
            raise InvalidPathError("path segment must be non-empty")
        if SEPARATOR in part:
            raise InvalidPathError(
                f"path segment {part!r} must not contain separator {SEPARATOR!r}"
            )
    return SEPARATOR.join(parts)


def parse(s: str) -> list[str]:
    """Split a canonical path string into its segments."""
    if not s:
        raise InvalidPathError("path must be non-empty")
    parts = s.split(SEPARATOR)
    for part in parts:
        if not part:
            raise InvalidPathError(f"path {s!r} has an empty segment")
    return parts


def resolve(path: str, inventory: Inventory) -> FieldEntry | None:
    """Return the FieldEntry whose path matches, or None if not found."""
    for field in inventory.fields:
        if field.path == path:
            return field
    return None
