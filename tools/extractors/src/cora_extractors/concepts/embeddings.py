"""Semantic-clustering pass for the concepts analyzer.

The Phase 6a string-similarity bucketer catches matches whose normalized
leaf names are identical (``PostalCode`` ↔ ``Zip_Postal_Code`` is *not*
caught — different normalized keys). Phase 6c adds a semantic pass that
encodes each field's ``leaf_name :: definition`` with a sentence-embedding
model and clusters by cosine similarity. Catches matches like
``MoveInDate`` ↔ ``LeaseStartDate`` and ``RentAmount`` ↔ ``MonthlyRent``.

The module is import-safe without the ML stack installed — the encoder
factory raises a clear ImportError that the CLI handler turns into a
user-friendly message ("install with the [concepts-ml] extra"). The
``EmbeddingSuggester`` itself takes an ``EmbeddingEncoder`` protocol so
unit tests can stub the model.
"""

from __future__ import annotations

import math
from collections import defaultdict
from collections.abc import Sequence
from dataclasses import dataclass
from typing import Protocol

from cora_extractors.concepts.census import CensusRow
from cora_extractors.concepts.suggest import (
    _avg_cross_standard_jaccard,
    _crosswalk_coverage,
    normalize_leaf,
)
from cora_extractors.generators._common import Crosswalk

DEFAULT_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
DEFAULT_THRESHOLD = 0.78


class EmbeddingEncoder(Protocol):
    """Minimal interface the semantic suggester depends on.

    Implementations: ``SentenceTransformerEncoder`` (production), or any
    stub a test wants. ``encode`` returns one float vector per input text;
    vectors are expected to be L2-normalized so cosine similarity reduces
    to a dot product.
    """

    def encode(self, texts: Sequence[str]) -> list[list[float]]: ...


@dataclass(frozen=True)
class SemanticCluster:
    """A semantic-similarity cluster across ≥2 standards.

    Sibling of ``concepts.suggest.Cluster`` but explicit about the source
    (so the report writer can render the two pools differently). The
    ``avg_cosine`` field carries the mean pairwise cosine within the
    cluster as a quality signal.
    """

    canonical_key: str
    rows: tuple[CensusRow, ...]
    standards: tuple[str, ...]
    avg_cosine: float
    avg_def_jaccard: float
    already_covered_by: str | None


def make_encoder(model_name: str = DEFAULT_MODEL) -> EmbeddingEncoder:
    """Load the production sentence-transformers encoder.

    Raises ImportError with a useful message if the ML extra isn't
    installed. The model file is downloaded on first use and cached in
    the standard HuggingFace cache.
    """
    try:
        from sentence_transformers import SentenceTransformer
    except ImportError as exc:  # pragma: no cover — exercised manually
        raise ImportError(
            "sentence-transformers is not installed. Install the optional "
            "extra with: pip install -e 'tools/extractors[concepts-ml]'"
        ) from exc

    model = SentenceTransformer(model_name)

    class _Encoder:
        def encode(self, texts: Sequence[str]) -> list[list[float]]:
            arr = model.encode(
                list(texts), normalize_embeddings=True, convert_to_numpy=True
            )
            return [list(map(float, row)) for row in arr]

    return _Encoder()


def encode_inputs(rows: Sequence[CensusRow]) -> list[str]:
    """The text we feed to the encoder for each census row.

    ``leaf_name :: definition`` is a compact composite that gives the
    model both the field-name signal (which matters a lot when the
    definition is empty in the source XSD) and the prose signal (which
    matters when leaf names are too generic to disambiguate).
    """
    return [f"{row.leaf_name} :: {row.definition}".strip() for row in rows]


