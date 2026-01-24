---
title: Configuration Import & Export · Cloudflare Zaraz docs
url: https://developers.cloudflare.com/zaraz/advanced/import-export/index.md
source: llms
fetched_at: 2026-01-24T15:34:35.790178888-03:00
rendered_js: false
word_count: 133
summary: This document provides step-by-step instructions on how to export and import Zaraz configurations using the Cloudflare dashboard for backups or site migrations.
tags:
    - zaraz
    - cloudflare
    - configuration-management
    - backup
    - import-export
    - data-migration
category: guide
---

Exporting your Zaraz configuration can be useful if you want to create a local backup or if you need to import it to another website. Zaraz provides an easy way to export and import your configuration.

## Export your Zaraz configuration

To export your Zaraz configuration:

1. In the Cloudflare dashboard, go to the **Settings** page.

   [Go to **Settings**](https://dash.cloudflare.com/?to=/:account/tag-management/settings)

2. Go to **Advanced**.

3. Click "Export" to download your configuration.

## Import your Zaraz configuration

Warning

Importing a Zaraz configuration replaces your existing configuration, meaning that any information you did not back up could be lost. Consider exporting your existing configuration before importing a new one.

To import a Zaraz configuration:

1. In the Cloudflare dashboard, go to the **Settings** page.

   [Go to **Settings**](https://dash.cloudflare.com/?to=/:account/tag-management/settings)

2. Go to **Advanced**.

3. Click **Browse** to select your configuration file, and **Import** to import it.