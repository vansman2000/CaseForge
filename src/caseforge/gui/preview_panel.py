"""
Preview Panel

Displays the currently selected evidence.
"""

from PySide6.QtWidgets import QTextEdit


class PreviewPanel(QTextEdit):
    """Central evidence preview widget."""

    def __init__(self):
        super().__init__()

        self.setReadOnly(True)

        self.setPlaceholderText(
            "Welcome to CaseForge\n\n"
            "Open or create a case to begin.\n\n"
            "Imported evidence will appear here."
        )