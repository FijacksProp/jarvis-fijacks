from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from pathlib import Path

from jarvis_app.storage.database import connect


@dataclass(frozen=True, slots=True)
class Conversation:
    id: int
    title: str
    created_at: str
    updated_at: str


@dataclass(frozen=True, slots=True)
class Message:
    id: int
    conversation_id: int
    role: str
    content: str
    created_at: str


class ConversationRepository:
    def __init__(self, db_path: Path | None = None) -> None:
        self.db_path = db_path

    def create_conversation(self, title: str = "New Chat") -> int:
        with self._connect() as connection:
            cursor = connection.execute(
                "INSERT INTO conversations (title) VALUES (?)",
                (title,),
            )
            return int(cursor.lastrowid)

    def list_conversations(self) -> list[Conversation]:
        with self._connect() as connection:
            rows = connection.execute(
                """
                SELECT id, title, created_at, updated_at
                FROM conversations
                ORDER BY updated_at DESC, id DESC
                """
            ).fetchall()
        return [self._conversation_from_row(row) for row in rows]

    def get_messages(self, conversation_id: int) -> list[Message]:
        with self._connect() as connection:
            rows = connection.execute(
                """
                SELECT id, conversation_id, role, content, created_at
                FROM messages
                WHERE conversation_id = ?
                ORDER BY id ASC
                """,
                (conversation_id,),
            ).fetchall()
        return [self._message_from_row(row) for row in rows]

    def add_message(self, conversation_id: int, role: str, content: str) -> int:
        with self._connect() as connection:
            cursor = connection.execute(
                """
                INSERT INTO messages (conversation_id, role, content)
                VALUES (?, ?, ?)
                """,
                (conversation_id, role, content),
            )
            connection.execute(
                """
                UPDATE conversations
                SET updated_at = CURRENT_TIMESTAMP
                WHERE id = ?
                """,
                (conversation_id,),
            )
            return int(cursor.lastrowid)

    def rename_conversation(self, conversation_id: int, title: str) -> None:
        with self._connect() as connection:
            connection.execute(
                """
                UPDATE conversations
                SET title = ?, updated_at = CURRENT_TIMESTAMP
                WHERE id = ?
                """,
                (title, conversation_id),
            )

    def ensure_conversation(self) -> int:
        conversations = self.list_conversations()
        if conversations:
            return conversations[0].id
        return self.create_conversation()

    def _connect(self) -> sqlite3.Connection:
        return connect(self.db_path)

    @staticmethod
    def _conversation_from_row(row: sqlite3.Row) -> Conversation:
        return Conversation(
            id=int(row["id"]),
            title=str(row["title"]),
            created_at=str(row["created_at"]),
            updated_at=str(row["updated_at"]),
        )

    @staticmethod
    def _message_from_row(row: sqlite3.Row) -> Message:
        return Message(
            id=int(row["id"]),
            conversation_id=int(row["conversation_id"]),
            role=str(row["role"]),
            content=str(row["content"]),
            created_at=str(row["created_at"]),
        )

