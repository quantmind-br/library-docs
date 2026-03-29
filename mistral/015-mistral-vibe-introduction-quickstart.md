---
title: Quickstart | Mistral Docs
url: https://docs.mistral.ai/mistral-vibe/introduction/quickstart
source: crawler
fetched_at: 2026-01-29T07:34:19.352662429-03:00
rendered_js: false
word_count: 788
summary: A guide providing an overview and initial steps for getting started with Mistral AI's models and developer platform.
tags:
    - Mistral AI
    - quickstart
    - API
    - AI models
category: guide
---

Below is a quick guide to get you started with Vibe, for more details see [Configuration](https://docs.mistral.ai/mistral-vibe/introduction/configuration) to learn how to configure Vibe to your needs.

Before continuing, make sure you have [installed Vibe](https://docs.mistral.ai/mistral-vibe/introduction/install).

First, navigate to your project's root directory:

Once there, you can run Vibe:

![vibe_running_in_a_terminal](https://docs.mistral.ai/img/vibehome.png)

This will start the interactive CLI interface.

If this is your first time running Vibe, it will:

- Create a default configuration file at `~/.vibe/config.toml`
- Prompt you to pick a theme.

<!--THE END-->

![select_your_preferred_theme](https://docs.mistral.ai/img/vibetheme.png)

- Prompt you to enter your API key if it's not already configured, you can create one [here](https://console.mistral.ai/codestral/cli).

<!--THE END-->

![entering_the_API_key_on_first_launch](https://docs.mistral.ai/img/vibekey.png)

- Save your API key to `~/.vibe/.env` for future use

Alternatively, you can configure your API key separately using `vibe --setup`.

Once done, you can start interacting with the agent! Currently Vibe by default uses our **Devstral 2** model, you can also use Devstral Small 2 or even your own [custom model](https://docs.mistral.ai/mistral-vibe/introduction/configuration#change-providers).

![sending_a_query_to_vibe](https://docs.mistral.ai/img/vibequery.png)

### Learn how to use Vibe

We recommend using Vibe in interactive mode, but you can also use it in programmatic mode, learn more about both below.

Simply run `vibe` to enter the interactive chat loop, this mode simulates a chat interface with the agent.

- **Multi-line Input**: Press `Ctrl+J` or `Shift+Enter` for select terminals to insert a newline.
- **File Paths**: Reference files in your prompt using the `@` symbol for smart autocompletion (e.g., `> Read the file @src/agent.py`).
- **Shell Commands**: Prefix any command with `!` to execute it directly in your shell, bypassing the agent (e.g., `> !ls -l`).
- **External Editor**: Press `Ctrl+G` to edit your current input in an external editor.
- **Tool Output Toggle**: Press `Ctrl+O` to toggle the tool output view.
- **Todo View Toggle**: Press `Ctrl+T` to toggle the todo list view.
- **Auto-Approve Toggle**: Press `Shift+Tab` to toggle auto-approve mode on/off.

You can also directly start Vibe with a prompt with the following command:

Vibe also allows you to use slash commands and keyboard shortcuts for meta-actions and configuration changes during a session such as:

- `/h`, `/help`: Show a help message
- `/config`, `/theme`, `/model`: Edit configuration settings interactively
- `/clear`: Clear conversation history
- ...
- `Ctrl+T` Toggle todo view
- `Shift+Tab` Toggle auto-approve mode
- ... And more, use `/help` to display all available commands.

You can define your own slash commands through the skills system. Skills are reusable components that extend Vibe's functionality.

To create a custom slash command:

- Create a skill directory with a `SKILL.md` file
- Set `user-invocable = true` in the skill metadata
- Define the command logic in your skill

Example skill metadata:

Learn more about [Agents](https://docs.mistral.ai/mistral-vibe/agents_and_skills#skills).

Custom slash commands appear in the autocompletion menu alongside built-in commands.

You can define Agents and change them with `Shift+Tab`, below you can find a non-exaustive list of agents Vibe is packaged with:

- `default`: The standard default Vibe behavior, built for general usage requesting approval for tool execution.
- `plan`: Read-only agent for exploration and planning.
- `auto approve`: Automatically approves all tool executions without prompting.
- ...

Learn more about [Agents](https://docs.mistral.ai/mistral-vibe/agents_and_skills#agents).

**Trust Folder System** Vibe includes a trust folder system to ensure you only run the agent in directories you trust.

You can run Vibe non-interactively by piping input or using the `--prompt` flag. This is useful for scripting, it allows you to run Vibe in a more streamline manner. This will not enter the interactive chat loop interface.

By default, it uses `auto-approve` mode.

When using `--prompt`, you can specify additional options:

- **`--max-turns N`** : Limit the maximum number of assistant turns. The session will stop after N turns.
- **`--max-price DOLLARS`** : Set a maximum cost limit in dollars. The session will be interrupted if the cost exceeds this limit.
- **`--enabled-tools TOOL`** : Enable specific tools. In programmatic mode, this disables all other tools. Can be specified multiple times. Supports exact names, glob patterns (e.g., `bash*`), or regex with `re:` prefix (e.g., `re:^serena_.*$`).
- **`--output FORMAT`** : Set the output format. Options:
  
  - `text` (default): Human-readable text output
  - `json`: All messages as JSON at the end
  - `streaming`: Newline-delimited JSON per message

Example:

Vibe is built to keep you in control. For substantial tasks (refactors, multi-file updates, cleanups), Vibe splits the work into steps it can execute safely and asks for confirmation before proceeding.  
You can also cap the number of steps or set a maximum session cost, and control general permissions and usage in the config file, learn more about Configuration [here](https://docs.mistral.ai/mistral-vibe/introduction/configuration).

Before editing files or running commands, Vibe shows a full preview and asks for confirmation.

![vibe_showing_a_preview_of_changes_and_asking_for_confirmation](https://docs.mistral.ai/img/vibepermission.png)

After each step, you see exactly what was executed and the resulting output.

![vibe_displaying_generated_output_and_completed_steps](https://docs.mistral.ai/img/vibestep.png)

You’re ready to use Mistral Vibe in your terminal. Start with small tasks, try the interactive commands, and build up from there.

Need help? Type `/help`, check the [README](https://github.com/mistralai/mistral-vibe/blob/main/README.md), reach out on the [Mistral Discord](https://discord.gg/mistralai), or contact our [support team](https://help.mistral.ai/en/articles/347458-how-do-i-contact-mistral-ai-support).