# Risk Register

## Risk: Local Models Are Slow

Impact:

- User experience feels frustrating.

Mitigation:

- Start with 3B models.
- Stream responses.
- Keep prompts short.
- Use model selector for quality vs speed.

## Risk: Internal Storage Runs Out

Impact:

- Ollama models or app data fill the C drive.

Mitigation:

- Use external drive for models/data where possible.
- Add storage path settings early.
- Keep generated indexes optional.

## Risk: Automation Damages Files

Impact:

- Lost or changed user files.

Mitigation:

- Use approved tools only.
- Require confirmation for writes.
- Preview file operations.
- Add backups and action logs.

## Risk: UI Freezes During AI Responses

Impact:

- Desktop app feels broken.

Mitigation:

- Run Ollama calls in worker threads.
- Stream tokens safely to UI.
- Add stop button.

## Risk: Document Context Is Too Large

Impact:

- Poor answers or model errors.

Mitigation:

- Add file size limits.
- Chunk and summarize documents.
- Show truncation notices.

## Risk: Project Scope Gets Too Big

Impact:

- The project never reaches a usable version.

Mitigation:

- Keep V1 narrow.
- Treat voice, embeddings, workflows, and plugins as later versions.
- Use the task backlog as the source of truth.

## Risk: Ollama Setup Changes

Impact:

- Model storage or API behavior may differ across machines or versions.

Mitigation:

- Keep Ollama-specific code isolated.
- Add diagnostics screen.
- Store provider config in settings.

