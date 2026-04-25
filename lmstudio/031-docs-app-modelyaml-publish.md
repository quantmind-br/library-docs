---
title: Publish a `model.yaml`
url: https://lmstudio.ai/docs/app/modelyaml/publish
source: sitemap
fetched_at: 2026-04-07T21:29:19.672068813-03:00
rendered_js: false
word_count: 273
summary: This document guides users through the process of sharing portable language models by uploading a metadata file to the LM Studio Hub, detailing steps like cloning existing models, updating publisher information, authenticating via CLI, and finally publishing the model.
tags:
    - lm-studio-hub
    - model-publishing
    - metadata
    - command-line
    - model-sharing
category: guide
---

Share portable models by uploading a [`model.yaml`](https://lmstudio.ai/docs/app/modelyaml/) to your page on the LM Studio Hub.

After you publish a model.yaml to the LM Studio Hub, it will be available for other users to download with `lms get`.

###### Note: `model.yaml` refers to metadata only. This means it does not include the actual model weights.

## Quickstart[](#quickstart)

The easiest way to get started is by cloning an existing model, modifying it, and then running `lms push`.

For example, you can clone the Qwen 3 8B model:


This will result in a local copy `model.yaml`, `README` and other metadata files. Importantly, this does NOT download the model weights.

## Change the publisher to your user[](#change-the-publisher-to-your-user "Link to 'Change the publisher to your user'")

The first part in the `model:` field should be the username of the publisher. Change it to a username of a user or organization for which you have write access.

```

- model: qwen/qwen3-8b
+ model: your-user-here/qwen3-8b
base:
  - key: lmstudio-community/qwen3-8b-gguf
    sources:
# ... the rest of the file
```

## Sign in[](#sign-in "Link to 'Sign in'")

Authenticate with the Hub from the command line:


The CLI will print an authentication URL. After you approve access, the session token is saved locally so you can publish models.

## Publish your model[](#publish-your-model "Link to 'Publish your model'")

Run the push command in the directory containing `model.yaml`:


The command packages the file, uploads it, and prints a revision number for the new version.

### Override metadata at publish time[](#override-metadata-at-publish-time)

Use `--overrides` to tweak fields without editing the file:

```

lms push --overrides '{"description": "Qwen 3 8B model"}'
```

## Downloading a model and using it in LM Studio[](#downloading-a-model-and-using-it-in-lm-studio "Link to 'Downloading a model and using it in LM Studio'")

After publishing, the model appears under your user or organization profile on the LM Studio Hub.

It can then be downloaded with: