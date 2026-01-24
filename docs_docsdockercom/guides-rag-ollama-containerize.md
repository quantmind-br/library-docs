---
title: Containerize your app
url: https://docs.docker.com/guides/rag-ollama/containerize/
source: llms
fetched_at: 2026-01-24T14:11:27.827509963-03:00
rendered_js: false
word_count: 436
summary: This document provides a step-by-step guide on containerizing a Retrieval-Augmented Generation (RAG) application using Docker and Docker Compose, including integration with Ollama, Qdrant, and Streamlit.
tags:
    - rag-application
    - docker
    - containerization
    - ollama
    - qdrant
    - streamlit
    - genai
    - docker-compose
category: tutorial
---

## Containerize a RAG application

This section walks you through containerizing a RAG application using Docker.

> You can see more samples of containerized GenAI applications in the [GenAI Stack](https://github.com/docker/genai-stack) demo applications.

The sample application used in this guide is an example of RAG application, made by three main components, which are the building blocks for every RAG application. A Large Language Model hosted somewhere, in this case it is hosted in a container and served via [Ollama](https://ollama.ai/). A vector database, [Qdrant](https://qdrant.tech/), to store the embeddings of local data, and a web application, using [Streamlit](https://streamlit.io/) to offer the best user experience to the user.

Clone the sample application. Open a terminal, change directory to a directory that you want to work in, and run the following command to clone the repository:

You should now have the following files in your `winy` directory.

Containerizing an application involves packaging it along with its dependencies into a container, which ensures consistency across different environments. Here’s what you need to containerize an app like Winy :

1. Dockerfile: A Dockerfile that contains instructions on how to build a Docker image for your application. It specifies the base image, dependencies, configuration files, and the command to run your application.
2. Docker Compose File: Docker Compose is a tool for defining and running multi-container Docker applications. A Compose file allows you to configure your application's services, networks, and volumes in a single file.

Inside the `winy` directory, run the following command in a terminal.

Docker builds and runs your application. Depending on your network connection, it may take several minutes to download all the dependencies. You'll see a message like the following in the terminal when the application is running.

Open a browser and view the application at [http://localhost:8501](http://localhost:8501). You should see a simple Streamlit application.

The application requires a Qdrant database service and an LLM service to work properly. If you have access to services that you ran outside of Docker, specify the connection information in the `docker-compose.yaml`.

If you don't have the services running, continue with this guide to learn how you can run some or all of these services with Docker. Remember that the `ollama` service is empty; it doesn't have any model. For this reason you need to pull a model before starting to use the RAG application. All the instructions are in the following page.

In the terminal, press `ctrl`+`c` to stop the application.

In this section, you learned how you can containerize and run your RAG application using Docker.

In the next section, you'll learn how to properly configure the application with your preferred LLM model, completely locally, using Docker.