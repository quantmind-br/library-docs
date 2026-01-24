---
title: Finalize plans and begin setup
url: https://docs.docker.com/guides/admin-set-up/finalize-plans-and-setup/
source: llms
fetched_at: 2026-01-24T14:03:07.076210448-03:00
rendered_js: false
word_count: 420
summary: This document outlines the administrative steps for configuring and managing Docker Desktop in an enterprise environment, covering settings management, authentication, and product entitlements.
tags:
    - docker-desktop
    - enterprise-management
    - settings-management
    - single-sign-on
    - mdm-deployment
    - security-configuration
    - docker-business
category: guide
---

After reaching an agreement with the relevant teams about your baseline and security configurations as outlined in the previous section, configure Settings Management using either the [Docker Admin Console](https://docs.docker.com/enterprise/security/hardened-desktop/settings-management/configure-admin-console/) or an [`admin-settings.json` file](https://docs.docker.com/enterprise/security/hardened-desktop/settings-management/configure-json-file/).

Once the file is ready, collaborate with your MDM team to deploy your chosen settings, along with your chosen method for [enforcing sign-in](https://docs.docker.com/enterprise/security/enforce-sign-in/).

> Test this first with a small number of Docker Desktop developers to verify the functionality works as expected before deploying more widely.

If you have more than one organization, consider either [consolidating them into one organization](https://docs.docker.com/admin/organization/orgs/) or creating a [Docker company](https://docs.docker.com/admin/company/) to manage multiple organizations.

### [Set up single sign-on and domain verification](#set-up-single-sign-on-and-domain-verification)

Single sign-on (SSO) lets developers authenticate using their identity providers (IdPs) to access Docker. SSO is available for a whole company and all associated organizations, or an individual organization that has a Docker Business subscription. For more information, see the [documentation](https://docs.docker.com/enterprise/security/single-sign-on/).

You can also enable [SCIM](https://docs.docker.com/enterprise/security/provisioning/scim/) for further automation of provisioning and deprovisioning of users.

### [Set up Docker product entitlements included in the subscription](#set-up-docker-product-entitlements-included-in-the-subscription)

[Docker Build Cloud](https://docs.docker.com/build-cloud/) significantly reduces build times, both locally and in CI, by providing a dedicated remote builder and shared cache. Powered by the cloud, developer time and local resources are freed up so your team can focus on more important things, like innovation. To get started, [set up a cloud builder](https://app.docker.com/build/).

[Docker Scout](https://docs.docker.com/scout/) is a solution for proactively enhancing your software supply chain security. By analyzing your images, Docker Scout compiles an inventory of components, also known as a Software Bill of Materials (SBOM). The SBOM is matched against a continuously updated vulnerability database to pinpoint security weaknesses. To get started, see [Quickstart](https://docs.docker.com/scout/quickstart/).

[Testcontainers Cloud](https://testcontainers.com/cloud/docs/) allows developers to run containers in the cloud, removing the need to run heavy containers on your local machine.

[Docker Hardened Images](https://docs.docker.com/dhi/) are minimal, secure, and production-ready container base and application images maintained by Docker. Designed to reduce vulnerabilities and simplify compliance, DHIs integrate easily into your existing Docker-based workflows with little to no retooling required.

### [Ensure you're running a supported version of Docker Desktop](#ensure-youre-running-a-supported-version-of-docker-desktop)

> This step could affect the experience for users on older versions of Docker Desktop.

Existing users may be running outdated or unsupported versions of Docker Desktop. All users should update to a supported version. Docker Desktop versions released within the past 6 months from the latest release are supported.

Use an MDM solution to manage the version of Docker Desktop for users. Users may also get Docker Desktop directly from Docker or through a company software portal.