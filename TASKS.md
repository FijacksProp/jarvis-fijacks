# Task Backlog

Status key:

- todo: not started
- doing: in progress
- done: completed
- blocked: waiting on decision or dependency
- removed: intentionally removed from current direction

## Version 0 - Foundation

| Status | Task | Notes |
| --- | --- | --- |
| done | Confirm Python version | Python 3.14.3 is available; use 3.12/3.11 if dependencies fail |
| done | Install or verify Ollama | Ollama is installed and local API is reachable |
| done | Choose first model | `llama3.2:3b` installed and set as default |
| done | Decide external drive storage path | `E:\Jarvis\OllamaModels` and `E:\Jarvis\JarvisData` configured |
| done | Create initial app folder structure | Keep source, data, logs, and docs separate |
| done | Create virtual environment | `.venv` exists with pip 25.3, PySide6, and pytest |
| done | Add dependency file | pyproject.toml and requirements.txt added |

## Version 1 - MVP

| Status | Task | Notes |
| --- | --- | --- |
| done | Build PySide6 main window | Chat-first layout with actions sidebar |
| done | Build chat message components | User, assistant, and system messages render in chat |
| done | Implement Ollama client | Local HTTP requests and streaming |
| done | Implement model selector | Reads available models from Ollama |
| done | Add SQLite database | Conversations, messages, settings, actions schema exists |
| done | Save and load chat history | Basic left sidebar history list and message persistence |
| removed | Add app launcher tool | Removed from V1 direction; no favorites sidebar |
| removed | Add folder launcher tool | Removed from V1 direction; output folder quick action remains |
| done | Add file attachment support | Includes preview, remove selected, clear all, and quick file analysis prompts |
| done | Add save as note/report | Save last assistant response as a markdown note |
| todo | Add action confirmation UI | Required for write actions |
| todo | Add basic settings screen | Ollama URL, model, paths, shortcuts |

## Version 2 - Documents and Projects

| Status | Task | Notes |
| --- | --- | --- |
| done | Add PDF text extraction | Uses pypdf for text-based PDFs; OCR is not included yet |
| done | Add DOCX text extraction | Uses python-docx for paragraphs and table text |
| todo | Add project workspace profiles | Name, root folder, notes, preferred model |
| todo | Add folder search | Filename and content search |
| todo | Add document chunking | Avoid feeding huge files directly to model |
| todo | Add local summaries | Per document and per project |
| todo | Add tasks view | Simple local project tasks |

## Version 3 - Automation Workflows

| Status | Task | Notes |
| --- | --- | --- |
| todo | Create tool registry | Named tools with schemas and safety levels |
| todo | Add multi-step action queue | Assistant proposes, user approves |
| todo | Add file organization tool | Move/copy/rename with preview |
| todo | Add trusted script launcher | User-approved scripts only |
| todo | Add action audit log | Who/what/when/result |
| todo | Add reversible operations where possible | Keep backups for edits/moves |

## Version 4 - Voice

| Status | Task | Notes |
| --- | --- | --- |
| todo | Add push-to-talk voice input | Safer than always-listening |
| todo | Add local speech-to-text | Test Vosk or Whisper options |
| todo | Add local text-to-speech | pyttsx3 first, Piper later |
| todo | Add voice command mode | Short commands for PC actions |
| todo | Add tray mode | Optional background access |

## Version 5 - Polish and Packaging

| Status | Task | Notes |
| --- | --- | --- |
| todo | Package for Windows | PyInstaller or similar |
| todo | Add diagnostics screen | Ollama status, DB path, storage usage |
| todo | Add backup and restore | SQLite and generated outputs |
| todo | Add plugin/tool extension format | Future custom tools |
| todo | Add onboarding flow | Model, paths, favorite apps/folders |
