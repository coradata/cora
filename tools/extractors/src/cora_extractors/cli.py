"""Thin CLI registry over the Extractor and Validator seams.

One entrypoint (``cora``), three subcommands:

- ``cora extract <format> <source> [--config c.yaml] --output out.yaml``
- ``cora validate [<name>]``
- ``cora inventory summary <inventory.yaml>``

Format and validator adapters are registered as the modules implementing
the Extractor / Validator protocols. New adapters appear automatically
once added to the registry.
"""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence
from pathlib import Path

from cora_extractors import __version__
from cora_extractors.config import (
    ExcelDictionaryConfig,
    ExtractorConfig,
    JsonCatalogConfig,
    XsdConfig,
)
from cora_extractors.excel_dictionary import ExcelDictionaryExtractor
from cora_extractors.extractor import Extractor
from cora_extractors.json_catalog import JsonCatalogExtractor
from cora_extractors.summary import summarize_file
from cora_extractors.validator import Validator
from cora_extractors.validators.field_count import FieldCountValidator
from cora_extractors.validators.inventory_schema import InventorySchemaValidator
from cora_extractors.xsd import XsdExtractor

EXTRACTORS: dict[str, Extractor] = {
    "xsd": XsdExtractor(),
    "json": JsonCatalogExtractor(),
    "excel": ExcelDictionaryExtractor(),
}

CONFIG_TYPES: dict[str, type[ExtractorConfig]] = {
    "xsd": XsdConfig,
    "json": JsonCatalogConfig,
    "excel": ExcelDictionaryConfig,
}

VALIDATORS: dict[str, Validator] = {
    "inventory-schema": InventorySchemaValidator(),
    "field-count": FieldCountValidator(),
}


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="cora",
        description="CORA field-inventory toolkit (extractors, validators, summary).",
    )
    parser.add_argument("--version", action="version", version=f"cora {__version__}")
    subparsers = parser.add_subparsers(dest="cmd")

    _add_extract(subparsers)
    _add_validate(subparsers)
    _add_inventory(subparsers)

    args = parser.parse_args(argv)
    if args.cmd is None:
        parser.print_help()
        return 0
    handler = args.func
    return int(handler(args))


def _add_extract(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    p = subparsers.add_parser("extract", help="Extract a field inventory from a native artifact.")
    p.add_argument("format", choices=sorted(EXTRACTORS.keys()))
    p.add_argument("source", type=Path)
    p.add_argument("--config", type=Path, default=None)
    p.add_argument(
        "--standard",
        default=None,
        help="Standard short name (e.g. mits, redi). Defaults to module value.",
    )
    p.add_argument(
        "--module",
        default=None,
        help="Override the module name (defaults to source stem).",
    )
    p.add_argument(
        "--version",
        default=None,
        help="Override the version label (defaults to 'unknown').",
    )
    p.add_argument(
        "--repo-root",
        type=Path,
        default=None,
        help="Root used to make source_artifact relative; otherwise the absolute path is kept.",
    )
    p.add_argument("--output", type=Path, required=True)
    p.set_defaults(func=_cmd_extract)


def _add_validate(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    p = subparsers.add_parser("validate", help="Run registered validators against the repo.")
    p.add_argument(
        "name",
        nargs="?",
        choices=sorted(VALIDATORS.keys()),
        default=None,
        help="Run a single named validator. Omit to run all.",
    )
    p.add_argument(
        "--repo-root",
        type=Path,
        default=Path.cwd(),
        help="Repository root (defaults to current working directory).",
    )
    p.set_defaults(func=_cmd_validate)


def _add_inventory(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    p = subparsers.add_parser("inventory", help="Inventory consumer subcommands.")
    inv_subs = p.add_subparsers(dest="inventory_cmd", required=True)
    s = inv_subs.add_parser("summary", help="Print a summary of an inventory YAML.")
    s.add_argument("path", type=Path)
    s.set_defaults(func=_cmd_inventory_summary)


def _cmd_extract(args: argparse.Namespace) -> int:
    extractor = EXTRACTORS[args.format]
    config_cls = CONFIG_TYPES[args.format]
    config: ExtractorConfig | None
    if args.config is not None:
        config = config_cls.from_yaml(args.config)
    else:
        config = None

    inventory = extractor.extract(args.source, config, module=args.module)
    if args.standard:
        inventory.standard = args.standard
    if args.version:
        inventory.version = args.version
    if args.repo_root:
        repo = args.repo_root.resolve()
        try:
            rel = args.source.resolve().relative_to(repo)
            inventory.source_artifact = str(rel)
        except ValueError:
            pass  # source outside repo_root; keep what the extractor produced

    args.output.parent.mkdir(parents=True, exist_ok=True)
    inventory.to_yaml(args.output)
    return 0


def _cmd_validate(args: argparse.Namespace) -> int:
    names = [args.name] if args.name else sorted(VALIDATORS.keys())
    had_errors = False
    for name in names:
        validator = VALIDATORS[name]
        result = validator.check(args.repo_root)
        for finding in result.findings:
            print(f"[{name}:{finding.severity}] {finding.location}: {finding.message}")
        if result.has_errors:
            had_errors = True
    return 1 if had_errors else 0


def _cmd_inventory_summary(args: argparse.Namespace) -> int:
    print(summarize_file(args.path).render())
    return 0


if __name__ == "__main__":
    sys.exit(main())
