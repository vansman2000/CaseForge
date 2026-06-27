"""
New Case Dialog
"""

from PySide6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
)


class NewCaseDialog(QDialog):
    """Dialog used to gather information for a new CaseForge project."""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("New Case")

        self.case_name = QLineEdit()

        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok
            | QDialogButtonBox.StandardButton.Cancel
        )

        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        layout = QFormLayout()

        layout.addRow("Case Name:", self.case_name)
        layout.addWidget(buttons)

        self.setLayout(layout)

    def get_case_name(self) -> str:
        """Return the entered case name."""

        return self.case_name.text().strip()