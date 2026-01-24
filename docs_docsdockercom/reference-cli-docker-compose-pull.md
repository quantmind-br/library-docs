---
title: docker compose pull
url: https://docs.docker.com/reference/cli/docker/compose/pull/
source: llms
fetched_at: 2026-01-24T14:34:22.357686893-03:00
rendered_js: false
word_count: 143
summary: This document explains how to use the docker compose pull command to download service images defined in a configuration file without starting the containers.
tags:
    - docker-compose
    - cli-reference
    - image-management
    - container-images
    - docker-cli
category: reference
---

DescriptionPull service imagesUsage`docker compose pull [OPTIONS] [SERVICE...]`

## [Description](#description)

Pulls an image associated with a service defined in a `compose.yaml` file, but does not start containers based on those images

## [Options](#options)

OptionDefaultDescription`--ignore-buildable`Ignore images that can be built`--ignore-pull-failures`Pull what it can and ignores images with pull failures`--include-deps`Also pull services declared as dependencies`--policy`Apply pull policy ("missing"|"always")`-q, --quiet`Pull without printing progress information

## [Examples](#examples)

Consider the following `compose.yaml`:

```
services:db:image:postgresweb:build:.command:bundle exec rails s -p 3000 -b '0.0.0.0'volumes:- .:/myappports:- "3000:3000"depends_on:- db
```

If you run `docker compose pull ServiceName` in the same directory as the `compose.yaml` file that defines the service, Docker pulls the associated image. For example, to call the postgres image configured as the db service in our example, you would run `docker compose pull db`.

```
$ docker compose pull db
[+] Running 1/15
 ⠸ db Pulling                                                             12.4s
   ⠿ 45b42c59be33 Already exists                                           0.0s
   ⠹ 40adec129f1a Downloading  3.374MB/4.178MB                             9.3s
   ⠹ b4c431d00c78 Download complete                                        9.3s
   ⠹ 2696974e2815 Download complete                                        9.3s
   ⠹ 564b77596399 Downloading  5.622MB/7.965MB                             9.3s
   ⠹ 5044045cf6f2 Downloading  216.7kB/391.1kB                             9.3s
   ⠹ d736e67e6ac3 Waiting                                                  9.3s
   ⠹ 390c1c9a5ae4 Waiting                                                  9.3s
   ⠹ c0e62f172284 Waiting                                                  9.3s
   ⠹ ebcdc659c5bf Waiting                                                  9.3s
   ⠹ 29be22cb3acc Waiting                                                  9.3s
   ⠹ f63c47038e66 Waiting                                                  9.3s
   ⠹ 77a0c198cde5 Waiting                                                  9.3s
   ⠹ c8752d5b785c Waiting                                                  9.3s
```

`docker compose pull` tries to pull image for services with a build section. If pull fails, it lets you know this service image must be built. You can skip this by setting `--ignore-buildable` flag.