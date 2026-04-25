---
title: '`lms chat`'
url: https://lmstudio.ai/docs/cli/local-models/chat
source: sitemap
fetched_at: 2026-04-07T21:28:38.165290064-03:00
rendered_js: false
word_count: 167
summary: This document details the various command-line flags and subcommands available with `lms chat`, allowing users to interact with local language models for single prompts, interactive sessions, or piping input.
tags:
    - cli-tool
    - local-llm
    - command-flags
    - chat-interface
    - scripting
category: reference
---

Use `lms chat` to talk to a local model directly in the terminal. This is handy for quick experiments or scripting.

### Flags[](#flags)

\[model] (optional) : string

Identifier of the model to use. If omitted, you will be prompted to pick one.

-p, --prompt (optional) : string

Send a one-off prompt and print the response to stdout before exiting

-s, --system-prompt (optional) : string

Custom system prompt for the chat

--stats (optional) : flag

Show detailed prediction statistics after each response

--ttl (optional) : number

Seconds to keep the model loaded after the chat ends (default: 3600)

### Start an interactive chat[](#start-an-interactive-chat)


You will be prompted to pick a model if one is not provided.

### Chat with a specific model[](#chat-with-a-specific-model)


### Send a single prompt and exit[](#send-a-single-prompt-and-exit)

Use `-p` to print the response to stdout and exit instead of staying interactive:

```

lms chat my-model -p "Summarize this release note"
```

### Set a system prompt[](#set-a-system-prompt)

```

lms chat my-model -s "You are a terse assistant. Reply in two sentences."
```

### Keep the model loaded after chatting[](#keep-the-model-loaded-after-chatting)

```

lms chat my-model --ttl 600
```

### Pipe input from another command[](#pipe-input-from-another-command)

`lms chat` reads from stdin, so you can pipe content directly into a prompt:

```

cat my_file.txt | lms chat -p "Summarize this, please"
```