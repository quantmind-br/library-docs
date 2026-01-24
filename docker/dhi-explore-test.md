---
title: Image testing
url: https://docs.docker.com/dhi/explore/test/
source: llms
fetched_at: 2026-01-24T14:20:22.202105733-03:00
rendered_js: false
word_count: 450
summary: This document explains the testing strategy for Docker Hardened Images, covering security standards, functionality verification, and the process for verifying signed test attestations using Docker Scout.
tags:
    - docker-hardened-images
    - container-security
    - docker-scout
    - vulnerability-scanning
    - attestation-verification
    - compliance-standards
category: guide
---

## How Docker Hardened Images are tested

Docker Hardened Images (DHIs) are designed to be secure, minimal, and production-ready. To ensure their reliability and security, Docker employs a comprehensive testing strategy, which you can independently verify using signed attestations and open tooling.

Every image is tested for standards compliance, functionality, and security. The results of this testing are embedded as signed attestations, which can be [inspected and verified](#view-and-verify-the-test-attestation) programmatically using the Docker Scout CLI.

The testing process for DHIs focuses on two main areas:

- Image standards compliance: Ensuring that each image adheres to strict size, security, and compatibility standards.
- Application functionality: Verifying that applications within the images function correctly.

Each DHI undergoes rigorous checks to meet the following standards:

- Minimal attack surface: Images are built to be as small as possible, removing unnecessary components to reduce potential vulnerabilities.
- Near-zero known CVEs: Images are scanned using tools like Docker Scout to ensure they are free from known Common Vulnerabilities and Exposures (CVEs).
- Multi-architecture support: DHIs are built for multiple architectures (`linux/amd64` and `linux/arm64`) to ensure broad compatibility.
- Kubernetes compatibility: Images are tested to run seamlessly within Kubernetes clusters, ensuring they meet the requirements for container orchestration environments.

Docker tests Docker Hardened Images to ensure they behave as expected in typical usage scenarios. This includes verifying that:

- Applications start and run successfully in containerized environments.
- Runtime behavior aligns with upstream expectations.
- Build variants (like `-dev` images) support common development and build tasks.

The goal is to ensure that DHIs work out of the box for the most common use cases while maintaining the hardened, minimal design.

Docker integrates automated testing into its Continuous Integration/Continuous Deployment (CI/CD) pipelines:

- Automated scans: Each image build triggers automated scans for vulnerabilities and compliance checks.
- Reproducible builds: Build processes are designed to be reproducible, ensuring consistency across different environments.
- Continuous monitoring: Docker continuously monitors for new vulnerabilities and updates images accordingly to maintain security standards.

Docker provides a test attestation that details the testing and validation processes each DHI has undergone.

### [View and verify the test attestation](#view-and-verify-the-test-attestation)

You can view and verify this attestation using the Docker Scout CLI.

1. Use the `docker scout attest get` command with the test predicate type:
   
   > If the image exists locally on your device, you must prefix the image name with `registry://`. For example, use `registry://dhi.io/python` instead of `dhi.io/python`.
   
   For example:
   
   This contains a list of tests and their results.
   
   Example output:
2. Verify the test attestation signature. To ensure the attestation is authentic and signed by Docker, run:
   
   Example output:

If the attestation is valid, Docker Scout will confirm the signature and show the matching `cosign verify` command.

To view other attestations, such as SBOMs or vulnerability reports, see [Verify an image](https://docs.docker.com/dhi/how-to/verify/).