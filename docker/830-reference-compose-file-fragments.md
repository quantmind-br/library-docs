---
title: Fragments
url: https://docs.docker.com/reference/compose-file/fragments/
source: llms
fetched_at: 2026-01-24T14:42:16.500100074-03:00
rendered_js: false
word_count: 275
summary: This document explains how to use YAML anchors, aliases, and merge keys in Docker Compose to create reusable configuration blocks and reduce duplication. It demonstrates how these features simplify service and volume definitions while maintaining cleaner and more maintainable Compose files.
tags:
    - docker-compose
    - yaml-anchors
    - yaml-aliases
    - configuration-management
    - dry-principle
    - compose-specification
category: guide
---

With Compose, you can use built-in [YAML](https://www.yaml.org/spec/1.2/spec.html#id2765878) features to make your Compose file neater and more efficient. Anchors and aliases let you create re-usable blocks. This is useful if you start to find common configurations that span multiple services. Having re-usable blocks minimizes potential mistakes.

Anchors are created using the `&` sign. The sign is followed by an alias name. You can use this alias with the `*` sign later to reference the value following the anchor. Make sure there is no space between the `&` and the `*` characters and the following alias name.

You can use more than one anchor and alias in a single Compose file.

## [Example 1](#example-1)

```
volumes:db-data:&default-volumedriver:defaultmetrics:*default-volume
```

In the example above, a `default-volume` anchor is created based on the `db-data` volume. It is later reused by the alias `*default-volume` to define the `metrics` volume.

Anchor resolution takes place before [variables interpolation](https://docs.docker.com/reference/compose-file/interpolation/), so variables can't be used to set anchors or aliases.

## [Example 2](#example-2)

```
services:first:image:my-image:latestenvironment:&env- CONFIG_KEY- EXAMPLE_KEY- DEMO_VARsecond:image:another-image:latestenvironment:*env
```

If you have an anchor that you want to use in more than one service, use it in conjunction with an [extension](https://docs.docker.com/reference/compose-file/extension/) to make your Compose file easier to maintain.

## [Example 3](#example-3)

You may want to partially override values. Compose follows the rule outlined by [YAML merge type](https://yaml.org/type/merge.html).

In the following example, `metrics` volume specification uses alias to avoid repetition but overrides `name` attribute:

```
services:backend:image:example/databasevolumes:- db-data- metricsvolumes:db-data:&default-volumedriver:defaultname:"data"metrics:<<:*default-volumename:"metrics"
```

## [Example 4](#example-4)

You can also extend the anchor to add additional values.

```
services:first:image:my-image:latestenvironment:&envFOO:BARZOT:QUIXsecond:image:another-image:latestenvironment:<<:*envYET_ANOTHER:VARIABLE
```

> Note
> 
> [YAML merge](https://yaml.org/type/merge.html) only applies to mappings, and can't be used with sequences.

In example above, the environment variables must be declared using the `FOO: BAR` mapping syntax, while the sequence syntax `- FOO=BAR` is only valid when no fragments are involved.