---
title: LiteLLM AI Gateway Prompt Management | liteLLM
url: https://docs.litellm.ai/docs/proxy/litellm_prompt_management
source: sitemap
fetched_at: 2026-01-21T19:52:48.061484188-03:00
rendered_js: false
word_count: 851
summary: This document explains how to use the LiteLLM AI Gateway dashboard to create, manage, and version dynamic prompts for integration into applications via API.
tags:
    - litellm-gateway
    - prompt-management
    - version-control
    - prompt-engineering
    - llm-ops
    - api-integration
category: guide
---

Use the LiteLLM AI Gateway to create, manage and version your prompts.

## Quick Start[​](#quick-start "Direct link to Quick Start")

### Accessing the Prompts Interface[​](#accessing-the-prompts-interface "Direct link to Accessing the Prompts Interface")

1. Navigate to **Experimental &gt; Prompts** in your LiteLLM dashboard
2. You'll see a table displaying all your existing prompts with the following columns:
   
   - **Prompt ID**: Unique identifier for each prompt
   - **Model**: The LLM model configured for the prompt
   - **Created At**: Timestamp when the prompt was created
   - **Updated At**: Timestamp of the last update
   - **Type**: Prompt type (e.g., db)
   - **Actions**: Delete and manage prompt options (admin only)

