---
title: Slack
url: https://docs.docker.com/scout/integrations/team-collaboration/slack/
source: llms
fetched_at: 2026-01-24T14:29:19.944989415-03:00
rendered_js: false
word_count: 357
summary: This document provides instructions for integrating Docker Scout with Slack to receive real-time notifications regarding image vulnerabilities and policy compliance updates.
tags:
    - docker-scout
    - slack-integration
    - webhooks
    - vulnerability-scanning
    - notifications
    - container-security
category: guide
---

## Integrate Docker Scout with Slack

You can integrate Docker Scout with Slack by creating a Slack webhook and adding it to the Docker Scout Dashboard. Docker Scout will notify you about when a new vulnerability is disclosed, and it affects one or more of your images.

![Slack notification from Docker Scout](https://docs.docker.com/scout/images/scout-slack-notification.png)

Example Slack notification from Docker Scout

![Slack notification from Docker Scout](https://docs.docker.com/scout/images/scout-slack-notification.png)

## [How it works](#how-it-works)

After configuring the integration, Docker Scout sends notifications about changes to policy compliance and vulnerability exposure for your repositories, to the Slack channels associated with the webhook.

> Note
> 
> Notifications are only triggered for the *last pushed* image tags for each repository. "Last pushed" refers to the image tag that was most recently pushed to the registry and analyzed by Docker Scout. If the last pushed image is not by a newly disclosed CVE, then no notification will be triggered.

For more information about Docker Scout notifications, see [Notification settings](https://docs.docker.com/scout/explore/dashboard/#notification-settings)

## [Setup](#setup)

To add a Slack integration:

1. Create a webhook, see [Slack documentation](https://api.slack.com/messaging/webhooks).
2. Go to the [Slack integration page](https://scout.docker.com/settings/integrations/slack/) in the Docker Scout Dashboard.
3. In the **How to integrate** section, enter a **Configuration name**. Docker Scout uses this label as a display name for the integration, so you might want to change the default name into something more meaningful. For example the `#channel-name`, or the name of the team that this configuration belongs to.
4. Paste the webhook you just created in the **Slack webhook** field.
   
   Select the **Test webhook** button if you wish to verify the connection. Docker Scout will send a test message to the specified webhook.
5. Select whether you want to enable notifications for all your Scout-enabled image repositories, or enter the names of the repositories that you want to send notifications for.
6. When you're ready to enable the integration, select **Create**.

After creating the webhook, Docker Scout begins to send notifications updates to the Slack channels associated with the webhook.

## [Remove a Slack integration](#remove-a-slack-integration)

To remove a Slack integration:

1. Go to the [Slack integration page](https://scout.docker.com/settings/integrations/slack/) in the Docker Scout Dashboard.
2. Select the **Remove** icon for the integration that you want to remove.
3. Confirm by selecting **Remove** again in the confirmation dialog.