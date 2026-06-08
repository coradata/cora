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
from cora_extractors.cdm_json import CdmJsonExtractor
from cora_extractors.concepts import (
    DEFAULT_MODEL as CONCEPTS_DEFAULT_MODEL,
)
from cora_extractors.concepts import (
    DEFAULT_THRESHOLD as CONCEPTS_DEFAULT_THRESHOLD,
)
from cora_extractors.concepts import (
    collect_census,
    make_encoder,
    suggest_clusters,
    suggest_semantic_clusters,
    write_census_csv,
    write_census_summary,
    write_scaffold,
    write_semantic_suggestions,
    write_suggestions,
)
from cora_extractors.concepts.report import (
    OUTPUT_DIR as CONCEPTS_OUTPUT_DEFAULT,
)
from cora_extractors.concepts.report import (
    SUGGESTIONS_SEMANTIC_MD as CONCEPTS_SEMANTIC_FILENAME,
)
from cora_extractors.concepts.suggest import normalize_leaf
from cora_extractors.config import (
    CdmJsonConfig,
    ExcelDictionaryConfig,
    ExcelMultiSheetDictionaryConfig,
    ExtractorConfig,
    JsonCatalogConfig,
    XsdConfig,
)
from cora_extractors.excel_dictionary import ExcelDictionaryExtractor
from cora_extractors.excel_multisheet import ExcelMultiSheetDictionaryExtractor
from cora_extractors.extractor import Extractor
from cora_extractors.generator import Generator
from cora_extractors.generators._common import load_crosswalks
from cora_extractors.generators.concept_graphs import ConceptGraphsGenerator
from cora_extractors.generators.concept_pages import ConceptPagesGenerator
from cora_extractors.generators.coverage_matrix import CoverageMatrixGenerator
from cora_extractors.generators.index import IndexGenerator
from cora_extractors.generators.inventory_pages import InventoryPagesGenerator
from cora_extractors.inventory import ENRICHABLE_ATTRIBUTES, Inventory
from cora_extractors.json_catalog import JsonCatalogExtractor
from cora_extractors.summary import summarize_file
from cora_extractors.validator import Validator
from cora_extractors.validators.crosswalk_paths import CrosswalkPathsValidator
from cora_extractors.validators.field_count import FieldCountValidator
from cora_extractors.validators.inventory_schema import InventorySchemaValidator
from cora_extractors.xsd import XsdExtractor

EXTRACTORS: dict[str, Extractor] = {
    "xsd": XsdExtractor(),
    "json": JsonCatalogExtractor(),
    "excel": ExcelDictionaryExtractor(),
    "excel-multisheet": ExcelMultiSheetDictionaryExtractor(),
    "cdm-json": CdmJsonExtractor(),
}

CONFIG_TYPES: dict[str, type[ExtractorConfig]] = {
    "xsd": XsdConfig,
    "json": JsonCatalogConfig,
    "excel": ExcelDictionaryConfig,
    "excel-multisheet": ExcelMultiSheetDictionaryConfig,
    "cdm-json": CdmJsonConfig,
}

VALIDATORS: dict[str, Validator] = {
    "inventory-schema": InventorySchemaValidator(),
    "field-count": FieldCountValidator(),
    "crosswalk-paths": CrosswalkPathsValidator(),
}

# Order matters: index runs last so its links reference files already
# written by the other generators (clarifies intent, not enforcement).
GENERATORS: list[Generator] = [
    CoverageMatrixGenerator(),
    ConceptPagesGenerator(),
    ConceptGraphsGenerator(),
    InventoryPagesGenerator(),
    IndexGenerator(),
]

DOCS_OUTPUT_DEFAULT = Path("docs/generated")


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
    _add_docs(subparsers)
    _add_concepts(subparsers)

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

    m = inv_subs.add_parser(
        "merge",
        help=(
            "Enrich one inventory with another via Inventory.enrich. "
            "Asymmetric, type-scoped fill-in; see docs/adr/0001-enrich-vs-merge.md."
        ),
    )
    m.add_argument("--into", type=Path, required=True, help="Primary inventory (self).")
    m.add_argument("--from", dest="from_", type=Path, required=True, help="Secondary inventory.")
    m.add_argument(
        "--attribute",
        action="append",
        default=[],
        choices=sorted(ENRICHABLE_ATTRIBUTES),
        required=True,
        help="Trust-list attribute; pass once per attribute (e.g., --attribute definition).",
    )
    m.add_argument("--output", type=Path, required=True)
    m.set_defaults(func=_cmd_inventory_merge)


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


