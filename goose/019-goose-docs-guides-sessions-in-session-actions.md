---
title: In-Session Actions | goose
url: https://block.github.io/goose/docs/guides/sessions/in-session-actions
source: github_pages
fetched_at: 2026-01-22T22:14:25.850794091-03:00
rendered_js: true
word_count: 1528
summary: This document explains how to manage and control AI sessions in goose through message editing, task queuing, and interruptions. It provides instructions for refining conversation history, chaining prompts for complex tasks, and redirecting the AI's workflow.
tags:
    - conversation-management
    - message-editing
    - task-queuing
    - prompt-chaining
    - workflow-control
    - session-forking
category: guide
---

goose provides features you can use to manage conversations and share information during sessions.

## Edit Message[​](#edit-message "Direct link to Edit Message")

Edit your previously sent messages to refine conversations, correct course, or try different approaches.

**Example Message Flow:**

Your original conversation has five messages. After editing message 3, all message and response context from messages 4 and 5 is deleted.

```
┌─────┐   ┌─────┐   ┌─────┐   ┌─────┐   ┌─────┐
│  1  │ → │  2  │ → │  3  │ → │  4  │ → │  5  │
└─────┘   └─────┘   └─────┘   └─────┘   └─────┘

                   Edit here
                       ↓
┌─────┐   ┌─────┐   ┌─────┐    continue from here in
│  1  │ → │  2  │ → │  3  │ →  current session, or
└─────┘   └─────┘   └─────┘    copy to new session
```

You choose to continue working in the current session or create a fork in a new session:

