"""
Case model.
"""

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


@dataclass(slots=True)
class Case:
    """Represents an open CaseForge project."""

    name: str
    root: Path
    created: datetime