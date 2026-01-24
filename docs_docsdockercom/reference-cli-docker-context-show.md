---
title: docker context show
url: https://docs.docker.com/reference/cli/docker/context/show/
source: llms
fetched_at: 2026-01-24T14:35:47.297378592-03:00
rendered_js: false
word_count: 107
summary: This document explains the usage and purpose of the docker context show command for identifying the currently active Docker context.
tags:
    - docker-cli
    - docker-context
    - context-management
    - cli-reference
category: reference
---

DescriptionPrint the name of the current contextUsage`docker context show`

## [Description](#description)

Print the name of the current context, possibly set by `DOCKER_CONTEXT` environment variable or `--context` global option.

## [Examples](#examples)

### [Print the current context](#print-the-current-context)

The following example prints the currently used [`docker context`](https://docs.docker.com/reference/cli/docker/context/):

```
$ docker context show'
default
```

As an example, this output can be used to dynamically change your shell prompt to indicate your active context. The example below illustrates how this output could be used when using Bash as your shell.

Declare a function to obtain the current context in your `~/.bashrc`, and set this command as your `PROMPT_COMMAND`

```
function docker_context_prompt() {
        PS1="context: $(docker context show)> "
}
PROMPT_COMMAND=docker_context_prompt
```

After reloading the `~/.bashrc`, the prompt now shows the currently selected `docker context`:

```
$ source ~/.bashrc
context: default> docker context create --docker host=unix:///var/run/docker.sock my-context
my-context
Successfully created context "my-context"
context: default> docker context use my-context
my-context
Current context is now "my-context"
context: my-context> docker context use default
default
Current context is now "default"
context: default>
```