![Prompt Table](https://docs.litellm.ai/assets/images/prompt_table-785da09b565e4e174be873a0d2c5af0d.png)

## Create a Prompt[​](#create-a-prompt "Direct link to Create a Prompt")

Click the **+ Add New Prompt** button to create a new prompt.

### Step 1: Select Your Model[​](#step-1-select-your-model "Direct link to Step 1: Select Your Model")

Choose the LLM model you want to use from the dropdown menu at the top. You can select from any of your configured models (e.g., `aws/anthropic/bedrock-claude-3-5-sonnet`, `gpt-4o`, etc.).

### Step 2: Set the Developer Message[​](#step-2-set-the-developer-message "Direct link to Step 2: Set the Developer Message")

The **Developer message** section allows you to set optional system instructions for the model. This acts as the system prompt that guides the model's behavior.

For example:

```
Respond as jack sparrow would
```

This will instruct the model to respond in the style of Captain Jack Sparrow from Pirates of the Caribbean.

![Add Prompt with Developer Message](https://docs.litellm.ai/assets/images/add_prompt-04fccc66f876fd8dfa4c84113176eae6.png)

### Step 3: Add Prompt Messages[​](#step-3-add-prompt-messages "Direct link to Step 3: Add Prompt Messages")

In the **Prompt messages** section, you can add the actual prompt content. Click **+ Add message** to add additional messages to your prompt template.

### Step 4: Use Variables in Your Prompts[​](#step-4-use-variables-in-your-prompts "Direct link to Step 4: Use Variables in Your Prompts")

Variables allow you to create dynamic prompts that can be customized at runtime. Use the `{{variable_name}}` syntax to insert variables into your prompts.

For example:

```
Give me a recipe for {{dish}}
```

The UI will automatically detect variables in your prompt and display them in the **Detected variables** section.

![Add Prompt with Variables](https://docs.litellm.ai/assets/images/add_prompt_var-b82c67aa4db84ae69f7597e1b3fb0c8f.png)

### Step 5: Test Your Prompt[​](#step-5-test-your-prompt "Direct link to Step 5: Test Your Prompt")

Before saving, you can test your prompt directly in the UI:

1. Fill in the template variables in the right panel (e.g., set `dish` to `cookies`)
2. Type a message in the chat interface to test the prompt
3. The assistant will respond using your configured model, developer message, and substituted variables

![Test Prompt with Variables](https://docs.litellm.ai/assets/images/add_prompt_use_var1-b82c67aa4db84ae69f7597e1b3fb0c8f.png)

The result will show the model's response with your variables substituted:

![Prompt Test Results](https://docs.litellm.ai/assets/images/add_prompt_use_var-302274ae931eea38191d358ec471c5f6.png)

### Step 6: Save Your Prompt[​](#step-6-save-your-prompt "Direct link to Step 6: Save Your Prompt")

Once you're satisfied with your prompt, click the **Save** button in the top right corner to save it to your prompt library.

## Using Your Prompts[​](#using-your-prompts "Direct link to Using Your Prompts")

Now that your prompt is published, you can use it in your application via the LiteLLM proxy API. Click the **Get Code** button in the UI to view code snippets customized for your prompt.

### Basic Usage[​](#basic-usage "Direct link to Basic Usage")

Call a prompt using just the prompt ID and model:

- cURL
- Python
- JavaScript

Basic Prompt Call

```
curl -X POST 'http://localhost:4000/chat/completions' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer sk-1234' \
  -d '{
    "model": "gpt-4",
    "prompt_id": "your-prompt-id"
  }' | jq
```

### With Custom Messages[​](#with-custom-messages "Direct link to With Custom Messages")

Add custom messages to your prompt:

- cURL
- Python
- JavaScript

Prompt with Custom Messages

```
curl -X POST 'http://localhost:4000/chat/completions' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer sk-1234' \
  -d '{
    "model": "gpt-4",
    "prompt_id": "your-prompt-id",
    "messages": [
      {
        "role": "user",
        "content": "hi"
      }
    ]
  }' | jq
```

### With Prompt Variables[​](#with-prompt-variables "Direct link to With Prompt Variables")

Pass variables to your prompt template using `prompt_variables`:

- cURL
- Python
- JavaScript

Prompt with Variables

```
curl -X POST 'http://localhost:4000/chat/completions' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer sk-1234' \
  -d '{
    "model": "gpt-4",
    "prompt_id": "your-prompt-id",
    "prompt_variables": {
      "dish": "cookies"
    }
  }' | jq
```

## Prompt Versioning[​](#prompt-versioning "Direct link to Prompt Versioning")

LiteLLM automatically versions your prompts each time you update them. This allows you to maintain a complete history of changes and roll back to previous versions if needed.

### View Prompt Details[​](#view-prompt-details "Direct link to View Prompt Details")

Click on any prompt ID in the prompts table to view its details page. This page shows:

- **Prompt ID**: The unique identifier for your prompt
- **Version**: The current version number (e.g., v4)
- **Prompt Type**: The storage type (e.g., db)
- **Created At**: When the prompt was first created
- **Last Updated**: Timestamp of the most recent update
- **LiteLLM Parameters**: The raw JSON configuration

![Prompt Details](https://docs.litellm.ai/assets/images/edit_prompt-20bc1797ab336d1d5ceaf9c0c04c04b4.png)

### Update a Prompt[​](#update-a-prompt "Direct link to Update a Prompt")

To update an existing prompt:

1. Click on the prompt you want to update from the prompts table
2. Click the **Prompt Studio** button in the top right
3. Make your changes to:
   
   - Model selection
   - Developer message (system instructions)
   - Prompt messages
   - Variables
4. Test your changes in the chat interface on the right
5. Click the **Update** button to save the new version

![Edit Prompt in Studio](https://docs.litellm.ai/assets/images/edit_prompt2-da10e9c66961568004be08ce74ad4fa5.png)

Each time you click **Update**, a new version is created (v1 → v2 → v3, etc.) while maintaining the same prompt ID.

### View Version History[​](#view-version-history "Direct link to View Version History")

To view all versions of a prompt:

1. Open the prompt in **Prompt Studio**
2. Click the **History** button in the top right
3. A **Version History** panel will open on the right side

![Version History Panel](https://docs.litellm.ai/assets/images/edit_prompt3-fddf675e320f42586424f4561362bb53.png)

The version history panel displays:

- **Latest version** (marked with a "Latest" badge and "Active" status)
- All previous versions (v4, v3, v2, v1, etc.)
- Timestamps for each version
- Database save status ("Saved to Database")

### View and Restore Older Versions[​](#view-and-restore-older-versions "Direct link to View and Restore Older Versions")

To view or restore an older version:

1. In the **Version History** panel, click on any previous version (e.g., v2)
2. The prompt studio will load that version's configuration
3. You can see:
   
   - The developer message from that version
   - The prompt messages from that version
   - The model and parameters used
   - All variables defined at that time

![View Older Version](https://docs.litellm.ai/assets/images/edit_prompt4-8e401504cb15e04a408a72b92f5edc7d.png)

The selected version will be highlighted with an "Active" badge in the version history panel.

To restore an older version:

1. View the older version you want to restore
2. Click the **Update** button
3. This will create a new version with the content from the older version

### Use Specific Versions in API Calls[​](#use-specific-versions-in-api-calls "Direct link to Use Specific Versions in API Calls")

By default, API calls use the latest version of a prompt. To use a specific version, pass the `prompt_version` parameter:

- cURL
- Python
- JavaScript

Use Specific Prompt Version

```
curl -X POST 'http://localhost:4000/chat/completions' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer sk-1234' \
  -d '{
    "model": "gpt-4",
    "prompt_id": "jack-sparrow",
    "prompt_version": 2,
    "messages": [
      {
        "role": "user",
        "content": "Who are u"
      }
    ]
  }' | jq
```