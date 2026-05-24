from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from jarvis_app.ai.ollama_client import OllamaClient
from jarvis_app.config import AppConfig
from jarvis_app.storage.database import initialize


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.config = AppConfig.load()
        initialize()
        self.ollama = OllamaClient(self.config.ollama_base_url)

        self.setWindowTitle("Local Jarvis Assistant")
        self.resize(1180, 760)
        self._build_ui()
        self._update_status()

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
        self.chat_list.addItem("New Chat")

        settings_button = QPushButton("Settings")

        layout.addWidget(title)
        layout.addWidget(self.chat_list)
        layout.addWidget(settings_button)
        return panel

    def _build_chat_panel(self) -> QWidget:
        panel = QWidget()
        panel.setObjectName("chatPanel")
        layout = QVBoxLayout(panel)

        self.status_label = QLabel("Checking Ollama...")
        self.status_label.setObjectName("statusLabel")

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
        self.send_button.clicked.connect(self._send_placeholder_message)
        button_row.addWidget(self.attach_button)
        button_row.addStretch()
        button_row.addWidget(self.send_button)

        layout.addWidget(self.status_label)
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
        quick_actions = QLabel("Quick actions will appear here.")
        quick_actions.setWordWrap(True)
        context = QLabel("Current context: no files attached.")
        context.setWordWrap(True)

        layout.addWidget(title)
        layout.addWidget(QPushButton("Open Output Folder"))
        layout.addWidget(QPushButton("Save Last Response"))
        layout.addWidget(quick_actions)
        layout.addStretch()
        layout.addWidget(context)
        return panel

    def _update_status(self) -> None:
        if self.ollama.health():
            models = self.ollama.list_models()
            if models:
                self.status_label.setText(f"Ollama ready. Models: {', '.join(models)}")
            else:
                self.status_label.setText("Ollama ready, but no models are installed.")
            return
        self.status_label.setText("Ollama is not running or not installed.")

    def _send_placeholder_message(self) -> None:
        message = self.message_input.toPlainText().strip()
        if not message:
            return
        self.chat_log.append(f"<b>You:</b> {message}")
        self.chat_log.append("<b>Jarvis:</b> Local chat wiring is next. The UI shell is alive.")
        self.message_input.clear()


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
        """
    )
    window = MainWindow()
    window.show()
    return app.exec()

