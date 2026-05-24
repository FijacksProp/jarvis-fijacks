# UI and UX Plan

## Interface Model

The app uses a chat-first layout with two supporting sidebars.

```text
+------------------+-------------------------------+----------------------+
| History/Projects | Chat                          | Actions/Context      |
|                  |                               |                      |
| Recent chats     | Messages                      | Quick actions        |
| Workspaces       | Attachments                   | Favorite apps        |
| Settings         | Message input                 | Favorite folders     |
|                  |                               | Pending actions      |
+------------------+-------------------------------+----------------------+
```

## Main Window

Sections:

- Left sidebar: navigation and history
- Center: chat
- Right sidebar: actions and context
- Top area: model selector, Ollama status, current workspace
- Bottom area: message input, attach button, send/stop button

## Visual Direction

The first UI should be simple, clean, and functional.

Style:

- Quiet desktop productivity feel
- Clear contrast
- Compact spacing
- Professional but not boring
- Avoid heavy animations
- Avoid complicated dashboards in V1

## Chat Area

Message types:

- User message
- Assistant message
- System/status message
- Tool/action result
- Error message

Important controls:

- Send
- Stop
- Attach file
- Save response
- Copy response
- Retry response

## Actions Sidebar

Sections:

1. Quick Actions
2. Favorite Apps
3. Favorite Folders
4. Current Context
5. Pending Actions
6. Recent Outputs

Version 1 quick actions:

- New note
- Save last response
- Open output folder
- Open configured app
- Open configured folder

## Safety UX

Low-risk actions can execute directly:

- Open configured app
- Open configured folder
- Read selected file

Write or file-changing actions need confirmation:

- Create file
- Overwrite file
- Rename file
- Move file
- Delete file
- Run trusted script

Confirmation should show:

- Action name
- Target path
- Reason
- Expected result
- Confirm and cancel buttons

## Settings

Version 1 settings:

- Ollama base URL
- Default model
- App data path
- Output folder
- Favorite apps
- Favorite folders
- Theme preference

Version 2 settings:

- Document extraction options
- Search/index folders
- Workspace defaults

Version 4 settings:

- Microphone device
- Speech-to-text engine
- Text-to-speech voice
- Push-to-talk hotkey

## First Screen

On first launch, show a simple setup checklist:

- Ollama status
- Installed models
- Default output folder
- Favorite folders
- Favorite apps

The app should still allow the user to skip and configure later.

