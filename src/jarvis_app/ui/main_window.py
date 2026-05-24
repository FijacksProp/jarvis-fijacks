from __future__ import annotations

from datetime import datetime
from html import escape
from pathlib import Path
import re

from PySide6.QtCore import QObject, Qt, QThread, Signal
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QSizePolicy,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from jarvis_app.ai.ollama_client import OllamaClient
from jarvis_app.config import AppConfig
from jarvis_app.core.attachments import (
    AttachedFile,
    AttachmentError,
    attachment_preview,
    build_user_message_with_attachments,
    format_file_size,
    read_attachment,
)
from jarvis_app.core.prompts import SYSTEM_PROMPT
from jarvis_app.storage.conversations import ConversationRepository, Message
from jarvis_app.storage.database import initialize
from jarvis_app.tools.openers import ToolError, open_folder


class ChatWorker(QObject):
    token_received = Signal(str)
    finished = Signal(str)
    failed = Signal(str)

    def __init__(
        self,
        client: OllamaClient,
        model: str,
        messages: list[dict[str, str]],
    ) -> None:
        super().__init__()
        self.client = client
        self.model = model
        self.messages = messages
        self._cancelled = False

    def run(self) -> None:
        content = ""
        try:
            stream = self.client.chat(self.model, self.messages, stream=True)
            for event in stream:
                if self._cancelled:
                    break
                token = event.get("message", {}).get("content", "")
                if not token:
                    continue
                content += token
                self.token_received.emit(token)
            self.finished.emit(content)
        except Exception as exc:
            self.failed.emit(str(exc))

    def cancel(self) -> None:
        self._cancelled = True


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.config = AppConfig.load()
        initialize()
        self.ollama = OllamaClient(self.config.ollama_base_url, timeout_seconds=900)
        self.conversations = ConversationRepository()
        self.current_conversation_id = self.conversations.ensure_conversation()
        self.messages: list[Message] = []
        self.attached_files: list[AttachedFile] = []
        self.pending_assistant_text = ""
        self.worker_thread: QThread | None = None
        self.worker: ChatWorker | None = None

        self.setWindowTitle("Local Jarvis Assistant")
        self.resize(1180, 760)
        self._build_ui()
        self._update_status()
        self._load_conversation_list()
        self._load_current_conversation()

    def _build_ui(self) -> None:
        root = QWidget()
        layout = QHBoxLayout(root)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)

        history = self._build_history_panel()
        chat = self._build_chat_panel()
        actions = self._build_actions_panel()

        layout.addWidget(history, 1)
        layout.addWidget(chat, 3)
        layout.addWidget(actions, 1)

        self.setCentralWidget(root)

    def _build_history_panel(self) -> QWidget:
        panel = QWidget()
        panel.setObjectName("historyPanel")
        layout = QVBoxLayout(panel)

        title = QLabel("Chats")
        title.setObjectName("panelTitle")
        self.chat_list = QListWidget()
        self.chat_list.currentItemChanged.connect(self._conversation_selected)

        new_chat_button = QPushButton("New Chat")
        new_chat_button.clicked.connect(self._create_new_chat)
        settings_button = QPushButton("Settings")

        layout.addWidget(title)
        layout.addWidget(new_chat_button)
        layout.addWidget(self.chat_list)
        layout.addWidget(settings_button)
        return panel

    def _build_chat_panel(self) -> QWidget:
        panel = QWidget()
        panel.setObjectName("chatPanel")
        layout = QVBoxLayout(panel)

        top_row = QHBoxLayout()
        self.status_label = QLabel("Checking Ollama...")
        self.status_label.setObjectName("statusLabel")
        self.model_selector = QComboBox()
        self.model_selector.setMinimumWidth(180)
        top_row.addWidget(self.status_label)
        top_row.addStretch()
        top_row.addWidget(QLabel("Model"))
        top_row.addWidget(self.model_selector)

        self.chat_log = QTextEdit()
        self.chat_log.setReadOnly(True)
        self.chat_log.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.chat_log.setPlaceholderText("Jarvis chat will appear here.")

        self.message_input = QTextEdit()
        self.message_input.setFixedHeight(90)
        self.message_input.setPlaceholderText("Type a message...")

        button_row = QHBoxLayout()
        self.attach_button = QPushButton("Attach")
        self.send_button = QPushButton("Send")
        self.stop_button = QPushButton("Stop")
        self.stop_button.setEnabled(False)
        self.attach_button.clicked.connect(self._attach_files)
        self.send_button.clicked.connect(self._send_message)
        self.stop_button.clicked.connect(self._stop_generation)
        button_row.addWidget(self.attach_button)
        button_row.addStretch()
        button_row.addWidget(self.stop_button)
        button_row.addWidget(self.send_button)

        layout.addLayout(top_row)
        layout.addWidget(self.chat_log)
        layout.addWidget(self.message_input)
        layout.addLayout(button_row)
        return panel

    def _build_actions_panel(self) -> QWidget:
        panel = QWidget()
        panel.setObjectName("actionsPanel")
        layout = QVBoxLayout(panel)

        title = QLabel("Actions")
        title.setObjectName("panelTitle")

        quick_actions = QLabel("Quick")
        quick_actions.setObjectName("sectionTitle")
        open_output_button = QPushButton("Open Output Folder")
        open_output_button.clicked.connect(self._open_output_folder)
        save_response_button = QPushButton("Save Last Response")
        save_response_button.clicked.connect(self._save_last_response)

        files_title = QLabel("Attached Files")
        files_title.setObjectName("sectionTitle")
        self.attached_files_list = QListWidget()
        self.attached_files_list.setMaximumHeight(220)
        self.attached_files_list.currentItemChanged.connect(self._attachment_selected)
        attachment_buttons = QHBoxLayout()
        self.remove_attachment_button = QPushButton("Remove Selected")
        self.clear_attachments_button = QPushButton("Clear All")
        self.remove_attachment_button.clicked.connect(self._remove_selected_attachment)
        self.clear_attachments_button.clicked.connect(self._clear_attachments)
        attachment_buttons.addWidget(self.remove_attachment_button)
        attachment_buttons.addWidget(self.clear_attachments_button)

        analysis_title = QLabel("File Analysis")
        analysis_title.setObjectName("sectionTitle")
        summarize_button = QPushButton("Summarize Files")
        review_code_button = QPushButton("Review Code")
        study_notes_button = QPushButton("Study Notes")
        summarize_button.clicked.connect(lambda: self._send_attachment_prompt("summarize"))
        review_code_button.clicked.connect(lambda: self._send_attachment_prompt("code_review"))
        study_notes_button.clicked.connect(lambda: self._send_attachment_prompt("study_notes"))

        self.attachment_preview_label = QLabel("Select an attached file to preview it.")
        self.attachment_preview_label.setWordWrap(True)
        self.attachment_context_label = QLabel("No files attached.")
        self.attachment_context_label.setWordWrap(True)

        layout.addWidget(title)
        layout.addWidget(quick_actions)
        layout.addWidget(open_output_button)
        layout.addWidget(save_response_button)
        layout.addWidget(files_title)
        layout.addWidget(self.attached_files_list)
        layout.addLayout(attachment_buttons)
        layout.addWidget(analysis_title)
        layout.addWidget(summarize_button)
        layout.addWidget(review_code_button)
        layout.addWidget(study_notes_button)
        layout.addStretch()
        layout.addWidget(self.attachment_preview_label)
        layout.addWidget(self.attachment_context_label)
        self._refresh_attachments()
        return panel

    def _update_status(self) -> None:
        if self.ollama.health():
            models = self.ollama.list_models()
            self.model_selector.clear()
            self.model_selector.addItems(models)
            if self.config.default_model and self.config.default_model in models:
                self.model_selector.setCurrentText(self.config.default_model)
            if models:
                self.status_label.setText(f"Ollama ready. Models: {', '.join(models)}")
            else:
                self.status_label.setText("Ollama ready, but no models are installed.")
            return
        self.status_label.setText("Ollama is not running or not installed.")

    def _send_message(self) -> None:
        message = self.message_input.toPlainText().strip()
        if not message:
            return
        model = self.model_selector.currentText().strip()
        if not model:
            self.status_label.setText("Install or select a model before chatting.")
            return

        if self.worker_thread is not None:
            return

        self.conversations.add_message(self.current_conversation_id, "user", message)
        if self._should_rename_current_chat():
            self.conversations.rename_conversation(
                self.current_conversation_id,
                self._title_from_message(message),
            )
            self._load_conversation_list(select_current=False)

        self.message_input.clear()
        self._load_current_conversation()
        self.pending_assistant_text = ""
        self._render_chat()

        prompt_messages = self._prompt_messages(message)
        self._start_worker(model, prompt_messages)

    def _start_worker(self, model: str, messages: list[dict[str, str]]) -> None:
        self.send_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        self.status_label.setText(f"Jarvis is thinking with {model}...")

        self.worker_thread = QThread()
        self.worker = ChatWorker(self.ollama, model, messages)
        self.worker.moveToThread(self.worker_thread)
        self.worker_thread.started.connect(self.worker.run)
        self.worker.token_received.connect(self._append_assistant_token)
        self.worker.finished.connect(self._assistant_finished)
        self.worker.failed.connect(self._assistant_failed)
        self.worker.finished.connect(self.worker_thread.quit)
        self.worker.failed.connect(self.worker_thread.quit)
        self.worker_thread.finished.connect(self._worker_cleaned_up)
        self.worker_thread.start()

    def _stop_generation(self) -> None:
        if self.worker is not None:
            self.worker.cancel()
            self.status_label.setText("Stopping after the current token...")

    def _append_assistant_token(self, token: str) -> None:
        self.pending_assistant_text += token
        self._render_chat()

    def _assistant_finished(self, content: str) -> None:
        final_content = content.strip()
        if final_content:
            self.conversations.add_message(
                self.current_conversation_id,
                "assistant",
                final_content,
            )
        self.pending_assistant_text = ""
        self._load_current_conversation()
        self.status_label.setText("Ollama ready.")

    def _assistant_failed(self, error: str) -> None:
        self.pending_assistant_text = ""
        self.conversations.add_message(
            self.current_conversation_id,
            "system",
            f"Ollama error: {error}",
        )
        self._load_current_conversation()
        self.status_label.setText("Ollama request failed.")

    def _worker_cleaned_up(self) -> None:
        if self.worker is not None:
            self.worker.deleteLater()
        if self.worker_thread is not None:
            self.worker_thread.deleteLater()
        self.worker = None
        self.worker_thread = None
        self.send_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self._load_conversation_list(select_current=False)

    def _open_output_folder(self) -> None:
        output_dir = Path(self.config.output_dir).expanduser().resolve()
        output_dir.mkdir(parents=True, exist_ok=True)
        self._run_sidebar_action(lambda: open_folder(str(output_dir)))

    def _save_last_response(self) -> None:
        last_response = self._last_assistant_message()
        if not last_response:
            self._show_action_error("There is no assistant response to save yet.")
            return

        notes_dir = Path(self.config.output_dir).expanduser().resolve() / "notes"
        notes_dir.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        title = self._active_chat_title()
        filename = f"{timestamp}-{self._slugify(title)}.md"
        output_path = notes_dir / filename
        output_path.write_text(last_response.content, encoding="utf-8")

        self.conversations.add_message(
            self.current_conversation_id,
            "system",
            f"Saved note: {output_path}",
        )
        self._load_current_conversation()
        self.status_label.setText(f"Saved note: {output_path.name}")

    def _attach_files(self) -> None:
        file_paths, _filter = QFileDialog.getOpenFileNames(
            self,
            "Attach files",
            str(Path.home()),
            "Supported Files (*.txt *.md *.py *.js *.ts *.json *.html *.css *.csv *.xml *.yaml *.yml *.toml *.ini *.log *.pdf *.docx);;Text/Code Files (*.txt *.md *.py *.js *.ts *.json *.html *.css *.csv *.xml *.yaml *.yml *.toml *.ini *.log);;Documents (*.pdf *.docx);;All Files (*.*)",
        )
        if not file_paths:
            return

        added = 0
        existing_paths = {file.path for file in self.attached_files}
        for file_path in file_paths:
            try:
                attached = read_attachment(file_path)
            except AttachmentError as exc:
                self._show_action_error(str(exc))
                continue
            if attached.path in existing_paths:
                continue
            self.attached_files.append(attached)
            existing_paths.add(attached.path)
            added += 1

        self._refresh_attachments()
        if added:
            self.status_label.setText(f"Attached {added} file(s).")

    def _clear_attachments(self) -> None:
        self.attached_files.clear()
        self._refresh_attachments()
        self.status_label.setText("Attachments cleared.")

    def _remove_selected_attachment(self) -> None:
        item = self.attached_files_list.currentItem()
        if item is None:
            self._show_action_error("Select an attached file first.")
            return
        path = item.data(Qt.UserRole)
        self.attached_files = [
            attached for attached in self.attached_files if str(attached.path) != str(path)
        ]
        self._refresh_attachments()
        self.status_label.setText("Attachment removed.")

    def _attachment_selected(
        self,
        current: QListWidgetItem | None,
        _previous: QListWidgetItem | None,
    ) -> None:
        if current is None:
            self._update_attachment_preview(None)
            return
        selected_path = current.data(Qt.UserRole)
        selected = next(
            (
                attached
                for attached in self.attached_files
                if str(attached.path) == str(selected_path)
            ),
            None,
        )
        self._update_attachment_preview(selected)

    def _send_attachment_prompt(self, prompt_type: str) -> None:
        if not self.attached_files:
            self._show_action_error("Attach at least one file first.")
            return
        prompts = {
            "summarize": "Summarize the attached file(s). Focus on the main points, important details, and any action items.",
            "code_review": "Review the attached code file(s). Find likely bugs, explain risks, and suggest concise improvements.",
            "study_notes": "Turn the attached file(s) into clear study notes with definitions, key ideas, and short revision questions.",
        }
        self.message_input.setPlainText(prompts[prompt_type])
        self._send_message()

    def _refresh_attachments(self) -> None:
        if not hasattr(self, "attached_files_list"):
            return
        self.attached_files_list.clear()
        for attached in self.attached_files:
            label = f"{attached.name} ({attached.extension}, {format_file_size(attached.size_bytes)})"
            item = QListWidgetItem(label)
            item.setToolTip(str(attached.path))
            item.setData(Qt.UserRole, str(attached.path))
            self.attached_files_list.addItem(item)

        count = len(self.attached_files)
        if count:
            if self.attached_files_list.currentRow() < 0:
                self.attached_files_list.setCurrentRow(0)
            total_chars = sum(len(file.content) for file in self.attached_files)
            self.attachment_context_label.setText(
                f"{count} file(s) attached. About {total_chars:,} characters will be included with your messages until cleared."
            )
        else:
            self.attachment_context_label.setText("No files attached.")
            self._update_attachment_preview(None)

    def _update_attachment_preview(self, file: AttachedFile | None) -> None:
        if file is None:
            self.attachment_preview_label.setText("Select an attached file to preview it.")
            return
        truncated = " yes" if file.truncated else " no"
        self.attachment_preview_label.setText(
            f"Name: {file.name}\n"
            f"Type: {file.extension}\n"
            f"Size: {format_file_size(file.size_bytes)}\n"
            f"Truncated: {truncated}\n\n"
            f"Preview:\n{attachment_preview(file)}"
        )

    def _run_sidebar_action(self, action) -> None:
        try:
            result = action()
        except (OSError, ToolError) as exc:
            self._show_action_error(str(exc))
            return
        self.conversations.add_message(
            self.current_conversation_id,
            "system",
            result.message,
        )
        self._load_current_conversation()
        self.status_label.setText(result.message)

    def _show_action_error(self, message: str) -> None:
        self.status_label.setText(message)
        QMessageBox.warning(self, "Jarvis Action", message)

    def _last_assistant_message(self) -> Message | None:
        for message in reversed(self.messages):
            if message.role == "assistant" and message.content.strip():
                return message
        return None

    def _active_chat_title(self) -> str:
        for conversation in self.conversations.list_conversations():
            if conversation.id == self.current_conversation_id:
                return conversation.title
        return "jarvis-note"

    def _prompt_messages(self, latest_message: str) -> list[dict[str, str]]:
        history = self.messages[-12:]
        if history and history[-1].role == "user" and history[-1].content == latest_message:
            history = history[:-1]
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        for item in history:
            if item.role in {"user", "assistant"}:
                messages.append({"role": item.role, "content": item.content})
        messages.append(
            {
                "role": "user",
                "content": build_user_message_with_attachments(
                    latest_message,
                    self.attached_files,
                ),
            }
        )
        return messages

    def _load_conversation_list(self, select_current: bool = True) -> None:
        self.chat_list.blockSignals(True)
        self.chat_list.clear()
        for conversation in self.conversations.list_conversations():
            item = QListWidgetItem(conversation.title)
            item.setData(Qt.UserRole, conversation.id)
            self.chat_list.addItem(item)
            if select_current and conversation.id == self.current_conversation_id:
                self.chat_list.setCurrentItem(item)
        self.chat_list.blockSignals(False)

    def _load_current_conversation(self) -> None:
        self.messages = self.conversations.get_messages(self.current_conversation_id)
        self._render_chat()

    def _conversation_selected(
        self,
        current: QListWidgetItem | None,
        _previous: QListWidgetItem | None,
    ) -> None:
        if current is None or self.worker_thread is not None:
            return
        conversation_id = current.data(Qt.UserRole)
        if conversation_id == self.current_conversation_id:
            return
        self.current_conversation_id = int(conversation_id)
        self.pending_assistant_text = ""
        self._load_current_conversation()

    def _create_new_chat(self) -> None:
        if self.worker_thread is not None:
            return
        self.current_conversation_id = self.conversations.create_conversation()
        self.pending_assistant_text = ""
        self._load_conversation_list()
        self._load_current_conversation()

    def _render_chat(self) -> None:
        parts: list[str] = []
        for message in self.messages:
            parts.append(self._message_html(message.role, message.content))
        if self.pending_assistant_text:
            parts.append(self._message_html("assistant", self.pending_assistant_text))
        if not parts:
            parts.append("<p class='empty'>Start a local chat with Jarvis.</p>")
        self.chat_log.setHtml(self._document_html("".join(parts)))
        self.chat_log.verticalScrollBar().setValue(self.chat_log.verticalScrollBar().maximum())

    @staticmethod
    def _document_html(body: str) -> str:
        return f"""
        <html>
          <head>
            <style>
              body {{ color: #f4f6f8; font-family: Segoe UI, Arial, sans-serif; }}
              .message {{ margin: 0 0 14px 0; line-height: 1.45; }}
              .role {{ font-weight: 700; margin-bottom: 4px; }}
              .user .role {{ color: #90cdf4; }}
              .assistant .role {{ color: #9ae6b4; }}
              .system .role {{ color: #fbd38d; }}
              .content {{ white-space: pre-wrap; }}
              .empty {{ color: #9aa4b2; }}
            </style>
          </head>
          <body>{body}</body>
        </html>
        """

    @staticmethod
    def _message_html(role: str, content: str) -> str:
        labels = {
            "user": "You",
            "assistant": "Jarvis",
            "system": "System",
        }
        label = labels.get(role, role.title())
        safe_content = escape(content).replace("\n", "<br>")
        return (
            f"<div class='message {escape(role)}'>"
            f"<div class='role'>{escape(label)}</div>"
            f"<div class='content'>{safe_content}</div>"
            "</div>"
        )

    def _should_rename_current_chat(self) -> bool:
        conversations = {
            conversation.id: conversation
            for conversation in self.conversations.list_conversations()
        }
        current = conversations.get(self.current_conversation_id)
        return current is not None and current.title == "New Chat" and not self.messages

    @staticmethod
    def _title_from_message(message: str) -> str:
        collapsed = " ".join(message.split())
        return collapsed[:42] + ("..." if len(collapsed) > 42 else "")

    @staticmethod
    def _slugify(value: str) -> str:
        normalized = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower()).strip("-")
        return normalized[:48] or "jarvis-note"


def run() -> int:
    app = QApplication([])
    app.setStyleSheet(
        """
        QMainWindow, QWidget {
            background: #121417;
            color: #f4f6f8;
            font-size: 14px;
        }
        QTextEdit, QListWidget {
            background: #1b1f24;
            border: 1px solid #303842;
            border-radius: 6px;
            padding: 8px;
        }
        QPushButton {
            background: #2b6cb0;
            border: 0;
            border-radius: 6px;
            padding: 8px 12px;
            color: white;
        }
        QPushButton:hover {
            background: #3182ce;
        }
        QLabel#panelTitle {
            font-weight: 700;
            font-size: 16px;
        }
        QLabel#statusLabel {
            color: #a8c7fa;
        }
        QLabel#sectionTitle {
            color: #cbd5e0;
            font-weight: 700;
            margin-top: 8px;
        }
        """
    )
    window = MainWindow()
    window.show()
    return app.exec()
