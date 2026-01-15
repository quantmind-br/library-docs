---
title: Slack - Factory Documentation
url: https://docs.factory.ai/integrations/slack
source: sitemap
fetched_at: 2026-01-13T19:04:28.831170723-03:00
rendered_js: false
word_count: 368
summary: This guide explains how to integrate Factory with Slack to enable seamless interaction between the two platforms, including setup steps, verification procedures, and an overview of native tools for reading and posting messages.
tags:
    - slack-integration
    - factory
    - bot-setup
    - thread-context
    - troubleshooting
category: guide
---

This guide will walk you through the process of integrating Factory with Slack, enabling seamless interaction between Factory and your Slack conversations.

## Prerequisites

- A Factory account with admin privileges
- Admin access to your Slack workspace
- Ability to install apps in your Slack workspace

## Integration Steps

## Verification

To ensure the integration is working correctly:

1. Mention `@Factory` in a thread within a channel where the app has been added.
2. Verify that Factory responds with a link to open the conversation in Factory.
3. Click the link and confirm that the Slack thread content appears in your new Factory session.

Factory provides four native tools to interact with Slack:

ToolWhat it does**Get Slack Channels**Lists all channels the bot can access**Post Slack Message**Sends a message to a channel or replies to an existing thread**Read Thread Messages**Reads the messages from a Slack thread**Get Channel History**Retrieves recent messages from a channel

## Additional Features

Besides the tools above, the Slack integration also allows you to:

- Mention `@Factory` in any Slack thread to receive a link to continue the conversation in Factory
- Import Slack thread context into Factory by clicking the provided link
- Reference Slack threads in Factory by pasting a thread URL into a Factory chat

When a Slack thread is imported, Factory has access to the entire conversation history, allowing it to provide context-aware assistance.

## Best Practices

- Add the Factory app only to channels where development discussions occur.
- Use threads rather than channel messages when mentioning Factory.
- Provide sufficient context in the Slack thread before mentioning Factory.
- Regularly review the permissions granted to the Factory app in your Slack settings.

## Troubleshooting

If you encounter issues during integration:

- Ensure you have admin rights in both Factory and your Slack workspace.
- Verify that the Factory app has been added to the channel where you’re mentioning it.
- If you see a “not\_in\_channel” error toast when trying to paste a Slack thread URL, it means the Factory bot needs to be invited to that channel. Use `/invite @Factory` in the channel to resolve this issue.
- Check that your organization’s firewall isn’t blocking webhook communications.
- For persistent issues, contact Factory support with specific error messages.

[**Security and Compliance**  
\
Learn about Factory’s security measures and how we protect your data](#)