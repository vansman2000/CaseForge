from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QDockWidget,
    QMainWindow,
    QMessageBox,
)

from caseforge.gui.case_explorer import CaseExplorer
from caseforge.gui.dialogs.new_case_dialog import NewCaseDialog
from caseforge.gui.menu_bar import build_menu_bar
from caseforge.gui.preview_panel import PreviewPanel
from caseforge.gui.properties_panel import PropertiesPanel
from caseforge.gui.status_bar import build_status_bar
from caseforge.services.case_service import CaseService


class MainWindow(QMainWindow):
    """Main application window."""

    def __init__(self):
        super().__init__()

        self.case_service = CaseService()

        self.setWindowTitle("CaseForge")
        self.resize(1600, 900)

        self._create_ui()

    def new_case(self) -> None:
        """Create a new CaseForge project."""

        dialog = NewCaseDialog(self)

        if dialog.exec():
            case_name = dialog.get_case_name()

            if not case_name:
                QMessageBox.warning(
                    self,
                    "CaseForge",
                    "Please enter a case name.",
                )
                return

            cases_folder = Path.home() / "CaseForgeCases"
            cases_folder.mkdir(exist_ok=True)

            case = self.case_service.create_case(
                cases_folder,
                case_name,
            )

            QMessageBox.information(
                self,
                "Case Created",
                f'Created:\n\n{case.root}',
            )

    def _create_ui(self) -> None:
        build_menu_bar(self)

        self.setStatusBar(build_status_bar())

        self.preview = PreviewPanel()
        self.setCentralWidget(self.preview)

        self.case_explorer = CaseExplorer()

        explorer = QDockWidget("Case Explorer", self)
        explorer.setWidget(self.case_explorer)
        explorer.setMinimumWidth(250)

        self.addDockWidget(Qt.LeftDockWidgetArea, explorer)

        self.properties = PropertiesPanel()

        properties = QDockWidget("Properties", self)
        properties.setWidget(self.properties)
        properties.setMinimumWidth(300)

        self.addDockWidget(Qt.RightDockWidgetArea, properties)