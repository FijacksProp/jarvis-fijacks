# Data, Storage, and Privacy

## Local-First Storage

The assistant should store data locally by default.

Data types:

- Chat history
- Settings
- Favorite apps/folders
- Workspaces
- Action logs
- Generated notes/reports
- File indexes
- Optional embeddings

## Suggested Data Locations

Because internal free storage is limited, large or growing data should be placed on the external drive when possible.

Internal drive:

- App code
- Small config files
- Logs

External drive:

- Ollama models if configured successfully
- Assistant data folder
- Generated outputs
- Document indexes
- Backups

Example assistant data structure:

```text
JarvisData/
  jarvis.sqlite3
  outputs/
    notes/
    reports/
    summaries/
  attachments/
  indexes/
  backups/
  logs/
```

## SQLite Tables

Initial schema:

- conversations
- messages
- settings
- favorite_apps
- favorite_folders
- workspaces
- action_logs
- generated_outputs

Later schema:

- documents
- document_chunks
- document_indexes
- tasks
- tool_definitions
- trusted_scripts

## Privacy Rules

- Do not send data to cloud services by default.
- Do not scan folders unless user selects or configures them.
- Show selected context files in the UI.
- Allow user to delete chats and indexes.
- Keep logs useful but not overly invasive.

## Backup Plan

Version 1:

- Manual backup by copying data folder.

Version 3:

- In-app backup button.
- Export SQLite database and outputs.

Version 5:

- Scheduled local backup.
- Restore flow.

## Retention Rules

Suggested defaults:

- Keep chat history until user deletes it.
- Keep generated outputs until user deletes them.
- Keep action logs for 90 days, configurable later.
- Allow clearing indexes without deleting source files.

