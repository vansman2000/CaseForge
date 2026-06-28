"""
Evidence Service

Imports evidence into the current case.
"""

from datetime import datetime
from pathlib import Path
import shutil

from caseforge.models.evidence import Evidence
from caseforge.repositories.evidence_repository import EvidenceRepository


class EvidenceService:
    """Handles importing evidence into a CaseForge project."""

    FILE_TYPES = {
        ".jpg": "Photos",
        ".jpeg": "Photos",
        ".png": "Photos",
        ".gif": "Photos",
        ".bmp": "Photos",

        ".pdf": "Documents",
        ".doc": "Documents",
        ".docx": "Documents",
        ".txt": "Documents",

        ".mp3": "Audio",
        ".wav": "Audio",
        ".m4a": "Audio",

        ".mp4": "Video",
        ".mov": "Video",
        ".avi": "Video",
    }

    def import_files(self, case, files):
        """
        Import files into the appropriate folders and
        save them to the database.
        """

        repository = EvidenceRepository(
            case.root / "case.db"
        )

        imported = []

        for filename in files:

            source = Path(filename)

            extension = source.suffix.lower()

            folder = self.FILE_TYPES.get(
                extension,
                "Evidence",
            )

            destination = (
                case.root /
                folder /
                source.name
            )

            destination.parent.mkdir(
                parents=True,
                exist_ok=True,
            )

            shutil.copy2(source, destination)

            evidence = Evidence(
                filename=destination.name,
                path=destination,
                evidence_type=folder,
                imported=datetime.now(),
            )

            repository.save(evidence)

            imported.append(evidence)

        return imported