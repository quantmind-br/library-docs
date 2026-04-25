---
title: Importing and Sharing
url: https://lmstudio.ai/docs/app/presets/import
source: sitemap
fetched_at: 2026-04-07T21:29:23.274877746-03:00
rendered_js: false
word_count: 272
summary: This document explains various methods for importing presets into the application, detailing options to import from local files, external URLs, using the command line interface (CLI), and locating where shared presets are stored.
tags:
    - import-presets
    - preset-management
    - cli-usage
    - file-import
    - url-import
category: guide
---

You can import preset by file or URL. This is useful for sharing presets with others, or for importing presets from other users.

* * *

## Import Presets[](#import-presets)

First, click the presets dropdown in the sidebar. You will see a list of your presets along with 2 buttons: `+ New Preset` and `Import`.

Click the `Import` button to import a preset.

![undefined](https://lmstudio.ai/assets/docs/preset-import-button.png)

## Import Presets from File[](#import-presets-from-file "Link to 'Import Presets from File'")

Once you click the Import button, you can select the source of the preset you want to import. You can either import from a file or from a URL.

![undefined](https://lmstudio.ai/assets/docs/import-preset-from-file.png)

Import one or more Presets from file

## Import Presets from URL[](#import-presets-from-url "Link to 'Import Presets from URL'")

Presets that are [published](https://lmstudio.ai/docs/app/presets/publish) to the LM Studio Hub can be imported by providing their URL.

Importing public presets does not require logging in within LM Studio.

![undefined](https://lmstudio.ai/assets/docs/import-preset-from-url.png)

### Using `lms` CLI[](#using-lms-cli)

You can also use the CLI to import presets from URL. This is useful for sharing presets with others.

```

lms get {author}/{preset-name}
```

Example:

```

lms get neil/qwen3-thinking
```

### Find your config-presets directory[](#find-your-config-presets-directory)

LM Studio manages config presets on disk. Presets are local and private by default. You or others can choose to share them by sharing the file.

Click on the `•••` button in the Preset dropdown and select "Reveal in Finder" (or "Show in Explorer" on Windows).

![undefined](https://lmstudio.ai/assets/docs/preset-reveal-in-finder.png)

Reveal Preset in your local file system

This will download the preset file and automatically surface it in the preset dropdown in the app.

### Where Hub shared presets are stored[](#where-hub-shared-presets-are-stored)

Presets you share, and ones you download from the LM Studio Hub are saved in `~/.lmstudio/hub` on macOS and Linux, or `%USERPROFILE%\.lmstudio\hub` on Windows.