def suggest_semantic_clusters(
    rows: list[CensusRow],
    crosswalks: list[Crosswalk] | None = None,
    *,
    encoder: EmbeddingEncoder,
    threshold: float = DEFAULT_THRESHOLD,
) -> list[SemanticCluster]:
    """Cluster census rows by cosine similarity of their embeddings.

    Greedy connected-component clustering: build the similarity graph by
    pairing every cross-standard row pair whose cosine ≥ threshold, then
    return the connected components that touch ≥2 distinct standards.
    String-match clusters (rows that already share a normalized leaf name)
    are excluded — the Phase 6a string pass owns those.
    """
    if not rows:
        return []

    coverage = _crosswalk_coverage(crosswalks or [])
    embeddings = encoder.encode(encode_inputs(rows))
    n = len(rows)

    # Union-find over row indices.
    parent = list(range(n))

    def find(i: int) -> int:
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    def union(i: int, j: int) -> None:
        a, b = find(i), find(j)
        if a != b:
            parent[a] = b

    # Pair only across distinct standards — same-standard rows are not
    # the cross-standard matches we're hunting for.
    for i in range(n):
        for j in range(i + 1, n):
            if rows[i].standard == rows[j].standard:
                continue
            sim = _cosine(embeddings[i], embeddings[j])
            if sim >= threshold:
                union(i, j)

    # Collect components.
    groups: dict[int, list[int]] = defaultdict(list)
    for i in range(n):
        groups[find(i)].append(i)

    string_match_keys = _string_match_keys(rows)
    clusters: list[SemanticCluster] = []
    for member_idxs in groups.values():
        if len(member_idxs) < 2:
            continue
        member_rows = tuple(
            sorted(
                (rows[i] for i in member_idxs),
                key=lambda r: (r.standard, r.module, r.path),
            )
        )
        stds = tuple(sorted({r.standard for r in member_rows}))
        if len(stds) < 2:
            continue

        canonical_key = _canonical_key(member_rows)
        if canonical_key in string_match_keys:
            # Phase 6a's string-match pass already surfaced this cluster
            # under the same canonical key — leave it to that pool.
            continue

        avg_cosine = _avg_cross_standard_cosine(member_idxs, rows, embeddings)
        clusters.append(
            SemanticCluster(
                canonical_key=canonical_key,
                rows=member_rows,
                standards=stds,
                avg_cosine=avg_cosine,
                avg_def_jaccard=_avg_cross_standard_jaccard(member_rows),
                already_covered_by=coverage.get(canonical_key),
            )
        )

    clusters.sort(
        key=lambda c: (c.already_covered_by is not None, -c.avg_cosine, c.canonical_key)
    )
    return clusters


def _string_match_keys(rows: Sequence[CensusRow]) -> set[str]:
    """Normalized leaf keys that already form a ≥2-standard cluster under
    Phase 6a's bare-string bucketer. We hand those clusters off to the
    string-match report and only surface *additional* matches here."""
    by_key: dict[str, set[str]] = defaultdict(set)
    for r in rows:
        by_key[normalize_leaf(r.leaf_name)].add(r.standard)
    return {k for k, stds in by_key.items() if len(stds) >= 2}


def _canonical_key(rows: tuple[CensusRow, ...]) -> str:
    """Pick a stable, human-readable key for a semantic cluster.

    Heuristic: the most common normalized leaf name across the cluster's
    rows; tie-break by the alphabetically first one. This gives reviewers
    a meaningful name to scaffold from.
    """
    counts: dict[str, int] = defaultdict(int)
    for r in rows:
        counts[normalize_leaf(r.leaf_name)] += 1
    top_count = max(counts.values())
    return sorted(k for k, c in counts.items() if c == top_count)[0]


def _cosine(a: Sequence[float], b: Sequence[float]) -> float:
    """Cosine similarity assuming non-zero vectors. Encoder output is
    expected to be L2-normalized so this reduces to a dot product, but we
    compute the normalised form to stay correct against stub encoders."""
    dot = 0.0
    na = 0.0
    nb = 0.0
    for x, y in zip(a, b, strict=True):
        dot += x * y
        na += x * x
        nb += y * y
    if na == 0.0 or nb == 0.0:
        return 0.0
    return dot / (math.sqrt(na) * math.sqrt(nb))


def _avg_cross_standard_cosine(
    member_idxs: Sequence[int],
    rows: Sequence[CensusRow],
    embeddings: Sequence[Sequence[float]],
) -> float:
    """Mean pairwise cosine across rows from distinct standards.

    Quality signal mirroring the Jaccard one — same pair domain
    (distinct-standard pairs), different similarity measure (the
    embedding cosine that drove the cluster, not the token overlap).
    """
    pairs: list[float] = []
    for i_idx in range(len(member_idxs)):
        for j_idx in range(i_idx + 1, len(member_idxs)):
            i = member_idxs[i_idx]
            j = member_idxs[j_idx]
            if rows[i].standard == rows[j].standard:
                continue
            pairs.append(_cosine(embeddings[i], embeddings[j]))
    return sum(pairs) / len(pairs) if pairs else 0.0
