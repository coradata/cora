"""Path grammar for inventory field references.

The path value is the canonical, format-agnostic reference that crosswalks
use to point at fields. Extractors construct paths through this module
(never by string concatenation) so the grammar stays consistent across
XSD, JSON, Excel, and future formats.

Grammar v1:
  - Segments are separated by SEPARATOR ("/").
  - Each segment may contain ASCII letters, digits, underscore, and hyphen.
    ``build()`` slugifies its input by replacing any other character (including
    SEPARATOR and whitespace) with ``_``, collapsing consecutive ``_``, and
    stripping leading/trailing ``_``. Case is preserved so XSD PascalCase
    (``AddressType/Description``) survives intact while messy Excel labels
    (``Number of Shares/ Units``) canonicalise to ``Number_of_Shares_Units``.
  - Empty input segments — or segments that reduce to empty after
    slugification — are invalid.
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

import re
from collections.abc import Sequence
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from cora_extractors.inventory import FieldEntry, Inventory

SEPARATOR = "/"

_NON_SEGMENT_CHAR = re.compile(r"[^A-Za-z0-9_-]+")


class InvalidPathError(ValueError):
    """Raised when a path or path segment violates the grammar."""


def slugify(segment: str) -> str:
    """Canonicalise a raw segment string.

    Replaces any character outside ``[A-Za-z0-9_-]`` with ``_``, collapses
    runs, and trims leading/trailing ``_``. Preserves case.
    """
    s = _NON_SEGMENT_CHAR.sub("_", segment.strip())
    s = re.sub("_+", "_", s).strip("_")
    if not s:
        raise InvalidPathError(
            f"segment {segment!r} reduces to empty after slugification"
        )
    return s


def build(parts: Sequence[str]) -> str:
    """Construct a canonical path string from raw segments.

    Each part is slugified before joining; the inputs do not need to be
    pre-cleaned. Empty inputs (or inputs that reduce to empty) are rejected.
    """
    if not parts:
        raise InvalidPathError("path must have at least one segment")
    return SEPARATOR.join(slugify(part) for part in parts)


def parse(s: str) -> list[str]:
    """Split a canonical path string into its segments.

    Expects an already-canonical input (produced by ``build``). Empty
    segments (e.g. from ``"a//c"``) are rejected.
    """
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
