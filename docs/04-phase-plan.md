# Phase Plan

## Phase 0.1 - Environment Check

Tasks:

- Verify Python version.
- Verify Ollama installation.
- Check available internal and external storage.
- Choose the app data location.
- Choose the model storage location if supported by local Ollama setup.

Deliverables:

- Environment notes.
- First local model selected.
- Storage path decision recorded.

## Phase 0.2 - Project Skeleton

Tasks:

- Create source folder structure.
- Add dependency management.
- Add basic config loading.
- Add basic logging.
- Add empty PySide6 shell.

Deliverables:

- App window opens.
- Config file can be read/written.
- Logs are created locally.

## Phase 0.3 - Ollama Smoke Test

Tasks:

- Build an Ollama client.
- Add health/status check.
- List installed models.
- Send a test chat request.

Deliverables:

- Local model response in a test script.
- Error message if Ollama is not running.

## Phase 1.1 - Chat UI

Tasks:

- Build main window layout.
- Add left history sidebar.
- Add central chat panel.
- Add right actions sidebar.
- Add message input.
- Add send button and keyboard shortcut.

Deliverables:

- User can type messages.
- UI can display user and assistant messages.

## Phase 1.2 - Streaming Local Chat

Tasks:

- Connect UI to Ollama client.
- Stream model response into chat.
- Add stop generation button.
- Add model selector.
- Handle no-model and server-offline states.

Deliverables:

- User can chat locally inside the app.
- User can change model from settings or top bar.

## Phase 1.3 - SQLite History

Tasks:

- Create database schema.
- Save conversations.
- Save messages.
- Load recent chats.
- Rename and delete conversations.

Deliverables:

- Chat history survives app restart.
- User can switch between previous chats.

## Phase 1.4 - Basic PC Actions

Tasks:

- Add favorite apps settings.
- Add favorite folders settings.
- Implement open app tool.
- Implement open folder tool.
- Add action result messages.

Deliverables:

- User can open configured apps/folders from sidebar.
- Assistant can propose these actions.

## Phase 1.5 - File Attachments

Tasks:

- Add attach file button.
- Read supported text/code files.
- Show attached file chips.
- Build context from selected files.
- Add file size limits.

Deliverables:

- User can ask questions about selected text/code files.

## Phase 1.6 - Notes and Reports

Tasks:

- Add output folder setting.
- Add save response as note.
- Add save response as report.
- Add generated output list.
- Add confirmation before overwriting.

Deliverables:

- User can save useful responses as local files.

## Phase 2.1 - Document Extraction

Tasks:

- Add PDF extraction.
- Add DOCX extraction.
- Add chunking.
- Add document summary prompt.

Deliverables:

- User can summarize and ask questions about PDF/DOCX files.

## Phase 2.2 - Workspaces

Tasks:

- Create project/workspace table.
- Add workspace sidebar section.
- Save root folder and notes per workspace.
- Allow workspace-specific context.

Deliverables:

- User can organize chats and files by project.

## Phase 2.3 - Search and Indexing

Tasks:

- Add filename search.
- Add basic content search.
- Add optional embeddings later.
- Store search/index metadata.

Deliverables:

- User can search selected folders from the assistant.

## Phase 3.1 - Tool Registry

Tasks:

- Define tool interface.
- Add tool schemas.
- Add safety levels.
- Add action queue.

Deliverables:

- Assistant actions are structured and auditable.

## Phase 3.2 - File Organization

Tasks:

- Add copy/move/rename preview.
- Add backup or rollback where possible.
- Add conflict handling.
- Add logs.

Deliverables:

- User can safely organize files through assistant-guided actions.

## Phase 4.1 - Voice Input

Tasks:

- Add push-to-talk button.
- Add local STT option.
- Add transcript confirmation.

Deliverables:

- User can speak a command and edit transcript before sending.

## Phase 4.2 - Voice Output

Tasks:

- Add local TTS engine.
- Add voice settings.
- Add mute/stop controls.

Deliverables:

- Assistant can read selected responses aloud.

## Phase 5.1 - Packaging

Tasks:

- Add packaging script.
- Add Windows shortcut.
- Add installer or portable package.
- Add diagnostics screen.

Deliverables:

- User can run the app as a normal desktop program.

