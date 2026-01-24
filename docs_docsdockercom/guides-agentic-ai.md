---
title: Agentic AI applications
url: https://docs.docker.com/guides/agentic-ai/
source: llms
fetched_at: 2026-01-24T14:03:16.721631537-03:00
rendered_js: false
word_count: 1770
summary: This document explains how to build, run, and orchestrate agentic AI applications using Docker Compose, Model Runner, and the Model Context Protocol (MCP). It provides a walkthrough for deploying AI workloads both locally and in GPU-accelerated environments using Docker Offload.
tags:
    - docker-compose
    - agentic-ai
    - mcp-gateway
    - docker-offload
    - model-runner
    - llm-orchestration
    - ai-infrastructure
category: guide
---

## Build and run agentic AI applications with Docker

Agentic applications are transforming how software gets built. These apps don't just respond, they decide, plan, and act. They're powered by models, orchestrated by agents, and integrated with APIs, tools, and services in real time.

All these new agentic applications, no matter what they do, share a common architecture. It's a new kind of stack, built from three core components:

- Models: These are your GPTs, CodeLlamas, Mistrals. They're doing the reasoning, writing, and planning. They're the engine behind the intelligence.
- Agent: This is where the logic lives. Agents take a goal, break it down, and figure out how to get it done. They orchestrate everything. They talk to the UI, the tools, the model, and the gateway.
- MCP gateway: This is what links your agents to the outside world, including APIs, tools, and services. It provides a standard way for agents to call capabilities via the Model Context Protocol (MCP).

Docker makes this AI-powered stack simpler, faster, and more secure by unifying models, tool gateways, and cloud infrastructure into a developer-friendly workflow that uses Docker Compose.

