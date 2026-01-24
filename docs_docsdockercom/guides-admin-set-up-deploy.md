---
title: Deploy your Docker setup
url: https://docs.docker.com/guides/admin-set-up/deploy/
source: llms
fetched_at: 2026-01-24T14:03:06.214840158-03:00
rendered_js: false
word_count: 161
summary: This document outlines the final steps for administrators to enforce Single Sign-On (SSO) and deploy configuration settings through MDM for a Docker organization.
tags:
    - sso-enforcement
    - docker-administration
    - security-policy
    - mdm-configuration
    - identity-management
category: guide
---

> Warning
> 
> Communicate with your users before proceeding, and confirm that your IT and MDM teams are prepared to handle any unexpected issues, as these steps will affect all existing users signing into your Docker organization.

## [Enforce SSO](#enforce-sso)

Enforcing SSO means that anyone who has a Docker profile with an email address that matches your verified domain must sign in using your SSO connection. Make sure the Identity provider groups associated with your SSO connection cover all the developer groups that you want to have access to the Docker subscription.

For instructions on how to enforce SSO, see [Enforce SSO](https://docs.docker.com/enterprise/security/single-sign-on/connect/).

## [Deploy configuration settings and enforce sign-in to users](#deploy-configuration-settings-and-enforce-sign-in-to-users)

Have the MDM team deploy the configuration files for Docker to all users.

## [Next steps](#next-steps)

Congratulations, you've successfully completed the admin implementation process for Docker.

To continue optimizing your Docker environment:

- Review your [organization's usage data](https://docs.docker.com/admin/organization/insights/) to track adoption
- Monitor [Docker Scout findings](https://docs.docker.com/scout/explore/analysis/) for security insights
- Explore [additional security features](https://docs.docker.com/enterprise/security/) to enhance your configuration