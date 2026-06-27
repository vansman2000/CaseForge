"""
CaseForge Menu Bar
"""

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow


def build_menu_bar(window: QMainWindow) -> None:
    menu_bar = window.menuBar()

    file_menu = menu_bar.addMenu("&File")

    new_case_action = QAction("New Case...", window)
    new_case_action.setShortcut("Ctrl+N")

    def test():
        print(">>> MENU ACTION FIRED <<<")
        window.new_case()

    new_case_action.triggered.connect(test)

    file_menu.addAction(new_case_action)

    file_menu.addSeparator()

    exit_action = QAction("Exit", window)
    exit_action.triggered.connect(window.close)
    file_menu.addAction(exit_action)