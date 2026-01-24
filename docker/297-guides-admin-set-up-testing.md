---
title: Testing
url: https://docs.docker.com/guides/admin-set-up/testing/
source: llms
fetched_at: 2026-01-24T14:08:15.171299298-03:00
rendered_js: false
word_count: 323
summary: This document provides instructions for verifying and testing Docker enterprise features, including SSO, SCIM, and image access management, to ensure proper configuration and enforcement.
tags:
    - docker-enterprise
    - sso-testing
    - scim-verification
    - access-management
    - security-testing
    - enterprise-deployment
category: guide
---

Table of contents

* * *

## [SSO and SCIM testing](#sso-and-scim-testing)

Test SSO and SCIM by signing in to Docker Desktop or Docker Hub with the email address linked to a Docker account that is part of the verified domain. Developers who sign in using their Docker usernames remain unaffected by the SSO and SCIM setup.

> Important
> 
> Some users may need CLI based logins to Docker Hub, and for this they will need a [personal access token (PAT)](https://docs.docker.com/security/access-tokens/).

## [Test Registry Access Management and Image Access Management](#test-registry-access-management-and-image-access-management)

> Warning
> 
> Communicate with your users before proceeding, as this step will impact all existing users signing into your Docker organization.

If you plan to use [Registry Access Management (RAM)](https://docs.docker.com/enterprise/security/hardened-desktop/registry-access-management/) and/or [Image Access Management (IAM)](https://docs.docker.com/enterprise/security/hardened-desktop/image-access-management/):

1. Ensure your test developer signs in to Docker Desktop using their organization credentials
2. Have them attempt to pull an unauthorized image or one from a disallowed registry via the Docker CLI
3. Verify they receive an error message indicating that the registry is restricted by the organization

## [Deploy settings and enforce sign in to test group](#deploy-settings-and-enforce-sign-in-to-test-group)

Deploy the Docker settings and enforce sign-in for a small group of test users via MDM. Have this group test their development workflows with containers on Docker Desktop and Docker Hub to ensure all settings and the sign-in enforcement function as expected.

## [Test Docker Build Cloud capabilities](#test-docker-build-cloud-capabilities)

Have one of your Docker Desktop testers [connect to the cloud builder you created and use it to build](https://docs.docker.com/build-cloud/usage/).

## [Test Testcontainers Cloud](#test-testcontainers-cloud)

Have a test developer [connect to Testcontainers Cloud](https://testcontainers.com/cloud/docs/#getting-started) and run a container in the cloud to verify the setup is working correctly.

## [Verify Docker Scout monitoring of repositories](#verify-docker-scout-monitoring-of-repositories)

Check the [Docker Scout dashboard](https://scout.docker.com/) to confirm that data is being properly received for the repositories where Docker Scout has been enabled.

## [Verify access to Docker Hardened Images](#verify-access-to-docker-hardened-images)

Have a test developer attempt to [pull a Docker Hardened Image](https://docs.docker.com/dhi/get-started/) to confirm that the team has proper access and can integrate these images into their workflows.