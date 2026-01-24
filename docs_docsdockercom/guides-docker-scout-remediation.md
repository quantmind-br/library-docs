---
title: Remediation
url: https://docs.docker.com/guides/docker-scout/remediation/
source: llms
fetched_at: 2026-01-24T14:04:25.344603108-03:00
rendered_js: false
word_count: 134
summary: This document explains Docker Scout's remediation feature, which provides actionable recommendations to resolve security policy violations and improve supply chain compliance.
tags:
    - docker-scout
    - remediation
    - security-policy
    - supply-chain
    - vulnerability-management
category: guide
---

Docker Scout's [remediation feature](https://docs.docker.com/scout/policy/remediation/) helps you address supply chain and security issues by offering tailored recommendations based on policy evaluations. These recommendations guide you in improving policy compliance or enhancing image metadata, allowing Docker Scout to perform more accurate evaluations in the future.

You can use this feature to ensure that your base images are up-to-date and that your supply chain attestations are complete. When a violation occurs, Docker Scout provides recommended fixes, such as updating your base image or adding missing attestations. If there isn’t enough information to determine compliance, Docker Scout suggests actions to help resolve the issue.

In the Docker Scout Dashboard, you can view and act on these recommendations by reviewing violations or compliance uncertainties. With integrations like GitHub, you can even automate updates, directly fixing issues from the dashboard.