"""Field-count Validator adapter.

Asserts every committed ``standards/*/current/inventory/*.yaml`` has at
least N fields, where N is either a per-inventory override or a default.
Catches silently empty extractions (e.g., wrong config columns, broken
includes) that would slip past schema validation.
"""

from __future__ import annotations

from pathlib import Path

import yaml
from pydantic import BaseModel, ConfigDict, Field

from cora_extractors.inventory import Inventory
from cora_extractors.validator import ValidationResult

INVENTORY_GLOB = "standards/*/current/inventory/*.yaml"
DEFAULT_CONFIG_PATH = Path("tools/extractors/configs/field-count-minimums.yaml")


class FieldCountMinimumsConfig(BaseModel):
    """Per-inventory field-count minimums.

    ``overrides`` is keyed by ``"<standard>/<module>"`` (e.g.
    ``"mits/property-marketing"``). Any inventory without an override
    must clear ``default_minimum``.
    """

    model_config = ConfigDict(extra="forbid")

    default_minimum: int = Field(default=5, ge=0)
    overrides: dict[str, int] = Field(default_factory=dict)

    @classmethod
    def load(cls, path: Path) -> FieldCountMinimumsConfig:
        if not path.exists():
            return cls()
        data = yaml.safe_load(path.read_text()) or {}
        return cls.model_validate(data)


class FieldCountValidator:
    """Validator adapter at the ``Validator`` seam."""

    name = "field-count"

    def check(self, repo_root: Path) -> ValidationResult:
        result = ValidationResult()
        config = FieldCountMinimumsConfig.load(repo_root / DEFAULT_CONFIG_PATH)

        inventories = sorted(repo_root.glob(INVENTORY_GLOB))
        for inv_path in inventories:
            try:
                inventory = Inventory.from_yaml(inv_path)
            except Exception as exc:  # pragma: no cover - belt-and-braces
                result.add("error", str(inv_path), f"failed to load: {exc}")
                continue

            key = f"{inventory.standard}/{inventory.module}"
            minimum = config.overrides.get(key, config.default_minimum)
            count = len(inventory.fields)
            if count < minimum:
                result.add(
                    "error",
                    str(inv_path),
                    f"{key}: {count} fields, below minimum {minimum}",
                )
        return result
