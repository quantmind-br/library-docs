---
title: 'Interface: Docker'
url: https://docs.docker.com/reference/api/extensions-sdk/Docker/
source: llms
fetched_at: 2026-01-24T14:30:58.748055618-03:00
rendered_js: false
word_count: 11
summary: This document demonstrates how to execute Docker CLI commands and handle real-time output streams using the Docker Desktop Extension SDK. It details the implementation of callbacks for processing standard output, standard error, and execution termination events.
tags:
    - docker-desktop-sdk
    - cli-execution
    - streaming-api
    - javascript-sdk
    - docker-extension
category: api
---

```
await ddClient.docker.cli.exec("logs", ["-f", "..."], {
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