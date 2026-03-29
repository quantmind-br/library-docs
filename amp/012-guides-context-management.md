---
title: Context Management in Amp
url: https://ampcode.com/guides/context-management
source: crawler
fetched_at: 2026-02-06T02:07:50.057088554-03:00
rendered_js: false
word_count: 1792
summary: This document explains the fundamental concept of the context window in large language models and provides instructions on how to manage context within the Amp agent platform using file mentions, shell mode, and editing tools.
tags:
    - context-window
    - llm-fundamentals
    - amp-platform
    - prompt-engineering
    - token-management
    - coding-agent
category: concept
---

![Context Management visualization](https://ampcode.com/%28guides%29/context-management-title-image.jpg)

## Important Context

The context window is the entire input a large language model receives when generating output.

It contains everything that defines a conversation with a language model: your messages, the model’s replies, any tool calls, and even the thinking blocks the model outputs to “reason”.

The longer the conversation, the more there is in the context window.

Each time you send a new message, the message is added to the context window and the entire thing sent to the model:

![Inference adds to the context window](https://ampcode.com/context/inference-1.png)

The model then “reads” all of the conversation in the context window, not just your new message, and generates a response. Then, on the next turn, when you reply to the model’s response, the model’s response and your new message are added to the conversation:

![The longer the conversation, the more there is in the context window](https://ampcode.com/context/inference-2.png)

Yes, *everything* that happens between you and a model goes into the context window, including the tool calls. It’s all represented as text, too.

If you ask the model to run a bash command your message goes in the context window. The model’s response with its confirmation that it wants to run the bash tool on your machine goes in there too, including the input parameters to the tool. Then, the bash command is executed on your machine, the results go in the context window, and it’s all sent back up again:

![Inference adds to the context window](https://ampcode.com/context/inference-tool-calls.png)

This is how the context window fundamentally works, regardless of which model, or which chat application, or which agent you use.

Equally fundamental are the following three things you should know about the context window:

**It can only get so big**. Different language models have different limits for how much context they can run inference on, but all have one. That means every conversation with a model will, at some point, run into a limit and can’t continue: the model can’t accept more input than what’s already in the conversation.

**Everything’s multiplied with everything else**. To simplify drastically: in order to run inference, all the text in the context window is turned into tokens and tokens are, essentially, numbers. As part of running inference, the model then multiplies every token with every other token. That means: *everything in the context window has an influence on the output*. Some words and tokens have more influence than others, but everything counts to *some* extent. That’s why you don’t want to have text in your context window that you don’t want to influence the result.

**Quality degrades: the more context, the worse the results.** Most models provide better results with *less* context. There are exceptions and nuances to this idea, but, generally speaking, for the best results you should try to keep your conversations short & focused. The longer your conversation goes on, the higher the chances are the model goes “off the rails”: hallucinating things that don’t exist, failing to do the same things over and over again, declaring victory while standing on a mountain of glass shards.

The context window is important. And it’s important to care about what’s in it. It not only influences the outcome of your conversation with the agent, the conversation *is* the outcome.

## Context in Amp

These context window fundamentals still hold true in Amp, even though you’re not only talking to a model in Amp, you’re talking to an **agent**.

Here’s our definition of agent: an agent is a model plus a system prompt plus tools. Tools allow the model to interact with the world outside its context window.

In Amp, you can think of the *Thread*, your conversation with the agent, as the context window. What you see in a *Thread* — your messages, the agent’s replies, the tool calls — is roughly equivalent to the context window that ultimately gets sent to the model provider to run inference on.

But since you are talking to an *agent*, not just a model, there’s more in the context window: the system prompt and the tool definitions — what turns the model into an agent — along with some other data.

![What's in the context window](https://ampcode.com/context/system-prompt.png)

Amp provides a **system prompt** that instructs the model how to do its job as a coding agent, how to communicate with you, how to use certain tools and when to use them, to not use too many emojis, and so on.

All **tool definitions** go into the system prompt. Each tool definition describes what a tool does, what its input parameters are, and what output the model can expect when using the tool.

The **AGENTS.md** files you have in your codebase go into the context window too. That’s how you can tell the agent about your codebase and its conventions without having to repeat it by hand in every new thread.

Amp also adds **environmental data** to the context window: which operating system you use, what files are in the current directory, whether you have a file open or not and, if so, whether you have selected some text or not.

Change one of these ingredients and how the agent behaves might change drastically. If you, for example, replace the `AGENTS.md` in the context window with a collection of Shakespearean sonnets, the agent’s response to `"Run the tests in the ./cli folder"` might be disappointing.

The context window is important.

## Working with the context window

Amp gives you several options to manage what’s in the context window and what isn’t.

You can *add* context by @-mentioning files, using shell mode, or asking the agent to run specific tools.

You can *change or remove* context by editing messages or restoring the context window to an earlier point in the conversation.

To turn a single context window into multiple, with different content, Amp allows you to use handoff to distill the contents of a context window into a message for another, fresh context window.

Or you can reference other Amp threads, meaning: other context windows, to let the agent decide which information to pull out of *that* context window into *this* one.

## Mentioning Files

In the Amp CLI and editor extensions you can include the content of files in the context window by @-mentioning them:

1. Type `@` followed by parts of the filename you want to include
2. Hit return to insert the filename into your message

Once you submit your message, Amp will try to read all the filenames that are mentioned with `@<filename>`. Binary files are ignored, image files are attached as images, and text files will be included as is, except that they’re truncated so as to not use up too much of the context window. Right now, they’re truncated to a maximum of 500 lines and 2KB per line. If that’s not enough, the agent’s usually smart enough to read the rest of the file, if needed.

![Mentioning files](https://ampcode.com/context/mentioning-files.png)

Remember that everything in the context window is multiplied with everything else. Mentioning files - meaning: explicitly putting file contents into the context window - is a powerful way to influence in which direction the agent will go.

## Shell Mode

When using the Amp CLI, you can use [Shell Mode](https://ampcode.com/manual#cli-shell-mode) to execute terminal commands inside of the Amp CLI and then put the commands along with their output and exit status, into the context window.

Type `$` followed by a command, hit return to execute it, and the command and its output will be included in the context window the next time you send a message:

![Mentioning files](https://ampcode.com/context/shell-mode.png)

## Edit & Restore

Amp gives you the ability to *edit* previous messages of yours in a thread.

In the editor extensions, you click on a previous message and it puts you into edit-mode, allowing you to change that message.

In the Amp CLI, you can use `arrow-up / arrow-down` or `tab / shift-tab` to navigate to a previous message and then press `e` to edit it.

Once you submit an edited message, the context window, the thread, gets reset so that the just-edited message is the new *last* message in the thread. Then inference runs again.

This allows you to remove things from the context window you no longer want in there. Instead of having a “false turn” permanently in the conversation, you can remove it.

![Editing a previous message](https://ampcode.com/context/edit-message.png)

You can also *restore* the state of a thread to a previous message. In the editor extension, you need to hover over a previous message and then click *Restore*. In the Amp CLI, instead of pressing `e` to edit, you use `r` to restore.

When you restore to a message, that message is removed and the thread is restored to include everything up and *excluding* that message:

![Restoring to a previous message](https://ampcode.com/context/restoring-message.png)

## Handoff

Handoff is a feature in Amp that lets you easily extract data from a thread and take it with you to a new, focused thread.

When using Handoff in an existing thread, you first specify a goal for what you want to do next, say “I want to now add a UI component for the data structure we just added”. Another model then analyzes the thread you’re handing off from, to extract relevant information in messages, tool calls, and files. Based on that, a new message that contains the relevant information and files is drafted and put in the prompt editor of a new thread. You can then either adjust that message or submit it right away, to create a new, focused thread.

Handoff is a great tool to keep threads (and thus the context window) small and focused, while working on bigger projects that require multiple threads with the same information.

![Using Handoff to create a new thread](https://ampcode.com/context/handoff.png)

## Referencing Threads

You can extract information from other threads by referencing them. Either reference the full URL of a thread in a message or just thread ID.

In both the Amp CLI and editor extensions, you can use the @-mention menu to find threads by title.

When you reference a thread in a message, the agent in Amp can use the `read_thread` tool to extract relevant information from the referenced threads. It does this by tasking a second model to extract the information that’s relevant to your prompt, which allows you to get to information from another thread, without having to include all of it.

The prompt with which you reference threads, e.g. “Extract the final, working SQL query from thread T-1234”, is used to extract the relevant information. In this case, the second model will be tasked to extract a single SQL query from the thread, but not the other things that you might have discussed in that thread.

![Reference other threads to extract information out of them](https://ampcode.com/context/referencing-threads.png)

## Further Reading

See [200k Tokens Is Plenty](https://ampcode.com/200k-tokens-is-plenty).