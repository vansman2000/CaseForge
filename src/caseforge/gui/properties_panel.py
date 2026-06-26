"""
Properties Panel

Displays metadata about the currently selected item.
"""

from PySide6.QtWidgets import QTextEdit


class PropertiesPanel(QTextEdit):
    """Displays metadata for the selected evidence."""

    def __init__(self):
        super().__init__()

        self.setReadOnly(True)

        self.setPlaceholderText(
            "Properties\n\n"
            "No item selected."
        )