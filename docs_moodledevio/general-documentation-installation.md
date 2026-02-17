---
title: Installation | Moodle Developer Resources
url: https://moodledev.io/general/documentation/installation
source: sitemap
fetched_at: 2026-02-17T16:02:05.420864-03:00
rendered_js: false
word_count: 303
summary: This document provides instructions for setting up a development environment to contribute to Docusaurus-based documentation, covering local installation, cloud-based setups like Gitpod, and essential CLI commands.
tags:
    - docusaurus
    - development-environment
    - documentation-contribution
    - gitpod
    - local-setup
    - cli-commands
    - markdown-editing
category: guide
---

Our documentation is built using [Docusaurus](https://docusaurus.io), a powerful open source documentation project written in JavaScript.

It's easy to get your development environment set up and if you plan to contribute regularly to our documentation, then we recommend you setup a [local development environment](#local-development) for the best results. If you're only planning to contribute as a once-off then you may want to consider trying [Gitpod](#quick-start-with-gitpod).

## Installation[​](#installation "Direct link to Installation")

### Local development[​](#local-development "Direct link to Local development")

To set up a local development environment we recommend install [NVM](https://github.com/nvm-sh/nvm), and then running:

```
nvm install
corepack enable
yarn
```

note

From time to time you may need to repeat this process as we update the NodeJS version requirements or add dependencies.

### Quick start with Gitpod[​](#quick-start-with-gitpod "Direct link to Quick start with Gitpod")

Gitpod is a free, cloud-based, development environment providing VS Code and a suitable development environment right in your browser.

By [launching your workspace](https://gitpod.io/#https://github.com/moodle/devdocs) you can automatically:

- clone our devdocs repo
- install all dependencies
- run `yarn start`

You can write and preview your contributions from right within your browser, and even commit them and create a pull request.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/moodle/devdocs)

GitHub has also launched their own lightweight online editor which integrates tightly with GitHub. Take a look at [github.dev](https://github.dev/moodle/devdocs).

info

Gitpod is an alternative to local development and completely optional. We recommend [setting up a local development environment](#installation) if you plan to contribute regularly.

## Useful commands[​](#useful-commands "Direct link to Useful commands")

### Starting the development server[​](#starting-the-development-server "Direct link to Starting the development server")

The development server is the best way to edit docs locally. Once the development server has started, the docs will open in your browser. You can then make changes to the source markdown files (`*.md` and `*.mdx`), which should be automatically live reloaded in your browser.

### Building the docs and serving them locally[​](#building-the-docs-and-serving-them-locally "Direct link to Building the docs and serving them locally")

This is probably only something you would do if you were developing or testing the build process.

### Migrating a document[​](#migrating-a-document "Direct link to Migrating a document")

For full documentation on document migration see the [notes on contributing](https://moodledev.io/general/documentation/contributing#migrating-legacy-docs)

```
yarn migrate [https://docs.moodle.org/dev/Old_doc_location] [newLocation]
```

### Linting documents[​](#linting-documents "Direct link to Linting documents")