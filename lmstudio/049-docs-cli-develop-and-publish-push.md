---
title: '`lms push` (Beta)'
url: https://lmstudio.ai/docs/cli/develop-and-publish/push
source: sitemap
fetched_at: 2026-04-07T21:27:57.744710152-03:00
rendered_js: false
word_count: 117
summary: This document explains the command-line process and various flags required to publish a new revision of a plugin, preset, or model configuration within the LMS ecosystem.
tags:
    - lms-publish
    - cli-command
    - plugin-deployment
    - model-yaml
    - revision-management
category: guide
---

Run `lms push` from inside a [plugin](https://lmstudio.ai/docs/typescript/plugins), [preset](https://lmstudio.ai/docs/app/presets), or [`model.yaml`](https://lmstudio.ai/docs/app/modelyaml) project to publish a new revision. If a `model.yaml` exists, the CLI will generate a `manifest.json` for you before pushing.

For plugins, the CLI will ask for confirmation unless you pass `-y`.

### Publish the current folder[](#publish-the-current-folder)


### Flags[](#flags)

--description (optional) : string

Override the artifact description for this push

--overrides (optional) : string

JSON string to override manifest fields (parsed with JSON.parse)

-y, --yes (optional) : flag

Suppress confirmations and warnings

--private (optional) : flag

Mark the artifact as private when first published

--write-revision (optional) : flag

Write the returned revision number to manifest.json

### Advanced[](#advanced)

#### Publish quietly and keep the revision in manifest.json

```

lms push -y --write-revision
```

#### Override metadata for this upload

```

lms push --description "New beta build" --overrides '{"tags": ["beta"]}'
```