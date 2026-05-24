# Feature Specs

## Feature: Local Chat

Purpose:

Allow the user to chat with a local Ollama model from the desktop app.

Version:

- V1

Requirements:

- Send user messages to Ollama.
- Stream assistant responses.
- Show clear error if Ollama is not running.
- Let user choose installed model.
- Save messages to SQLite.

Acceptance:

- User can close and reopen the app without losing chat history.
- User sees assistant response streaming.
- User can stop generation.

## Feature: Chat History

Purpose:

Store conversations locally.

Version:

- V1

Requirements:

- Create new chat.
- Rename chat.
- Delete chat with confirmation.
- Load previous chat.
- Store created and updated timestamps.

Acceptance:

- Chats appear in the left sidebar.
- Messages reload correctly after restart.

## Feature: File Attachments

Purpose:

Let user ask questions about selected files.

Version:

- V1 text/code/PDF/DOCX files

Requirements:

- Support selected text, code, PDF, and DOCX file types.
- Limit file size in V1.
- Display attached files.
- Include extracted content in prompt context.
- Warn when file is too large.

Acceptance:

- User can attach a Python or markdown file and ask for explanation.

Current V1 behavior:

- The Attach button beside the input opens a file picker.
- Attached files appear in the right sidebar.
- Attached files show type, size, and a readable preview.
- Attached file text is bundled directly into the user prompt as explicit file context.
- User can remove one selected attachment or clear all attachments.
- Quick analysis buttons can summarize files, review code, or create study notes.
- File-aware prompt instructions tell Jarvis to answer from attached files first and say when the answer is not present.
- Supported file types include text, markdown, common code files, JSON, HTML, CSS, CSV, XML, YAML, TOML, INI, logs, PDF, and DOCX.
- Text-based PDFs are supported; scanned/image PDFs need OCR, which is not in V1 yet.
- PDF/DOCX attachments use a shorter excerpt than code/text files so the local 3B model can respond reliably on the target PC.

## Feature: Save Notes and Reports

Purpose:

Turn useful assistant output into local files.

Version:

- V1

Requirements:

- Save response as markdown note.
- Save response as report.
- Use configured output folder.
- Avoid overwriting without confirmation.

Acceptance:

- User can save generated content and open it from recent outputs.

Current V1 behavior:

- User can save the last assistant response as a markdown note under the configured output folder.
- The save action is logged back into the current chat as a system message.

## Feature: Workspace Profiles

Purpose:

Organize chats, files, and actions around projects.

Version:

- V2

Requirements:

- Workspace has name, root path, notes, created date.
- Chats can be linked to workspace.
- Actions can use workspace context.

Acceptance:

- User can switch to a project and keep project-specific context.

## Feature: Folder Search

Purpose:

Find local files and relevant content.

Version:

- V2

Requirements:

- Search filenames.
- Search text content for supported files.
- Show matched files.
- Allow user to attach/open matched files.

Acceptance:

- User can search a school folder for a keyword and view results.

## Feature: Action Queue

Purpose:

Let assistant propose multi-step actions safely.

Version:

- V3

Requirements:

- Actions display before execution.
- Each action has name, reason, arguments, safety level.
- User can approve, reject, or edit when possible.
- Execution result is logged.

Acceptance:

- Assistant can propose "open folder, search files, summarize matches" as separate visible steps.
