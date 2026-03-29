---
title: docker container attach
url: https://docs.docker.com/reference/cli/docker/container/attach/
source: llms
fetched_at: 2026-01-24T14:34:51.786061834-03:00
rendered_js: false
word_count: 655
summary: This document explains the usage and options of the 'docker attach' command for connecting local terminal streams to a running container.
tags:
    - docker
    - docker-cli
    - container-management
    - terminal-attachment
    - interactive-mode
category: reference
---

DescriptionAttach local standard input, output, and error streams to a running containerUsage`docker container attach [OPTIONS] CONTAINER`Aliases

An alias is a short or memorable alternative for a longer command.

`docker attach`

Use `docker attach` to attach your terminal's standard input, output, and error (or any combination of the three) to a running container using the container's ID or name. This lets you view its output or control it interactively, as though the commands were running directly in your terminal.

> The `attach` command displays the output of the container's `ENTRYPOINT` and `CMD` process. This can appear as if the attach command is hung when in fact the process may simply not be writing any output at that time.

You can attach to the same contained process multiple times simultaneously, from different sessions on the Docker host.

To stop a container, use `CTRL-c`. This key sequence sends `SIGKILL` to the container. If `--sig-proxy` is true (the default),`CTRL-c` sends a `SIGINT` to the container. If the container was run with `-i` and `-t`, you can detach from a container and leave it running using the `CTRL-p CTRL-q` key sequence.

> A process running as PID 1 inside a container is treated specially by Linux: it ignores any signal with the default action. So, the process doesn't terminate on `SIGINT` or `SIGTERM` unless it's coded to do so.

You can't redirect the standard input of a `docker attach` command while attaching to a TTY-enabled container (using the `-i` and `-t` options).

While a client is connected to container's `stdio` using `docker attach`, Docker uses a ~1MB memory buffer to maximize the throughput of the application. Once this buffer is full, the speed of the API connection is affected, and so this impacts the output process' writing speed. This is similar to other applications like SSH. Because of this, it isn't recommended to run performance-critical applications that generate a lot of output in the foreground over a slow client connection. Instead, use the `docker logs` command to get access to the logs.

OptionDefaultDescription[`--detach-keys`](#detach-keys)Override the key sequence for detaching a container`--no-stdin`Do not attach STDIN`--sig-proxy``true`Proxy all received signals to the process

### [Attach to and detach from a running container](#attach-to-and-detach-from-a-running-container)

The following example starts an Alpine container running `top` in detached mode, then attaches to the container;

As the container was started without the `-i`, and `-t` options, signals are forwarded to the attached process, which means that the default `CTRL-p CTRL-q` detach key sequence produces no effect, but pressing `CTRL-c` terminates the container:

Repeating the example above, but this time with the `-i` and `-t` options set;

Now, when attaching to the container, and pressing the `CTRL-p CTRL-q` ("read escape sequence"), the Docker CLI is handling the detach sequence, and the `attach` command is detached from the container. Checking the container's status with `docker ps` shows that the container is still running in the background:

### [Get the exit code of the container's command](#get-the-exit-code-of-the-containers-command)

And in this second example, you can see the exit code returned by the `bash` process is returned by the `docker attach` command to its caller too:

### [Override the detach sequence (--detach-keys)](#detach-keys)

Use the `--detach-keys` option to override the Docker key sequence for detach. This is useful if the Docker default sequence conflicts with key sequence you use for other applications. There are two ways to define your own detach key sequence, as a per-container override or as a configuration property on your entire configuration.

To override the sequence for an individual container, use the `--detach-keys="<sequence>"` flag with the `docker attach` command. The format of the `<sequence>` is either a letter \[a-Z], or the `ctrl-` combined with any of the following:

- `a-z` (a single lowercase alpha character )
- `@` (at sign)
- `[` (left bracket)
- `\\` (two backward slashes)
- `_` (underscore)
- `^` (caret)

These `a`, `ctrl-a`, `X`, or `ctrl-\\` values are all examples of valid key sequences. To configure a different configuration default key sequence for all containers, see [**Configuration file** section](https://docs.docker.com/reference/cli/docker/#configuration-files).