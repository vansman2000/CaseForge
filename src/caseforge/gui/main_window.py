from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFileDialog,
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
from caseforge.services.evidence_service import EvidenceService

from caseforge.models.evidence import Evidence


class MainWindow(QMainWindow):
    """Main application window."""

    def __init__(self):
        super().__init__()

        self.case_service = CaseService()
        self.evidence_service = EvidenceService()

        self.current_case = None

        self.setWindowTitle("CaseForge")
        self.resize(1600, 900)

        self._create_ui()

    def new_case(self) -> None:
        """Create a new CaseForge project."""

        dialog = NewCaseDialog(self)

        if not dialog.exec():
            return

        case_name = dialog.get_case_name().strip()

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

        self.current_case = case

        self.case_explorer.load_case(case)

        QMessageBox.information(
            self,
            "Case Created",
            f"Created:\n\n{case.root}",
        )

    def import_evidence(self) -> None:
        """Import evidence into the current case."""

        if self.current_case is None:
            QMessageBox.warning(
                self,
                "CaseForge",
                "Create or open a case first.",
            )
            return

        files, _ = QFileDialog.getOpenFileNames(
            self,
            "Import Evidence",
        )

        if not files:
            return

        try:
            imported = self.evidence_service.import_files(
                self.current_case,
                files,
            )

            self.statusBar().showMessage(
                f"Imported {len(imported)} file(s).",
                5000,
            )

            self.case_explorer.load_case(self.current_case)

        except Exception as e:
            QMessageBox.critical(
                self,
                "Import Error",
                str(e),
            )

            print("IMPORT ERROR:", e)

    def on_tree_item_clicked(self, item, column):
        """Preview the selected evidence."""

        evidence = item.data(0, Qt.UserRole)

        if isinstance(evidence, Evidence):

            self.preview.preview_file(
                str(evidence.path)
            )

            self.properties.show_file(
                str(evidence.path)
            )

        else:
            self.properties.clear_properties()

    def _create_ui(self) -> None:
        """Build the main interface."""

        build_menu_bar(self)

        self.setStatusBar(build_status_bar())

        self.preview = PreviewPanel()
        self.setCentralWidget(self.preview)

        self.case_explorer = CaseExplorer()

        self.case_explorer.itemClicked.connect(
            self.on_tree_item_clicked
        )

        explorer = QDockWidget(
            "Case Explorer",
            self,
        )

        explorer.setWidget(self.case_explorer)
        explorer.setMinimumWidth(250)

        self.addDockWidget(
            Qt.LeftDockWidgetArea,
            explorer,
        )

        self.properties = PropertiesPanel()

        properties = QDockWidget(
            "Properties",
            self,
        )

        properties.setWidget(self.properties)
        properties.setMinimumWidth(300)

        self.addDockWidget(
            Qt.RightDockWidgetArea,
            properties,
        )