def _cmd_inventory_merge(args: argparse.Namespace) -> int:
    primary = Inventory.from_yaml(args.into)
    secondary = Inventory.from_yaml(args.from_)
    merged = primary.enrich(secondary, attributes=set(args.attribute))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    merged.to_yaml(args.output)
    return 0


def _add_docs(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    p = subparsers.add_parser("docs", help="Generated documentation site subcommands.")
    docs_subs = p.add_subparsers(dest="docs_cmd", required=True)

    b = docs_subs.add_parser(
        "build",
        help=(
            "Run every Generator adapter against the repo and write Markdown "
            "into --output (default: docs/generated/)."
        ),
    )
    b.add_argument(
        "--repo-root",
        type=Path,
        default=Path.cwd(),
        help="Repository root (defaults to current working directory).",
    )
    b.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Output directory. Defaults to <repo-root>/docs/generated.",
    )
    b.set_defaults(func=_cmd_docs_build)

    c = docs_subs.add_parser(
        "check",
        help=(
            "Re-run all generators into a temp directory and diff against the "
            "committed docs/generated/. Exits non-zero if anything differs."
        ),
    )
    c.add_argument("--repo-root", type=Path, default=Path.cwd())
    c.set_defaults(func=_cmd_docs_check)


def _cmd_docs_build(args: argparse.Namespace) -> int:
    repo_root = args.repo_root.resolve()
    output_dir = (
        args.output.resolve() if args.output is not None else repo_root / DOCS_OUTPUT_DEFAULT
    )
    output_dir.mkdir(parents=True, exist_ok=True)
    for gen in GENERATORS:
        gen.generate(repo_root, output_dir)
    return 0


def _cmd_docs_check(args: argparse.Namespace) -> int:
    import tempfile

    repo_root = args.repo_root.resolve()
    committed = repo_root / DOCS_OUTPUT_DEFAULT

    with tempfile.TemporaryDirectory(prefix="cora-docs-check-") as tmp:
        tmp_path = Path(tmp)
        for gen in GENERATORS:
            gen.generate(repo_root, tmp_path)

        differences = _diff_dirs(committed, tmp_path)
        if differences:
            print("docs/generated/ is out of date — regenerate with `cora docs build`:")
            for d in differences:
                print(f"  - {d}")
            return 1
    return 0


def _diff_dirs(committed: Path, freshly_built: Path) -> list[str]:
    """Return a sorted list of relative paths that differ between the two dirs."""
    import filecmp

    differences: list[str] = []

    def _walk(rel: Path) -> None:
        left = committed / rel
        right = freshly_built / rel
        if not left.exists() and not right.exists():
            return
        if not left.exists():
            for child in right.rglob("*"):
                if child.is_file():
                    differences.append(f"missing in committed: {child.relative_to(freshly_built)}")
            return
        if not right.exists():
            for child in left.rglob("*"):
                if child.is_file():
                    differences.append(f"missing in fresh build: {child.relative_to(committed)}")
            return
        cmp = filecmp.dircmp(left, right)
        for name in cmp.left_only:
            differences.append(f"only in committed (stale): {(rel / name).as_posix()}")
        for name in cmp.right_only:
            differences.append(f"only in fresh build (new): {(rel / name).as_posix()}")
        for name in cmp.diff_files:
            differences.append(f"content differs: {(rel / name).as_posix()}")
        for name in cmp.common_dirs:
            _walk(rel / name)

    _walk(Path("."))
    return sorted(set(differences))


