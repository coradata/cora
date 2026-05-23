"""Extractor seam.

An Extractor takes a native artifact (XSD, JSON, Excel, ...) and produces
an Inventory. Format-specific modules (xsd, json_catalog, excel_dictionary)
implement this protocol. The CLI is a thin registry over the registered
adapters.
"""

from __future__ import annotations

from pathlib import Path
from typing import Protocol, runtime_checkable

from cora_extractors.config import ExtractorConfig
from cora_extractors.inventory import Inventory


@runtime_checkable
class Extractor(Protocol):
    """A format-specific extractor adapter."""

    name: str

    def extract(
        self,
        source: Path,
        config: ExtractorConfig | None = None,
        *,
        module: str | None = None,
    ) -> Inventory: ...
