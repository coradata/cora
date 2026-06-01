"""Crosswalk-paths Validator adapter.

For each ``crosswalks/concepts/*.yaml`` mapping that isn't ``not_present``,
asserts that ``mappings.<standard>.field`` resolves against at least one
``standards/<standard>/current/inventory/*.yaml`` via
``cora_extractors.path.resolve``. Catches typos and stale references when
inventories change.

Sanity checks:
- ``confidence: not_present`` requires ``field: null`` (and vice versa).
- ``confidence in {divergent, not_present}`` requires a ``notes`` narrative.
"""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path

import yaml

from cora_extractors.inventory import Inventory
from cora_extractors.path import resolve as resolve_path
from cora_extractors.validator import ValidationResult

CROSSWALK_GLOB = "crosswalks/concepts/*.yaml"
INVENTORY_GLOB = "standards/*/current/inventory/*.yaml"


class CrosswalkPathsValidator:
    """Validator adapter at the ``Validator`` seam."""

    name = "crosswalk-paths"

    def check(self, repo_root: Path) -> ValidationResult:
        result = ValidationResult()

        inventories: dict[str, list[Inventory]] = defaultdict(list)
        for yp in sorted(repo_root.glob(INVENTORY_GLOB)):
            std = yp.parts[-4]
            try:
                inventories[std].append(Inventory.from_yaml(yp))
            except Exception as exc:
                result.add(
                    "warning",
                    str(yp.relative_to(repo_root)),
                    f"failed to load inventory: {exc}",
                )

        crosswalks = sorted(repo_root.glob(CROSSWALK_GLOB))
        if not crosswalks:
            result.add(
                "info",
                "crosswalks/concepts/",
                "no crosswalks found to validate (empty directory)",
            )
            return result

        for cw_path in crosswalks:
            location = str(cw_path.relative_to(repo_root))
            try:
                data = yaml.safe_load(cw_path.read_text()) or {}
            except yaml.YAMLError as exc:
                result.add("error", location, f"YAML parse error: {exc}")
                continue

            concept = data.get("concept", "(unknown)")
            mappings = data.get("mappings", {})
            if not isinstance(mappings, dict):
                result.add(
                    "error", location, f"{concept!r}: mappings must be an object"
                )
                continue

            for std, mapping in mappings.items():
                if not isinstance(mapping, dict):
                    result.add(
                        "error",
                        location,
                        f"{concept!r}: mappings.{std} must be an object",
                    )
                    continue
                _check_mapping(
                    result=result,
                    location=location,
                    concept=concept,
                    std=std,
                    mapping=mapping,
                    inventories=inventories.get(std, []),
                )

        return result


def _check_mapping(
    *,
    result: ValidationResult,
    location: str,
    concept: str,
    std: str,
    mapping: dict[str, object],
    inventories: list[Inventory],
) -> None:
    confidence = mapping.get("confidence")
    field = mapping.get("field")
    notes = mapping.get("notes")

    # Schema-level invariants the JSON Schema can't enforce.
    if confidence == "not_present":
        if field is not None:
            result.add(
                "error",
                location,
                f"{concept!r}: mappings.{std}.field must be null when confidence=not_present",
            )
        if not notes:
            result.add(
                "error",
                location,
                f"{concept!r}: mappings.{std}.notes required when confidence=not_present",
            )
        return  # nothing to resolve

    if confidence == "divergent" and not notes:
        result.add(
            "error",
            location,
            f"{concept!r}: mappings.{std}.notes required when confidence=divergent",
        )

    if field is None:
        result.add(
            "error",
            location,
            f"{concept!r}: mappings.{std}.field is null but confidence is {confidence!r}",
        )
        return
    if not isinstance(field, str):
        result.add(
            "error",
            location,
            f"{concept!r}: mappings.{std}.field must be a string (got {type(field).__name__})",
        )
        return

    if not inventories:
        result.add(
            "error",
            location,
            f"{concept!r}: mappings.{std} references a standard with no committed inventories",
        )
        return

    if not any(resolve_path(field, inv) is not None for inv in inventories):
        modules = ", ".join(inv.module for inv in inventories)
        result.add(
            "error",
            location,
            f"{concept!r}: mappings.{std}.field {field!r} not found in any "
            f"{std} inventory (searched modules: {modules})",
        )