def _add_concepts(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    p = subparsers.add_parser(
        "concepts",
        help="Concept-corpus analyzer (census, candidate-cluster suggestions, drift check).",
    )
    concepts_subs = p.add_subparsers(dest="concepts_cmd", required=True)

    c = concepts_subs.add_parser(
        "census",
        help=(
            "Walk every committed inventory and emit a flat catalogue of leaf fields "
            "(CSV + Markdown summary). Default output dir: docs/concepts-analysis/."
        ),
    )
    c.add_argument("--repo-root", type=Path, default=Path.cwd())
    c.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Output directory. Defaults to <repo-root>/docs/concepts-analysis.",
    )
    c.set_defaults(func=_cmd_concepts_census)

    s = concepts_subs.add_parser(
        "suggest",
        help=(
            "Cluster census rows into candidate concepts across standards and write "
            "a Markdown review report. Pass --semantic to additionally run the "
            "sentence-transformers embedding pass (requires the concepts-ml extra)."
        ),
    )
    s.add_argument("--repo-root", type=Path, default=Path.cwd())
    s.add_argument("--output-dir", type=Path, default=None)
    s.add_argument(
        "--semantic",
        action="store_true",
        help=(
            "Also run the embedding-based semantic clustering pass. Requires "
            "the [concepts-ml] extra; writes suggestions-semantic.md."
        ),
    )
    s.add_argument(
        "--threshold",
        type=float,
        default=CONCEPTS_DEFAULT_THRESHOLD,
        help=(
            f"Cosine threshold for semantic clustering "
            f"(default {CONCEPTS_DEFAULT_THRESHOLD}). Higher = stricter."
        ),
    )
    s.add_argument(
        "--model",
        default=CONCEPTS_DEFAULT_MODEL,
        help=f"sentence-transformers model name (default {CONCEPTS_DEFAULT_MODEL}).",
    )
    s.set_defaults(func=_cmd_concepts_suggest)

    k = concepts_subs.add_parser(
        "check",
        help=(
            "Re-run census + suggest into a temp directory and diff against the "
            "committed docs/concepts-analysis/. Exits non-zero if anything differs. "
            "Pass --semantic to also regenerate and diff the semantic report."
        ),
    )
    k.add_argument("--repo-root", type=Path, default=Path.cwd())
    k.add_argument(
        "--semantic",
        action="store_true",
        help=(
            "Also regenerate suggestions-semantic.md and include it in the diff. "
            "Requires the [concepts-ml] extra."
        ),
    )
    k.add_argument("--threshold", type=float, default=CONCEPTS_DEFAULT_THRESHOLD)
    k.add_argument("--model", default=CONCEPTS_DEFAULT_MODEL)
    k.set_defaults(func=_cmd_concepts_check)

    sc = concepts_subs.add_parser(
        "scaffold",
        help=(
            "Generate a draft crosswalks/concepts/<name>.yaml from a cluster. "
            "Pass --cluster <key> to auto-pickup a string-match cluster, or "
            "--field <std>=<path> (repeatable) to specify rows explicitly."
        ),
    )
    sc.add_argument("name", help="Canonical concept name (lowercase snake_case).")
    sc.add_argument("--repo-root", type=Path, default=Path.cwd())
    sc.add_argument(
        "--cluster",
        default=None,
        help=(
            "Cluster canonical_key (e.g. 'last_name') from the string-match "
            "suggestions report. The scaffolder collects every census row "
            "whose normalized leaf name matches."
        ),
    )
    sc.add_argument(
        "--field",
        action="append",
        default=[],
        help=(
            "Explicit per-standard mapping in the form <standard>=<path>. "
            "Repeatable. Overrides --cluster when both are given."
        ),
    )
    sc.set_defaults(func=_cmd_concepts_scaffold)


def _cmd_concepts_census(args: argparse.Namespace) -> int:
    repo_root = args.repo_root.resolve()
    out_dir = (
        args.output_dir.resolve()
        if args.output_dir is not None
        else repo_root / CONCEPTS_OUTPUT_DEFAULT
    )
    rows = collect_census(repo_root)
    write_census_csv(rows, out_dir)
    write_census_summary(rows, out_dir)
    print(f"Wrote {len(rows):,} rows to {(out_dir / 'field-census.csv')}")
    return 0


def _cmd_concepts_suggest(args: argparse.Namespace) -> int:
    repo_root = args.repo_root.resolve()
    out_dir = (
        args.output_dir.resolve()
        if args.output_dir is not None
        else repo_root / CONCEPTS_OUTPUT_DEFAULT
    )
    rows = collect_census(repo_root)
    crosswalks = load_crosswalks(repo_root)
    clusters = suggest_clusters(rows, crosswalks)
    write_suggestions(clusters, out_dir)
    uncovered = sum(1 for c in clusters if c.already_covered_by is None)
    print(
        f"Wrote {len(clusters)} clusters ({uncovered} uncovered) "
        f"to {(out_dir / 'suggestions.md')}"
    )

    if args.semantic:
        encoder = make_encoder(args.model)
        semantic_clusters = suggest_semantic_clusters(
            rows, crosswalks, encoder=encoder, threshold=args.threshold
        )
        write_semantic_suggestions(
            semantic_clusters, out_dir, model_name=args.model, threshold=args.threshold
        )
        semantic_uncovered = sum(
            1 for c in semantic_clusters if c.already_covered_by is None
        )
        print(
            f"Wrote {len(semantic_clusters)} semantic clusters "
            f"({semantic_uncovered} uncovered) to "
            f"{(out_dir / CONCEPTS_SEMANTIC_FILENAME)}"
        )
    return 0


