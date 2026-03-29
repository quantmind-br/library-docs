---
title: Tool-Level Permissions
url: https://ampcode.com/news/tool-level-permissions
source: crawler
fetched_at: 2026-02-06T02:08:40.820900718-03:00
rendered_js: false
word_count: 136
summary: This document explains how to configure granular tool-level permissions in Amp, allowing users to define specific rules for allowing, rejecting, or delegating tool calls and Bash commands.
tags:
    - permissions
    - tool-management
    - configuration
    - access-control
    - security-policy
category: configuration
---

Instead of only allowing you to configure which Bash commands are allowed to run and which aren't, Amp now gives you the ability to define which tool it's allowed to run, and with which arguments.

When Amp wants to call a tool, it first checks your list of permissions to find an entry that matches the tool and the tool call arguments. The matched entry then tells Amp to either *allow* the tool call, *reject* it, *ask* you for confirmation, or *delegate* the decision to another program. If no matching entry is found, Amp checks the built-in permission list that contains sensible defaults.

You can define these granular tool-level permissions by adding entries to the `amp.permissions` list in your [configuration file](https://ampcode.com/manual#permissions). Here's an example:

```
"amp.permissions": [
  // Ask before running a command containing "git commit"
  { "tool": "Bash", "matches": { "cmd": "*git commit*" }, "action": "ask"},
  // Reject command containing "python " or "python3 "
  { "tool": "Bash", "matches": { "cmd": ["*python *", "*python3 *"] }, "action": "reject"},
  // Ask before running any MCP tool
  { "tool": "mcp__*", "action": "ask"},
  // Delegate everything else to a permission helper (must be on $PATH)
  { "tool": "*", "action": "delegate", "to": "my-permission-helper"}
]
```

You can read more about the new tool-level permissions [in the manual](https://ampcode.com/manual#permissions).