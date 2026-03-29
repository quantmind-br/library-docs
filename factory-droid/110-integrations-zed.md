---
title: Zed
url: https://docs.factory.ai/integrations/zed.md
source: llms
fetched_at: 2026-02-05T21:44:52.223539505-03:00
rendered_js: false
word_count: 819
summary: This document provides step-by-step instructions for integrating Factory Droid as a custom AI agent within the Zed editor, covering extension installation, authentication, and manual CLI configuration.
tags:
    - zed-editor
    - factory-droid
    - ai-agent
    - mcp-server
    - setup-guide
    - configuration
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.factory.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Zed

> Use Factory Droid as a custom AI agent inside Zed, with full MCP server support.

## Setup

Before wiring Zed to Factory Droid, make sure you have Zed installed. Afterwards:

1. [Install the Factory Droid extension.](https://zed.dev/extensions/factory-droid)
2. Open the Agent Panel.
3. Click the **+** button in the top-right corner.
4. In the agent dropdown, select **Factory Droid**.
5. If you are unauthenticated you will see a message indicating you must authenticate.
   1. Keep track of the device code rendered, and click the "Login" button.

      <img src="https://mintcdn.com/factory/vk3165sy85E5xFyE/images/zed/authentication-flow-zed.png?fit=max&auto=format&n=vk3165sy85E5xFyE&q=85&s=50948bdaca925ca51d81a28ede04bbaa" alt="Zed authentication screen showing a device code and Login button" style={{ width: '70%' }} data-og-width="990" width="990" data-og-height="712" height="712" data-path="images/zed/authentication-flow-zed.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/factory/vk3165sy85E5xFyE/images/zed/authentication-flow-zed.png?w=280&fit=max&auto=format&n=vk3165sy85E5xFyE&q=85&s=f237f4a1d688babfdbe39e0b65fa3e03 280w, https://mintcdn.com/factory/vk3165sy85E5xFyE/images/zed/authentication-flow-zed.png?w=560&fit=max&auto=format&n=vk3165sy85E5xFyE&q=85&s=bd7990dcac0fd366e52578fe44dd9fe1 560w, https://mintcdn.com/factory/vk3165sy85E5xFyE/images/zed/authentication-flow-zed.png?w=840&fit=max&auto=format&n=vk3165sy85E5xFyE&q=85&s=0a58abba3885a2d3e340b7f22e621f50 840w, https://mintcdn.com/factory/vk3165sy85E5xFyE/images/zed/authentication-flow-zed.png?w=1100&fit=max&auto=format&n=vk3165sy85E5xFyE&q=85&s=277491c343ce9ea2b2f172845679121e 1100w, https://mintcdn.com/factory/vk3165sy85E5xFyE/images/zed/authentication-flow-zed.png?w=1650&fit=max&auto=format&n=vk3165sy85E5xFyE&q=85&s=9f99a97b0e7dd962adf97d9008dd2d08 1650w, https://mintcdn.com/factory/vk3165sy85E5xFyE/images/zed/authentication-flow-zed.png?w=2500&fit=max&auto=format&n=vk3165sy85E5xFyE&q=85&s=9fe11fde8c4d49f34d5c7d17f0c8d689 2500w" />

   2. This will open your web browser and ask you to login/signup to Factory, followed by a screen to confirm your device's code.

      <img src="https://mintcdn.com/factory/vk3165sy85E5xFyE/images/zed/authentication-flow-factory.png?fit=max&auto=format&n=vk3165sy85E5xFyE&q=85&s=08e002e4a0fb5593a5a61cd8f8dc32aa" alt="Factory web authentication screen prompting for device code confirmation" data-og-width="1986" width="1986" data-og-height="1470" height="1470" data-path="images/zed/authentication-flow-factory.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/factory/vk3165sy85E5xFyE/images/zed/authentication-flow-factory.png?w=280&fit=max&auto=format&n=vk3165sy85E5xFyE&q=85&s=a2799603fb61067a776ace3c2659429d 280w, https://mintcdn.com/factory/vk3165sy85E5xFyE/images/zed/authentication-flow-factory.png?w=560&fit=max&auto=format&n=vk3165sy85E5xFyE&q=85&s=c8f7893a1ff3cf597424607da42b850d 560w, https://mintcdn.com/factory/vk3165sy85E5xFyE/images/zed/authentication-flow-factory.png?w=840&fit=max&auto=format&n=vk3165sy85E5xFyE&q=85&s=9adebbd3d336bba7cd60e3860d515590 840w, https://mintcdn.com/factory/vk3165sy85E5xFyE/images/zed/authentication-flow-factory.png?w=1100&fit=max&auto=format&n=vk3165sy85E5xFyE&q=85&s=34645d56f2d3fa5db49cb3a91a6a043d 1100w, https://mintcdn.com/factory/vk3165sy85E5xFyE/images/zed/authentication-flow-factory.png?w=1650&fit=max&auto=format&n=vk3165sy85E5xFyE&q=85&s=883638d3916383906ef700e17979e08c 1650w, https://mintcdn.com/factory/vk3165sy85E5xFyE/images/zed/authentication-flow-factory.png?w=2500&fit=max&auto=format&n=vk3165sy85E5xFyE&q=85&s=6a1dd840a9b23ff4f5e0d4884728cc70 2500w" />

## (Alternative) Manual Setup

If you prefer to manually configure Droid inside Zed, you can follow the instructions below.

1. **Factory CLI installed (supported on all operating systems except Windows ARM machines)**

   * Install via:

     ```bash  theme={null}
     curl -fsSL https://app.factory.ai/cli | sh
     ```

   * Ensure `droid` is on your PATH, or note its full path.

2. **Zed installed**
   * Zed on macOS, Linux, or x86\_64 Windows.
   * Access to `~/.config/zed/settings.json`.

3. **(Optional) Factory API key** - instead of using the login flow, you can set up an API key:
   * Sign up at [https://app.factory.ai](https://app.factory.ai).
   * Configure billing if required.
   * Create an API key at [https://app.factory.ai/settings/api-keys](https://app.factory.ai/settings/api-keys).
   * Set the `FACTORY_API_KEY` environment variable in your shell (for example, add `export FACTORY_API_KEY=your_key_here` to your shell profile).

<Note>
  You cannot create a Factory account or manage billing from inside Zed. All
  account setup happens in the Factory web app.
</Note>

### Configure Factory Droid as an Agent (`agent_servers`)

Edit `~/.config/zed/settings.json` and add a **Factory Droid** entry under `agent_servers`:

```json  theme={null}
"agent_servers": {
  "Factory Droid": {
    "type": "custom",
    "command": "*path/to/droid/cli*",
    "args": ["exec", "--output-format", "acp"]
  }
}
```

* `type: "custom"` – tells Zed this is a user-defined agent
* `command` – full path to the `droid` binary
* `args` – run Droid in exec mode and speak ACP to Zed

If you prefer to use an API key instead of the login flow, add an `env` block:

```json  theme={null}
"agent_servers": {
  "Factory Droid": {
    "type": "custom",
    "command": "*path/to/droid/cli*",
    "args": ["exec", "--output-format", "acp"],
    "env": {
      "FACTORY_API_KEY": "$FACTORY_API_KEY"
    }
  }
}
```

## Start a Droid Session in Zed

Once `agent_servers` and `context_servers` are configured, you can start chatting with Droid from the Agent Panel.

### Open the Agent Panel

* macOS: `Cmd` + `?`
* Linux/Windows: `Ctrl` + `?`

### Start a New Chat with Factory Droid

1. Open the Agent Panel.
2. Click the **+** button in the top-right corner.
3. In the agent dropdown, select **Factory Droid**.
4. Start chatting.

<img src="https://mintcdn.com/factory/gSNLHBriX1BhnAJ4/images/zed/start-a-new-chat.png?fit=max&auto=format&n=gSNLHBriX1BhnAJ4&q=85&s=614307b2d6e5d369f87e836facf2f41e" alt="Zed Agent Panel with + button highlighted and Factory Droid selected in the agent dropdown" data-og-width="2050" width="2050" data-og-height="1320" height="1320" data-path="images/zed/start-a-new-chat.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/factory/gSNLHBriX1BhnAJ4/images/zed/start-a-new-chat.png?w=280&fit=max&auto=format&n=gSNLHBriX1BhnAJ4&q=85&s=3b7383ce711a41c649f5989a9d49ff05 280w, https://mintcdn.com/factory/gSNLHBriX1BhnAJ4/images/zed/start-a-new-chat.png?w=560&fit=max&auto=format&n=gSNLHBriX1BhnAJ4&q=85&s=77a1ead985231b584225f5d6d7cd6440 560w, https://mintcdn.com/factory/gSNLHBriX1BhnAJ4/images/zed/start-a-new-chat.png?w=840&fit=max&auto=format&n=gSNLHBriX1BhnAJ4&q=85&s=d885c123d85edd95c1e406aa80aa5f42 840w, https://mintcdn.com/factory/gSNLHBriX1BhnAJ4/images/zed/start-a-new-chat.png?w=1100&fit=max&auto=format&n=gSNLHBriX1BhnAJ4&q=85&s=706f0db081a42da4131ce20d15f6a5af 1100w, https://mintcdn.com/factory/gSNLHBriX1BhnAJ4/images/zed/start-a-new-chat.png?w=1650&fit=max&auto=format&n=gSNLHBriX1BhnAJ4&q=85&s=8b62842f3ff275c0cfb0001fa1e67f6d 1650w, https://mintcdn.com/factory/gSNLHBriX1BhnAJ4/images/zed/start-a-new-chat.png?w=2500&fit=max&auto=format&n=gSNLHBriX1BhnAJ4&q=85&s=dd6cc2b69e95483c669bad778c878a9f 2500w" />

## Resume Existing Sessions

Zed does not currently provide a way to reload or restore past Factory Droid sessions from the Agent Panel.

* Each Agent Panel conversation is effectively a fresh session.
* For longer work streams, keep the panel open or start new chats with a brief recap so Droid can quickly reorient.

## Editor Context and Limitations

There is no dedicated Factory Droid plugin for Zed yet, but Zed supports **`@`-tagging files** inside agent chats.

* Use `@` to reference relevant files when you ask Droid to inspect or modify code.
* Combine `@`-tags with plain-language instructions, just as you would in the CLI.

Example:

```text  theme={null}
Refactor the state management in @src/components/TodoList.tsx to use a reducer instead of multiple useState hooks.
```

<img src="https://mintcdn.com/factory/gSNLHBriX1BhnAJ4/images/zed/@-tag-file.png?fit=max&auto=format&n=gSNLHBriX1BhnAJ4&q=85&s=5de149777740f185f702aa7e1adc2f34" alt="Zed Agent Panel showing a message with an @-tagged file reference" data-og-width="2050" width="2050" data-og-height="1320" height="1320" data-path="images/zed/@-tag-file.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/factory/gSNLHBriX1BhnAJ4/images/zed/@-tag-file.png?w=280&fit=max&auto=format&n=gSNLHBriX1BhnAJ4&q=85&s=046cc37ac3406145179e392f7caf8ec6 280w, https://mintcdn.com/factory/gSNLHBriX1BhnAJ4/images/zed/@-tag-file.png?w=560&fit=max&auto=format&n=gSNLHBriX1BhnAJ4&q=85&s=8b9542fff015906217c03d555a3eab2a 560w, https://mintcdn.com/factory/gSNLHBriX1BhnAJ4/images/zed/@-tag-file.png?w=840&fit=max&auto=format&n=gSNLHBriX1BhnAJ4&q=85&s=896c853a7774e39746b952fcd43dd42d 840w, https://mintcdn.com/factory/gSNLHBriX1BhnAJ4/images/zed/@-tag-file.png?w=1100&fit=max&auto=format&n=gSNLHBriX1BhnAJ4&q=85&s=ef25bcb14f93d1c813cfa4ed872cd726 1100w, https://mintcdn.com/factory/gSNLHBriX1BhnAJ4/images/zed/@-tag-file.png?w=1650&fit=max&auto=format&n=gSNLHBriX1BhnAJ4&q=85&s=7348e65bbeb8f9da0f01a29f6fd75db9 1650w, https://mintcdn.com/factory/gSNLHBriX1BhnAJ4/images/zed/@-tag-file.png?w=2500&fit=max&auto=format&n=gSNLHBriX1BhnAJ4&q=85&s=1ce2d5cf044eb1deb00f17dc22c03377 2500w" />

## Models and Autonomy

Model selection and autonomy behavior inside Zed follow the same rules as the Droid CLI.

* Choose your model and reasoning level using the same patterns described in [Choosing Your Model](/cli/user-guides/choosing-your-model).
* Use lower autonomy for planning and higher autonomy once you trust the plan.
* Zed supports **`Shift+Tab` for switching autonomy modes**, matching the default shortcut in the Droid CLI.

## (Optional) Configure MCP Servers (`context_servers`)

Zed’s `context_servers` section is where you configure **MCP servers**. Each entry is a real MCP server that exposes tools and context, which Factory Droid can call while you chat.

For example, to add a Chrome DevTools MCP server:

```json  theme={null}
"context_servers": {
  "chrome-devtools": {
    "command": "npx",
    "args": ["-y", "chrome-devtools@latest"]
  }
}
```

* `chrome-devtools` – server name used inside Zed
* `command` – executable to run (here, `npx`)
* `args` – how to launch the MCP server; update the package name to the actual server you want to use

You can define multiple MCP servers under `context_servers` for internal tools, data sources, or other services.

When you chat with **Factory Droid** in Zed, it can call any of these MCP servers as tools.

## Troubleshooting

If Factory Droid does not appear or respond in Zed:

* Verify the CLI:
  * Run `droid exec --output-format acp` in a regular terminal to ensure the CLI and API key work.
* Check `settings.json`:
  * Confirm the `agent_servers` and `context_servers` blocks are valid JSON (including commas and quotes).
  * Ensure the `command` and `args` for both Droid and your MCP servers run successfully outside Zed.
* Confirm your OS:
  * Make sure you are not running on Windows on ARM.

If an MCP server is failing, try launching it manually with the same `command` and `args` used in `context_servers` to debug configuration or dependency issues.