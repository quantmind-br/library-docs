---
title: Invoke host binaries
url: https://docs.docker.com/extensions/extensions-sdk/guides/invoke-host-binaries/
source: llms
fetched_at: 2026-01-24T14:28:00.950261819-03:00
rendered_js: false
word_count: 422
summary: This document explains how to bundle and execute host-side binaries or shell scripts within a Docker extension using the extension SDK.
tags:
    - docker-extensions
    - host-binaries
    - sdk-integration
    - cross-platform
    - cli-execution
    - metadata-configuration
category: guide
---

In some cases, your extension may need to invoke some command from the host. For example, you might want to invoke the CLI of your cloud provider to create a new resource, or the CLI of a tool your extension provides, or even a shell script that you want to run on the host.

You could do that by executing the CLI from a container with the extension SDK. But this CLI needs to access the host's filesystem, which isn't easy nor fast if it runs in a container.

This page describes how to run executables on the host (binaries, shell scripts) that are shipped as part of your extension and deployed to the host. As extensions can run on multiple platforms, this means that you need to ship the executables for all the platforms you want to support.

Learn more about extensions [architecture](https://docs.docker.com/extensions/extensions-sdk/architecture/).

> Note that extensions run with user access rights, this API is not restricted to binaries listed in the [host section](https://docs.docker.com/extensions/extensions-sdk/architecture/metadata/#host-section) of the extension metadata (some extensions might install software during user interaction, and invoke newly installed binaries even if not listed in the extension metadata).

In this example, the CLI is a simple `Hello world` script that must be invoked with a parameter and returns a string.

Create a `bash` script for macOS and Linux, in the file `binaries/unix/hello.sh` with the following content:

Create a `batch script` for Windows in another file `binaries/windows/hello.cmd` with the following content:

Then update the `Dockerfile` to copy the `binaries` folder into the extension's container filesystem and make the files executable.

In your extension, use the Docker Desktop Client object to [invoke the shell script](https://docs.docker.com/extensions/extensions-sdk/dev/api/backend/#invoke-an-extension-binary-on-the-host) provided by the extension with the `ddClient.extension.host.cli.exec()` function. In this example, the binary returns a string as result, obtained by `result?.stdout`, as soon as the extension view is rendered.

> We don't have an example for Vue yet. [Fill out the form](https://docs.google.com/forms/d/e/1FAIpQLSdxJDGFJl5oJ06rG7uqtw1rsSBZpUhv_s9HHtw80cytkh2X-Q/viewform?usp=pp_url&entry.1333218187=Vue) and let us know if you'd like a sample with Vue.

> We don't have an example for Angular yet. [Fill out the form](https://docs.google.com/forms/d/e/1FAIpQLSdxJDGFJl5oJ06rG7uqtw1rsSBZpUhv_s9HHtw80cytkh2X-Q/viewform?usp=pp_url&entry.1333218187=Angular) and let us know if you'd like a sample with Angular.

> We don't have an example for Svelte yet. [Fill out the form](https://docs.google.com/forms/d/e/1FAIpQLSdxJDGFJl5oJ06rG7uqtw1rsSBZpUhv_s9HHtw80cytkh2X-Q/viewform?usp=pp_url&entry.1333218187=Svelte) and let us know if you'd like a sample with Svelte.

The host binaries must be specified in the `metadata.json` file so that Docker Desktop copies them on to the host when installing the extension. Once the extension is uninstalled, the binaries that were copied are removed as well.

The `path` must reference the path of the binary inside the container.