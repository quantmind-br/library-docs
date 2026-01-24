---
title: Compare images
url: https://docs.docker.com/dhi/how-to/compare/
source: llms
fetched_at: 2026-01-24T14:20:29.175389201-03:00
rendered_js: false
word_count: 569
summary: This document explains how to use the Docker Scout CLI to compare Docker Hardened Images with standard or custom images to evaluate security improvements, package differences, and vulnerability reductions.
tags:
    - docker-scout
    - hardened-images
    - container-security
    - vulnerability-management
    - image-comparison
    - devsecops
category: guide
---

## Compare Docker Hardened Images

Docker Hardened Images (DHIs) are designed to provide enhanced security, minimized attack surfaces, and production-ready foundations for your applications. Comparing a DHI to a standard image helps you understand the security improvements, package differences, and overall benefits of adopting hardened images.

This page explains how to use Docker Scout to compare a Docker Hardened Image with another image, such as a Docker Official Image (DOI) or a custom image, to evaluate differences in vulnerabilities, packages, and configurations.

Docker Scout provides a built-in comparison feature that lets you analyze the differences between two images. This is useful for:

- Evaluating the security improvements when migrating from a standard image to a DHI
- Understanding package and vulnerability differences between image variants
- Assessing the impact of customizations or updates

### [Basic comparison](#basic-comparison)

To compare a Docker Hardened Image with another image, use the [`docker scout compare`](https://docs.docker.com/reference/cli/docker/scout/compare/) command:

For example, to compare a DHI Node.js image with the official Node.js image:

This command provides a detailed comparison including:

- Vulnerability differences (CVEs added, removed, or changed)
- Package differences (packages added, removed, or updated)
- Overall security posture improvements

### [Filter unchanged packages](#filter-unchanged-packages)

To focus only on the differences and ignore unchanged packages, use the `--ignore-unchanged` flag:

This output highlights only the packages and vulnerabilities that differ between the two images, making it easier to identify the security improvements and changes.

### [Show overview only](#show-overview-only)

For a concise overview of the comparison results, you can extract just the overview section using standard shell tools:

The result is a clean summary showing the key differences between the two images. Example output:

The comparison output includes the following sections.

### [Overview](#overview)

The overview section provides high-level statistics about both images:

- Target and comparison image details (digest, tag, platform, provenance)
- Vulnerability counts for each image
- Size comparison
- Package counts

Look for:

- Vulnerability reductions (negative numbers in the delta row)
- Size reductions showing storage efficiency
- Package count reductions indicating a minimal attack surface

### [Environment Variables](#environment-variables)

The environment variables section shows environment variables that differ between the two images, prefixed with `+` for added or `-` for removed.

Look for:

- Removed environment variables that may have been necessary for your specific use-case

### [Labels](#labels)

The labels section displays labels that differ between the two images, prefixed with `+` for added or `-` for removed.

### [Packages and Vulnerabilities](#packages-and-vulnerabilities)

The packages and vulnerabilities section lists all package differences and their associated security vulnerabilities. Packages are prefixed with:

- `-` for packages removed from the target image (not present in the compared image)
- `+` for packages added to the target image (not present in the base image)
- `↑` for packages upgraded in the target image
- `↓` for packages downgraded in the target image

For packages with associated vulnerabilities, the CVEs are listed with their severity levels and identifiers.

Look for:

- Removed packages and vulnerabilities: Indicates a reduced attack surface in the DHI
- Added packages: May indicate DHI-specific tooling or dependencies
- Upgraded packages: Shows version updates that may include security fixes

### [Evaluate migration benefits](#evaluate-migration-benefits)

Before migrating from a Docker Official Image to a DHI, compare them to understand the security improvements. For example:

This helps justify the migration by showing concrete vulnerability reductions and package minimization.

### [Assess customization impact](#assess-customization-impact)

After customizing a DHI, compare the customized version with the original to ensure you haven't introduced new vulnerabilities. For example:

### [Track updates over time](#track-updates-over-time)

Compare different versions of the same DHI to see what changed between releases. For example: