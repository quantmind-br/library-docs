---
title: View Docker Scout policy status
url: https://docs.docker.com/scout/policy/view/
source: llms
fetched_at: 2026-01-24T14:29:27.077476878-03:00
rendered_js: false
word_count: 411
summary: This document explains how to monitor and track policy compliance for container images using the Docker Scout Dashboard and CLI. It provides instructions on analyzing policy trends, viewing detailed violation reports, and following remediation steps for security and licensing issues.
tags:
    - docker-scout
    - policy-tracking
    - vulnerability-management
    - compliance-monitoring
    - artifact-security
    - remediation-guidance
category: guide
---

You can track policy status for your artifacts from the [Docker Scout Dashboard](#dashboard), or using the [CLI](#cli).

The **Overview** tab of the [Docker Scout Dashboard](https://scout.docker.com/) displays a summary of recent changes in policy for your repositories. This summary shows images that have seen the most change in their policy evaluation between the most recent image and the previous image.

![Policy overview](https://docs.docker.com/scout/images/policy-overview.webp)

![Policy overview](https://docs.docker.com/scout/images/policy-overview.webp)

### [Policy status per repository](#policy-status-per-repository)

The **Images** tab shows the current policy status, and recent policy trend, for all images in the selected environment. The **Policy status** column in the list shows:

- Number of fulfilled policies versus the total number of policies
- Recent policy trends

![Policy status in the image list](https://docs.docker.com/scout/images/policy-image-list.webp)

![Policy status in the image list](https://docs.docker.com/scout/images/policy-image-list.webp)

The policy trend, denoted by the directional arrows, indicates whether an image is better, worse, or unchanged in terms of policy, compared to the previous image in the same environment.

- The green arrow pointing upwards shows the number of policies that got better in the latest pushed image.
- The red arrow pointing downwards shows the number of policies that got worse in the latest pushed image.
- The bidirectional gray arrow shows the number of policies that were unchanged in the latest version of this image.

If you select a repository, you can open the **Policy** tab for a detailed description of the policy delta for the most recently analyzed image and its predecessor.

### [Detailed results and remediation](#detailed-results-and-remediation)

To view the full evaluation results for an image, navigate to the image tag in the Docker Scout Dashboard and open the **Policy** tab. This shows a breakdown for all policy violations for the current image.

![Detailed Policy Evaluation results](https://docs.docker.com/scout/images/policy-detailed-results.webp)

![Detailed Policy Evaluation results](https://docs.docker.com/scout/images/policy-detailed-results.webp)

This view also provides recommendations on how to improve improve policy status for violated policies.

![Policy details in the tag view](https://docs.docker.com/scout/images/policy-tag-view.webp)

![Policy details in the tag view](https://docs.docker.com/scout/images/policy-tag-view.webp)

For vulnerability-related policies, the policy details view displays the fix version that removes the vulnerability, when a fix version is available. To fix the issue, upgrade the package version to the fix version.

For licensing-related policies, the list shows all packages whose license doesn't meet the policy criteria. To fix the issue, find a way to remove the dependency to the violating package, for example by looking for an alternative package distributed under a more appropriate license.

To view policy status for an image from the CLI, use the `docker scout policy` command.

For more information about the command, refer to the [CLI reference](https://docs.docker.com/reference/cli/docker/scout/policy/).