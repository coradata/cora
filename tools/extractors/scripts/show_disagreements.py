"""Inspect multi-source disagreements in an enriched inventory.

Reports per-attribute provenance entries where claims disagree (one source
overrode another), plus the count and a sample of unmatched enrichments.

Usage:
    .venv/bin/python tools/extractors/scripts/show_disagreements.py \\
        standards/mits/current/inventory/lead-management.yaml \\
        [--attribute definition] [--attribute range] [--unmatched-sample 10]

When --attribute is omitted, all enrichable attributes are surfaced. Useful
for spot-checking what Excel changed before merging a Phase 3c-style PR;
also useful after re-running the enrich pipeline to see what shifted.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from cora_extractors.inventory import Inventory


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0] if __doc__ else None)
    parser.add_argument("inventory", type=Path, help="Path to an enriched inventory YAML.")
    parser.add_argument(
        "--attribute",
        action="append",
        default=[],
        help=(
            "Restrict to disagreements on these attributes (e.g. --attribute definition). "
            "Pass multiple times to allow multiple; omit to show all."
        ),
    )
    parser.add_argument(
        "--unmatched-sample",
        type=int,
        default=5,
        help="How many unmatched_enrichments rows to print (default 5; 0 to suppress).",
    )
    args = parser.parse_args(argv)

    inv = Inventory.from_yaml(args.inventory)
    attr_filter: set[str] | None = set(args.attribute) if args.attribute else None

    rows: list[tuple[str, str, str, list[tuple[str, str]]]] = []
    for f in inv.fields:
        for p in f.provenance or []:
            if p.chosen is None:
                continue  # agreement, no decision
            if attr_filter is not None and p.attribute not in attr_filter:
                continue
            leaf = f.path.split("/")[-1]
            domain = f.domain or "(no domain)"
            claims = [(c.source, _short(c.value)) for c in p.claims]
            rows.append((domain, leaf, p.attribute, claims))

    print(f"{inv.standard}/{inv.module} — {len(inv.fields)} fields total")
    print(f"  source_label: {inv.source_label}")
    if attr_filter:
        print(f"  filtered to attributes: {sorted(attr_filter)}")
    print(f"  disagreements: {len(rows)}")
    for domain, leaf, attr, claims in rows:
        chosen = next((c[0] for c in claims if c[1] == _short(_get_top_level(inv, domain, leaf, attr))), "?")
        print(f"\n  [{attr}] {domain}/{leaf}  (chosen: {chosen})")
        for source, value in claims:
            marker = "* " if source == chosen else "  "
            print(f"    {marker}{source}: {value}")

    um = inv.unmatched_enrichments or []
    print(f"\n  unmatched_enrichments: {len(um)}")
    if args.unmatched_sample > 0:
        for u in um[: args.unmatched_sample]:
            domain = u.domain or "(no domain)"
            print(f"    [{u.source}] {domain}/{u.field}  ({u.location or '?'})")
        if len(um) > args.unmatched_sample:
            print(f"    ... and {len(um) - args.unmatched_sample} more")
    return 0


def _short(value: object) -> str:
    s = repr(value)
    if len(s) > 80:
        return s[:77] + "..."
    return s


def _get_top_level(inv: Inventory, domain: str, leaf: str, attr: str) -> object:
    for f in inv.fields:
        if (f.domain or "(no domain)") == domain and f.path.split("/")[-1] == leaf:
            return getattr(f, attr, None)
    return None


if __name__ == "__main__":
    sys.exit(main())