- [Edit in Place](#edit-in-place) to update the current session and delete all message and response context after the edited message. This lets you start your conversation over from a given point.
- [Fork Session](#fork-session) to create a new session with all conversation history prior to and including the edited message. This lets you explore different approaches while preserving your original conversation.

### Edit in Place[​](#edit-in-place "Direct link to Edit in Place")

Edit in Place gives you complete control over the conversation history by overwriting all context that follows the edited message. Your change can be as simple as fixing a path in your last message or completely starting over from a given point.

Editing in place is useful when:

- You realize a prompt you sent was unclear or incomplete
- goose misunderstood your intent and went in the wrong direction

<!--THE END-->

- goose Desktop
- goose CLI

<!--THE END-->

1. Hover over any of your previous messages
2. Click the `Edit` button that appears
3. Make your changes in the inline editor
4. Click `Edit in Place` to save your changes and reprompt goose

goose removes all conversation history after the edited message and responds contextually from that point.

Deleted Context

With Edit in Place, subsequent conversation history is permanently deleted from the session and removed from goose's context. Use this option only if you don't need goose to remember the context that follows the edited message.

### Fork Session[​](#fork-session "Direct link to Fork Session")

Fork Session creates a new session with your edited message while preserving the original conversation. You can experiment with variations and compare results while keeping the original session as a reference point.

Forking sessions is useful to:

- Compare different approaches to the same problem side-by-side
- Test how different prompts affect goose's responses

<!--THE END-->

- goose Desktop
- goose CLI

<!--THE END-->

1. Hover over any of your previous messages
2. Click the `Edit` button that appears
3. Make your changes in the inline editor
4. Click `Fork Session` to save your changes and start a new session (or use `Cmd+Enter` (macOS) or `Ctrl+Enter` (Windows/Linux))

goose copies the conversation history from the original session to the new session. The new session is named "(edited)" and the original session is unchanged.

### Editing Scenario Tips[​](#editing-scenario-tips "Direct link to Editing Scenario Tips")

- **Iterative Prompt Refinement**: Start with a basic prompt, then edit and refine based on goose's response. This often works better than trying to craft the perfect prompt from the start.
- **When to Edit vs. Interrupt**: Editing earlier messages when a conversation has gone off track can be more effective than trying to correct course using new messages or [interruptions](#interrupt-task). By editing messages, you rewrite history. With interruptions, you only affect the conversation from the current message onwards.
- **Preserving Progress**: Use Fork Session when you've made good progress but want to try a different approach. This way you can always return to the original if the new direction doesn't work out.

## Queue Messages[​](#queue-messages "Direct link to Queue Messages")

Queue messages while goose is processing a task to manage your workflow. This is useful when:

- You want to prepare next steps while goose is working
- You have a sequence of related tasks to complete
- You're using [voice dictation](#voice-dictation) and need to capture thoughts quickly

tip

goose may perform better when complex tasks are split into subtasks, a technique called [*prompt chaining*](https://www.promptingguide.ai/techniques/prompt_chaining). This structured approach can both improve accuracy and give you more control over the process.

- goose Desktop
- goose CLI

Add a message to the queue:

1. While goose is processing a response, type your next message
2. Press `Enter` to add it to the queue (or interrupts if using [interruption keywords](#interrupt-task))

Queued messages appear as numbered cards showing the queue order. The first message in the queue is automatically sent when goose finishes each response.

Related Features

- In general, pressing `Enter` while goose is processing a task queues the message, but clicking `Send` sends the task immediately and [interrupts the task](#interrupt-task)
- When you type common interrupt keywords like "stop", "wait", or "hold on" in a queued message, goose pauses until you enter or send the next message and then continues processing the queue

#### Queue Management Controls[​](#queue-management-controls "Direct link to Queue Management Controls")

Queued messages run automatically in order as goose finishes each task, but you can manage the queue:

- **Edit a message**: Click the message text to reveal the edit controls, then type your change and click `Save`
- **Reorder messages**: Hover over the message card to reveal the button, then grab it and drag the message up or down
- **Send a message**: Click the button to send a message immediately and interrupt the current task
- **Delete a message**: Click the button to delete the message
- **Clear the queue**: Click `Clear All` on the **Message Queue** card
- **Collapse or expand the queue**: Click the or button on the **Message Queue** card

#### Example Message Flow[​](#example-message-flow "Direct link to Example Message Flow")

**Without queuing:**

You send: "Can you refactor our authentication code to support OAuth 2.0 and add proper error handling? Also include unit tests for the OAuth flow, update the API documentation to reflect these changes, and create a migration script to help existing users transition to the new system."

This approach might lead to overwhelming responses where important details get missed or tasks are handled superficially. Even sending a single prompt with clear sequential steps doesn't allow goose to focus on each task individually or build context progressively.

**With queuing:**

1. You send: "Refactor the authentication code to support OAuth 2.0"
2. While goose is working, you queue the following messages:
   
   - "And add proper error handling"
   - "Add unit tests for the OAuth flow"
   - "Update the API documentation"
   - "Create migration script for existing users"

Each task builds on the previous one.

## Interrupt Task[​](#interrupt-task "Direct link to Interrupt Task")

Interrupt goose while it's processing a task to take control of the conversation. This is useful when:

- goose is heading in the wrong direction
- You realize you need to add important context
- You want to switch to a completely different task

<!--THE END-->

- goose Desktop
- goose CLI

There are two ways to interrupt a task:

#### Send interruption keyword[​](#send-interruption-keyword "Direct link to Send interruption keyword")

1. Type a prompt that includes common interruption keywords like `stop`, `wait`, `hold on`, `actually`, or `instead`. Using keywords alone or at the beginning of sentences works best for reliable detection.
2. Click `Send`

goose stops processing the current task and asks for more information.

#### Provide immediate redirection[​](#provide-immediate-redirection "Direct link to Provide immediate redirection")

1. Type a prompt with more context and clarification or that changes direction. For example:
   
   - "I forgot to mention this is for a mobile app"
   - "Let's focus on React instead of TypeScript"
2. Click `Send`

goose stops processing the current task and pivots to the new request context.

Related features

- Clicking `Send` while goose is processing a task interrupts the task but pressing `Enter` [queues the message](#queue-messages)
- Typing a stop or pause keyword in a queued message also stops goose from processing the current task
- You can also [edit a sent message](#edit-message) to provide more context and clarification or change direction during a session

Interruption Keywords List

## Voice Dictation[​](#voice-dictation "Direct link to Voice Dictation")

Speak to goose directly instead of typing your prompts.

- goose Desktop
- goose CLI

To enable voice dictation:

1. Click the button in the top-left to open the sidebar
2. Click `Settings` in the sidebar
3. Click `Chat`
4. Under `Voice Dictation`, toggle `Enable Voice Dictation` on
5. Choose between `OpenAI Whisper` or `ElevenLabs` as your dictation provider
6. Enter your API key for the provider you chose

To use voice dictation:

1. Return to the chat interface (click `Chat` in the sidebar)
2. Click the microphone on the right of the chat box and begin speaking

The first time you use voice dictation, goose will request access to your microphone. While recording, you'll see a live waveform of your audio in the input field, a timer, and the current size of your recording. Click the microphone button again to finish recording.

**If you don't see the microphone**, check the [models you have configured](https://block.github.io/goose/docs/getting-started/providers). ElevenLabs can be used as a dictation provider alongside any LLM, but OpenAI Whisper requires that you have an OpenAI model configured in goose, even if using another LLM provider for chat.

#### Important Notes[​](#important-notes "Direct link to Important Notes")

- You can record up to 10 minutes or 25MB of audio
- The audio is processed by your chosen provider (OpenAI or ElevenLabs)
- Voice input is appended to any existing text in the text input field, so you can combine typing and speaking your prompts
- Recordings are not stored locally after transcription

Provide goose with context from your codebase, documents, and other files to get more relevant and accurate assistance.

- goose Desktop
- goose CLI

Share files with goose in several ways:

1. **Drag and Drop**: Simply drag files from your computer's file explorer/finder and drop them anywhere in the chat window. The file paths will be automatically added to your message.
2. **File Browser**: Click the button at the bottom of the app to open your system's file browser and select files
3. **Manual Path**: Type or paste the file path directly into the chat input
4. **Quick File Search**: Use the [`@` shortcut key](https://block.github.io/goose/docs/guides/file-management#quick-file-search-in-goose-desktop) to quickly find and include files