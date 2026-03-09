---
title: Cloud Templates – Installation & Usage
url: https://docs.factory.ai/web/machine-connection/cloud-templates/installation-and-usage.md
source: llms
fetched_at: 2026-03-03T01:15:04.32087-03:00
rendered_js: false
word_count: 223
summary: This document provides instructions for setting up, configuring, and using remote development environments within Factory sessions through Cloud Templates.
tags:
    - cloud-templates
    - factory-sessions
    - remote-development
    - environment-setup
    - configuration
    - developer-tools
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.factory.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Cloud Templates – Installation & Usage

> Set up, connect to, and use Cloud Templates inside Factory sessions

A **cloud template** is a fully-configured, on-demand development environment that lives in the cloud. Cloud templates give you the same tools and dependencies you'd expect locally, so you can build, test, and run code directly from Factory.

<Note>
  To get the most out of cloud templates, configure environment variables and a setup script during template creation. The setup script installs dependencies and prepares your development environment automatically, ensuring every team member has an identical setup.
</Note>

## System Requirements

* A repository enabled in Factory
* Manager role or higher to create cloud templates

<Steps>
  <Step title="Open Cloud Templates Settings">
    1. In Factory, click the **Settings** icon from the left sidebar.
    2. Select **Cloud Templates**.
  </Step>

  <Step title="Create a New Cloud Template">
    1. Click **Create Template**.
    2. Enter the repository you want to use.
    3. Give your template a friendly name (e.g., “frontend-template”).
    4. (Optional) Configure a setup script to run during template initialization.
    5. Click **Create**.

    <Note>
      Factory clones your repo and prepares the environment—this can take a minute for large projects.
    </Note>
  </Step>

  <Step title="Verify Template Ready">
    The new template appears in the list with a status indicator. Once it shows **Ready**, you can use it from any session.
  </Step>
</Steps>

***

## Launching a Cloud Template inside a Session

<Steps>
  <Step title="Open or Start a Session">
    Join any Factory session as usual.
  </Step>

  <Step title="Connect to Cloud Machine">
    1. On the session start page, click the Machine Connection button.
    2. Choose **Remote** tab.
    3. Select the template you created earlier.
    4. Factory attaches the cloud template to your session.

    <Frame>
            <img src="https://mintcdn.com/factory/Hp3lbmWjJVrQVsgq/images/web/machine-connection-start.gif?s=81a3f3be856a4b9d9df4cb828715e2a1" alt="machine-connection-start.gif" data-og-width="1156" width="1156" data-og-height="720" height="720" data-path="images/web/machine-connection-start.gif" data-optimize="true" data-opv="3" />
    </Frame>
  </Step>

  <Step title="Confirm Connection">
    A green indicator and remote working directory appear on the top-right next to your profile dropdown menu. You’re now interacting with the cloud template.
  </Step>
</Steps>

***

## Everyday Usage

<CardGroup cols={2}>
  <Card title="Run CLI Commands" icon="terminal">
    Use the **Terminal** toolkit to execute commands like:
    <pre>npm run dev
    pytest
    git status</pre>
    Output streams live into chat and logs.
  </Card>

  <Card title="Edit & Save Files" icon="file-code">
    Open files from the repo, make changes, and save.\
    Files persist in the cloud template and can be committed upstream when ready.
  </Card>

  <Card title="Auto-Save Controls" icon="save">
    Auto-save is disabled by default—enable it from the **Session Settings** panel whenever you want live file syncing.
  </Card>
</CardGroup>

***

## Troubleshooting & Help

<AccordionGroup>
  <Accordion title="Can't connect from session">
    Ensure you:

    1. Selected **Remote Machine** (not Local).
    2. Refresh the page, or try again in a different session
  </Accordion>
</AccordionGroup>

<Card title="Need More Help?" icon="life-ring" href="/web/machine-connection/cloud-templates/troubleshooting">
  Visit the full Cloud Template Troubleshooting Guide
</Card>