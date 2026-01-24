---
title: JSONArgsRecommended
url: https://docs.docker.com/reference/build-checks/json-args-recommended/
source: llms
fetched_at: 2026-01-24T14:32:18.458824626-03:00
rendered_js: false
word_count: 285
summary: This document explains the differences between shell and exec forms for Dockerfile ENTRYPOINT and CMD instructions, focusing on signal handling and PID 1 behavior.
tags:
    - dockerfile
    - entrypoint
    - cmd
    - signal-handling
    - pid-1
    - container-best-practices
category: guide
---

`ENTRYPOINT` and `CMD` instructions both support two different syntaxes for arguments:

- Shell form: `CMD my-cmd start`
- Exec form: `CMD ["my-cmd", "start"]`

When you use shell form, the executable runs as a child process to a shell, which doesn't pass signals. This means that the program running in the container can't detect OS signals like `SIGTERM` and `SIGKILL` and respond to them correctly.

❌ Bad: the `ENTRYPOINT` command doesn't receive OS signals.

To make sure the executable can receive OS signals, use the exec form for `CMD` and `ENTRYPOINT`, which lets you run the executable as the main process (`PID 1`) in the container, avoiding a shell parent process.

✅ Good: the `ENTRYPOINT` receives OS signals.

Note that running programs as PID 1 means the program now has the special responsibilities and behaviors associated with PID 1 in Linux, such as reaping child processes.

### [Workarounds](#workarounds)

There might still be cases when you want to run your containers under a shell. When using exec form, shell features such as variable expansion, piping (`|`) and command chaining (`&&`, `||`, `;`), are not available. To use such features, you need to use shell form.

Here are some ways you can achieve that. Note that this still means that executables run as child-processes of a shell.

#### [Create a wrapper script](#create-a-wrapper-script)

You can create an entrypoint script that wraps your startup commands, and execute that script with a JSON-formatted `ENTRYPOINT` command.

✅ Good: the `ENTRYPOINT` uses JSON format.

#### [Explicitly specify the shell](#explicitly-specify-the-shell)

You can use the [`SHELL`](https://docs.docker.com/reference/dockerfile/#shell) Dockerfile instruction to explicitly specify a shell to use. This will suppress the warning since setting the `SHELL` instruction indicates that using shell form is a conscious decision.

✅ Good: shell is explicitly defined.