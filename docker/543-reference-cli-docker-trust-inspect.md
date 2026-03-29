---
title: docker trust inspect
url: https://docs.docker.com/reference/cli/docker/trust/inspect/
source: llms
fetched_at: 2026-01-24T14:41:38.161315323-03:00
rendered_js: false
word_count: 404
summary: This document explains how to use the docker trust inspect command to retrieve low-level signature and key information for signed Docker image repositories.
tags:
    - docker-cli
    - docker-trust
    - content-trust
    - image-signing
    - security-metadata
category: reference
---

DescriptionReturn low-level information about keys and signaturesUsage`docker trust inspect IMAGE[:TAG] [IMAGE[:TAG]...]`

`docker trust inspect` provides low-level JSON information on signed repositories. This includes all image tags that are signed, who signed them, and who can sign new tags.

OptionDefaultDescription`--pretty`Print the information in a human friendly format

### [Get low-level details about signatures for a single image tag](#get-low-level-details-about-signatures-for-a-single-image-tag)

Use the `docker trust inspect` to get trust information about an image. The following example prints trust information for the `alpine:latest` image:

The output is in JSON format, for example:

The `SignedTags` key will list the `SignedTag` name, its `Digest`, and the `Signers` responsible for the signature.

`AdministrativeKeys` will list the `Repository` and `Root` keys.

If signers are set up for the repository via other `docker trust` commands, `docker trust inspect` includes a `Signers` key:

The output is in JSON format, for example:

If the image tag is unsigned or unavailable, `docker trust inspect` does not display any signed tags.

However, if other tags are signed in the same image repository, `docker trust inspect` reports relevant key information:

The output is in JSON format, for example:

### [Get details about signatures for all image tags in a repository](#get-details-about-signatures-for-all-image-tags-in-a-repository)

If no tag is specified, `docker trust inspect` will report details for all signed tags in the repository:

The output is in JSON format, for example:

### [Get details about signatures for multiple images](#get-details-about-signatures-for-multiple-images)

`docker trust inspect` can take multiple repositories and images as arguments, and reports the results in an ordered list:

The output is in JSON format, for example:

### [Formatting](#formatting)

You can print the inspect output in a human-readable format instead of the default JSON output, by using the `--pretty` option:

### [Get details about signatures for a single image tag](#get-details-about-signatures-for-a-single-image-tag)

The `SIGNED TAG` is the signed image tag with a unique content-addressable `DIGEST`. `SIGNERS` lists all entities who have signed.

The administrative keys listed specify the root key of trust, as well as the administrative repository key. These keys are responsible for modifying signers, and rotating keys for the signed repository.

If signers are set up for the repository via other `docker trust` commands, `docker trust inspect --pretty` displays them appropriately as a `SIGNER` and specify their `KEYS`:

However, if other tags are signed in the same image repository, `docker trust inspect` reports relevant key information.

### [Get details about signatures for all image tags in a repository](#get-details-about-signatures-for-all-image-tags-in-a-repository-1)

Here's an example with signers that are set up by `docker trust` commands: