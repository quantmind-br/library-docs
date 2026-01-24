---
title: Get started with DMR
url: https://docs.docker.com/ai/model-runner/get-started/
source: llms
fetched_at: 2026-01-24T14:14:17.407359118-03:00
rendered_js: false
word_count: 700
summary: This document provides instructions for setting up and using Docker Model Runner to manage, execute, and publish AI models locally on Docker Desktop and Docker Engine.
tags:
    - docker-model-runner
    - local-inference
    - ai-models
    - docker-desktop
    - containerization
    - machine-learning
category: guide
---

Docker Model Runner (DMR) lets you run and manage AI models locally using Docker. This page shows you how to enable DMR, pull and run a model, configure model settings, and publish custom models.

You can enable DMR using Docker Desktop or Docker Engine. Follow the instructions below based on your setup.

### [Docker Desktop](#docker-desktop)

1. In the settings view, go to the **AI** tab.
2. Select the **Enable Docker Model Runner** setting.
3. If you use Windows with a supported NVIDIA GPU, you also see and can select **Enable GPU-backed inference**.
4. Optional: To enable TCP support, select **Enable host-side TCP support**.
   
   1. In the **Port** field, type the port you want to use.
   2. If you interact with Model Runner from a local frontend web app, in **CORS Allows Origins**, select the origins that Model Runner should accept requests from. An origin is the URL where your web app runs, for example `http://localhost:3131`.

You can now use the `docker model` command in the CLI and view and interact with your local models in the **Models** tab in the Docker Desktop Dashboard.

> For Docker Desktop versions 4.45 and earlier, this setting was under the **Beta features** tab.

### [Docker Engine](#docker-engine)

1. Ensure you have installed [Docker Engine](https://docs.docker.com/engine/install/).
2. Docker Model Runner is available as a package. To install it, run:
3. Test the installation:

> TCP support is enabled by default for Docker Engine on port `12434`.

### [Update DMR in Docker Engine](#update-dmr-in-docker-engine)

To update Docker Model Runner in Docker Engine, uninstall it with [`docker model uninstall-runner`](https://docs.docker.com/reference/cli/docker/model/uninstall-runner/) then reinstall it:

> With the above command, local models are preserved. To delete the models during the upgrade, add the `--models` option to the `uninstall-runner` command.

Models are cached locally.

> When you use the Docker CLI, you can also pull models directly from [HuggingFace](https://huggingface.co/).

1. Select **Models** and select the **Docker Hub** tab.
2. Find the model you want and select **Pull**.

![Screenshot showing the Docker Hub view.](https://docs.docker.com/ai/model-runner/images/dmr-catalog.png)

![Screenshot showing the Docker Hub view.](https://docs.docker.com/ai/model-runner/images/dmr-catalog.png)

1. Select **Models** and select the **Local** tab.
2. Select the play button. The interactive chat screen opens.

![Screenshot showing the Local view.](https://docs.docker.com/ai/model-runner/images/dmr-run.png)

![Screenshot showing the Local view.](https://docs.docker.com/ai/model-runner/images/dmr-run.png)

You can configure a model, such as its maximum token limit and more, use Docker Compose. See [Models and Compose - Model configuration options](https://docs.docker.com/ai/compose/models-and-compose/#model-configuration-options).

> This works for any Container Registry supporting OCI Artifacts, not only Docker Hub.

You can tag existing models with a new name and publish them under a different namespace and repository:

For more details, see the [`docker model tag`](https://docs.docker.com/reference/cli/docker/model/tag) and [`docker model push`](https://docs.docker.com/reference/cli/docker/model/push) command documentation.

You can also package a model file in GGUF format as an OCI Artifact and publish it to Docker Hub.

For more details, see the [`docker model package`](https://docs.docker.com/reference/cli/docker/model/package/) command documentation.

### [Display the logs](#display-the-logs)

To troubleshoot issues, display the logs:

Select **Models** and select the **Logs** tab.

![Screenshot showing the Models view.](https://docs.docker.com/ai/model-runner/images/dmr-logs.png)

![Screenshot showing the Models view.](https://docs.docker.com/ai/model-runner/images/dmr-logs.png)

### [Inspect requests and responses](#inspect-requests-and-responses)

Inspecting requests and responses helps you diagnose model-related issues. For example, you can evaluate context usage to verify you stay within the model's context window or display the full body of a request to control the parameters you are passing to your models when developing with a framework.

In Docker Desktop, to inspect the requests and responses for each model:

1. Select **Models** and select the **Requests** tab. This view displays all the requests to all models:
   
   - The time the request was sent.
   - The model name and version
   - The prompt/request
   - The context usage
   - The time it took for the response to be generated.
2. Select one of the requests to display further details:
   
   - In the **Overview** tab, view the token usage, response metadata and generation speed, and the actual prompt and response.
   - In the **Request** and **Response** tabs, view the full JSON payload of the request and the response.

> You can also display the requests for a specific model when you select a model and then select the **Requests** tab.

- [API reference](https://docs.docker.com/ai/model-runner/api-reference/) - OpenAI and Ollama-compatible API documentation
- [Configuration options](https://docs.docker.com/ai/model-runner/configuration/) - Context size and runtime parameters
- [Inference engines](https://docs.docker.com/ai/model-runner/inference-engines/) - llama.cpp and vLLM details
- [IDE integrations](https://docs.docker.com/ai/model-runner/ide-integrations/) - Connect Cline, Continue, Cursor, and more
- [Open WebUI integration](https://docs.docker.com/ai/model-runner/openwebui-integration/) - Set up a web chat interface
- [Models and Compose](https://docs.docker.com/ai/compose/models-and-compose/) - Use models in Compose applications
- [Docker Model Runner CLI reference](https://docs.docker.com/reference/cli/docker/model) - Complete CLI documentation