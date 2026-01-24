---
title: Merge
url: https://docs.docker.com/reference/compose-file/merge/
source: llms
fetched_at: 2026-01-24T14:42:21.342836742-03:00
rendered_js: false
word_count: 453
summary: This document explains the technical rules and mechanisms for merging multiple Docker Compose files into a single application model, including handling of mappings, sequences, and unique resources.
tags:
    - docker-compose
    - yaml-merging
    - compose-specification
    - configuration-management
    - container-orchestration
    - resource-overrides
category: reference
---

## Merge Compose files

Compose lets you define a Compose application model through multiple Compose files. When doing so, Compose follows certain rules to merge Compose files.

These rules are outlined below.

A YAML `mapping` gets merged by adding missing entries and merging the conflicting ones.

Merging the following example YAML trees:

Results in a Compose application model equivalent to the YAML tree:

A YAML `sequence` is merged by appending values from the overriding Compose file to the previous one.

Merging the following example YAML trees:

Results in a Compose application model equivalent to the YAML tree:

### [Shell commands](#shell-commands)

When merging Compose files that use the services attributes [command](https://docs.docker.com/reference/compose-file/services/#command), [entrypoint](https://docs.docker.com/reference/compose-file/services/#entrypoint) and [healthcheck: `test`](https://docs.docker.com/reference/compose-file/services/#healthcheck), the value is overridden by the latest Compose file, and not appended.

Merging the following example YAML trees:

Results in a Compose application model equivalent to the YAML tree:

### [Unique resources](#unique-resources)

Applies to the [ports](https://docs.docker.com/reference/compose-file/services/#ports), [volumes](https://docs.docker.com/reference/compose-file/services/#volumes), [secrets](https://docs.docker.com/reference/compose-file/services/#secrets) and [configs](https://docs.docker.com/reference/compose-file/services/#configs) services attributes. While these types are modeled in a Compose file as a sequence, they have special uniqueness requirements:

AttributeUnique keyvolumestargetsecretstargetconfigstargetports{ip, target, published, protocol}

When merging Compose files, Compose appends new entries that do not violate a uniqueness constraint and merge entries that share a unique key.

Merging the following example YAML trees:

Results in a Compose application model equivalent to the YAML tree:

### [Reset value](#reset-value)

In addition to the previously described mechanism, an override Compose file can also be used to remove elements from your application model. For this purpose, the custom [YAML tag](https://yaml.org/spec/1.2.2/#24-tags) `!reset` can be set to override a value set by the overridden Compose file. A valid value for attribute must be provided, but will be ignored and target attribute will be set with type's default value or `null`.

For readability, it is recommended to explicitly set the attribute value to the null (`null`) or empty array `[]` (with `!reset null` or `!reset []`) so that it is clear that resulting attribute will be cleared.

A base `compose.yaml` file:

And a `compose.override.yaml` file:

Results in:

### [Replace value](#replace-value)

Requires: Docker Compose [2.24.4](https://github.com/docker/compose/releases/tag/v2.24.4) and later

While `!reset` can be used to remove a declaration from a Compose file using an override file, `!override` allows you to fully replace an attribute, bypassing the standard merge rules. A typical example is to fully replace a resource definition, to rely on a distinct model but using the same name.

A base `compose.yaml` file:

To remove the original port, but expose a new one, the following override file is used:

This results in:

If `!override` had not been used, both `8080:80` and `8443:443` would be exposed as per the [merging rules outlined above](#sequence).

For more information on how merge can be used to create a composite Compose file, see [Working with multiple Compose files](https://docs.docker.com/compose/how-tos/multiple-compose-files/)