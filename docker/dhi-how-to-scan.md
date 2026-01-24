---
title: Scan an image
url: https://docs.docker.com/dhi/how-to/scan/
source: llms
fetched_at: 2026-01-24T14:21:00.122999514-03:00
rendered_js: false
word_count: 974
summary: This document provides instructions for scanning Docker Hardened Images for vulnerabilities using tools like Docker Scout, Grype, and Trivy, including guidance on CI/CD integration and VEX statement filtering.
tags:
    - docker-hardened-images
    - vulnerability-scanning
    - docker-scout
    - trivy
    - grype
    - vex-statements
    - ci-cd
    - security
category: guide
---

## Scan Docker Hardened Images

Docker Hardened Images (DHIs) are designed to be secure by default, but like any container image, it's important to scan them regularly as part of your vulnerability management process.

You can scan DHIs using the same tools you already use for standard images, such as Docker Scout, Grype, and Trivy. DHIs follow the same formats and standards for compatibility across your security tooling. Before you scan an image, the image must be mirrored into your organization on Docker Hub.

> When you have a Docker Hardened Images Enterprise subscription, [Docker Scout](https://docs.docker.com/scout/) is automatically enabled at no additional cost for all mirrored Docker Hardened Image repositories on Docker Hub. You can view scan results directly in the Docker Hub UI under your organization's repository.

> You must authenticate to the Docker Hardened Images registry (`dhi.io`) to pull images. Use your Docker ID credentials (the same username and password you use for Docker Hub) when signing in. If you don't have a Docker account, [create one](https://docs.docker.com/accounts/create-account/) for free.
> 
> Run `docker login dhi.io` to authenticate.

Docker Scout is integrated into Docker Desktop and the Docker CLI. It provides vulnerability insights, CVE summaries, and direct links to remediation guidance.

### [Scan a DHI using Docker Scout](#scan-a-dhi-using-docker-scout)

To scan a Docker Hardened Image using Docker Scout, run the following command:

Example output:

For more detailed filtering and JSON output, see [Docker Scout CLI reference](https://docs.docker.com/reference/cli/docker/scout/).

### [Automate DHI scanning in CI/CD with Docker Scout](#automate-dhi-scanning-in-cicd-with-docker-scout)

Integrating Docker Scout into your CI/CD pipeline enables you to automatically verify that images built from Docker Hardened Images remain free from known vulnerabilities during the build process. This proactive approach ensures the continued security integrity of your images throughout the development lifecycle.

#### [Example GitHub Actions workflow](#example-github-actions-workflow)

The following is a sample GitHub Actions workflow that builds an image and scans it using Docker Scout:

The `exit-code: true` parameter ensures that the workflow fails if any critical or high-severity vulnerabilities are detected, preventing the deployment of insecure images.

For more details on using Docker Scout in CI, see [Integrating Docker Scout with other systems](https://docs.docker.com/scout/integrations/).

### [Comparing Docker Scout results with other scanners](#comparing-docker-scout-results-with-other-scanners)

Some vulnerabilities reported by other scanners may not appear in Docker Scout results. This can happen for several reasons:

- Hardware-specific vulnerabilities: Certain vulnerabilities may only affect specific hardware architectures (for example, Power10 processors) that are not relevant to Docker images, so they are not reported by Docker Scout.
- VEX statement filtering: Docker Scout automatically applies VEX statements to document and suppress vulnerabilities that do not apply to the image. If your scanner does not consume VEX statements, you may see more vulnerabilities reported than what appears in Docker Scout results.
- Temporary vulnerability identifiers: Temporary vulnerability identifiers (like `TEMP-xxxxxxx` from Debian) are not surfaced by Docker Scout, as they are not intended for external reference.

While Docker Scout handles this filtering automatically, you can manually configure similar filtering with other scanners using [Grype ignore rules](https://github.com/anchore/grype#specifying-matches-to-ignore) in its configuration file (`~/.grype.yaml`) or [Trivy policy exceptions](https://trivy.dev/v0.19.2/misconfiguration/policy/exceptions/) using REGO rules to filter out specific vulnerabilities by CVE ID, package name, fix state, or other criteria. You can also use VEX statements with other scanners as described in [Use VEX to filter known non-exploitable CVEs](#use-vex-to-filter-known-non-exploitable-cves).

[Grype](https://github.com/anchore/grype) is an open-source scanner that checks container images against vulnerability databases like the NVD and distro advisories.

### [Scan a DHI using Grype](#scan-a-dhi-using-grype)

After installing Grype, you can scan a Docker Hardened Image by pulling the image and running the scan command:

Example output:

You should include the `--vex` flag to apply VEX statements during the scan, which filter out known non-exploitable CVEs. For more information, see the [VEX section](#use-vex-to-filter-known-non-exploitable-cves).

[Trivy](https://github.com/aquasecurity/trivy) is an open-source vulnerability scanner for containers and other artifacts. It detects vulnerabilities in OS packages and application dependencies.

### [Scan a DHI using Trivy](#scan-a-dhi-using-trivy)

After installing Trivy, you can scan a Docker Hardened Image by pulling the image and running the scan command:

To filter vulnerabilities using VEX statements, Trivy supports multiple approaches. Docker recommends using VEX Hub, which provides a seamless workflow for automatically downloading and applying VEX statements from configured repositories.

#### [Using VEX Hub (recommended)](#using-vex-hub-recommended)

Configure Trivy to download the Docker Hardened Images advisories repository from VEX Hub. Run the following commands to set up the VEX repository:

After setting up VEX Hub, you can scan a Docker Hardened Image with VEX filtering:

For example, scanning the `dhi.io/python:3.13` image:

Example output:

The `--vex repo` flag applies VEX statements from the configured repository during the scan, which filters out known non-exploitable CVEs.

#### [Using local VEX files](#using-local-vex-files)

In addition to VEX Hub, Trivy also supports the use of local VEX files for vulnerability filtering. You can download the VEX attestation that Docker Hardened Images provide and use it directly with Trivy.

First, download the VEX attestation for your image:

Then scan the image with the local VEX file:

Docker Hardened Images include signed VEX (Vulnerability Exploitability eXchange) attestations that identify vulnerabilities not relevant to the image’s runtime behavior.

When using Docker Scout, these VEX statements are automatically applied and no manual configuration needed.

> By default, VEX attestations are fetched from `registry.scout.docker.com`. Ensure that you can access this registry if your network has outbound restrictions. You can also mirror the attestations to an alternate registry. For more details, see [Mirror to a third-party registry](https://docs.docker.com/dhi/how-to/mirror/#mirror-to-a-third-party-registry).

To manually create a JSON file of VEX attestations for tools that support it:

> The `docker scout vex get` command requires [Docker Scout CLI](https://github.com/docker/scout-cli/) version 1.18.3 or later.
> 
> If the image exists locally on your device, you must prefix the image name with `registry://`. For example, use `registry://docs/dhi-python:3.13` instead of `docs/dhi-python:3.13`.

For example:

This creates a `vex.json` file containing the VEX statements for the specified image. You can then use this file with tools that support VEX to filter out known non-exploitable CVEs.

For example, with Grype you can use the `--vex` flag to apply the VEX statements during the scan: