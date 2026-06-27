"""
Evidence Service

Imports evidence into the current case.
"""

from pathlib import Path
import shutil


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
        Import files into the appropriate folders.

        Returns a list of imported file paths.
        """

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

            shutil.copy2(source, destination)

            imported.append(destination)

        return imported