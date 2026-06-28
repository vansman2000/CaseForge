"""
Evidence Repository

Handles persistent storage of Evidence objects.
"""

import sqlite3
from pathlib import Path

from caseforge.models.evidence import Evidence


class EvidenceRepository:
    """Repository for Evidence records."""

    def __init__(self, database_path: Path):
        self.database_path = database_path

        self._initialize_database()

    def _connection(self):
        return sqlite3.connect(self.database_path)

    def _initialize_database(self) -> None:
        """Create database schema."""

        with self._connection() as connection:

            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS evidence (

                    id INTEGER PRIMARY KEY AUTOINCREMENT,

                    filename TEXT NOT NULL,

                    path TEXT NOT NULL,

                    evidence_type TEXT NOT NULL,

                    title TEXT,

                    exhibit_number INTEGER,

                    notes TEXT,

                    tags TEXT,

                    imported TEXT NOT NULL

                )
                """
            )

    def save(self, evidence: Evidence) -> None:
        """Save one Evidence object."""

        with self._connection() as connection:

            connection.execute(
                """
                INSERT INTO evidence (

                    filename,
                    path,
                    evidence_type,
                    title,
                    exhibit_number,
                    notes,
                    tags,
                    imported

                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    evidence.filename,
                    str(evidence.path),
                    evidence.evidence_type,
                    evidence.title,
                    evidence.exhibit_number,
                    evidence.notes,
                    ",".join(evidence.tags),
                    evidence.imported.isoformat(),
                ),
            )

    def all(self):
        """Return every evidence row."""

        with self._connection() as connection:

            return connection.execute(
                """
                SELECT
                    filename,
                    path,
                    evidence_type,
                    title,
                    exhibit_number,
                    notes,
                    tags,
                    imported
                FROM evidence
                """
            ).fetchall()