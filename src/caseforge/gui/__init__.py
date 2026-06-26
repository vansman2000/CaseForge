from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QDockWidget,
    QLabel,
    QListWidget,
    QMainWindow,
    QMenu,
    QMenuBar,
    QStatusBar,
    QTextEdit,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CaseForge")
        self.resize(1400, 900)

        self._create_menu()
        self._create_panels()

        status = QStatusBar()
        status.showMessage("Ready")
        self.setStatusBar(status)

    def _create_menu(self):

        menu = QMenuBar()

        file_menu = QMenu("&File", self)
        file_menu.addAction("New Case")
        file_menu.addAction("Open Case")
        file_menu.addSeparator()
        file_menu.addAction("Import Evidence ZIP")
        file_menu.addSeparator()
        file_menu.addAction("Exit", self.close)

        case_menu = QMenu("&Case", self)
        build_menu = QMenu("&Build", self)
        tools_menu = QMenu("&Tools", self)
        help_menu = QMenu("&Help", self)

        menu.addMenu(file_menu)
        menu.addMenu(case_menu)
        menu.addMenu(build_menu)
        menu.addMenu(tools_menu)
        menu.addMenu(help_menu)

        self.setMenuBar(menu)

    def _create_panels(self):

        case_tree = QListWidget()

        case_tree.addItems([
            "My Case",
            "Evidence",
            "Timeline",
            "Damages",
            "Transcripts",
            "Binder",
            "Reports",
        ])

        left = QDockWidget("Case Explorer", self)
        left.setWidget(case_tree)
        left.setMinimumWidth(250)

        self.addDockWidget(Qt.LeftDockWidgetArea, left)

        properties = QTextEdit()
        properties.setReadOnly(True)

        right = QDockWidget("Properties", self)
        right.setWidget(properties)
        right.setMinimumWidth(280)

        self.addDockWidget(Qt.RightDockWidgetArea, right)

        preview = QTextEdit()
        preview.setReadOnly(True)
        preview.setText(
            "CaseForge\n\n"
            "Evidence preview will appear here."
        )

        self.setCentralWidget(preview)