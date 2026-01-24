---
title: Common challenges and questions
url: https://docs.docker.com/guides/docker-scout/common-questions/
source: llms
fetched_at: 2026-01-24T14:09:24.391060771-03:00
rendered_js: false
word_count: 385
summary: This document provides answers to common questions about Docker Scout, covering its security capabilities, installation methods, and integration with various container registries.
tags:
    - docker-scout
    - container-security
    - sbom
    - software-supply-chain
    - vulnerability-management
    - container-registry
category: reference
---

Table of contents

* * *

### [How is Docker Scout different from other security tools?](#how-is-docker-scout-different-from-other-security-tools)

Docker Scout takes a broader approach to container security compared to third-party security tools. Third-party security tools, if they offer remediation guidance at all, miss the mark on their limited scope of application security posture within the software supply chain, and often limited guidance when it comes to suggested fixes. Such tools have either limitations on runtime monitoring or no runtime protection at all. When they do offer runtime monitoring, it’s limited in its adherence to key policies. Third-party security tools offer a limited scope of policy evaluation for Docker-specific builds. By focusing on the entire software supply chain, providing actionable guidance, and offering comprehensive runtime protection with strong policy enforcement, Docker Scout goes beyond just identifying vulnerabilities in your containers. It helps you build secure applications from the ground up.

### [Can I use Docker Scout with external registries other than Docker Hub?](#can-i-use-docker-scout-with-external-registries-other-than-docker-hub)

You can use Scout with registries other than Docker Hub. Integrating Docker Scout with third-party container registries enables Docker Scout to run image analysis on those repositories so that you can get insights into the composition of those images even if they aren't hosted on Docker Hub.

The following container registry integrations are available:

- Artifactory
- Amazon Elastic Container Registry
- Azure Container Registry

Learn more about configuring Scout with your registries in [Integrating Docker Scout with third-party registries](https://docs.docker.com/scout/integrations/#container-registries).

### [Does Docker Scout CLI come by default with Docker Desktop?](#does-docker-scout-cli-come-by-default-with-docker-desktop)

Yes, the Docker Scout CLI plugin comes pre-installed with Docker Desktop.

### [Is it possible to run `docker scout` commands on a Linux system without Docker Desktop?](#is-it-possible-to-run-docker-scout-commands-on-a-linux-system-without-docker-desktop)

If you run Docker Engine without Docker Desktop, Docker Scout doesn't come pre-installed, but you can [install it as a standalone binary](https://docs.docker.com/scout/install/).

### [How is Docker Scout using an SBOM?](#how-is-docker-scout-using-an-sbom)

An SBOM, or software bill of materials, is a list of ingredients that make up software components. [Docker Scout uses SBOMs](https://docs.docker.com/scout/concepts/sbom/) to determine the components that are used in a Docker image. When you analyze an image, Docker Scout will either use the SBOM that is attached to the image (as an attestation), or generate an SBOM on the fly by analyzing the contents of the image.

The SBOM is cross-referenced with the advisory database to determine if any of the components in the image have known vulnerabilities.