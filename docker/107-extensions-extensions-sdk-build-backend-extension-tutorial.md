---
title: Add a backend to your extension
url: https://docs.docker.com/extensions/extensions-sdk/build/backend-extension-tutorial/
source: llms
fetched_at: 2026-01-24T14:27:24.674174026-03:00
rendered_js: false
word_count: 989
summary: This document explains how to develop and integrate a backend service within a Docker extension to manage state and serve data via APIs. It covers directory structure, Dockerfile configuration, and communication between the frontend and the backend.
tags:
    - docker-extensions-sdk
    - backend-services
    - docker-desktop
    - go-backend
    - extension-development
    - socket-communication
    - metadata-json
category: tutorial
---

Your extension can ship a backend part with which the frontend can interact with. This page provides information on why and how to add a backend.

Before you start, make sure you have installed the latest version of [Docker Desktop](https://www.docker.com/products/docker-desktop/).

> Tip
> 
> Check the [Quickstart guide](https://docs.docker.com/extensions/extensions-sdk/quickstart/) and `docker extension init <my-extension>`. They provide a better base for your extension as it's more up-to-date and related to your install of Docker Desktop.

Thanks to the Docker Extensions SDK, most of the time you should be able to do what you need from the Docker CLI directly from [the frontend](https://docs.docker.com/extensions/extensions-sdk/build/frontend-extension-tutorial/#use-the-extension-apis-client).

Nonetheless, there are some cases where you might need to add a backend to your extension. So far, extension builders have used the backend to:

- Store data in a local database and serve them back with a REST API.
- Store the extension state, for example when a button starts a long-running process, so that if you navigate away from the extension user interface and comes back, the frontend can pick up where it left off.

For more information about extension backends, see [Architecture](https://docs.docker.com/extensions/extensions-sdk/architecture/#the-backend).

If you created your extension using the `docker extension init` command, you already have a backend setup. Otherwise, you have to first create a `vm` directory that contains the code and updates the Dockerfile to containerize it.

Here is the extension folder structure with a backend:

1. Contains everything required to build the backend and copy it in the extension's container filesystem.
2. The source folder that contains the backend code of the extension.

Although you can start from an empty directory or from the `vm-ui extension` [sample](https://github.com/docker/extensions-sdk/tree/main/samples), it is highly recommended that you start from the `docker extension init` command and change it to suit your needs.

> The `docker extension init` generates a Go backend. But you can still use it as a starting point for your own extension and use any other language like Node.js, Python, Java, .Net, or any other language and framework.

In this tutorial, the backend service simply exposes one route that returns a JSON payload that says "Hello".

> We recommend that, the frontend and the backend communicate through sockets, and named pipes on Windows, instead of HTTP. This prevents port collision with any other running application or container running on the host. Also, some Docker Desktop users are running in constrained environments where they can't open ports on their machines. When choosing the language and framework for your backend, make sure it supports sockets connection.

> We don't have a working example for Node yet. [Fill out the form](https://docs.google.com/forms/d/e/1FAIpQLSdxJDGFJl5oJ06rG7uqtw1rsSBZpUhv_s9HHtw80cytkh2X-Q/viewform?usp=pp_url&entry.25798127=Node) and let us know if you'd like a sample for Node.

> We don't have a working example for Python yet. [Fill out the form](https://docs.google.com/forms/d/e/1FAIpQLSdxJDGFJl5oJ06rG7uqtw1rsSBZpUhv_s9HHtw80cytkh2X-Q/viewform?usp=pp_url&entry.25798127=Python) and let us know if you'd like a sample for Python.

> We don't have a working example for Java yet. [Fill out the form](https://docs.google.com/forms/d/e/1FAIpQLSdxJDGFJl5oJ06rG7uqtw1rsSBZpUhv_s9HHtw80cytkh2X-Q/viewform?usp=pp_url&entry.25798127=Java) and let us know if you'd like a sample for Java.

> We don't have a working example for .NET. [Fill out the form](https://docs.google.com/forms/d/e/1FAIpQLSdxJDGFJl5oJ06rG7uqtw1rsSBZpUhv_s9HHtw80cytkh2X-Q/viewform?usp=pp_url&entry.25798127=.Net) and let us know if you'd like a sample for .NET.

> When using the `docker extension init`, it creates a `Dockerfile` that already contains what is needed for a Go backend.

To deploy your Go backend when installing the extension, you need first to configure the `Dockerfile`, so that it:

- Builds the backend application
- Copies the binary in the extension's container filesystem
- Starts the binary when the container starts listening on the extension socket

> To ease version management, you can reuse the same image to build the frontend, build the backend service, and package the extension.

> We don't have a working Dockerfile for Node yet. [Fill out the form](https://docs.google.com/forms/d/e/1FAIpQLSdxJDGFJl5oJ06rG7uqtw1rsSBZpUhv_s9HHtw80cytkh2X-Q/viewform?usp=pp_url&entry.25798127=Node) and let us know if you'd like a Dockerfile for Node.

> We don't have a working Dockerfile for Python yet. [Fill out the form](https://docs.google.com/forms/d/e/1FAIpQLSdxJDGFJl5oJ06rG7uqtw1rsSBZpUhv_s9HHtw80cytkh2X-Q/viewform?usp=pp_url&entry.25798127=Python) and let us know if you'd like a Dockerfile for Python.

> We don't have a working Dockerfile for Java yet. [Fill out the form](https://docs.google.com/forms/d/e/1FAIpQLSdxJDGFJl5oJ06rG7uqtw1rsSBZpUhv_s9HHtw80cytkh2X-Q/viewform?usp=pp_url&entry.25798127=Java) and let us know if you'd like a Dockerfile for Java.

> We don't have a working Dockerfile for .Net. [Fill out the form](https://docs.google.com/forms/d/e/1FAIpQLSdxJDGFJl5oJ06rG7uqtw1rsSBZpUhv_s9HHtw80cytkh2X-Q/viewform?usp=pp_url&entry.25798127=.Net) and let us know if you'd like a Dockerfile for .Net.

To start the backend service of your extension inside the VM of Docker Desktop, you have to configure the image name in the `vm` section of the `metadata.json` file.

For more information on the `vm` section of the `metadata.json`, see [Metadata](https://docs.docker.com/extensions/extensions-sdk/architecture/metadata/).

> Do not replace the `${DESKTOP_PLUGIN_IMAGE}` placeholder in the `metadata.json` file. The placeholder is replaced automatically with the correct image name when the extension is installed.

Using the [advanced frontend extension example](https://docs.docker.com/extensions/extensions-sdk/build/frontend-extension-tutorial/), we can invoke our extension backend.

Use the Docker Desktop Client object and then invoke the `/hello` route from the backend service with `ddClient. extension.vm.service.get` that returns the body of the response.

Replace the `ui/src/App.tsx` file with the following code:

> We don't have an example for Vue yet. [Fill out the form](https://docs.google.com/forms/d/e/1FAIpQLSdxJDGFJl5oJ06rG7uqtw1rsSBZpUhv_s9HHtw80cytkh2X-Q/viewform?usp=pp_url&entry.1333218187=Vue) and let us know if you'd like a sample with Vue.

> We don't have an example for Angular yet. [Fill out the form](https://docs.google.com/forms/d/e/1FAIpQLSdxJDGFJl5oJ06rG7uqtw1rsSBZpUhv_s9HHtw80cytkh2X-Q/viewform?usp=pp_url&entry.1333218187=Angular) and let us know if you'd like a sample with Angular.

> We don't have an example for Svelte yet. [Fill out the form](https://docs.google.com/forms/d/e/1FAIpQLSdxJDGFJl5oJ06rG7uqtw1rsSBZpUhv_s9HHtw80cytkh2X-Q/viewform?usp=pp_url&entry.1333218187=Svelte) and let us know if you'd like a sample with Svelte.

Since you have modified the configuration of the extension and added a stage in the Dockerfile, you must re-build the extension.

Once built, you need to update it, or install it if you haven't already done so.

Now you can see the backend service running in the **Containers** view of the Docker Desktop Dashboard and watch the logs when you need to debug it.

> You may need to turn on the **Show system containers** option in **Settings** to see the backend container running. See [Show extension containers](https://docs.docker.com/extensions/extensions-sdk/dev/test-debug/#show-the-extension-containers) for more information.

Open the Docker Desktop Dashboard and select the **Containers** tab. You should see the response from the backend service call displayed.

- Learn how to [share and publish your extension](https://docs.docker.com/extensions/extensions-sdk/extensions/).
- Learn more about extensions [architecture](https://docs.docker.com/extensions/extensions-sdk/architecture/).