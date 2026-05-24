# Decision Log

This file records major project decisions so the direction remains clear.

## Decision 001 - Build Local-First

Date: 2026-05-23

Decision:

The assistant will run locally by default and will not depend on paid APIs for core features.

Reason:

The goal is a private, offline-friendly personal assistant.

## Decision 002 - Use Ollama First

Date: 2026-05-23

Decision:

Use Ollama as the first local AI engine.

Reason:

Ollama is simple to install, has a local HTTP API, and supports many local models.

## Decision 003 - Use Python and PySide6 First

Date: 2026-05-23

Decision:

Build the first desktop app using Python and PySide6.

Reason:

Python is strong for Windows automation, local file handling, AI workflows, and fast iteration.

## Decision 004 - Chat-First UI With Actions Sidebar

Date: 2026-05-23

Decision:

The app will use a chat-first interface like ChatGPT, supported by an actions sidebar.

Reason:

This keeps interaction natural while still making PC automation visible and controllable.

## Decision 005 - Approved Tools Only

Date: 2026-05-23

Decision:

The assistant will use approved tools for automation instead of unrestricted shell access.

Reason:

This reduces the risk of unsafe or accidental PC changes.

## Decision 006 - Start With Lightweight Models

Date: 2026-05-23

Decision:

The first version should target small local models, especially 3B models, with optional 7B/8B models.

Reason:

The target PC has 16GB RAM and integrated graphics, so speed and memory use matter.

