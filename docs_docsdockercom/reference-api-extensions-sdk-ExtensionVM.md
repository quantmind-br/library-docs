---
title: 'Interface: ExtensionVM'
url: https://docs.docker.com/reference/api/extensions-sdk/ExtensionVM/
source: llms
fetched_at: 2026-01-24T14:31:23.978271056-03:00
rendered_js: false
word_count: 120
summary: This document defines the VM interface for the Docker Extensions SDK, detailing how to execute and stream commands within backend containers and interact with HTTP services.
tags:
    - docker-extensions
    - sdk
    - backend-container
    - cli-execution
    - extension-vm
    - command-streaming
category: api
---

Table of contents

* * *

**`Since`**

0.2.0

## [Properties](#properties)

### [cli](#cli)

• `Readonly` **cli**: [`ExtensionCli`](https://docs.docker.com/reference/api/extensions-sdk/ExtensionCli/)

Executes a command in the backend container.

Example: Execute the command `ls -l` inside the backend container:

```
await ddClient.extension.vm.cli.exec(
  "ls",
  ["-l"]
);
```

Streams the output of the command executed in the backend container.

When the extension defines its own `compose.yaml` file with multiple containers, the command is executed on the first container defined. Change the order in which containers are defined to execute commands on another container.

Example: Spawn the command `ls -l` inside the backend container:

```
await ddClient.extension.vm.cli.exec("ls", ["-l"], {
           stream: {
             onOutput(data): void {
                 // As we can receive both `stdout` and `stderr`, we wrap them in a JSON object
                 JSON.stringify(
                   {
                     stdout: data.stdout,
                     stderr: data.stderr,
                   },
                   null,
                   "  "
                 );
             },
             onError(error: any): void {
               console.error(error);
             },
             onClose(exitCode: number): void {
               console.log("onClose with exit code " + exitCode);
             },
           },
         });
```

**`Param`**

Command to execute.

**`Param`**

Arguments of the command to execute.

**`Param`**

The callback function where to listen from the command output data and errors.

* * *

### [service](#service)

• `Optional` `Readonly` **service**: [`HttpService`](https://docs.docker.com/reference/api/extensions-sdk/HttpService/)