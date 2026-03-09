---
title: JetBrains IDEs
url: https://docs.factory.ai/integrations/jetbrains.md
source: llms
fetched_at: 2026-03-03T01:14:39.259794-03:00
rendered_js: false
word_count: 859
summary: This document provides instructions for installing and configuring Factory Droid as an AI agent within JetBrains IDEs. It covers both automatic setup via the ACP registry and manual configuration using the CLI.
tags:
    - jetbrains
    - factory-droid
    - ai-agent
    - ide-integration
    - acp
    - setup-guide
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.factory.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# JetBrains IDEs

> Use Factory Droid as an AI agent inside JetBrains IDEs via ACP.

## Setup

In any JetBrains IDE (2025.3+) with JetBrains AI (make sure to update to the latest version):

1. Open **Settings > Tools > AI Assistant > Agents** or select **"Install From ACP Registry..."** in the agent picker menu.
2. Find **Factory Droid**.
3. Click **Install**.
4. Open the AI Chat panel and select **Factory Droid** from the agent dropdown.
5. If you are unauthenticated you will see a message indicating you must authenticate.
   1. Keep track of the device code rendered, and click the "Login" button.
   2. This will open your web browser and ask you to login/signup to Factory, followed by a screen to confirm your device's code.

## (Alternative) Manual Setup

If you prefer to manually configure Droid inside JetBrains, you can follow the instructions below.

1. **Factory CLI installed (supported on all operating systems except Windows ARM machines)**
   * Install via:

     ```bash  theme={null}
     curl -fsSL https://app.factory.ai/cli | sh
     ```

   * Ensure the `droid` binary is on your PATH (or note its full path).

