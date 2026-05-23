"""Validator seam.

A Validator inspects committed artifacts (inventories, crosswalks, ...)
and reports problems as a structured ValidationResult. The CLI exposes
a single ``cora validate`` entrypoint that dispatches to registered
adapters.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal, Protocol, runtime_checkable

Severity = Literal["error", "warning", "info"]


@dataclass(frozen=True)
class Finding:
    """One issue raised by a Validator."""

    severity: Severity
    location: str
    message: str


@dataclass
class ValidationResult:
    """Aggregated findings from a single Validator run."""

    findings: list[Finding] = field(default_factory=list)

    @property
    def has_errors(self) -> bool:
        return any(f.severity == "error" for f in self.findings)

    def add(self, severity: Severity, location: str, message: str) -> None:
        self.findings.append(Finding(severity=severity, location=location, message=message))


@runtime_checkable
class Validator(Protocol):
    """A named check that runs against the repository state."""

    name: str

    def check(self, repo_root: Path) -> ValidationResult: ...