def _cmd_concepts_check(args: argparse.Namespace) -> int:
    import tempfile

    repo_root = args.repo_root.resolve()
    committed = repo_root / CONCEPTS_OUTPUT_DEFAULT

    with tempfile.TemporaryDirectory(prefix="cora-concepts-check-") as tmp:
        tmp_path = Path(tmp)
        rows = collect_census(repo_root)
        write_census_csv(rows, tmp_path)
        write_census_summary(rows, tmp_path)
        crosswalks = load_crosswalks(repo_root)
        clusters = suggest_clusters(rows, crosswalks)
        write_suggestions(clusters, tmp_path)

        if args.semantic:
            encoder = make_encoder(args.model)
            semantic_clusters = suggest_semantic_clusters(
                rows, crosswalks, encoder=encoder, threshold=args.threshold
            )
            write_semantic_suggestions(
                semantic_clusters,
                tmp_path,
                model_name=args.model,
                threshold=args.threshold,
            )
        else:
            # Don't ask the diff to flag the committed semantic file as
            # "missing in fresh build" when the gate isn't running the
            # semantic pass — copy it over before diffing.
            committed_semantic = committed / CONCEPTS_SEMANTIC_FILENAME
            if committed_semantic.exists():
                import shutil

                shutil.copy(committed_semantic, tmp_path / CONCEPTS_SEMANTIC_FILENAME)

        differences = _diff_dirs(committed, tmp_path)
        if differences:
            cmd_hint = (
                "`cora concepts census`, `cora concepts suggest`, "
                "and `cora concepts suggest --semantic`"
                if args.semantic
                else "`cora concepts census` and `cora concepts suggest`"
            )
            print(f"docs/concepts-analysis/ is out of date — regenerate with {cmd_hint}:")
            for d in differences:
                print(f"  - {d}")
            return 1
    return 0


def _cmd_concepts_scaffold(args: argparse.Namespace) -> int:
    repo_root = args.repo_root.resolve()
    name: str = args.name
    rows = collect_census(repo_root)

    selected_rows: list[object]
    if args.field:
        # Explicit per-standard paths: --field mits=NameType/LastName
        wanted: dict[str, str] = {}
        for spec in args.field:
            if "=" not in spec:
                print(f"--field {spec!r} must be in the form <standard>=<path>")
                return 2
            std, path = spec.split("=", 1)
            wanted[std.strip()] = path.strip()
        by_key = {(r.standard, r.path): r for r in rows}
        selected_rows = []
        missing: list[str] = []
        for std, path in wanted.items():
            row = by_key.get((std, path))
            if row is None:
                missing.append(f"{std}:{path}")
            else:
                selected_rows.append(row)
        if missing:
            print("the following --field paths were not found in any committed inventory:")
            for m in missing:
                print(f"  - {m}")
            return 2
    elif args.cluster:
        key = args.cluster
        selected_rows = [r for r in rows if normalize_leaf(r.leaf_name) == key]
        if not selected_rows:
            print(
                f"no rows match the cluster key {key!r}. Run "
                f"`cora concepts suggest --repo-root {args.repo_root}` and pick "
                f"a key from the report."
            )
            return 2
    else:
        print("scaffold requires either --cluster <key> or one or more --field args.")
        return 2

    all_standards = sorted({r.standard for r in rows})
    standards_present = sorted({r.standard for r in selected_rows})  # type: ignore[attr-defined]
    out = write_scaffold(
        name,
        selected_rows,  # type: ignore[arg-type]
        standards_present=standards_present,
        all_standards=all_standards,
        repo_root=repo_root,
    )
    print(f"Wrote draft crosswalk to {out}")
    print(
        "TODO markers remain in the file — fill in canonical_definition, "
        "confidence per mapping, narrative notes, and aliases before committing."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
