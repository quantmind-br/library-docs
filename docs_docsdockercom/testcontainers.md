---
title: Testcontainers
url: https://docs.docker.com/testcontainers/
source: llms
fetched_at: 2026-01-24T14:30:25.912994875-03:00
rendered_js: false
word_count: 209
summary: This document introduces Testcontainers, an open-source library for managing Docker-based service dependencies during development and testing, covering supported languages and environment requirements.
tags:
    - testcontainers
    - docker
    - integration-testing
    - containerization
    - testing-framework
    - software-development
category: guide
---

Table of contents

* * *

Testcontainers is a set of open source libraries that provides easy and lightweight APIs for bootstrapping local development and test dependencies with real services wrapped in Docker containers. Using Testcontainers, you can write tests that depend on the same services you use in production without mocks or in-memory services.

## [Quickstart](#quickstart)

### [Supported languages](#supported-languages)

Testcontainers provide support for the most popular languages, and Docker sponsors the development of the following Testcontainers implementations:

- [Go](https://golang.testcontainers.org/quickstart/)
- [Java](https://java.testcontainers.org/quickstart/junit_5_quickstart/)

The rest are community-driven and maintained by independent contributors.

### [Prerequisites](#prerequisites)

Testcontainers requires a Docker-API compatible container runtime. During development, Testcontainers is actively tested against recent versions of Docker on Linux, as well as against Docker Desktop on Mac and Windows. These Docker environments are automatically detected and used by Testcontainers without any additional configuration being necessary.

It is possible to configure Testcontainers to work for other Docker setups, such as a remote Docker host or Docker alternatives. However, these are not actively tested in the main development workflow, so not all Testcontainers features might be available and additional manual configuration might be necessary.

If you have further questions about configuration details for your setup or whether it supports running Testcontainers-based tests, contact the Testcontainers team and other users from the Testcontainers community on [Slack](https://slack.testcontainers.org/).