# Local Personal Jarvis AI Desktop Assistant

This repository is the planning and implementation home for a local-first Windows desktop AI assistant.

The goal is to build a simple, useful desktop assistant that can chat locally, help with coding and study work, analyze selected files, generate documents, and perform safe PC automation without relying on paid APIs.

## Current Direction

- Platform: Windows desktop
- First UI style: chat-first interface with an actions sidebar
- First stack: Python, PySide6, Ollama, SQLite
- Local AI engine: Ollama
- Primary use: PC automation, with coding, study, documents, and project management also included
- Hardware target: 16GB RAM, Intel UHD Graphics 620, about 15GB free internal storage, 500GB external drive

## Planning Documents

- [Project Plan](PROJECT_PLAN.md)
- [Task Backlog](TASKS.md)
- [Product Vision](docs/01-product-vision.md)
- [System Architecture](docs/02-system-architecture.md)
- [Version Roadmap](docs/03-version-roadmap.md)
- [Phase Plan](docs/04-phase-plan.md)
- [Feature Specs](docs/05-feature-specs.md)
- [UI and UX Plan](docs/06-ui-ux-plan.md)
- [Local AI and Models](docs/07-local-ai-models.md)
- [Automation and Safety](docs/08-automation-safety.md)
- [Data, Storage, and Privacy](docs/09-data-storage-privacy.md)
- [Testing and Release Plan](docs/10-testing-release.md)
- [Risk Register](docs/11-risk-register.md)
- [Decision Log](docs/12-decision-log.md)
- [Environment Check](docs/13-environment-check.md)

## First Run

After dependencies are installed:

```powershell
python -m jarvis_app
```

For development from the repository root without installing the package:

```powershell
$env:PYTHONPATH="src"
python -m jarvis_app
```

## Development Rule

The assistant should start useful and safe, then become more capable in layers. Version 1 should not try to do everything. It should provide a clean local chat experience, saved history, safe app/folder actions, and basic file reading first.
