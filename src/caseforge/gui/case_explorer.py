"""
Case Explorer

Displays the navigation tree for the current case.
"""

from datetime import datetime
from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTreeWidget, QTreeWidgetItem

from caseforge.models.evidence import Evidence


class CaseExplorer(QTreeWidget):
    """Navigation tree displayed on the left side of the application."""

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

    def __init__(self):
        super().__init__()

        self.setHeaderHidden(True)

    def load_case(self, case) -> None:
        """Display a CaseForge project."""

        self.clear()

        case_item = QTreeWidgetItem([case.name])
        self.addTopLevelItem(case_item)

        for folder in sorted(case.root.iterdir()):

            if not folder.is_dir():
                continue

            folder_item = QTreeWidgetItem([folder.name])
            case_item.addChild(folder_item)

            for file in sorted(folder.iterdir()):

                if not file.is_file():
                    continue

                evidence = Evidence(
                    filename=file.name,
                    path=file,
                    evidence_type=self.FILE_TYPES.get(
                        file.suffix.lower(),
                        folder.name,
                    ),
                    imported=datetime.fromtimestamp(
                        file.stat().st_ctime
                    ),
                )

                file_item = QTreeWidgetItem(
                    [evidence.display_name]
                )

                # Store the Evidence object instead of a path
                file_item.setData(
                    0,
                    Qt.UserRole,
                    evidence,
                )

                folder_item.addChild(file_item)

            folder_item.setExpanded(True)

        case_item.setExpanded(True)