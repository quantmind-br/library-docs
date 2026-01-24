---
title: Extension Backend
url: https://docs.docker.com/extensions/extensions-sdk/dev/api/backend/
source: llms
fetched_at: 2026-01-24T14:27:35.60392876-03:00
rendered_js: false
word_count: 405
summary: This document describes how to use the Docker Desktop Extension SDK to communicate with backend services in the extension VM and execute binaries on the host system.
tags:
    - docker-extensions
    - extensions-sdk
    - backend-communication
    - host-api
    - vm-api
    - command-execution
category: reference
---

The `ddClient.extension.vm` object can be used to communicate with the backend defined in the [vm section](https://docs.docker.com/extensions/extensions-sdk/architecture/metadata/#vm-section) of the extension metadata.

▸ **get**(`url`): `Promise`&lt;`unknown`&gt;

Performs an HTTP GET request to a backend service.

See [Service API Reference](https://docs.docker.com/reference/api/extensions-sdk/HttpService/) for other methods such as POST, UPDATE, and DELETE.

> Deprecated extension backend communication
> 
> The methods below that use `window.ddClient.backend` are deprecated and will be removed in a future version. Use the methods specified above.

The `window.ddClient.backend` object can be used to communicate with the backend defined in the [vm section](https://docs.docker.com/extensions/extensions-sdk/architecture/metadata/#vm-section) of the extension metadata. The client is already connected to the backend.

Example usages:

For example, execute the command `ls -l` inside the backend container:

Stream the output of the command executed in the backend container. For example, spawn the command `ls -l` inside the backend container:

For more details, refer to the [Extension VM API Reference](https://docs.docker.com/reference/api/extensions-sdk/ExtensionVM/)

> Deprecated extension backend command execution
> 
> This method is deprecated and will be removed in a future version. Use the specified method above.

If your extension ships with additional binaries that should be run inside the backend container, you can use the `execInVMExtension` function:

Invoke a binary on the host. The binary is typically shipped with your extension using the [host section](https://docs.docker.com/extensions/extensions-sdk/architecture/metadata/#host-section) in the extension metadata. Note that extensions run with user access rights, this API is not restricted to binaries listed in the [host section](https://docs.docker.com/extensions/extensions-sdk/architecture/metadata/#host-section) of the extension metadata (some extensions might install software during user interaction, and invoke newly installed binaries even if not listed in the extension metadata).

For example, execute the shipped binary `kubectl -h` command in the host:

As long as the `kubectl` binary is shipped as part of your extension, you can spawn the `kubectl -h` command in the host and get the output stream:

You can stream the output of the command executed in the backend container or in the host.

For more details, refer to the [Extension Host API Reference](https://docs.docker.com/reference/api/extensions-sdk/ExtensionHost/)

> Deprecated invocation of extension binary
> 
> This method is deprecated and will be removed in a future version. Use the method specified above.

To execute a command in the host:

To stream the output of the command executed in the backend container or in the host:

> You cannot use this to chain commands in a single `exec()` invocation (like `cmd1 $(cmd2)` or using pipe between commands).
> 
> You need to invoke `exec()` for each command and parse results to pass parameters to the next command if needed.