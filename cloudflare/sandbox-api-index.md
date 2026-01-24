---
title: API Reference · Cloudflare Sandbox SDK docs
url: https://developers.cloudflare.com/sandbox/api/index.md
source: llms
fetched_at: 2026-01-24T15:22:25.731159212-03:00
rendered_js: false
word_count: 137
summary: This document provides an overview of the Sandbox SDK API, detailing capabilities for container lifecycle management, remote code execution, file handling, and persistent storage.
tags:
    - sandbox-sdk
    - api-reference
    - code-execution
    - container-management
    - file-system
    - remote-commands
category: api
---

The Sandbox SDK provides a comprehensive API for executing code, managing files, running processes, and exposing services in isolated sandboxes.

[Lifecycle](https://developers.cloudflare.com/sandbox/api/lifecycle/)

Create and manage sandbox containers. Get sandbox instances, configure options, and clean up resources.

[Commands](https://developers.cloudflare.com/sandbox/api/commands/)

Execute commands and stream output. Run scripts, manage background processes, and capture execution results.

[Files](https://developers.cloudflare.com/sandbox/api/files/)

Read, write, and manage files in the sandbox filesystem. Includes directory operations and file metadata.

[Code Interpreter](https://developers.cloudflare.com/sandbox/api/interpreter/)

Execute Python and JavaScript code with rich outputs including charts, tables, and formatted data.

[Ports](https://developers.cloudflare.com/sandbox/api/ports/)

Expose services running in the sandbox via preview URLs. Access web servers and APIs from the internet.

[Storage](https://developers.cloudflare.com/sandbox/api/storage/)

Mount S3-compatible buckets (R2, S3, GCS) as local filesystems for persistent data storage across sandbox lifecycles.

[Sessions](https://developers.cloudflare.com/sandbox/api/sessions/)

Create isolated execution contexts within a sandbox. Each session maintains its own shell state, environment variables, and working directory.