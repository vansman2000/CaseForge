"""
Evidence model.

Represents one piece of evidence in a CaseForge project.
"""

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path


@dataclass(slots=True)
class Evidence:
    """Represents a single evidence item."""

    filename: str

    path: Path

    evidence_type: str

    imported: datetime

    title: str = ""

    exhibit_number: int | None = None

    notes: str = ""

    tags: list[str] = field(default_factory=list)

    @property
    def display_name(self) -> str:
        """Return the best name to display."""

        return self.title if self.title else self.filename