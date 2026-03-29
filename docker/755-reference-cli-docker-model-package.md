---
title: docker model package
url: https://docs.docker.com/reference/cli/docker/model/package/
source: llms
fetched_at: 2026-01-24T14:38:25.420834705-03:00
rendered_js: false
word_count: 215
summary: Provides documentation for the `docker model package` command, detailing how to package GGUF, Safetensors, or existing models into Docker OCI artifacts.
tags:
    - docker-model
    - oci-artifact
    - gguf
    - safetensors
    - command-line-interface
    - model-management
category: reference
---

DescriptionPackage a GGUF file, Safetensors directory, or existing model into a Docker model OCI artifact.Usage`docker model package (--gguf <path> | --safetensors-dir <path> | --from <model>) [--license <path>...] [--context-size <tokens>] [--push] MODEL`

## [Description](#description)

Package a GGUF file, Safetensors directory, or existing model into a Docker model OCI artifact, with optional licenses. The package is sent to the model-runner, unless --push is specified. When packaging a sharded GGUF model, --gguf should point to the first shard. All shard files should be siblings and should include the index in the file name (e.g. model-00001-of-00015.gguf). When packaging a Safetensors model, --safetensors-dir should point to a directory containing .safetensors files and config files (\*.json, merges.txt). All files will be auto-discovered and config files will be packaged into a tar archive. When packaging from an existing model using --from, you can modify properties like context size to create a variant of the original model.

## [Options](#options)

OptionDefaultDescription`--chat-template`absolute path to chat template file (must be Jinja format)`--context-size`context size in tokens`--dir-tar`relative path to directory to package as tar (can be specified multiple times)  
`--from`reference to an existing model to repackage`--gguf`absolute path to gguf file`-l, --license`absolute path to a license file`--push`push to registry (if not set, the model is loaded into the Model Runner content store)  
`--safetensors-dir`absolute path to directory containing safetensors files and config