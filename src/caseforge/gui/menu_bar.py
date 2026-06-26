"""
CaseForge Menu Bar
"""

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow


def build_menu_bar(window: QMainWindow) -> None:
    """Create the application's menu bar."""

    menu_bar = window.menuBar()

    #
    # File
    #
    file_menu = menu_bar.addMenu("&File")

    file_menu.addAction(QAction("New Case", window))
    file_menu.addAction(QAction("Open Case...", window))
    file_menu.addAction(QAction("Save Case", window))

    file_menu.addSeparator()

    file_menu.addAction(QAction("Import Evidence ZIP...", window))

    file_menu.addSeparator()

    exit_action = QAction("Exit", window)
    exit_action.triggered.connect(window.close)

    file_menu.addAction(exit_action)

    #
    # Case
    #
    menu_bar.addMenu("&Case")

    #
    # Evidence
    #
    menu_bar.addMenu("&Evidence")

    #
    # Build
    #
    menu_bar.addMenu("&Build")

    #
    # Reports
    #
    menu_bar.addMenu("&Reports")

    #
    # Tools
    #
    menu_bar.addMenu("&Tools")

    #
    # Help
    #
    menu_bar.addMenu("&Help")