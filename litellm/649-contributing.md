---
title: Contributing to Documentation | liteLLM
url: https://docs.litellm.ai/contributing
source: sitemap
fetched_at: 2026-01-21T19:41:07.784943782-03:00
rendered_js: false
word_count: 126
summary: This document provides instructions for setting up, running, and contributing to the LiteLLM documentation using MkDocs in a local environment.
tags:
    - litellm
    - documentation
    - mkdocs
    - local-setup
    - contribution-guide
category: tutorial
---

Clone litellm

```
git clone https://github.com/BerriAI/litellm.git
```

### Local setup for locally running docs[​](#local-setup-for-locally-running-docs "Direct link to Local setup for locally running docs")

#### Installation[​](#installation "Direct link to Installation")

#### Locally Serving Docs[​](#locally-serving-docs "Direct link to Locally Serving Docs")

If you see `command not found: mkdocs` try running the following

This command builds your Markdown files into HTML and starts a development server to browse your documentation. Open up [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your web browser to see your documentation. You can make changes to your Markdown files and your docs will automatically rebuild.

[Full tutorial here](https://docs.readthedocs.io/en/stable/intro/getting-started-with-mkdocs.html)

### Making changes to Docs[​](#making-changes-to-docs "Direct link to Making changes to Docs")

- All the docs are placed under the `docs` directory
- If you are adding a new `.md` file or editing the hierarchy edit `mkdocs.yml` in the root of the project
- After testing your changes, make a change to the `main` branch of [github.com/BerriAI/litellm](https://github.com/BerriAI/litellm)

<!--THE END-->

- [Local setup for locally running docs](#local-setup-for-locally-running-docs)
- [Making changes to Docs](#making-changes-to-docs)