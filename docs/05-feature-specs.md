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

## Feature: Favorite Apps

Purpose:

Open trusted apps from the assistant.

Version:

- V1

Requirements:

- User can add app name and executable path.
- App appears in action sidebar.
- Tool opens only configured apps.
- Failed launch shows error.

Acceptance:

- User can open VS Code, browser, or other approved apps from the sidebar.

## Feature: Favorite Folders

Purpose:

Open trusted folders from the assistant.

Version:

- V1

Requirements:

- User can add folder name and path.
- Folder appears in action sidebar.
- Tool validates folder exists before opening.

Acceptance:

- User can open school, projects, or documents folders from the sidebar.

## Feature: File Attachments

Purpose:

Let user ask questions about selected files.

Version:

- V1 text/code files
- V2 PDF/DOCX

Requirements:

- Support selected file types.
- Limit file size in V1.
- Display attached files.
- Include extracted content in prompt context.
- Warn when file is too large.

Acceptance:

- User can attach a Python or markdown file and ask for explanation.

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

