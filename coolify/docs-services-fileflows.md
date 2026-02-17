---
title: FileFlows
url: https://coolify.io/docs/services/fileflows.md
source: llms
fetched_at: 2026-02-17T14:43:56.351852-03:00
rendered_js: false
word_count: 69
summary: This document introduces FileFlows, an automated file processing application, and provides basic installation instructions including configuration for hardware transcoding in a Coolify environment.
tags:
    - file-automation
    - fileflows
    - coolify
    - installation-guide
    - hardware-transcoding
    - media-processing
category: guide
---

## What is FileFlows?

Are you tired of manually managing your files? Meet FileFlows — the ultimate solution for automatic file processing!

FileFlows lets you monitor and process any file type with custom flows. Videos, audio, images, archives, comics, eBooks—you name it!

## Installation

1. Create the service within Coolify.
2. If your device supports it, enable hardware transcoding by uncommenting this section in the compose file:

```yaml
#devices:
# - "/dev/dri:/dev/dri"
```

## Screenshots

## Links

* [The official website](https://fileflows.com/)
* [Doc](https://fileflows.com/docs)