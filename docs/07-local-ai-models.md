# Local AI and Models

## Hardware Strategy

Target hardware:

- 16GB RAM
- Intel UHD Graphics 620
- Limited internal storage
- 500GB external drive available

This means the app should be designed around efficient local inference.

Guidelines:

- Prefer 3B models for responsiveness.
- Use 7B or 8B models only when better quality is worth slower responses.
- Avoid 13B+ models for normal use on this machine.
- Keep context sizes moderate.
- Chunk documents before sending content to the model.
- Store large model/data files outside the internal drive when possible.

## Ollama Role

Ollama is the first AI provider.

Responsibilities:

- Run local models.
- Provide chat API.
- Provide model list.
- Provide embeddings later if needed.

The app should keep provider logic separate so another local provider can be added later.

## Candidate Model Types

General assistant:

- Small 3B instruct model for default chat
- 7B or 8B instruct model for higher quality when performance is acceptable

Coding:

- Small coder model for quick explanation and debugging
- Larger coder model only if the machine handles it comfortably

Embeddings:

- Local embedding model for semantic document search in later versions

Candidate models to test through Ollama:

- llama3.2:3b or similar small general model
- qwen2.5:3b or similar small general model
- qwen2.5-coder:3b or 7b for coding
- deepseek-coder style model if performance is acceptable
- nomic-embed-text or similar embedding model for indexing

Exact model names should be verified locally with Ollama before installation.

## Model Selection Plan

Phase 0:

- Install one small general model.
- Test chat speed.
- Measure memory use.

Phase 1:

- Add one coding model if storage allows.
- Expose model selector in the UI.

Phase 2:

- Add embedding model for file/project search.

## Prompt Modes

Version 1 should support general chat only, with hidden system instructions.

Version 2 can add modes:

- General
- Coding
- Study
- Report writing
- Proposal writing
- Document analysis
- PC automation

## Context Management

The app should not dump huge files into the prompt.

Rules:

- Limit attached file content in V1.
- Summarize or chunk large files in V2.
- Track which files are active context.
- Show when context was truncated.
- Keep system prompts short.

