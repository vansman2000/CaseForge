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

        self._populate()

    def _populate(self) -> None:

        case = QTreeWidgetItem(["My Case"])

        evidence = QTreeWidgetItem(["Evidence"])
        photos = QTreeWidgetItem(["Photos"])
        pdfs = QTreeWidgetItem(["PDF Documents"])
        audio = QTreeWidgetItem(["Audio"])
        transcripts = QTreeWidgetItem(["Transcripts"])

        evidence.addChildren([
            photos,
            pdfs,
            audio,
            transcripts,
        ])

        timeline = QTreeWidgetItem(["Timeline"])
        damages = QTreeWidgetItem(["Damages"])
        reports = QTreeWidgetItem(["Reports"])
        binder = QTreeWidgetItem(["Binder"])

        case.addChildren([
            evidence,
            timeline,
            damages,
            reports,
            binder,
        ])

        self.addTopLevelItem(case)

        case.setExpanded(True)
        evidence.setExpanded(True)