---
title: Preview changes before publishing · Cloudflare Zaraz docs
url: https://developers.cloudflare.com/zaraz/history/preview-mode/index.md
source: llms
fetched_at: 2026-01-24T15:34:52.353536159-03:00
rendered_js: false
word_count: 344
summary: This document explains how to enable and use the Preview & Publish workflow in Cloudflare Zaraz to test configuration changes before they go live. It provides step-by-step instructions for activating preview mode, testing with a debug key, and publishing or reverting changes.
tags:
    - cloudflare-zaraz
    - preview-mode
    - debugging
    - workflow-management
    - configuration-testing
category: guide
---

Zaraz allows you to test your configurations before publishing them. This is helpful to avoid unintended consequences when deploying a new tool or trigger.

After enabling Preview & Publish you will also have access to [Zaraz History](https://developers.cloudflare.com/zaraz/history/versions/).

## Enable Preview & Publish mode

By default, Zaraz is configured to commit changes in real time. To enable preview mode and test new features you are adding to Zaraz:

1. In the Cloudflare dashboard, go to the **History** page.

   [Go to **History**](https://dash.cloudflare.com/?to=/:account/tag-management/history)

2. Enable **Preview & Publish Workflow**.

You are now working in preview mode. To commit changes and make them live, you will have to select **Publish** on your account.

### Test changes before publishing them

Now that you have Zaraz working in preview mode, you can open your website and test your settings:

1. In the Cloudflare dashboard, go to the **Settings** page.

   [Go to **Settings**](https://dash.cloudflare.com/?to=/:account/tag-management/settings)

2. Navigate to the website where you want to test your new settings.

3. Access the browser’s developer tools. For example, to access developer tools in Google Chrome, select **View** > **Developer** > **Developer Tools**.

4. Select the **Console** pane and enter the following command to start Zaraz’s preview mode:

   ```js
   zaraz.preview("<YOUR_DEBUG_KEY>");
   ```

5. Your website will reload along with Zaraz debugger, and Zaraz will use the most recent changes in preview mode.

6. If you are satisfied with your changes, go back to the dashboard and select **Publish** to apply them to all users. If not, use the dashboard to continue adjusting your configuration.

To exit preview mode, close Zaraz debugger.

## Disable Preview & Publish mode

Disable Preview & Publish mode to work in real time. When you work in real time, any changes made on the dashboard are applied instantly to the domain you are working on.

1. In the Cloudflare dashboard, go to the **History** page.

   [Go to **History**](https://dash.cloudflare.com/?to=/:account/tag-management/history)

2. Disable **Preview & Publish Workflow**.

3. In the modal, decide if you want to delete all unpublished changes, or if you want to publish any change made in the meantime.

Zaraz is now working in real time. Any change you make will be immediately applied the domain you are working on.