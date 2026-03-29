---
title: Create an action · Cloudflare Zaraz docs
url: https://developers.cloudflare.com/zaraz/custom-actions/create-action/index.md
source: llms
fetched_at: 2026-01-24T15:34:46.240590984-03:00
rendered_js: false
word_count: 188
summary: This document provides step-by-step instructions for creating and configuring actions within Cloudflare Zaraz to perform specific tasks based on predefined triggers.
tags:
    - cloudflare-zaraz
    - custom-actions
    - tag-management
    - event-triggers
    - third-party-tools
category: guide
---

Once you have your triggers ready, you can use them to configure your actions. An action defines a specific task that your tool will perform.

To create an action, first [add a third-party tool](https://developers.cloudflare.com/zaraz/get-started/). If you have already added a third-party tool, follow these steps to create an action.

1. In the Cloudflare dashboard, go to the **Tag setup** page.

   [Go to **Tag setup**](https://dash.cloudflare.com/?to=/:account/tag-management/zaraz)

2. Go to **Tools Configuration**.

3. Under **Third-party tools**, locate the tool you want to configure an action for, and select **Edit**.

4. Under Custom actions select **Create action**.

5. Give the action a descriptive name.

6. In the **Firing Triggers** field, choose the relevant trigger or triggers you [previously created](https://developers.cloudflare.com/zaraz/custom-actions/create-trigger/). If you choose more than one trigger, the action will start when any of the selected triggers are matched.

7. Depending on the tool you are adding an action for, you might also have the option to choose an **Action type**. You might also need to fill in more fields in order to complete setting up the action.

8. Select **Save**.

The new action will appear under **Tool actions**. To edit or disable/enable an action, refer to [Edit tools and actions](https://developers.cloudflare.com/zaraz/custom-actions/edit-tools-and-actions/).