"""
Case Explorer

Displays the navigation tree for the current case.
"""

from pathlib import Path

from PySide6.QtWidgets import QTreeWidget, QTreeWidgetItem


class CaseExplorer(QTreeWidget):
    """Navigation tree displayed on the left side of the application."""

    def __init__(self):
        super().__init__()

        self.setHeaderHidden(True)

    def load_case(self, case) -> None:
        """Display a CaseForge project."""

        self.clear()

        case_item = QTreeWidgetItem([case.name])
        self.addTopLevelItem(case_item)

        # Show every folder in the case
        for folder in sorted(case.root.iterdir()):

            if not folder.is_dir():
                continue

            folder_item = QTreeWidgetItem([folder.name])
            case_item.addChild(folder_item)

            # Show every file in that folder
            for file in sorted(folder.iterdir()):

                if file.is_file():
                    file_item = QTreeWidgetItem([file.name])
                    folder_item.addChild(file_item)

            folder_item.setExpanded(True)

        case_item.setExpanded(True)