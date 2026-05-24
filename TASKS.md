# Task Backlog

Status key:

- todo: not started
- doing: in progress
- done: completed
- blocked: waiting on decision or dependency

## Version 0 - Foundation

| Status | Task | Notes |
| --- | --- | --- |
| done | Confirm Python version | Python 3.14.3 is available; use 3.12/3.11 if dependencies fail |
| blocked | Install or verify Ollama | Ollama CLI is not currently on PATH |
| blocked | Choose first model | Depends on Ollama being installed |
| done | Decide external drive storage path | `E:\Jarvis\OllamaModels` and `E:\Jarvis\JarvisData` configured |
| done | Create initial app folder structure | Keep source, data, logs, and docs separate |
| done | Create virtual environment | `.venv` exists with pip 25.3, PySide6, and pytest |
| done | Add dependency file | pyproject.toml and requirements.txt added |

## Version 1 - MVP

| Status | Task | Notes |
| --- | --- | --- |
| todo | Build PySide6 main window | Chat-first layout with actions sidebar |
| todo | Build chat message components | User, assistant, system, tool messages |
| todo | Implement Ollama client | Local HTTP requests and streaming |
| todo | Implement model selector | Read available models from Ollama |
| todo | Add SQLite database | Conversations, messages, settings, actions |
| todo | Save and load chat history | Left sidebar history list |
| todo | Add app launcher tool | Approved apps only |
| todo | Add folder launcher tool | Approved folders only |
| todo | Add file attachment support | Start with txt, md, py, js, json, html, css |
| todo | Add save as note/report | Write into configured output folder |
| todo | Add action confirmation UI | Required for write actions |
| todo | Add basic settings screen | Ollama URL, model, paths, shortcuts |

## Version 2 - Documents and Projects

| Status | Task | Notes |
| --- | --- | --- |
| todo | Add PDF text extraction | Use pypdf or PyMuPDF |
| todo | Add DOCX text extraction | Use python-docx |
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
