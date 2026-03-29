---
title: Shareable Recipes | goose
url: https://block.github.io/goose/docs/guides/recipes/session-recipes
source: github_pages
fetched_at: 2026-01-22T22:14:15.637868605-03:00
rendered_js: true
word_count: 1601
summary: This document provides instructions on how to create, edit, share, and schedule reusable recipes in goose to automate and replicate specific agent workflows and tool configurations.
tags:
    - goose-recipes
    - workflow-automation
    - recipe-management
    - scheduling
    - agent-configuration
category: guide
---

Sometimes you finish a task in goose and realize, "Hey, this setup could be useful again." Maybe you have curated a great combination of tools, defined a clear goal, and want to preserve that flow. Or maybe you're trying to help someone else replicate what you just did without walking them through it step by step.

You can turn your current goose session into a reusable recipe that includes the tools, goals, and setup you're using right now and package it into a new Agent that others (or future you) can launch with a single click.

## Create Recipe[​](#create-recipe "Direct link to Create Recipe")

- goose Desktop
- goose CLI
- Recipe Generator

Create a recipe from the current session or from a template.

- Current Session
- Template

<!--THE END-->

1. While in the session you want to save as a recipe, click the button at the bottom of the app
2. In the dialog that opens, review and edit the recipe fields as needed:
   
   - **Title** and **description**
   - **Instructions** that tell goose what to do
   - **Initial prompt** to pre-fill the chat input
   - **Message** to display at the top of the recipe and **activity buttons** for users to click
   - **Parameters** to accept dynamic values
   - **Response JSON schema** for [structured output in automations](https://block.github.io/goose/docs/guides/recipes/session-recipes#structured-output-for-automation)
3. When you're finished, you can:
   
   - Click `Create Recipe` to save the recipe to your Recipe Library
   - Click `Create & Run Recipe` to save and immediately run the recipe in a new session

warning

You cannot create a recipe from an existing recipe session, but you can view or [edit the recipe](#edit-recipe).

## Edit Recipe[​](#edit-recipe "Direct link to Edit Recipe")

- goose Desktop
- goose CLI

<!--THE END-->

1. Click the button in the top-left to open the sidebar
2. Click `Recipes` in the sidebar
3. Find the recipe you want to edit and click the button
4. In the dialog that appears, edit any of the following:
   
   - **Title** and **description**
   - **Instructions** that tell goose what to do
   - **Initial prompt** to pre-fill the chat input
   - **Message** to display at the top of the recipe and **activity buttons** for users to click
   - **Parameters** to accept dynamic values
   - **Response JSON schema** for [structured output in automations](https://block.github.io/goose/docs/guides/recipes/session-recipes#structured-output-for-automation)
5. When you're finished, you can:
   
   - Copy the recipe link to share the recipe with others
   - Click `Save Recipe` to save your changes
   - Click `Save & Run Recipe` to save and immediately run the recipe in a new session

Edit In-Use Recipe

You can also access the edit dialog while using a recipe in a session: Just click the button at the bottom of the app. The button shows up after you've sent your first message.

## Use Recipe[​](#use-recipe "Direct link to Use Recipe")

- goose Desktop
- goose CLI

<!--THE END-->

1. Open the recipe using a direct link or manual URL entry, or from your Recipe library:
   
   **Direct Link:**
   
   1. Click a recipe link shared with you
   
   **Manual URL Entry:**
   
   1. Paste a recipe link into your browser's address bar
   2. Press `Enter` and click the `Open Goose.app` prompt
   
   **Recipe Library:**
   
   1. Click the button in the top-left to open the sidebar
   2. Click `Recipes` in the sidebar
   3. Find your recipe in the Recipe Library
   4. Click `Use` next to the recipe you want to open
   
   **Slash Command:**
   
   1. Enter a [custom slash command](https://block.github.io/goose/docs/guides/context-engineering/slash-commands) in any goose chat session
2. The first time you run a recipe, a warning dialog displays the recipe's title, description, and instructions for you to review. If you trust the recipe content, click `Trust and Execute` to continue. You won't be prompted again for the same recipe unless it changes.
3. If the recipe contains parameters, enter your values in the `Recipe Parameters` dialog and click `Start Recipe`.
   
   Parameters are dynamic values used in the recipe:
   
   - **Required parameters** are marked with red asterisks (\*)
   - **Optional parameters** show default values that can be changed
4. To run the recipe, click an activity bubble or send the prompt.

Privacy & Isolation

- Each person gets their own private session
- No data is shared between users
- Your session won't affect the original recipe creator's session

## Validate Recipe[​](#validate-recipe "Direct link to Validate Recipe")

- goose Desktop
- goose CLI

Recipe validation is only available through the CLI.

Share your recipe with goose users using a recipe link or recipe file.

Privacy & Isolation

Each recipient gets their own private session when using your shared recipe. No data is shared between users, and your original session and recipe remain unaffected.

You can share a recipe with Desktop users via a recipe link.

- goose Desktop
- goose CLI

Copy the deeplink from your Recipe Library to share with others:

1. Click the button in the top-left to open the sidebar
2. Click `Recipes` in the sidebar
3. Find the recipe you want to share and click the button to copy the link

When someone clicks the link, it will open goose Desktop with your recipe configuration. They can also use your recipe link to [import a recipe](https://block.github.io/goose/docs/guides/recipes/storing-recipes#importing-recipes) for future use.

You can share a recipe with Desktop or CLI users by sending the recipe file directly.

- Desktop users can [import the recipe](https://block.github.io/goose/docs/guides/recipes/storing-recipes#importing-recipes) (YAML only).
- CLI users can run a YAML or JSON recipe using `goose run --recipe <FILE>` or open it directly in goose Desktop with `goose recipe open <FILE>`. See the [CLI Commands guide](https://block.github.io/goose/docs/guides/goose-cli-commands#recipe) for details.

## Schedule Recipe[​](#schedule-recipe "Direct link to Schedule Recipe")

- goose Desktop
- goose CLI

Automate goose recipes by running them on a schedule. When creating a schedule, you'll configure:

- **Name**: A descriptive name for the schedule
- **Source**: The recipe to run
- **Execution mode**: Whether the recipe runs in the background (no window, results saved) or foreground (opens window if goose Desktop is running, otherwise runs in background)
- **Frequency and time**: When to run the recipe (e.g. every 20 minutes, weekly at 10 AM on Friday). Your selection is converted into a [cron expression](https://en.wikipedia.org/wiki/Cron#Cron_expression) used by goose.

**Schedule from Recipe Library:**

1. Click the button in the top-left to open the sidebar
2. Click `Recipes` in the sidebar
3. Find the recipe you want to schedule and click the button
4. Click `Create Schedule`
5. In the dialog that appears, configure the schedule. For **Source**, your recipe link is already provided.
6. Click `Create Schedule`

**Schedule from Scheduler View:**

1. Click the button in the top-left to open the sidebar
2. Click `Scheduler`
3. Click `Create Schedule`
4. In the dialog that appears, configure the schedule. For **Source**, select a `.yaml` or `.yml` file or provide a [recipe link](#share-recipe).
5. Click `Create Schedule`

**Manage Scheduled Recipes**

Your scheduled recipes are listed in the `Scheduler` page. Click on a schedule to view details, see when it was last run, and perform actions with the scheduled recipe:

- `Run Schedule Now` to trigger the recipe manually
- `Edit Schedule` to change the scheduled frequency
- `Pause Schedule` to stop the recipe from running automatically

At the bottom of the `Schedule Details` page you can view the list of sessions created by the scheduled recipe and open or restore each session.

## Core Components[​](#core-components "Direct link to Core Components")

A recipe needs these core components:

- **Instructions**: Define the agent's behavior and capabilities
  
  - Acts as the agent's mission statement
  - Makes the agent ready for any relevant task
  - Required if no prompt is provided
- **Prompt** (Optional): Starts the conversation automatically
  
  - Without a prompt, the agent waits for user input
  - Useful for specific, immediate tasks
  - Required if no instructions are provided
- **Activities**: Example tasks that appear as clickable bubbles
  
  - Help users understand what the recipe can do
  - Make it easy to get started

## Advanced Features[​](#advanced-features "Direct link to Advanced Features")

### Automated Retry Logic[​](#automated-retry-logic "Direct link to Automated Retry Logic")

Recipes can include retry logic to automatically attempt task completion multiple times until success criteria are met. This is particularly useful for:

- **Automation workflows** that need to ensure successful completion
- **Development tasks** like running tests that may need multiple attempts
- **System operations** that require validation and cleanup

**Basic retry configuration:**

```
retry:
max_retries:3
checks:
-type: shell
command:"test -f output.txt"# Check if output file exists
on_failure:"rm -f temp_files*"# Cleanup on failure
```

**How it works:**

1. Recipe executes normally with provided instructions
2. After completion, success checks validate the results
3. If validation fails and retries remain:
   
   - Optional cleanup command runs
   - Agent state resets to initial conditions
   - Recipe execution starts over
4. Process continues until either success or max retries reached

See the [Recipe Reference Guide](https://block.github.io/goose/docs/guides/recipes/recipe-reference#retry) for complete retry configuration options and examples.

### Structured Output for Automation[​](#structured-output-for-automation "Direct link to Structured Output for Automation")

Recipes can enforce [structured JSON output](https://block.github.io/goose/docs/guides/recipes/recipe-reference#response), making them ideal for automation workflows that need to parse and process agent responses reliably. Key benefits include:

- **Reliable parsing**: Consistent JSON format for scripts, automation, and CI/CD pipelines
- **Built-in validation**: Ensures output matches your requirements
- **Easy extraction**: Final output appears as a single line for simple parsing

Structured output is particularly useful for:

- **Development workflows**: Code analysis reports, test results with pass/fail counts, and build status with deployment readiness
- **Data processing**: Results with counts and validation status, content analysis with structured findings
- **Documentation generation**: Consistent metadata and structured project reports for further processing

**Example structured output configuration:**

```
response:
json_schema:
type: object
properties:
build_status:
type: string
enum:["success","failed","warning"]
description:"Overall build result"
tests_passed:
type: number
description:"Number of tests that passed"
tests_failed:
type: number
description:"Number of tests that failed"
artifacts:
type: array
items:
type: string
description:"Generated build artifacts"
deployment_ready:
type: boolean
description:"Whether the build is ready for deployment"
required:
- build_status
- tests_passed
- tests_failed
- deployment_ready
```

**How it works:**

1. Recipe runs normally with provided instructions
2. goose calls a `final_output` tool with JSON matching your schema
3. Output is validated against the JSON schema
4. If validation fails, goose receives error details and must correct the output
5. Final validated JSON appears as the last line of output for easy extraction

**Example automation usage:**

```
# Run recipe and extract JSON output
goose run --recipe analysis.yaml --params project_path=./src > output.log
RESULT=$(tail -n 1 output.log)
echo "Analysis Status: $(echo $RESULT | jq -r '.build_status')"
echo "Issues Found: $(echo $RESULT | jq -r '.tests_failed')"
```

info

Structured output is supported in recipes run in both the goose CLI and goose Desktop. However, creating and editing the `json_schema` configuration must be done manually in the recipe file.

## What's Included[​](#whats-included "Direct link to What's Included")

A recipe captures:

- AI instructions (goal/purpose)
- Suggested activities (examples for the user to click)
- Enabled extensions and their configurations
- Project folder or file context
- Initial setup (but not full conversation history)
- The model and provider to use when running the recipe (optional)
- Retry logic and success validation configuration (if configured)

To protect your privacy and system integrity, goose excludes:

- Global and local memory
- API keys and personal credentials
- System-level goose settings

This means others may need to supply their own credentials or memory context if the recipe depends on those elements.

## Learn More[​](#learn-more "Direct link to Learn More")

Check out the [Recipes](https://block.github.io/goose/docs/guides/recipes) guide for more docs, tools, and resources to help you master goose recipes.