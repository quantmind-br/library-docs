---
title: Create an advanced frontend extension
url: https://docs.docker.com/extensions/extensions-sdk/build/frontend-extension-tutorial/
source: llms
fetched_at: 2026-01-24T14:27:24.746180383-03:00
rendered_js: false
word_count: 1159
summary: This document provides a comprehensive guide on setting up, building, and configuring a Docker extension with a frontend using the Extensions SDK. It covers essential steps including project initialization, Dockerfile and metadata configuration, and integration with the Docker Desktop API.
tags:
    - docker-extensions
    - extension-sdk
    - frontend-development
    - docker-desktop
    - react
    - metadata-json
    - extension-api
category: guide
---

To start creating your extension, you first need a directory with files which range from the extension’s source code to the required extension-specific files. This page provides information on how to set up an extension with a more advanced frontend.

Before you start, make sure you have installed the latest version of [Docker Desktop](https://docs.docker.com/desktop/release-notes/).

The quickest way to create a new extension is to run `docker extension init my-extension` as in the [Quickstart](https://docs.docker.com/extensions/extensions-sdk/quickstart/). This creates a new directory `my-extension` that contains a fully functional extension.

> The `docker extension init` generates a React based extension. But you can still use it as a starting point for your own extension and use any other frontend framework, like Vue, Angular, Svelte, etc. or even stay with vanilla Javascript.

Although you can start from an empty directory or from the `react-extension` [sample folder](https://github.com/docker/extensions-sdk/tree/main/samples), it's highly recommended that you start from the `docker extension init` command and change it to suit your needs.

1. Contains everything required to build the extension and run it in Docker Desktop.
2. High-level folder containing your front-end app source code.
3. Assets that aren’t compiled or dynamically generated are stored here. These can be static assets like logos or the robots.txt file.
4. The src, or source folder contains all the React components, external CSS files, and dynamic assets that are brought into the component files.
5. The icon that is displayed in the left-menu of the Docker Desktop Dashboard.
6. A file that provides information about the extension such as the name, description, and version.

> When using the `docker extension init`, it creates a `Dockerfile` that already contains what is needed for a React extension.

Once the extension is created, you need to configure the `Dockerfile` to build the extension and configure the labels that are used to populate the extension's card in the Marketplace. Here is an example of a `Dockerfile` for a React extension:

> Note
> 
> In the example Dockerfile, you can see that the image label `com.docker.desktop.extension.icon` is set to an icon URL. The Extensions Marketplace displays this icon without installing the extension. The Dockerfile also includes `COPY docker.svg .` to copy an icon file inside the image. This second icon file is used to display the extension UI in the Dashboard, once the extension is installed.

> We don't have a working Dockerfile for Vue yet. [Fill out the form](https://docs.google.com/forms/d/e/1FAIpQLSdxJDGFJl5oJ06rG7uqtw1rsSBZpUhv_s9HHtw80cytkh2X-Q/viewform?usp=pp_url&entry.1333218187=Vue) and let us know if you'd like a Dockerfile for Vue.

> We don't have a working Dockerfile for Angular yet. [Fill out the form](https://docs.google.com/forms/d/e/1FAIpQLSdxJDGFJl5oJ06rG7uqtw1rsSBZpUhv_s9HHtw80cytkh2X-Q/viewform?usp=pp_url&entry.1333218187=Angular) and let us know if you'd like a Dockerfile for Angular.

> We don't have a working Dockerfile for Svelte yet. [Fill out the form](https://docs.google.com/forms/d/e/1FAIpQLSdxJDGFJl5oJ06rG7uqtw1rsSBZpUhv_s9HHtw80cytkh2X-Q/viewform?usp=pp_url&entry.1333218187=Svelte) and let us know if you'd like a Dockerfile for Svelte.

In order to add a tab in Docker Desktop for your extension, you have to configure it in the `metadata.json` file the root of your extension directory.

The `title` property is the name of the extension that is displayed in the left-menu of the Docker Desktop Dashboard. The `root` property is the path to the frontend application in the extension's container filesystem used by the system to deploy it on the host. The `src` property is the path to the HTML entry point of the frontend application within the `root` folder.

For more information on the `ui` section of the `metadata.json`, see [Metadata](https://docs.docker.com/extensions/extensions-sdk/architecture/metadata/#ui-section).

Now that you have configured the extension, you need to build the extension image that Docker Desktop will use to install it.

This built an image tagged `awesome-inc/my-extension:latest`, you can run `docker inspect awesome-inc/my-extension:latest` to see more details about it.

Finally, you can install the extension and see it appearing in the Docker Desktop Dashboard.

To use the Extension APIs and perform actions with Docker Desktop, the extension must first import the `@docker/extension-api-client` library. To install it, run the command below:

Then call the `createDockerDesktopClient` function to create a client object to call the extension APIs.

When using Typescript, you can also install `@docker/extension-api-client-types` as a dev dependency. This will provide you with type definitions for the extension APIs and auto-completion in your IDE.

![Auto completion in an IDE](https://docs.docker.com/extensions/extensions-sdk/build/images/types-autocomplete.png)

![Auto completion in an IDE](https://docs.docker.com/extensions/extensions-sdk/build/images/types-autocomplete.png)

For example, you can use the `docker.cli.exec` function to get the list of all the containers via the `docker ps --all` command and display the result in a table.

Replace the `ui/src/App.tsx` file with the following code:

![Screenshot of the container list.](https://docs.docker.com/extensions/extensions-sdk/build/images/react-extension.png)

![Screenshot of the container list.](https://docs.docker.com/extensions/extensions-sdk/build/images/react-extension.png)

> We don't have an example for Vue yet. [Fill out the form](https://docs.google.com/forms/d/e/1FAIpQLSdxJDGFJl5oJ06rG7uqtw1rsSBZpUhv_s9HHtw80cytkh2X-Q/viewform?usp=pp_url&entry.1333218187=Vue) and let us know if you'd like a sample with Vue.

> We don't have an example for Angular yet. [Fill out the form](https://docs.google.com/forms/d/e/1FAIpQLSdxJDGFJl5oJ06rG7uqtw1rsSBZpUhv_s9HHtw80cytkh2X-Q/viewform?usp=pp_url&entry.1333218187=Angular) and let us know if you'd like a sample with Angular.

> We don't have an example for Svelte yet. [Fill out the form](https://docs.google.com/forms/d/e/1FAIpQLSdxJDGFJl5oJ06rG7uqtw1rsSBZpUhv_s9HHtw80cytkh2X-Q/viewform?usp=pp_url&entry.1333218187=Svelte) and let us know if you'd like a sample with Svelte.

Extension UI code is rendered in a separate electron session and doesn't have a node.js environment initialized, nor direct access to the electron APIs.

This is to limit the possible unexpected side effects to the overall Docker Dashboard.

The extension UI code can't perform privileged tasks, such as making changes to the system, or spawning sub-processes, except by using the SDK APIs provided with the extension framework. The Extension UI code can also perform interactions with Docker Desktop, such as navigating to various places in the Dashboard, only through the extension SDK APIs.

Extensions UI parts are isolated from each other and extension UI code is running in its own session for each extension. Extensions can't access other extensions’ session data.

`localStorage` is one of the mechanisms of a browser’s web storage. It allows users to save data as key-value pairs in the browser for later use. `localStorage` doesn't clear data when the browser (the extension pane) closes. This makes it ideal for persisting data when navigating out of the extension to other parts of Docker Desktop.

If your extension uses `localStorage` to store data, other extensions running in Docker Desktop can't access the local storage of your extension. The extension’s local storage is persisted even after Docker Desktop is stopped or restarted. When an extension is upgraded, its local storage is persisted, whereas when it is uninstalled, its local storage is completely removed.

Since you have modified the code of the extension, you must build again the extension.

Once built, you need to update it.

Now you can see the backend service running in the containers tab of the Docker Desktop Dashboard and watch the logs when you need to debug it.

> You can turn on [hot reloading](https://docs.docker.com/extensions/extensions-sdk/dev/test-debug/#hot-reloading-whilst-developing-the-ui) to avoid the need to rebuild the extension every time you make a change.

- Add a [backend](https://docs.docker.com/extensions/extensions-sdk/build/backend-extension-tutorial/) to your extension.
- Learn how to [test and debug](https://docs.docker.com/extensions/extensions-sdk/dev/test-debug/) your extension.
- Learn how to [setup CI for your extension](https://docs.docker.com/extensions/extensions-sdk/dev/continuous-integration/).
- Learn more about extensions [architecture](https://docs.docker.com/extensions/extensions-sdk/architecture/).
- For more information and guidelines on building the UI, see the [Design and UI styling section](https://docs.docker.com/extensions/extensions-sdk/design/design-guidelines/).
- If you want to set up user authentication for the extension, see [Authentication](https://docs.docker.com/extensions/extensions-sdk/guides/oauth2-flow/).