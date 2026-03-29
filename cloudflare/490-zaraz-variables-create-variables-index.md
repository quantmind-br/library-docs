---
title: Create a variable · Cloudflare Zaraz docs
url: https://developers.cloudflare.com/zaraz/variables/create-variables/index.md
source: llms
fetched_at: 2026-01-24T15:34:57.087938221-03:00
rendered_js: false
word_count: 224
summary: This document explains how to create and manage reusable variables in Cloudflare Zaraz to streamline data updates across tools and triggers. It covers the different variable types available, including string, masked, and worker variables.
tags:
    - cloudflare-zaraz
    - variables
    - tag-management
    - configuration-guide
    - data-reuse
category: configuration
---

Variables are reusable blocks of information. They allow you to have one source of data you can reuse across tools and triggers in the dashboard. You can then update this data in a single place.

For example, instead of typing a specific user ID in multiple fields, you can create a variable with that information instead. If there is a change and you have to update the user ID, you just need to update the variable and the change will be reflected across the dashboard.

[Worker Variables](https://developers.cloudflare.com/zaraz/variables/worker-variables/) are a special type of variable that generates value dynamically.

## Create a new variable

1. In the Cloudflare dashboard, go to the **Tag setup** page.

   [Go to **Tag setup**](https://dash.cloudflare.com/?to=/:account/tag-management/zaraz)

2. Go to **Tools Configuration** > **Variables**.

3. Select **Create variable**, and give it a name.

4. In **Variable type** select between `String`, `Masked variable` or `Worker` from the drop-down menu. Use `Masked variable` when you have a private value that you do not want to share, such as an API token.

5. In **Variable value** enter the value of your variable.

6. Select **Save**.

Your variable is now ready to be used with tools and triggers.

## Next steps

Refer to [Add a third-party tool](https://developers.cloudflare.com/zaraz/get-started/) and [Create a trigger](https://developers.cloudflare.com/zaraz/custom-actions/create-trigger/) for more information on how to add a variable to tools and triggers.

If you need to edit or delete variables, refer to [Edit variables](https://developers.cloudflare.com/zaraz/variables/edit-variables/).