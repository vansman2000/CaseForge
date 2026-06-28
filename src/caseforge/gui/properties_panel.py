"""
Properties Panel

Displays metadata about the selected evidence.
"""

from pathlib import Path
from datetime import datetime

from PySide6.QtWidgets import QTextEdit


class PropertiesPanel(QTextEdit):
    """Displays metadata for the selected evidence."""

    def __init__(self):
        super().__init__()

        self.setReadOnly(True)

        self.clear_properties()

    def clear_properties(self) -> None:
        """Clear the properties panel."""

        self.setPlainText(
            "Evidence Properties\n\n"
            "No item selected."
        )

    def show_file(self, filename: str) -> None:
        """Display information about a file."""

        path = Path(filename)

        if not path.exists():
            self.clear_properties()
            return

        stat = path.stat()

        size_kb = stat.st_size / 1024

        modified = datetime.fromtimestamp(
            stat.st_mtime
        ).strftime("%Y-%m-%d %H:%M:%S")

        text = (
            "Evidence Properties\n"
            "====================\n\n"
            f"Filename:\n{path.name}\n\n"
            f"Type:\n{path.suffix.upper()}\n\n"
            f"Folder:\n{path.parent.name}\n\n"
            f"Size:\n{size_kb:.1f} KB\n\n"
            f"Modified:\n{modified}\n\n"
            f"Full Path:\n{path}"
        )

        self.setPlainText(text)