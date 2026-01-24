---
title: FIPS
url: https://docs.docker.com/dhi/core-concepts/fips/
source: llms
fetched_at: 2026-01-24T14:19:37.179738761-03:00
rendered_js: false
word_count: 439
summary: This document explains Docker Hardened Images Enterprise FIPS variants, detailing their role in regulatory compliance and providing instructions for locating and verifying them.
tags:
    - fips-140
    - docker-hardened-images
    - compliance
    - container-security
    - cryptography
    - docker-scout
category: guide
---

## FIPS DHI Enterprise

Subscription: Docker Hardened Images Enterprise

[FIPS 140](https://csrc.nist.gov/publications/detail/fips/140/3/final) is a U.S. government standard that defines security requirements for cryptographic modules that protect sensitive information. It is widely used in regulated environments such as government, healthcare, and financial services.

FIPS certification is managed by the [NIST Cryptographic Module Validation Program (CMVP)](https://csrc.nist.gov/projects/cryptographic-module-validation-program), which ensures cryptographic modules meet rigorous security standards.

FIPS 140 compliance is required or strongly recommended in many regulated environments where sensitive data must be protected, such as government, healthcare, finance, and defense. These standards ensure that cryptographic operations are performed using vetted, trusted algorithms implemented in secure modules.

Using software components that rely on validated cryptographic modules can help organizations:

- Satisfy federal and industry mandates, such as FedRAMP, which require or strongly recommend FIPS 140-validated cryptography.
- Demonstrate audit readiness, with verifiable evidence of secure, standards-based cryptographic practices.
- Reduce security risk, by blocking unapproved or unsafe algorithms (e.g., MD5) and ensuring consistent behavior across environments.

While Docker Hardened Images are available to all, the FIPS variant requires a Docker Hardened Images Enterprise subscription.

Docker Hardened Images (DHIs) include variants that use cryptographic modules validated under FIPS 140. These images are intended to help organizations meet compliance requirements by incorporating components that meet the standard.

- FIPS image variants use cryptographic modules that are already validated under FIPS 140.
- These variants are built and maintained by Docker to support environments with regulatory or compliance needs.
- Docker provides signed test attestations that document the use of validated cryptographic modules. These attestations can support internal audits and compliance reporting.

> Using a FIPS image variant helps meet compliance requirements but does not make an application or system fully compliant. Compliance depends on how the image is integrated and used within the broader system.

Docker Hardened Images that support FIPS are marked as **FIPS** compliant in the Docker Hardened Images catalog.

To find DHI repositories with FIPS image variants, [explore images](https://docs.docker.com/dhi/how-to/explore/) and:

- Use the **FIPS** filter on the catalog page
- Look for **FIPS** compliant on individual image listings

These indicators help you quickly locate repositories that support FIPS-based compliance needs. Image variants that include FIPS support will have a tag ending with `-fips`, such as `3.13-fips`.

To use a FIPS variant, you must [mirror](https://docs.docker.com/dhi/how-to/mirror/) the repository and then pull the FIPS image from your mirrored repository.

The FIPS variants of Docker Hardened Images contain a FIPS attestation that lists the actual cryptographic modules included in the image.

You can retrieve and inspect the FIPS attestation using the Docker Scout CLI:

For example:

The attestation output is a JSON array describing the cryptographic modules included in the image and their compliance status. For example: