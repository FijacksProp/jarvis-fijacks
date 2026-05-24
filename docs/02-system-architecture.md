# System Architecture

## High-Level Architecture

The app is split into five main parts:

1. Desktop UI
2. Assistant core
3. Tool and automation layer
4. Local AI provider
5. Local storage

```text
User
  |
  v
PySide6 Desktop UI
  |
  v
Assistant Core
  |        |         |
  |        |         v
  |        |    Tool Registry
  |        |         |
  |        |         v
  |        |    Safe PC Actions
  |        |
  |        v
  |    SQLite Storage
  |
  v
Ollama Local API
```

## Desktop UI

Responsibilities:

- Render chat messages.
- Stream assistant responses.
- Show chat history.
- Show action sidebar.
- Collect confirmations.
- Let user attach files.
- Expose settings.

Recommended modules:

```text
src/jarvis_app/ui/main_window.py
src/jarvis_app/ui/chat_view.py
src/jarvis_app/ui/sidebar_history.py
src/jarvis_app/ui/sidebar_actions.py
src/jarvis_app/ui/settings_dialog.py
```

## Assistant Core

Responsibilities:

- Build prompts.
- Manage conversation state.
- Call Ollama.
- Decide when a model response is plain text vs an action proposal.
- Pass approved actions to the tool layer.
- Save messages and metadata.

Recommended modules:

```text
src/jarvis_app/core/assistant.py
src/jarvis_app/core/prompts.py
src/jarvis_app/core/session.py
src/jarvis_app/core/context_builder.py
```

## Local AI Provider

Responsibilities:

- Connect to Ollama HTTP API.
- List available models.
- Send chat requests.
- Support streaming responses.
- Handle unavailable model or Ollama server errors.

Recommended modules:

```text
src/jarvis_app/ai/ollama_client.py
src/jarvis_app/ai/model_registry.py
```

## Tool and Automation Layer

Tools should be explicit, named, and safety-scored.

Example tool categories:

- open app
- open folder
- read file
- search folder
- create note
- save report
- copy/move/rename file
- launch trusted script

Recommended modules:

```text
src/jarvis_app/tools/registry.py
src/jarvis_app/tools/base.py
src/jarvis_app/tools/open_app.py
src/jarvis_app/tools/open_folder.py
src/jarvis_app/tools/files.py
src/jarvis_app/tools/notes.py
```

## Local Storage

Use SQLite for structured data and a local workspace folder for generated files.

Recommended modules:

```text
src/jarvis_app/storage/database.py
src/jarvis_app/storage/repositories.py
src/jarvis_app/storage/migrations.py
```

## Suggested Project Structure

```text
JARVIS/
  README.md
  PROJECT_PLAN.md
  TASKS.md
  docs/
  src/
    jarvis_app/
      ai/
      core/
      storage/
      tools/
      ui/
      utils/
  data/
    jarvis.sqlite3
    outputs/
    attachments/
    indexes/
  logs/
  tests/
```

## Main Runtime Flow

1. User sends message.
2. UI sends message and selected context to assistant core.
3. Assistant core builds prompt.
4. Ollama client streams model response.
5. Assistant core detects action proposals, if any.
6. UI shows response and pending actions.
7. User approves action.
8. Tool registry executes approved action.
9. Result is logged and added to chat.

## Action Proposal Format

For version 1, actions can be handled by app UI buttons and direct user clicks. Later, the assistant can produce structured JSON action proposals.

Example future format:

```json
{
  "type": "tool_request",
  "tool": "open_folder",
  "arguments": {
    "path": "D:/School"
  },
  "reason": "The user asked to open the school folder.",
  "safety_level": "low"
}
```

