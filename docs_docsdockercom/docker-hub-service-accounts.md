---
title: Service accounts
url: https://docs.docker.com/docker-hub/service-accounts/
source: llms
fetched_at: 2026-01-24T14:22:23.947718062-03:00
rendered_js: false
word_count: 159
summary: This document announces the deprecation of Enhanced Service Account add-ons and provides guidance on transitioning to Organization Access Tokens for automated image management.
tags:
    - docker-hub
    - service-accounts
    - organization-access-tokens
    - automation
    - ci-cd
    - security
category: reference
---

As of December 10, 2024, Enhanced Service Account add-ons are no longer available. Existing Service Account agreements will be honored until their current term expires, but new purchases or renewals of Enhanced Service Account add-ons are no longer available and customers must renew under a new subscription.

Docker recommends transitioning to [Organization Access Tokens (OATs)](https://docs.docker.com/enterprise/security/access-tokens/), which can provide similar functionality.

A service account is a Docker ID used for automated management of container images or containerized applications. Service accounts are typically used in automated workflows, and don't share Docker IDs with the members in the organization. Common use cases for service accounts include mirroring content on Docker Hub, or tying in image pulls from your CI/CD process.

Refer to the following table for details on the Enhanced Service Account add-ons:

\*The service account may exceed Pulls by up to 25% for up to 20 days during the year without incurring additional fees. Reports on consumption are available upon request.