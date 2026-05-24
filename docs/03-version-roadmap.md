# Version Roadmap

## Version 0 - Foundation

Goal: prepare the machine, tools, folder structure, and app skeleton.

Primary features:

- Python project setup
- Ollama connection check
- First local model test
- Empty PySide6 window
- SQLite database created
- Basic settings file

Exit criteria:

- App launches.
- Ollama status can be checked.
- Database can be created.
- First model can return a response from a test script.

## Version 1 - MVP Local Assistant

Goal: create a useful local desktop assistant with chat, history, basic file context, and safe PC actions.

Primary features:

- Chat-first desktop UI
- Ollama model selector
- Streaming local responses
- Local chat history
- Favorite apps and folders
- Open app and open folder tools
- Attach text/code/markdown files
- Save generated notes and reports
- Action confirmation for write operations

Exit criteria:

- User can use the app daily for simple chat and automation.
- Conversations persist after closing the app.
- Basic file analysis works for selected files.
- Assistant can open configured apps and folders safely.

## Version 2 - Documents and Projects

Goal: make the assistant useful for school, study, and project work.

Primary features:

- PDF and DOCX extraction
- Project/workspace profiles
- Local folder search
- Folder summary
- Simple task management
- Reusable prompt modes: coding, study, report, proposal
- Generated output library

Exit criteria:

- User can create a project workspace.
- User can ask questions about documents.
- User can find files by name/content.
- User can generate organized school/project outputs.

## Version 3 - Automation Workflows

Goal: turn single actions into safe multi-step workflows.

Primary features:

- Tool registry with schemas
- Multi-action queue
- Preview before file changes
- File organization operations
- Trusted script launcher
- Action logs
- Limited rollback/backups

Exit criteria:

- Assistant can propose a multi-step workflow.
- User can approve or reject each step.
- File operations show preview and are logged.

## Version 4 - Voice Assistant

Goal: add voice input/output without compromising privacy.

Primary features:

- Push-to-talk voice input
- Local speech-to-text
- Local text-to-speech
- Short command mode
- Optional tray mode

Exit criteria:

- User can trigger voice input manually.
- Voice commands can perform approved quick actions.
- Voice stays local.

## Version 5 - Polished Personal Command Center

Goal: improve reliability, packaging, diagnostics, and extensibility.

Primary features:

- Windows packaging
- Onboarding setup
- Backup and restore
- Diagnostics screen
- Plugin-style custom tools
- Better model management
- Optional advanced project indexing

Exit criteria:

- App can be installed and updated.
- User can back up data.
- Custom tools can be added without changing core code.