2. **(Optional) Factory API key** - instead of using the login flow, you can set up an API key:
   * Sign up at [https://app.factory.ai](https://app.factory.ai).
   * Add a payment method if prompted.
   * Create an API key at [https://app.factory.ai/settings/api-keys](https://app.factory.ai/settings/api-keys).
   * Set the `FACTORY_API_KEY` environment variable in your shell (for example, add `export FACTORY_API_KEY=your_key_here` to your shell profile).

<Note>
  You cannot sign up for Factory or manage billing entirely inside JetBrains.
  Account creation and API key management always happen in the web app.
</Note>

### Configure Factory Droid as an Agent

Edit `~/.jetbrains/acp.json` and add a **Factory Droid** entry under `agent_servers`:

```json  theme={null}
{
  "agent_servers": {
    "Factory Droid": {
      "command": "*path/to/droid/cli*",
      "args": ["exec", "--output-format", "acp"]
    }
  }
}
```

* `command` – full path to the `droid` binary
* `args` – run Droid in exec mode and speak ACP back to JetBrains

If you prefer to use an API key instead of the login flow, add an `env` block:

```json  theme={null}
{
  "agent_servers": {
    "Factory Droid": {
      "command": "*path/to/droid/cli*",
      "args": ["exec", "--output-format", "acp"],
      "env": {
        "FACTORY_API_KEY": "*your API key from https://app.factory.ai/settings/api-keys*"
      }
    }
  }
}
```

## Start a Droid Session in JetBrains

Once the agent server is configured, you interact with Droid entirely through the AI Assistant UI.

### Open the AI Chat Panel

* **Search Everywhere:** Press `Shift`+`Shift`, type **"AI Assistant"**, and open the tool window.
* **Menu:** Go to **View → Tool Windows → AI Assistant** (exact name may vary slightly by IDE).

### Start a New Chat with Factory Droid

1. In the **AI Chat** panel, click **+ New Chat**.
2. In the bottom-left agent dropdown, choose **Factory Droid**.
3. Start chatting as you would in the CLI.

The session uses your last-selected settings for Factory Droid (model, autonomy level, etc.).

<img src="https://mintcdn.com/factory/HpObF08fYbcspLQp/images/jetbrains/new-chat.png?fit=max&auto=format&n=HpObF08fYbcspLQp&q=85&s=f4a255d92ab37f4aec401e56206a9baf" alt="AI Chat panel with + New Chat clicked and Factory Droid selected in the bottom-left dropdown" data-og-width="2214" width="2214" data-og-height="1318" height="1318" data-path="images/jetbrains/new-chat.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/factory/HpObF08fYbcspLQp/images/jetbrains/new-chat.png?w=280&fit=max&auto=format&n=HpObF08fYbcspLQp&q=85&s=3c3069196d0a12a2095cf69dcb29dd48 280w, https://mintcdn.com/factory/HpObF08fYbcspLQp/images/jetbrains/new-chat.png?w=560&fit=max&auto=format&n=HpObF08fYbcspLQp&q=85&s=4b79a5fbc141404e96b6a18a7252e961 560w, https://mintcdn.com/factory/HpObF08fYbcspLQp/images/jetbrains/new-chat.png?w=840&fit=max&auto=format&n=HpObF08fYbcspLQp&q=85&s=97709f7086e6cbc42f690e6366776782 840w, https://mintcdn.com/factory/HpObF08fYbcspLQp/images/jetbrains/new-chat.png?w=1100&fit=max&auto=format&n=HpObF08fYbcspLQp&q=85&s=1f4cd07b9ddea8e4365f72e62e6645f4 1100w, https://mintcdn.com/factory/HpObF08fYbcspLQp/images/jetbrains/new-chat.png?w=1650&fit=max&auto=format&n=HpObF08fYbcspLQp&q=85&s=296f20360c0d775be79d2e87371014f7 1650w, https://mintcdn.com/factory/HpObF08fYbcspLQp/images/jetbrains/new-chat.png?w=2500&fit=max&auto=format&n=HpObF08fYbcspLQp&q=85&s=4aa449c1bf07852930c572a00735aa7f 2500w" />

## Resume Existing Sessions

JetBrains manages sessions through the AI Chat UI rather than CLI commands.

* In the AI Chat panel, click the **clock icon** in the top-right corner.
* Choose a past conversation to reopen it.

<img src="https://mintcdn.com/factory/HpObF08fYbcspLQp/images/jetbrains/chat-history.png?fit=max&auto=format&n=HpObF08fYbcspLQp&q=85&s=ad5b733ced6c026edcf83cca37c7a52d" alt="AI Chat session history dropdown (clock icon) with previous Factory Droid sessions listed" style={{ width: '35%', height: 'auto' }} data-og-width="508" width="508" data-og-height="278" height="278" data-path="images/jetbrains/chat-history.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/factory/HpObF08fYbcspLQp/images/jetbrains/chat-history.png?w=280&fit=max&auto=format&n=HpObF08fYbcspLQp&q=85&s=b5a3f92ab44dd56117a958ccc1ff2bae 280w, https://mintcdn.com/factory/HpObF08fYbcspLQp/images/jetbrains/chat-history.png?w=560&fit=max&auto=format&n=HpObF08fYbcspLQp&q=85&s=a3f3c75be89fcd4b2c9312b2ab111c21 560w, https://mintcdn.com/factory/HpObF08fYbcspLQp/images/jetbrains/chat-history.png?w=840&fit=max&auto=format&n=HpObF08fYbcspLQp&q=85&s=e7c4a3109cefaa763fae03d3bbdf8ffc 840w, https://mintcdn.com/factory/HpObF08fYbcspLQp/images/jetbrains/chat-history.png?w=1100&fit=max&auto=format&n=HpObF08fYbcspLQp&q=85&s=1187a779ab645313f511c7a9eb7fecf9 1100w, https://mintcdn.com/factory/HpObF08fYbcspLQp/images/jetbrains/chat-history.png?w=1650&fit=max&auto=format&n=HpObF08fYbcspLQp&q=85&s=26e437bcc2e9282ec47d3fcf03a7cd14 1650w, https://mintcdn.com/factory/HpObF08fYbcspLQp/images/jetbrains/chat-history.png?w=2500&fit=max&auto=format&n=HpObF08fYbcspLQp&q=85&s=535ee08c5995791b012a789eb42a1f09 2500w" />

## Models and Autonomy Controls

You can change models and autonomy levels directly from the AI Chat footer.

### Switch Models

* Use the **model dropdown** at the bottom of the AI Chat panel.
* Pick any Factory-supported model (for example, Claude Opus/Sonnet, GPT-5.1 variants, or others configured via BYOK).

<img src="https://mintcdn.com/factory/HpObF08fYbcspLQp/images/jetbrains/select-model.png?fit=max&auto=format&n=HpObF08fYbcspLQp&q=85&s=91cb6d3b95ac9b8c85b9efdbe008f331" alt="AI Chat footer showing model dropdown expanded" style={{ width: '50%', height: 'auto' }} data-og-width="850" width="850" data-og-height="688" height="688" data-path="images/jetbrains/select-model.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/factory/HpObF08fYbcspLQp/images/jetbrains/select-model.png?w=280&fit=max&auto=format&n=HpObF08fYbcspLQp&q=85&s=876822d258ee96a13bd191c1f2fc6e3f 280w, https://mintcdn.com/factory/HpObF08fYbcspLQp/images/jetbrains/select-model.png?w=560&fit=max&auto=format&n=HpObF08fYbcspLQp&q=85&s=b38dda542481c569a16f686a02d57b75 560w, https://mintcdn.com/factory/HpObF08fYbcspLQp/images/jetbrains/select-model.png?w=840&fit=max&auto=format&n=HpObF08fYbcspLQp&q=85&s=584113e6b374f3cf09816bffa0849cd4 840w, https://mintcdn.com/factory/HpObF08fYbcspLQp/images/jetbrains/select-model.png?w=1100&fit=max&auto=format&n=HpObF08fYbcspLQp&q=85&s=ea3e0b970993d768cb2a7bc18457fdc9 1100w, https://mintcdn.com/factory/HpObF08fYbcspLQp/images/jetbrains/select-model.png?w=1650&fit=max&auto=format&n=HpObF08fYbcspLQp&q=85&s=cb19128755465d78344e35604e2c58f1 1650w, https://mintcdn.com/factory/HpObF08fYbcspLQp/images/jetbrains/select-model.png?w=2500&fit=max&auto=format&n=HpObF08fYbcspLQp&q=85&s=d5e1cbc92b2e5a34abc3bf9edbcde573 2500w" />

### Change Autonomy Level

* Use the **autonomy dropdown** next to the model selector.
* Choose the autonomy level that matches your risk tolerance and workflow.

Recommended pattern:

* Start with a **planning-first** flow (low autonomy, spec-style prompts) for medium and large tasks.
* Once you are happy with the plan, increase autonomy to **Auto low** or **Auto medium** so Droid can execute more steps without constant confirmation.

<img src="https://mintcdn.com/factory/HpObF08fYbcspLQp/images/jetbrains/select-autonomy-mode.png?fit=max&auto=format&n=HpObF08fYbcspLQp&q=85&s=26f4b2a219dea00e125623a0aa768ae7" alt="AI Chat footer showing autonomy dropdown expanded" style={{ width: '43%', height: 'auto' }} data-og-width="734" width="734" data-og-height="766" height="766" data-path="images/jetbrains/select-autonomy-mode.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/factory/HpObF08fYbcspLQp/images/jetbrains/select-autonomy-mode.png?w=280&fit=max&auto=format&n=HpObF08fYbcspLQp&q=85&s=942c1909cd572d72dba623511f8bb7cf 280w, https://mintcdn.com/factory/HpObF08fYbcspLQp/images/jetbrains/select-autonomy-mode.png?w=560&fit=max&auto=format&n=HpObF08fYbcspLQp&q=85&s=7508370b7a1dfc00428bcf6a3361f0d5 560w, https://mintcdn.com/factory/HpObF08fYbcspLQp/images/jetbrains/select-autonomy-mode.png?w=840&fit=max&auto=format&n=HpObF08fYbcspLQp&q=85&s=bcef35d3314204de53e5e6fe85efa45c 840w, https://mintcdn.com/factory/HpObF08fYbcspLQp/images/jetbrains/select-autonomy-mode.png?w=1100&fit=max&auto=format&n=HpObF08fYbcspLQp&q=85&s=b41e6bcf4aa975bdc43eb3422f6e55c0 1100w, https://mintcdn.com/factory/HpObF08fYbcspLQp/images/jetbrains/select-autonomy-mode.png?w=1650&fit=max&auto=format&n=HpObF08fYbcspLQp&q=85&s=db3b0b794c62d06d86b5090ada5e5530 1650w, https://mintcdn.com/factory/HpObF08fYbcspLQp/images/jetbrains/select-autonomy-mode.png?w=2500&fit=max&auto=format&n=HpObF08fYbcspLQp&q=85&s=f28c70cacb735b303428e5cc917f27fa 2500w" />

## Editor Context and Limitations

The current JetBrains integration speaks ACP but does not yet expose full editor context to Droid.

* No automatic sharing of open files, selections, or diagnostics
* No IDE-native diff viewer wired directly to Droid patches

Treat this like a rich chat front-end to the CLI:

* Use clear prompts, reference files by path, and rely on autonomy modes and spec-style planning to manage larger changes.

## Troubleshooting

If Factory Droid does not appear or respond in AI Chat:

* Verify the **CLI**:
  * Run `droid exec --output-format acp` in a regular terminal to confirm the binary and API key work.
* Double-check the **agent server configuration**:
  * Correct path to `droid`
  * `args` includes both `exec` and `--output-format acp`
  * `FACTORY_API_KEY` is present and valid
* Confirm you are not on **Windows on ARM**, which is not yet supported.

For MCP-related issues, check that each MCP server’s command, arguments, and environment variables are valid when run outside JetBrains.