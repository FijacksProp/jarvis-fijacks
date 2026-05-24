# Project Plan

## 1. Project Summary

Build a local personal AI desktop assistant for Windows. It should feel like a small personal command center: chat-first, local-first, useful for PC automation, coding help, studying, document work, and project management.

The assistant should run without paid APIs. Ollama will provide local model inference. The first implementation will prioritize reliability, safety, and usability over flashy features.

## 2. User Context

Target machine:

- RAM: 16GB
- GPU: Intel UHD Graphics 620
- Storage: about 15GB free on internal drive
- Extra storage: 500GB external drive
- OS target: Windows

Important constraints:

- Local models must be small and efficient.
- App data and models should avoid filling the internal drive.
- Automation must be controlled and confirm risky actions.
- The UI should be simple and functional, but still clean and pleasant.

## 3. Product Principles

1. Local-first: user data stays on the machine by default.
2. Safe automation: the assistant gets approved tools, not unrestricted PC control.
3. Useful before magical: version 1 must be practical even with small local models.
4. Chat-first: the main interaction is natural conversation.
5. Transparent actions: file and PC actions should be visible, confirmable, and logged.
6. Incremental intelligence: document search, project analysis, voice, and workflows come after the core is stable.

## 4. Recommended Stack

First version:

- Python 3.11+
- PySide6 for desktop UI
- Ollama for local AI chat
- SQLite for chat history, settings, actions, and local memory
- Requests or httpx for Ollama API calls
- pathlib, subprocess, os, shutil for controlled PC actions

Later additions:

- PyMuPDF or pypdf for PDF reading
- python-docx for DOCX reading
- watchdog for folder monitoring
- local embeddings for semantic file search
- speech_recognition, faster-whisper, or Vosk for voice input
- pyttsx3 or Piper for local voice output

## 5. Interface Direction

The app will use a chat-first interface with an actions sidebar.

Main chat area:

- Conversation with assistant
- Streaming responses
- File attachment context
- Save output as note, report, or task

Left sidebar:

- Chat history
- Projects/workspaces
- Pinned chats
- Settings shortcut

Right actions sidebar:

- Quick actions
- Favorite apps and folders
- Selected context files
- Pending assistant actions
- Recent generated outputs
- Safety confirmations

## 6. Version Strategy

Version 0: Foundation and environment

- Confirm tools and folder structure
- Install Ollama and test a small model
- Set up Python desktop app skeleton
- Create local SQLite schema

Version 1: MVP local chat and basic automation

- Chat with Ollama
- Save chat history
- Model selection
- Basic app and folder launcher
- Create local notes/reports from chat
- Read selected text/code/markdown files
- Safety confirmation for write actions

Version 2: Documents, projects, and better context

- PDF and DOCX support
- Project workspace profiles
- Folder scanning
- Local file search
- Basic task/project management
- Better prompt templates for coding, study, and document work

Version 3: Automation workflows

- Multi-step approved actions
- Rules for common workflows
- File organization tools
- Script launcher for trusted scripts
- Action logs and undo support where practical

Version 4: Voice and assistant presence

- Voice input
- Local text-to-speech
- Wake button or push-to-talk
- Command mode for short PC actions
- Optional background tray mode

Version 5: Polish, packaging, and extensibility

- Windows installer/package
- Plugin-style tool registry
- Better model management
- Backup and restore
- Full settings and diagnostics

## 7. Success Criteria

Version 1 is successful if the user can:

- Start the desktop app.
- Select a local Ollama model.
- Chat with the assistant.
- Save and reopen chat history.
- Ask the assistant to open configured apps and folders.
- Attach a selected code/text/markdown file and ask questions about it.
- Generate a summary, report, or note and save it locally.
- See and approve actions before they change files.

Long-term success means the assistant becomes the user's local command center for everyday school, coding, file, and PC tasks.

## 8. Build Order

1. Build the app skeleton and UI layout.
2. Connect to Ollama and stream responses.
3. Add SQLite persistence.
4. Add settings and model selection.
5. Add safe quick actions.
6. Add file attachments and text extraction.
7. Add save output features.
8. Add project/workspace organization.
9. Add document indexing and search.
10. Add voice and advanced workflows.

## 9. Non-Goals for Version 1

- No unrestricted terminal agent.
- No always-listening microphone.
- No hidden background file access.
- No cloud sync.
- No automatic deletion, moving, or overwriting without confirmation.
- No huge model requirement.

