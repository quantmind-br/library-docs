---
title: STIG
url: https://docs.docker.com/dhi/core-concepts/stig/
source: llms
fetched_at: 2026-01-24T14:19:58.511753441-03:00
rendered_js: false
word_count: 477
summary: This document explains Docker Hardened Images (DHI) STIG variants, detailing how they meet government security standards and how to access and verify their compliance scan attestations.
tags:
    - docker-hardened-images
    - stig-compliance
    - container-security
    - docker-scout
    - compliance-attestation
    - security-hardening
category: guide
---

## STIG DHI Enterprise

Subscription: Docker Hardened Images Enterprise

[Security Technical Implementation Guides (STIGs)](https://public.cyber.mil/stigs/) are configuration standards published by the U.S. Defense Information Systems Agency (DISA). They define security requirements for operating systems, applications, databases, and other technologies used in U.S. Department of Defense (DoD) environments.

STIGs help ensure that systems are configured securely and consistently to reduce vulnerabilities. They are often based on broader requirements like the DoD's General Purpose Operating System Security Requirements Guide (GPOS SRG).

Following STIG guidance is critical for organizations that work with or support U.S. government systems. It demonstrates alignment with DoD security standards and helps:

- Accelerate Authority to Operate (ATO) processes for DoD systems
- Reduce the risk of misconfiguration and exploitable weaknesses
- Simplify audits and reporting through standardized baselines

Even outside of federal environments, STIGs are used by security-conscious organizations as a benchmark for hardened system configurations.

STIGs are derived from broader NIST guidance, particularly [NIST Special Publication 800-53](https://csrc.nist.gov/publications/sp800), which defines a catalog of security and privacy controls for federal systems. Organizations pursuing compliance with 800-53 or related frameworks (such as FedRAMP) can use STIGs as implementation guides that help meet applicable control requirements.

Docker Hardened Images (DHIs) include STIG variants that are scanned against custom STIG-based profiles and include signed STIG scan attestations. These attestations can support audits and compliance reporting.

While Docker Hardened Images are available to all, the STIG variant requires a Docker subscription.

Docker creates custom STIG-based profiles for images based on the GPOS SRG and DoD Container Hardening Process Guide. Because DISA has not published a STIG specifically for containers, these profiles help apply STIG-like guidance to container environments in a consistent, reviewable way and are designed to reduce false positives common in container images.

Docker Hardened Images that include STIG scan results are labeled as **STIG** in the Docker Hardened Images catalog.

To find DHI repositories with STIG image variants, [explore images](https://docs.docker.com/dhi/how-to/explore/) and:

- Use the **STIG** filter on the catalog page
- Look for **STIG** labels on individual image listings

To find a STIG image variant within a repository, go to the **Tags** tab in the repository, and find images labeled with **STIG** in the **Compliance** column.

To use a STIG variant, you must [mirror](https://docs.docker.com/dhi/how-to/mirror/) the repository and then pull the STIG image from your mirrored repository.

Docker provides a signed [STIG scan attestation](https://docs.docker.com/dhi/core-concepts/attestations/) for each STIG-ready image. These attestations include:

- A summary of the scan results, including the number of passed, failed, and not applicable checks
- The name and version of the STIG profile used
- Full output in both HTML and XCCDF (XML) formats

### [View STIG scan attestations](#view-stig-scan-attestations)

You can retrieve and inspect a STIG scan attestation using the Docker Scout CLI:

To extract and view the human-readable HTML report:

To extract the XML (XCCDF) report for integration with other tools:

### [View STIG scan summary](#view-stig-scan-summary)

To view just the scan summary without the full reports: