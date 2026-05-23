"""Tests for XsdConfig.include_remap and skip_unmapped_remote_includes."""

from __future__ import annotations

from pathlib import Path

import pytest

from cora_extractors.config import XsdConfig
from cora_extractors.xsd import XsdExtractor

FIXTURES = Path(__file__).resolve().parent / "fixtures" / "xsd" / "remote"


def test_unmapped_remote_skipped_by_default() -> None:
    """Default config silently skips unmapped remote includes."""
    inv = XsdExtractor().extract(FIXTURES / "uses-remote.xsd", module="orders")
    type_names = {t.name for t in inv.types}
    assert "Order" in type_names
    # SharedLine lives in the (unfetched) remote schema, so it's absent.
    assert "SharedLine" not in type_names


def test_remap_resolves_remote_url_to_local_file() -> None:
    """A remap entry redirects the remote URL to a local fixture."""
    config = XsdConfig(
        include_remap={"http://example.invalid/shared.xsd": "shared.xsd"},
    )
    inv = XsdExtractor().extract(FIXTURES / "uses-remote.xsd", config, module="orders")
    type_names = {t.name for t in inv.types}
    assert {"Order", "SharedLine"} <= type_names


def test_unmapped_remote_raises_when_skip_disabled() -> None:
    config = XsdConfig(skip_unmapped_remote_includes=False)
    with pytest.raises(ValueError, match="no entry in include_remap"):
        XsdExtractor().extract(FIXTURES / "uses-remote.xsd", config, module="orders")


def test_remap_emits_no_warning_when_match_found(
    capsys: pytest.CaptureFixture[str],
) -> None:
    config = XsdConfig(
        include_remap={"http://example.invalid/shared.xsd": "shared.xsd"},
    )
    XsdExtractor().extract(FIXTURES / "uses-remote.xsd", config, module="orders")
    captured = capsys.readouterr()
    assert "warning" not in captured.err


def test_unmapped_remote_emits_warning_when_skipped(
    capsys: pytest.CaptureFixture[str],
) -> None:
    XsdExtractor().extract(FIXTURES / "uses-remote.xsd", module="orders")
    captured = capsys.readouterr()
    assert "skipping unmapped remote xs:include" in captured.err
