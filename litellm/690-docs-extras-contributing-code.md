---
title: Contributing Code | liteLLM
url: https://docs.litellm.ai/docs/extras/contributing_code
source: sitemap
fetched_at: 2026-01-21T19:45:13.426070173-03:00
rendered_js: false
word_count: 449
summary: Outlines the required procedures and technical setup for contributing to the LiteLLM project, including PR checklists, testing protocols, and local environment configuration.
tags:
    - contribution-guide
    - pull-request
    - unit-testing
    - development-setup
    - docker
    - litellm
    - linting
category: guide
---

## **Checklist before submitting a PR**[​](#checklist-before-submitting-a-pr "Direct link to checklist-before-submitting-a-pr")

Here are the core requirements for any PR submitted to LiteLLM

- Sign the Contributor License Agreement (CLA) - [see details](#contributor-license-agreement-cla)
- Add testing, **Adding at least 1 test is a hard requirement** - [see details](#2-adding-testing-to-your-pr)
- Ensure your PR passes the following tests:
  
  - [Unit Tests](#3-running-unit-tests)
  - [Formatting / Linting Tests](#35-running-linting-tests)
- Keep scope as isolated as possible. As a general rule, your changes should address 1 specific problem at a time

## **Contributor License Agreement (CLA)**[​](#contributor-license-agreement-cla "Direct link to contributor-license-agreement-cla")

Before contributing code to LiteLLM, you must sign our [Contributor License Agreement (CLA)](https://cla-assistant.io/BerriAI/litellm). This is a legal requirement for all contributions to be merged into the main repository. The CLA helps protect both you and the project by clearly defining the terms under which your contributions are made.

**Important:** We strongly recommend reviewing and signing the CLA before starting work on your contribution to avoid any delays in the PR process. You can find the CLA [here](https://cla-assistant.io/BerriAI/litellm) and sign it through our CLA management system when you submit your first PR.

## Quick start[​](#quick-start "Direct link to Quick start")

## 1. Setup your local dev environment[​](#1-setup-your-local-dev-environment "Direct link to 1. Setup your local dev environment")

Here's how to modify the repo locally:

Step 1: Clone the repo

```
git clone https://github.com/BerriAI/litellm.git
```

Step 2: Install dev dependencies:

```
poetry install --with dev --extras proxy
```

That's it, your local dev environment is ready!

## 2. Adding Testing to your PR[​](#2-adding-testing-to-your-pr "Direct link to 2. Adding Testing to your PR")

- Add your test to the [`tests/test_litellm/` directory](https://github.com/BerriAI/litellm/tree/main/tests/litellm)
- This directory 1:1 maps the the `litellm/` directory, and can only contain mocked tests.
- Do not add real llm api calls to this directory.

### 2.1 File Naming Convention for `tests/test_litellm/`[​](#21-file-naming-convention-for-teststest_litellm "Direct link to 21-file-naming-convention-for-teststest_litellm")

The `tests/test_litellm/` directory follows the same directory structure as `litellm/`.

- `litellm/proxy/test_caching_routes.py` maps to `litellm/proxy/caching_routes.py`
- `test_{filename}.py` maps to `litellm/{filename}.py`

## 3. Running Unit Tests[​](#3-running-unit-tests "Direct link to 3. Running Unit Tests")

run the following command on the root of the litellm directory

## 3.5 Running Linting Tests[​](#35-running-linting-tests "Direct link to 3.5 Running Linting Tests")

run the following command on the root of the litellm directory

LiteLLM uses mypy for linting. On ci/cd we also run `black` for formatting.

## 4. Submit a PR with your changes\![​](#4-submit-a-pr-with-your-changes "Direct link to 4. Submit a PR with your changes!")

- push your fork to your GitHub repo
- submit a PR from there

## Advanced[​](#advanced "Direct link to Advanced")

### Building LiteLLM Docker Image[​](#building-litellm-docker-image "Direct link to Building LiteLLM Docker Image")

Some people might want to build the LiteLLM docker image themselves. Follow these instructions if you want to build / run the LiteLLM Docker Image yourself.

Step 1: Clone the repo

```
git clone https://github.com/BerriAI/litellm.git
```

Step 2: Build the Docker Image

Build using Dockerfile.non\_root

```
docker build -f docker/Dockerfile.non_root -t litellm_test_image .
```

Step 3: Run the Docker Image

Make sure config.yaml is present in the root directory. This is your litellm proxy config file.

```
docker run \
    -v $(pwd)/proxy_config.yaml:/app/config.yaml \
    -e DATABASE_URL="postgresql://xxxxxxxx" \
    -e LITELLM_MASTER_KEY="sk-1234" \
    -p 4000:4000 \
    litellm_test_image \
    --config /app/config.yaml --detailed_debug
```

### Running LiteLLM Proxy Locally[​](#running-litellm-proxy-locally "Direct link to Running LiteLLM Proxy Locally")

1. cd into the `proxy/` directory

<!--THE END-->

2. Run the proxy

```
python3 proxy_cli.py --config /path/to/config.yaml

# RUNNING on http://0.0.0.0:4000
```

- [**Checklist before submitting a PR**](#checklist-before-submitting-a-pr)
- [**Contributor License Agreement (CLA)**](#contributor-license-agreement-cla)
- [Quick start](#quick-start)
- [1. Setup your local dev environment](#1-setup-your-local-dev-environment)
- [2. Adding Testing to your PR](#2-adding-testing-to-your-pr)
  
  - [2.1 File Naming Convention for `tests/test_litellm/`](#21-file-naming-convention-for-teststest_litellm)
- [3. Running Unit Tests](#3-running-unit-tests)
- [3.5 Running Linting Tests](#35-running-linting-tests)
- [4. Submit a PR with your changes!](#4-submit-a-pr-with-your-changes)
- [Advanced](#advanced)
  
  - [Building LiteLLM Docker Image](#building-litellm-docker-image)
  - [Running LiteLLM Proxy Locally](#running-litellm-proxy-locally)