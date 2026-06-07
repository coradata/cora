"""Candidate-concept clustering across standards.

Cheap version: normalize leaf names (camelCase + separators → snake_case),
bucket by normalized form, keep clusters that touch ≥2 distinct standards.
Annotate each cluster with a definition-Jaccard quality signal across
standard pairs and a flag indicating whether an existing crosswalk already
covers the cluster (matched by canonical name or alias, both normalized).

Future work (Phase 6c): embeddings-based clustering for semantic matches
the string-similarity pass misses.
"""

from __future__ import annotations

import re
from collections import defaultdict
from dataclasses import dataclass
from itertools import product

from cora_extractors.concepts.census import CensusRow
from cora_extractors.generators._common import Crosswalk

_WORD_RE = re.compile(r"[A-Za-z][A-Za-z0-9]*")
_CAMEL_BOUNDARY_RE = re.compile(r"(?<!^)(?=[A-Z])")


@dataclass(frozen=True)
class Cluster:
    """A candidate concept cluster — fields likely the same concept across ≥2 standards."""

    canonical_key: str
    rows: tuple[CensusRow, ...]
    standards: tuple[str, ...]
    avg_def_jaccard: float
    already_covered_by: str | None


def normalize_leaf(name: str) -> str:
    """Normalize a leaf field name to a canonical key.

    Replaces hyphens/spaces with underscores, splits camelCase at uppercase
    boundaries, lowercases, and collapses runs of underscores.

    Examples:
        ``PostalCode``     -> ``postal_code``
        ``Zip_Postal_Code``-> ``zip_postal_code``
        ``Email-Address``  -> ``email_address``
    """
    with_seps = name.replace("-", "_").replace(" ", "_")
    snake = _CAMEL_BOUNDARY_RE.sub("_", with_seps)
    snake = re.sub(r"_+", "_", snake).strip("_").lower()
    return snake


def suggest_clusters(
    rows: list[CensusRow], crosswalks: list[Crosswalk] | None = None
) -> list[Cluster]:
    """Bucket census rows by normalized leaf name; keep ≥2-standard clusters."""
    coverage = _crosswalk_coverage(crosswalks or [])

    buckets: dict[str, list[CensusRow]] = defaultdict(list)
    for row in rows:
        buckets[normalize_leaf(row.leaf_name)].append(row)

    clusters: list[Cluster] = []
    for key, bucket_rows in buckets.items():
        stds = tuple(sorted({r.standard for r in bucket_rows}))
        if len(stds) < 2:
            continue
        ordered = tuple(sorted(bucket_rows, key=lambda r: (r.standard, r.module, r.path)))
        clusters.append(
            Cluster(
                canonical_key=key,
                rows=ordered,
                standards=stds,
                avg_def_jaccard=_avg_cross_standard_jaccard(ordered),
                already_covered_by=coverage.get(key),
            )
        )
    # Sort: uncovered first (actionable), then by # standards descending, then by key.
    clusters.sort(
        key=lambda c: (c.already_covered_by is not None, -len(c.standards), c.canonical_key)
    )
    return clusters


def _tokens(definition: str) -> set[str]:
    """Alphabetic word tokens for Jaccard."""
    return {m.group(0).lower() for m in _WORD_RE.finditer(definition)}


def _jaccard(a: set[str], b: set[str]) -> float:
    if not a and not b:
        return 1.0
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def _avg_cross_standard_jaccard(rows: tuple[CensusRow, ...]) -> float:
    """Average pairwise Jaccard on definitions across distinct-standard row pairs."""
    by_std: dict[str, list[CensusRow]] = defaultdict(list)
    for r in rows:
        by_std[r.standard].append(r)
    stds = sorted(by_std)
    pairs: list[float] = []
    for i, sa in enumerate(stds):
        for sb in stds[i + 1 :]:
            for ra, rb in product(by_std[sa], by_std[sb]):
                pairs.append(_jaccard(_tokens(ra.definition), _tokens(rb.definition)))
    return sum(pairs) / len(pairs) if pairs else 0.0


def _crosswalk_coverage(crosswalks: list[Crosswalk]) -> dict[str, str]:
    """Map every normalized concept/alias key to its canonical concept name."""
    coverage: dict[str, str] = {}
    for cw in crosswalks:
        coverage[normalize_leaf(cw.concept)] = cw.concept
        for alias in cw.aliases:
            coverage[normalize_leaf(alias)] = cw.concept
    return coverage
