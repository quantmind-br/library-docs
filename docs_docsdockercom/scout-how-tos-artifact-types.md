---
title: Use Scout with different artifact types
url: https://docs.docker.com/scout/how-tos/artifact-types/
source: llms
fetched_at: 2026-01-24T14:28:39.114851916-03:00
rendered_js: false
word_count: 428
summary: A guide on how to utilize Scout to analyze and manage various artifact types, such as container images and software packages.
tags:
    - Scout
    - artifacts
    - container security
    - software analysis
category: guide
---

Some of the Docker Scout CLI commands support prefixes for specifying the location or type of artifact that you would like to analyze.

By default, image analysis with the `docker scout cves` command targets images in the local image store of the Docker Engine. The following command always uses a local image if it exists:

If the image doesn't exist locally, Docker pulls the image before running the analysis. Analyzing the same image again would use the same local version by default, even if the tag has since changed in the registry.

By adding a `registry://` prefix to the image reference, you can force Docker Scout to analyze the registry version of the image:

The supported prefixes are:

PrefixDescription`image://` (default)Use a local image, or fall back to a registry lookup`local://`Use an image from the local image store (don't do a registry lookup)`registry://`Use an image from a registry (don't use a local image)`oci-dir://`Use an OCI layout directory`archive://`Use a tarball archive, as created by `docker save``fs://`Use a local directory or file

You can use prefixes with the following commands:

- `docker scout compare`
- `docker scout cves`
- `docker scout quickview`
- `docker scout recommendations`
- `docker scout sbom`

This section contains a few examples showing how you can use prefixes to specify artifacts for `docker scout` commands.

### [Analyze a local project](#analyze-a-local-project)

The `fs://` prefix lets you analyze local source code directly, without having to build it into a container image. The following `docker scout quickview` command gives you an at-a-glance vulnerability summary of the source code in the current working directory:

To view the details of vulnerabilities found in your local source code, you can use the `docker scout cves --details fs://.` command. Combine it with other flags to narrow down the results to the packages and vulnerabilities that you're interested in.

### [Compare a local project to an image](#compare-a-local-project-to-an-image)

With `docker scout compare`, you can compare the analysis of source code on your local filesystem with the analysis of a container image. The following example compares local source code (`fs://.`) with a registry image `registry://docker/scout-cli:latest`. In this case, both the baseline and target for the comparison use prefixes.

The previous example is truncated for brevity.

### [View the SBOM of an image tarball](#view-the-sbom-of-an-image-tarball)

The following example shows how you can use the `archive://` prefix to get the SBOM of an image tarball, created with `docker save`. The image in this case is `docker/scout-cli:latest`, and the SBOM is exported to file `sbom.spdx.json` in SPDX format.

Read about the commands and supported flags in the CLI reference documentation:

- [`docker scout quickview`](https://docs.docker.com/reference/cli/docker/scout/quickview/)
- [`docker scout cves`](https://docs.docker.com/reference/cli/docker/scout/cves/)
- [`docker scout compare`](https://docs.docker.com/reference/cli/docker/scout/compare/)