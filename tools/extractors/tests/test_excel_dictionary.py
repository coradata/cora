"""Excel data dictionary extractor specifics."""

from __future__ import annotations

from pathlib import Path

from cora_extractors.config import ExcelDictionaryConfig
from cora_extractors.excel_dictionary import ExcelDictionaryExtractor
from cora_extractors.path import resolve

FIXTURES = Path(__file__).resolve().parent / "fixtures" / "excel"


def test_a_extracts_five_rows_and_enumeration() -> None:
    config = ExcelDictionaryConfig.from_yaml(FIXTURES / "a" / "config.yaml")
    inv = ExcelDictionaryExtractor().extract(
        FIXTURES / "a" / "dictionary.xlsx", config, module="example_a"
    )
    paths = sorted(f.path for f in inv.fields)
    assert paths == sorted(
        ["tenant_name", "rent_amount", "status", "notes", "payment_history"]
    )
    status = resolve("status", inv)
    assert status is not None
    assert status.enumeration == ["current", "late", "delinquent"]
    assert status.cardinality == "required"


def test_b_handles_two_header_rows_and_different_column_order() -> None:
    config = ExcelDictionaryConfig.from_yaml(FIXTURES / "b" / "config.yaml")
    inv = ExcelDictionaryExtractor().extract(
        FIXTURES / "b" / "dictionary.xlsx", config, module="example_b"
    )
    paths = sorted(f.path for f in inv.fields)
    assert paths == sorted(
        ["loan_id", "principal", "term_months", "status", "interest_rate"]
    )
    loan_id = resolve("loan_id", inv)
    assert loan_id is not None
    # Definition is from column B in this layout.
    assert loan_id.definition == "Loan identifier."
    assert loan_id.range == "id"


def test_emits_no_types() -> None:
    config = ExcelDictionaryConfig.from_yaml(FIXTURES / "a" / "config.yaml")
    inv = ExcelDictionaryExtractor().extract(
        FIXTURES / "a" / "dictionary.xlsx", config, module="example_a"
    )
    assert inv.types == []
