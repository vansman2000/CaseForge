"""
CaseForge Status Bar
"""

from PySide6.QtWidgets import QStatusBar


def build_status_bar() -> QStatusBar:
    """Create the application's status bar."""

    status_bar = QStatusBar()

    status_bar.showMessage("Ready")

    return status_bar