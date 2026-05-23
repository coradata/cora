from __future__ import annotations

from datetime import UTC, datetime

import pytest

from cora_extractors.inventory import FieldEntry, Inventory
from cora_extractors.path import InvalidPathError, build, parse, resolve, slugify


def test_build_simple() -> None:
    assert build(["a", "b", "c"]) == "a/b/c"


def test_build_single_segment() -> None:
    assert build(["tenant_email"]) == "tenant_email"


def test_build_preserves_pascal_case() -> None:
    # MITS-style PascalCase passes through untouched.
    assert build(["AddressType", "Description"]) == "AddressType/Description"


def test_build_rejects_empty_parts() -> None:
    with pytest.raises(InvalidPathError):
        build([])


def test_build_rejects_empty_segment() -> None:
    with pytest.raises(InvalidPathError):
        build(["a", "", "c"])


def test_build_slugifies_segment_with_separator() -> None:
    # REDI label: "Number of Shares/ Units" — separator and whitespace become _.
    assert build(["Property", "Number of Shares/ Units"]) == "Property/Number_of_Shares_Units"


def test_build_slugifies_other_special_chars() -> None:
    assert build(["Type & Form (v2)?"]) == "Type_Form_v2"


def test_build_strips_leading_trailing_whitespace_and_underscores() -> None:
    assert build(["  hello world  "]) == "hello_world"


def test_build_rejects_segment_that_reduces_to_empty() -> None:
    with pytest.raises(InvalidPathError):
        build(["???"])


def test_slugify_collapses_runs() -> None:
    assert slugify("a   b///c") == "a_b_c"


def test_parse_simple() -> None:
    assert parse("a/b/c") == ["a", "b", "c"]


def test_parse_single_segment() -> None:
    assert parse("tenant_email") == ["tenant_email"]


def test_parse_rejects_empty() -> None:
    with pytest.raises(InvalidPathError):
        parse("")


def test_parse_rejects_double_separator() -> None:
    with pytest.raises(InvalidPathError):
        parse("a//c")


def test_build_parse_round_trip_canonical() -> None:
    # build(parse(s)) is identity for already-canonical paths.
    for s in ["a", "a/b", "a/b/c", "PhysicalProperty/Property/Identification/IDValue"]:
        assert build(parse(s)) == s


def test_build_idempotent_on_canonical_input() -> None:
    canonical = "AddressType/Number_of_Shares_Units"
    assert build(parse(canonical)) == canonical


def _mk_inventory() -> Inventory:
    return Inventory(
        standard="x",
        module="m",
        version="1",
        source_artifact="x.xsd",
        extractor="t@0",
        extracted_at=datetime(2026, 1, 1, tzinfo=UTC),
        fields=[
            FieldEntry(path="A/b", cardinality="required"),
            FieldEntry(path="A/c", cardinality="optional"),
        ],
    )


def test_resolve_finds_known_field() -> None:
    inv = _mk_inventory()
    found = resolve("A/b", inv)
    assert found is not None
    assert found.path == "A/b"


def test_resolve_returns_none_for_unknown() -> None:
    inv = _mk_inventory()
    assert resolve("A/missing", inv) is None