![A diagram of the agentic stack](https://docs.docker.com/guides/images/agentic-ai-diagram.webp)

![A diagram of the agentic stack](https://docs.docker.com/guides/images/agentic-ai-diagram.webp)

This guide walks you through the core components of agentic development and shows how Docker ties them all together with the following tools:

- [Docker Model Runner](https://docs.docker.com/ai/model-runner/) lets you run LLMs locally with simple command and OpenAI-compatible APIs.
- [Docker MCP Catalog and Toolkit](https://docs.docker.com/ai/mcp-catalog-and-toolkit/) helps you discover and securely run external tools, like APIs and databases, using the Model Context Protocol (MCP).
- [Docker MCP Gateway](https://docs.docker.com/ai/mcp-catalog-and-toolkit/mcp-gateway/) lets you orchestrate and manage MCP servers.
- [Docker Offload](https://docs.docker.com/offload/) provides a powerful, GPU-accelerated environment to run your AI applications with the same Compose-based workflow you use locally.
- [Docker Compose](https://docs.docker.com/ai/compose/models-and-compose/) is the tool that ties it all together, letting you define and run multi-container applications with a single file.

For this guide, you'll start by running the app in Docker Offload, using the same Compose workflow you're already familiar with. Then, if your machine hardware supports it, you'll run the same app locally using the same workflow. Finally, you'll dig into the Compose file, Dockerfile, and app to see how it all works together.

To follow this guide, you need to:

- [Install Docker Desktop 4.43 or later](https://docs.docker.com/get-started/get-docker/)
- [Enable Docker Model Runner](https://docs.docker.com/ai/model-runner/#enable-dmr-in-docker-desktop)
- [Join Docker Offload Beta](https://docs.docker.com/offload/quickstart/)

You'll use an existing sample application that demonstrates how to connect a model to an external tool using Docker's AI features.

You'll start by running the application in Docker Offload, which provides a managed environment for running AI workloads. This is ideal if you want to leverage cloud resources or if your local machine doesn't meet the hardware requirements to run the model locally. Docker Offload includes support for GPU-accelerated instances, making it ideal for compute-intensive workloads like AI model inference.

To run the application with Docker Offload, follow these steps:

1. Sign in to the Docker Desktop Dashboard.
2. In a terminal, start Docker Offload by running the following command:
   
   When prompted, choose the account you want to use for Docker Offload and select **Yes** when prompted **Do you need GPU support?**.
3. In the `adk/` directory of the cloned repository, run the following command in a terminal to build and run the application:
   
   The first time you run this command, Docker pulls the model from Docker Hub, which may take some time.
   
   The application is now running with Docker Offload. Note that the Compose workflow is the same when using Docker Offload as it is locally. You define your application in a `compose.yaml` file, and then use `docker compose up` to build and run it.
4. Visit [http://localhost:8080](http://localhost:8080). Enter a correct or incorrect fact in the prompt and hit enter. An agent searches DuckDuckGo to verify it and another agent revises the output.
   
   ![Screenshot of the application](https://docs.docker.com/guides/images/agentic-ai-app.png)
   
   ![Screenshot of the application](https://docs.docker.com/guides/images/agentic-ai-app.png)
5. Press ctrl-c in the terminal to stop the application when you're done.
6. Run the following command to stop Docker Offload:

If your machine meets the necessary hardware requirements, you can run the entire application stack locally using Docker Compose. This lets you test the application end-to-end, including the model and MCP gateway, without needing to run in the cloud. This particular example uses the [Gemma 3 4B model](https://hub.docker.com/r/ai/gemma3) with a context size of `10000`.

Hardware requirements:

- VRAM: 3.5 GB
- Storage: 2.31 GB

If your machine exceeds those requirements, consider running the application with a larger context size or a larger model to improve the agents performance. You can easily update model and context size in the `compose.yaml` file.

To run the application locally, follow these steps:

1. In the `adk/` directory of the cloned repository, run the following command in a terminal to build and run the application:
   
   The first time you run this command, Docker pulls the model from Docker Hub, which may take some time.
2. Visit [http://localhost:8080](http://localhost:8080). Enter a correct or incorrect fact in the prompt and hit enter. An agent searches DuckDuckGo to verify it and another agent revises the output.
3. Press ctrl-c in the terminal to stop the application when you're done.

You can find the `compose.yaml` file in the `adk/` directory. Open it in a text editor to see how the services are defined.

The app consists of three main components:

- The `adk` service, which is the web application that runs the agentic AI application. This service talks to the MCP gateway and model.
- The `mcp-gateway` service, which is the MCP gateway that connects the app to external tools and services.
- The `models` block, which defines the model to use with the application.

When you examine the `compose.yaml` file, you'll notice two notable elements for the model:

- A service‑level `models` block in the `adk` service
- A top-level `models` block

These two blocks together let Docker Compose automatically start and connect your ADK web app to the specified LLM.

> Looking for more models to use? Check out the [Docker AI Model Catalog](https://hub.docker.com/catalogs/models/).

When examining the `compose.yaml` file, you'll notice the gateway service is a Docker-maintained image, [`docker/mcp-gateway:latest`](https://hub.docker.com/r/docker/agents_gateway). This image is Docker's open source [MCP Gateway](https://github.com/docker/docker-mcp/) that enables your application to connect to MCP servers, which expose tools that models can call. In this example, it uses the [`duckduckgo` MCP server](https://hub.docker.com/mcp/server/duckduckgo/overview) to perform web searches.

> Looking for more MCP servers to use? Check out the [Docker MCP Catalog](https://hub.docker.com/catalogs/mcp/).

With only a few lines of instructions in a Compose file, you're able to run and connect all the necessary services of an agentic AI application.

In addition to the Compose file, the Dockerfile and the `entrypoint.sh` script it creates, play a role in wiring up the AI stack at build and runtime. You can find the `Dockerfile` in the `adk/` directory. Open it in a text editor.

The `entrypoint.sh` has five key environment variables:

- `MODEL_RUNNER_URL`: Injected by Compose (via the service-level `models:` block) to point at your Docker Model Runner HTTP endpoint.
- `MODEL_RUNNER_MODEL`: Injected by Compose to select which model to launch in Model Runner.
- `OPENAI_API_KEY`: If you define an `openai-api-key` secret in your Compose file, Compose will mount it at `/run/secrets/openai-api-key`. The entrypoint script reads that file and exports it as `OPENAI_API_KEY`, causing the app to use hosted OpenAI instead of Model Runner.
- `OPENAI_BASE_URL`: When no real key is present, this is set to `MODEL_RUNNER_URL` so the ADK's OpenAI-compatible client sends requests to Docker Model Runner.
- `OPENAI_MODEL_NAME`: When falling back to Model Runner, the model is prefixed with `openai/` so the client picks up the right model alias.

Together, these variables let the same ADK web server code seamlessly target either:

- Hosted OpenAI: if you supply `OPENAI_API_KEY` (and optionally `OPENAI_MODEL_NAME`)
- Model Runner: by remapping `MODEL_RUNNER_URL` and `MODEL_RUNNER_MODEL` into the OpenAI client’s expected variables

The `adk` web application is an agent implementation that connects to the MCP gateway and a model through environment variables and API calls. It uses the [ADK (Agent Development Kit)](https://github.com/google/adk-python) to define a root agent named Auditor, which coordinates two sub-agents, Critic and Reviser, to verify and refine model-generated answers.

The three agents are:

- Critic: Verifies factual claims using the toolset, such as DuckDuckGo.
- Reviser: Edits answers based on the verification verdicts provided by the Critic.
- Auditor: A higher-level agent that sequences the Critic and Reviser. It acts as the entry point, evaluating LLM-generated answers, verifying them, and refining the final output.

All of the application's behavior is defined in Python under the `agents/` directory. Here's a breakdown of the notable files:

- `agents/agent.py`: Defines the Auditor, a SequentialAgent that chains together the Critic and Reviser agents. This agent is the main entry point of the application and is responsible for auditing LLM-generated content using real-world verification tools.
- `agents/sub_agents/critic/agent.py`: Defines the Critic agent. It loads the language model (via Docker Model Runner), sets the agent’s name and behavior, and connects to MCP tools (like DuckDuckGo).
- `agents/sub_agents/critic/prompt.py`: Contains the Critic prompt, which instructs the agent to extract and verify claims using external tools.
- `agents/sub_agents/critic/tools.py`: Defines the MCP toolset configuration, including parsing `mcp/` strings, creating tool connections, and handling MCP gateway communication.
- `agents/sub_agents/reviser/agent.py`: Defines the Reviser agent, which takes the Critic’s findings and minimally rewrites the original answer. It also includes callbacks to clean up the LLM output and ensure it's in the right format.
- `agents/sub_agents/reviser/prompt.py`: Contains the Reviser prompt, which instructs the agent to revise the answer text based on the verified claim verdicts.

The MCP gateway is configured via the `MCPGATEWAY_ENDPOINT` environment variable. In this case, `http://mcp-gateway:8811/sse`. This allows the app to use Server-Sent Events (SSE) to communicate with the MCP gateway container, which itself brokers access to external tool services like DuckDuckGo.

Agent-based AI applications are emerging as a powerful new software architecture. In this guide, you explored a modular, chain-of-thought system where an Auditor agent coordinates the work of a Critic and a Reviser to fact-check and refine model-generated answers. This architecture shows how to combine local model inference with external tool integrations in a structured, modular way.

You also saw how Docker simplifies this process by providing a suite of tools that support local and cloud-based agentic AI development:

- [Docker Model Runner](https://docs.docker.com/ai/model-runner/): Run and serve open-source models locally via OpenAI-compatible APIs.
- [Docker MCP Catalog and Toolkit](https://docs.docker.com/ai/mcp-catalog-and-toolkit/): Launch and manage tool integrations that follow the Model Context Protocol (MCP) standard.
- [Docker MCP Gateway](https://docs.docker.com/ai/mcp-catalog-and-toolkit/mcp-gateway/): Orchestrate and manage MCP servers to connect agents to external tools and services.
- [Docker Compose](https://docs.docker.com/ai/compose/models-and-compose/): Define and run multi-container agentic AI applications with a single file, using the same workflow locally and in the cloud.
- [Docker Offload](https://docs.docker.com/offload/): Run GPU-intensive AI workloads in a secure, managed cloud environment using the same Docker Compose workflow you use locally.

With these tools, you can develop and test agentic AI applications efficiently, locally or in the cloud, using the same consistent workflow throughout.