"""
Case Service

Responsible for creating and loading CaseForge projects.
"""

from datetime import datetime
from pathlib import Path

from caseforge.project.case import Case
from caseforge.repositories.evidence_repository import EvidenceRepository


class CaseService:
    """Handles project creation and loading."""

    def create_case(self, parent_directory: Path, case_name: str) -> Case:
        project_root = parent_directory / f"{case_name}.caseforge"

        project_root.mkdir(parents=True, exist_ok=True)

        folders = [
            "Evidence",
            "Documents",
            "Photos",
            "Audio",
            "Video",
            "Exhibits",
        ]

        for folder in folders:
            (project_root / folder).mkdir(exist_ok=True)

        (project_root / "settings.json").write_text(
            "{\n"
            f'  "name": "{case_name}"\n'
            "}\n",
            encoding="utf-8",
        )

        database_path = project_root / "case.db"

        # Initialize the SQLite database and schema.
        EvidenceRepository(database_path)

        return Case(
            name=case_name,
            root=project_root,
            created=datetime.now(),
        )