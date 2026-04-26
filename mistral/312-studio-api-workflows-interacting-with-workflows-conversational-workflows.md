---
title: Conversational Workflows | Mistral Docs
url: https://docs.mistral.ai/studio-api/workflows/interacting-with-workflows/conversational_workflows
source: sitemap
fetched_at: 2026-04-26T04:14:15.678506508-03:00
rendered_js: false
word_count: 876
summary: This document explains how to build and integrate conversational workflows in the Mistral platform, covering input collection, UI components, status tracking, and workflow publishing.
tags:
    - conversational-workflows
    - interactive-ui
    - chat-interface
    - workflow-automation
    - python-sdk
    - user-input-handling
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Conversational workflows are meant to be integrated in conversations interface, allowing a user to trigger a workflow, interact with it by providing inputs during its execution, and follow its progress.

To use Conversational workflow features, install the Mistral plugin.

## Simple Conversation

The simplest conversational workflow sends an assistant message to the user, then waits for their response. Extend `InteractiveWorkflow` and use `send_assistant_message()` followed by `wait_for_input()` with `ChatInput`:

```python
```

`send_assistant_message()` displays a message to the user in the chat interface. It also accepts an optional `canvas` keyword argument to include a `CanvasResource` alongside the text (see [Canvas Editing](#canvas-editing-human-in-the-loop)). `ChatInput()` pauses the workflow and waits for the user to respond. You can optionally pass a `prompt` to `ChatInput()` to provide additional context (in placeholder) and `suggestions` to offer pre-filled options that users can select directly.

`wait_for_input()` accepts an optional `timeout` parameter. If the user doesn't respond within the specified duration, an `asyncio.TimeoutError` is raised. The timeout can be a `timedelta` or a number of seconds (`float`). By default, the workflow waits indefinitely.

Wrap the call in a `try`/`except asyncio.TimeoutError` block to handle the timeout gracefully instead of failing the workflow.

## Form Input

For workflows that need structured form input with typed fields, validation, and custom UI rendering, use `FormInput` instead of `ChatInput`:

```python
```

All field types (except `FileField`) support an optional `prefilled_value` parameter. This is a **UI hint only** — it pre-fills the form field but does not make the field optional. The value must still be explicitly submitted by the user. Invalid prefilled values (out of bounds, non-matching pattern, unknown option) are silently ignored.

### TextField

By default the workflow receives URLs (strings) pointing to files uploaded by the user. With `include_metadata=True`, it receives `FileWithMetadataValue` objects instead:

```python
```

> [!warning] These URLs may expire, so if your workflow needs long-term access to the files, it is responsible for storing them elsewhere.

## Confirmation Input

For workflows that need a simple single-choice confirmation with direct submit, use `ConfirmationInput` or `AcceptDeclineConfirmation`. These helpers create a single-field form where selecting an option immediately submits the form.

`ConfirmationInput` provides a list of options that should be rendered as buttons. Selection of an option should immediately submit the form:

```python
```

The returned object has a `choice` property containing the selected option value.

`AcceptDeclineConfirmation` is a specialized confirmation with two options: accept and decline. Clients can render this as a standard validation UI with keyboard shortcuts for quick responses:

```python
```

Use the `is_accepted()` helper function to check whether the user accepted or declined:

```python
```

## Todo List

Display a checklist of steps with real-time status updates using `TodoList`:

```python
```

There are two ways to update the status of a `TodoListItem`:

**Context Manager:**

```python
```

**Manual Control (for fine-grained status updates):**

```python
```

Use manual control when you need to update status at specific points, handle conditional flows, or implement custom exception handling.

## Agent Streaming

When using agents with `RemoteSession(stream=True)`, responses are automatically streamed to the UI as custom events. No additional code is needed:

```python
```

When `stream=True`, the agent's text output is streamed token-by-token to the UI. This provides a responsive experience for longer responses.

## Rich Content

Return rich content like markdown, code, or diagrams using `ResourceOutput`:

```python
```

## Canvas Editing (Human-in-the-Loop)

You can send a canvas mid-workflow using `send_assistant_message()` and then let the user edit it. The `canvas_uri` passed to `CanvasInput` must match the `uri` of a `CanvasResource` output from a previous step.

`CanvasInput` returns a model with:
- `canvas.title` — the title of the edited canvas
- `canvas.content` — the edited content
- `chatInput` — optional chat message (only present when `prompt` is provided and the user sends a message)

## UI Components

Workflows can render rich, interactive UI components in the chat interface using the design system component library. Components are defined as Python objects and sent as `UIComponentResource` resources.

All components are imported from `mistralai.workflows.plugins.mistralai.conversational_ui_components`.

Components that accept `children` can contain other components, allowing you to build complex layouts:

```python
```

## Tool UI States

Tool UI States provide optional visual representations of tool execution in the chat interface. When attached to `ChatAssistantWorkingTask`, they enable specialized UI feedback for different types of tool operations, allowing workflows to display the status and results of tool calls in a structured, user-friendly way.

There are three types of tool UI states:

```python
```

Represents file operations such as creating, replacing, or deleting files:

```python
```

Represents generic tool execution with various status states:

```python
```

Represents command execution with running/success/failed states:

```python
```

Tool UI States can be attached to `ChatAssistantWorkingTask` to provide visual feedback during tool execution:

```python
```

## Publishing as Assistant

To publish a conversational workflow as an assistant in Le Chat (Mistral's chat interface), your workflow must return a `ChatAssistantWorkflowOutput`. The output won't be displayed in Le Chat, but we enforce a common interface for inter-operability.

When a workflow accepts a union of input types, clients may need a way to know which variant to use. The `@input_tag` decorator adds an `x-input-tag` field to a model's JSON schema so clients can identify and select the right one:

```python
```

`SimpleParams.model_json_schema()` now contains `"x-input-tag": "simplified"`. Clients inspect the union members in the workflow's `input_schema` and select the variant whose tag they recognise.

## Error Signaling

To signal that a workflow has failed, set `isError=True` on the output. The text content is used as the error message displayed to the user, and the workflow is marked as failed in the conversation:

```python
```

## Structured Content

`ChatAssistantWorkflowOutput` accepts an optional `structuredContent` field (`dict[str, Any]`) for attaching arbitrary structured data to the workflow output.

## Full Example

Here's a full expense approval workflow combining todo list, user input, and streaming agent analysis:

```python
```