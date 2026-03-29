---
title: Contributing to Documentation | liteLLM
url: https://docs.litellm.ai/docs/extras/contributing
source: sitemap
fetched_at: 2026-01-21T19:45:11.970727534-03:00
rendered_js: false
word_count: 135
summary: This document provides instructions for setting up a local development environment to run, preview, and contribute to the LiteLLM documentation using Docusaurus.
tags:
    - documentation
    - local-setup
    - docusaurus
    - contributing-guide
    - git-workflow
    - npm-packages
category: guide
---

This website is built using [Docusaurus 2](https://docusaurus.io/), a modern static website generator.

Clone litellm

```
git clone https://github.com/BerriAI/litellm.git
```

### Local setup for locally running docs[​](#local-setup-for-locally-running-docs "Direct link to Local setup for locally running docs")

- Yarn
- pnpm

Installation

```
npm install --global yarn
```

Install requirement

Run website

Open docs here: [http://localhost:3000/](http://localhost:3000/)

This command builds your Markdown files into HTML and starts a development server to browse your documentation. Open up [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your web browser to see your documentation. You can make changes to your Markdown files and your docs will automatically rebuild.

[Full tutorial here](https://docs.readthedocs.io/en/stable/intro/getting-started-with-mkdocs.html)

### Making changes to Docs[​](#making-changes-to-docs "Direct link to Making changes to Docs")

- All the docs are placed under the `docs` directory
- If you are adding a new `.md` file or editing the hierarchy edit `mkdocs.yml` in the root of the project
- After testing your changes, make a change/pull request to the `main` branch of [github.com/BerriAI/litellm](https://github.com/BerriAI/litellm)

<!--THE END-->

- [Local setup for locally running docs](#local-setup-for-locally-running-docs)
- [Making changes to Docs](#making-changes-to-docs)