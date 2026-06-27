"""
Case Explorer

Displays the navigation tree for the current case.
"""

from PySide6.QtWidgets import QTreeWidget, QTreeWidgetItem


class CaseExplorer(QTreeWidget):
    """Navigation tree displayed on the left side of the application."""

    def __init__(self):
        super().__init__()

        self.setHeaderHidden(True)

    def load_case(self, case) -> None:
        """Display a CaseForge project."""

        self.clear()

        root = QTreeWidgetItem([case.name])

        folders = [
            "Evidence",
            "Photos",
            "Audio",
            "Video",
            "Documents",
            "Exhibits",
        ]

        for folder in folders:
            root.addChild(QTreeWidgetItem([folder]))

        self.addTopLevelItem(root)

        root.setExpanded(True)