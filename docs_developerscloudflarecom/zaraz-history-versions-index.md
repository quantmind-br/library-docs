---
title: Versions · Cloudflare Zaraz docs
url: https://developers.cloudflare.com/zaraz/history/versions/index.md
source: llms
fetched_at: 2026-01-24T15:34:53.291217139-03:00
rendered_js: false
word_count: 163
summary: This document explains how to track, manage, and revert configuration changes in Cloudflare Zaraz using the Version History feature.
tags:
    - cloudflare-zaraz
    - version-history
    - configuration-management
    - rollback-changes
    - preview-mode
category: guide
---

Version History enables you to keep track of all the Zaraz configuration changes made in your website. With Version History you can also revert changes to previous settings should there be a problem.

To access Version History you need to enable [Preview & Publish mode](https://developers.cloudflare.com/zaraz/history/preview-mode/) first. Then, you can access Version History under **Zaraz** > **History**.

## Access Version History

1. In the Cloudflare dashboard, go to the **History** page.

   [Go to **History**](https://dash.cloudflare.com/?to=/:account/tag-management/history)

2. If this is your first time using this feature, this page will be empty. Otherwise, you will have a list of changes made to your account with the following information:

   * Date of change
   * User who made the change
   * Description of the change

## Revert changes

Version History enables you to revert any changes made to your Zaraz settings.

1. In the Cloudflare dashboard, go to the **History** page.

   [Go to **History**](https://dash.cloudflare.com/?to=/:account/tag-management/history)

2. Find the changes you want to revert, and select **Restore**.

3. Confirm you want to revert your changes.

4. Select **Publish** to publish your changes.