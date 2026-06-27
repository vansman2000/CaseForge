"""
Preview Panel

Displays evidence previews.
"""

from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel, QScrollArea


class PreviewPanel(QScrollArea):
    """Displays a preview of the selected evidence."""

    IMAGE_EXTENSIONS = {
        ".jpg",
        ".jpeg",
        ".png",
        ".bmp",
        ".gif",
    }

    def __init__(self):
        super().__init__()

        self.label = QLabel("Select an item to preview.")

        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.setWidget(self.label)
        self.setWidgetResizable(True)

    def preview_file(self, filename: str) -> None:
        """Preview a file."""

        path = Path(filename)

        if path.suffix.lower() in self.IMAGE_EXTENSIONS:

            pixmap = QPixmap(str(path))

            if pixmap.isNull():
                self.label.setText("Unable to load image.")
                return

            pixmap = pixmap.scaled(
                900,
                900,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation,
            )

            self.label.setPixmap(pixmap)
            return

        self.label.setPixmap(QPixmap())
        self.label.setText(path.name)