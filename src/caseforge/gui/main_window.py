from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QDockWidget,
    QMainWindow,
    QTextEdit,
)

from caseforge.gui.menu_bar import build_menu_bar
from caseforge.gui.status_bar import build_status_bar
from caseforge.gui.case_explorer import CaseExplorer
from caseforge.gui.preview_panel import PreviewPanel
from caseforge.gui.properties_panel import PropertiesPanel


class MainWindow(QMainWindow):
    """Main application window."""

    def __init__(self):
        super().__init__()

        self.setWindowTitle("CaseForge")
        self.resize(1600, 900)

        self._create_ui()

    def _create_ui(self):

        build_menu_bar(self)

        self.setStatusBar(build_status_bar())

        self.preview = PreviewPanel()
        self.setCentralWidget(self.preview)

        self.case_explorer = CaseExplorer()

        dock = QDockWidget("Case Explorer", self)
        dock.setWidget(self.case_explorer)
        dock.setMinimumWidth(250)

        self.addDockWidget(Qt.LeftDockWidgetArea, dock)

        self.properties = PropertiesPanel()

        dock = QDockWidget("Properties", self)
        dock.setWidget(self.properties)
        dock.setMinimumWidth(300)

        self.addDockWidget(Qt.RightDockWidgetArea, dock)