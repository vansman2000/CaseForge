"""
Case Explorer

Displays the navigation tree for the current case.
"""

from PySide6.QtCore import Qt
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

        for folder in sorted(case.root.iterdir()):

            if not folder.is_dir():
                continue

            folder_item = QTreeWidgetItem([folder.name])
            case_item.addChild(folder_item)

            for file in sorted(folder.iterdir()):

                if not file.is_file():
                    continue

                file_item = QTreeWidgetItem([file.name])

                # Store the full file path in the tree item
                file_item.setData(
                    0,
                    Qt.UserRole,
                    str(file),
                )

                folder_item.addChild(file_item)

            folder_item.setExpanded(True)

        case_item.setExpanded(True)