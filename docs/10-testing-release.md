# Testing and Release Plan

## Testing Strategy

The project should use a mix of unit tests, integration tests, and manual desktop checks.

## Unit Tests

Test:

- Ollama client request building
- Database repositories
- Settings loading/saving
- Tool validation
- Path safety
- File readers
- Prompt/context building

## Integration Tests

Test:

- Save and load conversation.
- Attach file and build context.
- Execute open-folder action with a test path.
- Save generated note.
- Handle Ollama offline state.

## Manual UI Checks

Before each release:

- App launches.
- Chat sends and receives messages.
- Streaming works.
- Stop generation works.
- History loads.
- Settings save.
- Favorite app/folder actions work.
- File attachment works.
- Save note/report works.
- Error messages are understandable.

## Release Milestones

### Release 0.1

- App skeleton
- Ollama smoke test
- Empty UI shell

### Release 0.2

- Working local chat
- Model selector
- Basic settings

### Release 1.0

- MVP complete
- Chat history
- Safe app/folder actions
- File attachments
- Save outputs

### Release 2.0

- Document support
- Workspaces
- Search
- Study/project workflows

### Release 3.0

- Multi-step automation
- Action queue
- File organization

### Release 4.0

- Voice input/output
- Tray mode

### Release 5.0

- Packaged app
- Backup/restore
- Plugin-style tools

## Quality Gates

Version 1 should not be considered complete until:

- The app handles Ollama not running.
- SQLite history survives restart.
- File write actions require confirmation.
- No arbitrary shell execution is exposed.
- The UI does not freeze during model generation.

