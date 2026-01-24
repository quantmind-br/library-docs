---
title: 'Interface: ExtensionHost'
url: https://docs.docker.com/reference/api/extensions-sdk/ExtensionHost/
source: llms
fetched_at: 2026-01-24T14:31:23.794762986-03:00
rendered_js: false
word_count: 71
summary: This documentation explains the cli property of the host extension SDK, which allows for executing and streaming commands on the host machine.
tags:
    - docker-extensions-sdk
    - cli-execution
    - host-commands
    - streaming-output
    - typescript-api
category: api
---

Table of contents

* * *

**`Since`**

0.2.0

## [Properties](#properties)

### [cli](#cli)

• `Readonly` **cli**: [`ExtensionCli`](https://docs.docker.com/reference/api/extensions-sdk/ExtensionCli/)

Executes a command in the host.

For example, execute the shipped binary `kubectl -h` command in the host:

```
await ddClient.extension.host.cli.exec("kubectl", ["-h"]);
```

* * *

Streams the output of the command executed in the backend container or in the host.

Provided the `kubectl` binary is shipped as part of your extension, you can spawn the `kubectl -h` command in the host:

```
await ddClient.extension.host.cli.exec("kubectl", ["-h"], {
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