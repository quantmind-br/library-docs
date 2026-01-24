---
title: docker buildx debug build
url: https://docs.docker.com/reference/cli/docker/buildx/debug/build/
source: llms
fetched_at: 2026-01-24T14:32:59.377050339-03:00
rendered_js: false
word_count: 185
summary: This document provides a comprehensive reference of command-line options and flags used for building container images, covering aspects such as caching, networking, and metadata.
tags:
    - docker-build
    - cli-reference
    - container-images
    - build-options
    - image-metadata
category: reference
---

OptionDefaultDescription`--add-host`Add a custom host-to-IP mapping (format: `host:ip`)`--allow`Allow extra privileged entitlement (e.g., `network.host`, `security.insecure`, `device`)  
`--annotation`Add annotation to the image`--attest`Attestation parameters (format: `type=sbom,generator=image`)`--build-arg`Set build-time variables`--build-context`Additional build contexts (e.g., name=path)`--cache-from`External cache sources (e.g., `user/app:cache`, `type=local,src=path/to/dir`)  
`--cache-to`Cache export destinations (e.g., `user/app:cache`, `type=local,dest=path/to/dir`)  
`--call``build`Set method for evaluating build (`check`, `outline`, `targets`)`--cgroup-parent`Set the parent cgroup for the `RUN` instructions during build`--check`Shorthand for `--call=check``-f, --file`Name of the Dockerfile (default: `PATH/Dockerfile`)`--iidfile`Write the image ID to a file`--label`Set metadata for an image`--load`Shorthand for `--output=type=docker``--metadata-file`Write build result metadata to a file`--network`Set the networking mode for the `RUN` instructions during build`--no-cache`Do not use cache when building the image`--no-cache-filter`Do not cache specified stages`-o, --output`Output destination (format: `type=local,dest=path`)`--platform`Set target platform for build`--progress``auto`Set type of progress output (`auto`, `none`, `plain`, `quiet`, `rawjson`, `tty`). Use plain to show container output  
`--provenance`Shorthand for `--attest=type=provenance``--pull`Always attempt to pull all referenced images`--push`Shorthand for `--output=type=registry``-q, --quiet`Suppress the build output and print image ID on success`--sbom`Shorthand for `--attest=type=sbom``--secret`Secret to expose to the build (format: `id=mysecret[,src=/local/secret]`)  
`--shm-size`Shared memory size for build containers`--ssh`SSH agent socket or keys to expose to the build (format: `default|<id>[=<socket>|<key>[,<key>]]`)  
`-t, --tag`Image identifier (format: `[registry/]repository[:tag]`)`--target`Set the target build stage to build`--ulimit`Ulimit options