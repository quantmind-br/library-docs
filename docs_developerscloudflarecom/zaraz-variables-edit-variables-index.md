---
title: Edit a variable · Cloudflare Zaraz docs
url: https://developers.cloudflare.com/zaraz/variables/edit-variables/index.md
source: llms
fetched_at: 2026-01-24T15:34:55.216980192-03:00
rendered_js: false
word_count: 128
summary: This document provides step-by-step instructions for managing variables in Cloudflare Zaraz, specifically how to edit existing variables and the requirements for deleting them.
tags:
    - cloudflare-zaraz
    - variable-management
    - tag-setup
    - third-party-tools
    - trigger-configuration
category: guide
---

1. In the Cloudflare dashboard, go to the **Tag setup** page.

   [Go to **Tag setup**](https://dash.cloudflare.com/?to=/:account/tag-management/zaraz)

2. Go to **Tools Configuration** > **Variables**.

3. Locate the variable you want to edit, and select **Edit** to make your changes.

4. Select **Save** to save your edits.

## Delete a variable

Important

You cannot delete a variable being used in tools or triggers.

1. In the Cloudflare dashboard, go to the **Tag setup** page.

   [Go to **Tag setup**](https://dash.cloudflare.com/?to=/:account/tag-management/zaraz)

2. Go to **Tools Configuration** > **Third-party tools**.

3. Locate any tools using the variable, and delete the variable from those tools.

4. Select **Zaraz** > **Tools Configuration** > **Triggers**.

5. Locate all the triggers using the variable, and delete the variable from those triggers.

6. Navigate to **Zaraz** > **Tools Configuration** > **Variables**.

7. Locate the variable you want to delete, and select **Delete**.