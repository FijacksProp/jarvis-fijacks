# Automation and Safety

## Safety Philosophy

The assistant should be useful, but not reckless.

The model should never receive unrestricted control of the PC. Instead, the app exposes approved tools with clear boundaries.

## Tool Safety Levels

Level 0 - Read or open only:

- Open configured app
- Open configured folder
- Read selected file
- List files in selected folder

Level 1 - Create only:

- Create note in output folder
- Create report in output folder
- Create task

Level 2 - Modify files:

- Rename file
- Move file
- Copy file
- Edit selected file
- Create files outside output folder

Level 3 - Dangerous:

- Delete file
- Run script
- Run shell command
- Change system settings

Version 1 should support mostly Level 0 and limited Level 1.

## Confirmation Rules

No confirmation required:

- Open configured app
- Open configured folder
- Read user-selected file

Confirmation required:

- Create file
- Overwrite file
- Move file
- Rename file
- Run script

Blocked in early versions:

- Delete files
- Run arbitrary shell commands
- Modify system settings
- Access password/browser data

## Tool Design

Each tool should define:

- Name
- Description
- Arguments
- Safety level
- Allowed paths or allowed targets
- Requires confirmation
- Execution function
- Result summary

Example:

```text
Tool: open_folder
Args: folder_id or path
Safety: Level 0
Allowed: configured favorite folders, workspace root folders
Confirmation: no
```

## Audit Log

Every action should be recorded.

Fields:

- Action name
- Arguments
- Safety level
- Requested by user or assistant
- Confirmation status
- Execution result
- Timestamp
- Conversation ID

## Path Safety

Rules:

- Normalize paths before use.
- Validate existence before opening.
- Restrict write operations to configured output/workspace folders in early versions.
- Warn on system paths.
- Never silently overwrite.

## Automation Growth Path

Version 1:

- Open apps
- Open folders
- Save notes/reports
- Read selected files

Version 2:

- Search folders
- Create workspace files
- Generate summaries

Version 3:

- Multi-step action queue
- File organization
- Trusted scripts
- Backups for file edits/moves

Version 5:

- Plugin-style tools
- User-created automations

