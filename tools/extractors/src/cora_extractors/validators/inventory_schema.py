"""Inventory schema Validator adapter.

Runs JSON Schema validation plus structural-invariant checks
(``Inventory.validate_structure()``) over every committed
``standards/*/current/inventory/*.yaml``.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator
from pydantic import ValidationError

from cora_extractors.inventory import Inventory, StructuralError
from cora_extractors.validator import ValidationResult

SCHEMA_RELATIVE = Path("tools/extractors/schema/inventory.schema.json")
INVENTORY_GLOB = "standards/*/current/inventory/*.yaml"


class InventorySchemaValidator:
    """Validate every committed inventory against schema + structural invariants."""

    name = "inventory-schema"

    def check(self, repo_root: Path) -> ValidationResult:
        result = ValidationResult()
        schema_path = repo_root / SCHEMA_RELATIVE
        if not schema_path.exists():
            result.add(
                "error",
                str(schema_path),
                "inventory schema file is missing — cannot run validator",
            )
            return result

        schema = json.loads(schema_path.read_text())
        validator = Draft202012Validator(schema)

        inventories = sorted(repo_root.glob(INVENTORY_GLOB))
        for inv_path in inventories:
            self._check_one(inv_path, validator, result)
        return result

    def _check_one(
        self,
        inv_path: Path,
        validator: Draft202012Validator,
        result: ValidationResult,
    ) -> None:
        try:
            data: Any = yaml.safe_load(inv_path.read_text())
        except yaml.YAMLError as exc:
            result.add("error", str(inv_path), f"YAML parse failed: {exc}")
            return

        schema_errors = sorted(validator.iter_errors(data), key=lambda e: list(e.path))
        for err in schema_errors:
            ptr = "/".join(str(p) for p in err.path) or "<root>"
            result.add("error", f"{inv_path}#{ptr}", f"schema: {err.message}")

        if schema_errors:
            return

        try:
            inventory = Inventory.model_validate(data)
        except ValidationError as exc:
            result.add("error", str(inv_path), f"pydantic: {exc}")
            return

        try:
            inventory.validate_structure()
        except StructuralError as exc:
            for issue in exc.issues:
                result.add("error", str(inv_path), f"structural: {issue}")
