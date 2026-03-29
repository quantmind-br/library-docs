---
title: Through the Agent, Into the Shell
url: https://ampcode.com/news/through-the-agent-into-the-shell
source: crawler
fetched_at: 2026-02-06T02:08:35.70760267-03:00
rendered_js: false
word_count: 141
summary: This document introduces and explains the shell mode feature for the Amp CLI, which allows users to execute shell commands directly within the prompt and manage their inclusion in the agent context window.
tags:
    - amp-cli
    - shell-mode
    - command-line-interface
    - developer-tools
    - incognito-mode
category: guide
---

Finally: the Amp CLI now also lets you execute shell commands, right there in the prompt input.

It's called shell mode. You activate it by starting a message with `$`. Everything you type after that will be executed as a shell command. The command and its output will be included in the context window the next time you send a message to the agent.

It's a good way to show the agent the output of a command without the agent having to execute it.

Type `$$` and you'll activate the incognito version of shell mode in which the commands are executed in the same way, but not included in the context.

That, in turn, is handy when you want to run noisy commands to check on something, or fire off a quick command that you'd otherwise run in a separate terminal.