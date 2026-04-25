---
title: Project Setup
url: https://lmstudio.ai/docs/python/getting-started/project-setup
source: sitemap
fetched_at: 2026-04-07T21:30:53.948574004-03:00
rendered_js: false
word_count: 281
summary: This document provides information on using the lmstudio-python library, detailing installation instructions via PyPI and demonstrating methods for customizing the connection to the server API host and port.
tags:
    - lmstudio
    - python-sdk
    - api-connection
    - installation
    - server-config
category: guide
---

`lmstudio` is a library published on PyPI that allows you to use `lmstudio-python` in your own projects. It is open source and developed on GitHub. You can find the source code [here](https://github.com/lmstudio-ai/lmstudio-python).

## Installing `lmstudio-python`[](#installing-lmstudio-python "Link to 'Installing ,[object Object]'")

As it is published to PyPI, `lmstudio-python` may be installed using `pip` or your preferred project dependency manager (`pdm` and `uv` are shown, but other Python project management tools offer similar dependency addition commands).

## Customizing the server API host and TCP port[](#customizing-the-server-api-host-and-tcp-port "Link to 'Customizing the server API host and TCP port'")

All of the examples in the documentation assume that the server API is running locally on one of the default application ports (Note: in Python SDK versions prior to 1.5.0, the SDK also required that the optional HTTP REST server be enabled).

The network location of the server API can be overridden by passing a `"host:port"` string when creating the client instance.

### Checking a specified API server host is running[](#checking-a-specified-api-server-host-is-running)

*Required Python SDK version*: **1.5.0**

While the most common connection pattern is to let the SDK raise an exception if it can't connect to the specified API server host, the SDK also supports running the API check directly without creating an SDK client instance first:

### Determining the default local API server port[](#determining-the-default-local-api-server-port)

*Required Python SDK version*: **1.5.0**

When no API server host is specified, the SDK queries a number of ports on the local loopback interface for a running API server instance. This scan is repeated for each new client instance created. Rather than letting the SDK perform this scan implicitly, the SDK also supports running the scan explicitly, and passing in the reported API server details when creating clients: