"""Concept-corpus analyzer.

Tooling that surveys the committed inventory corpus and surfaces candidate
concepts for crosswalking. Two stages:

- ``census`` — flat catalogue of every leaf field across every inventory.
- ``suggest`` — candidate concept clusters across standards, with quality
  signals (definition-Jaccard) and already-covered status.

The output is committed to ``docs/concepts-analysis/`` and reviewed by hand
during editorial passes. The tool proposes; humans decide.
"""

from __future__ import annotations

from cora_extractors.concepts.census import CensusRow, collect_census
from cora_extractors.concepts.embeddings import (
    DEFAULT_MODEL,
    DEFAULT_THRESHOLD,
    EmbeddingEncoder,
    SemanticCluster,
    make_encoder,
    suggest_semantic_clusters,
)
from cora_extractors.concepts.report import (
    CENSUS_CSV,
    CENSUS_MD,
    OUTPUT_DIR,
    SUGGESTIONS_MD,
    SUGGESTIONS_SEMANTIC_MD,
    write_census_csv,
    write_census_summary,
    write_semantic_suggestions,
    write_suggestions,
)
from cora_extractors.concepts.scaffold import scaffold_crosswalk, write_scaffold
from cora_extractors.concepts.suggest import (
    Cluster,
    normalize_leaf,
    suggest_clusters,
)

__all__ = [
    "CENSUS_CSV",
    "CENSUS_MD",
    "CensusRow",
    "Cluster",
    "DEFAULT_MODEL",
    "DEFAULT_THRESHOLD",
    "EmbeddingEncoder",
    "OUTPUT_DIR",
    "SUGGESTIONS_MD",
    "SUGGESTIONS_SEMANTIC_MD",
    "SemanticCluster",
    "collect_census",
    "make_encoder",
    "normalize_leaf",
    "scaffold_crosswalk",
    "suggest_clusters",
    "suggest_semantic_clusters",
    "write_census_csv",
    "write_census_summary",
    "write_scaffold",
    "write_semantic_suggestions",
    "write_suggestions",
]
