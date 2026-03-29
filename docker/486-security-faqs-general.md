---
title: General
url: https://docs.docker.com/security/faqs/general/
source: llms
fetched_at: 2026-01-24T14:29:42.944730268-03:00
rendered_js: false
word_count: 334
summary: This document provides answers to frequently asked questions regarding Docker's security policies, authentication mechanisms, and account management features.
tags:
    - security-faq
    - authentication
    - docker-hub
    - docker-desktop
    - access-management
    - sso
    - activity-logs
    - session-tokens
category: reference
---

## General security FAQs

If you've discovered a security vulnerability in Docker, report it responsibly to [security@docker.com](mailto:security@docker.com) so Docker can quickly address it.

Docker Hub locks out users after 10 failed sign-in attempts within 5 minutes. The lockout duration is 5 minutes. This policy applies to Docker Hub, Docker Desktop, and Docker Scout authentication.

You can configure physical multi-factor authentication (MFA) through SSO using your identity provider (IdP). Check with your IdP if they support physical MFA devices like YubiKeys.

Docker uses tokens to manage user sessions with different expiration periods:

- Docker Desktop: Signs you out after 90 days, or 30 days of inactivity
- Docker Hub and Docker Home: Sign you out after 24 hours

Docker also supports your IdP's default session timeout through SAML attributes. For more information, see [SSO attributes](https://docs.docker.com/enterprise/security/provisioning/#sso-attributes).

Organizations use verified domains to distinguish user types. Team members with email domains other than verified domains appear as "Guest" users in the organization.

Docker activity logs are available for 90 days. You're responsible for exporting logs or setting up drivers to send logs to your internal systems for longer retention.

Yes, use the [Export Members](https://docs.docker.com/admin/organization/members/#export-members) feature to export a CSV file containing your organization's users with role and team information.

Docker Desktop uses the host operating system's secure key management to store authentication tokens:

- macOS: [Keychain](https://support.apple.com/guide/security/keychain-data-protection-secb0694df1a/web)
- Windows: [Security and Identity API via Wincred](https://learn.microsoft.com/en-us/windows/win32/api/wincred/)
- Linux: [Pass](https://www.passwordstore.org/).

If SCIM isn't turned on, you must manually remove users from the organization. SCIM can automate user removal, but only for users added after SCIM is turned on. Users added before SCIM was turned on must be removed manually.

For more information, see [Manage organization members](https://docs.docker.com/admin/organization/members/).

For information about metadata stored by Docker Scout, see [Data handling](https://docs.docker.com/scout/deep-dive/data-handling/).

Security vetting for extensions is on the roadmap but isn't currently implemented. Extensions aren't covered as part of Docker's Third-Party Risk Management Program.

No direct setting exists to disable private repositories. However, [Registry Access Management](https://docs.docker.com/enterprise/security/hardened-desktop/registry-access-management/) lets administrators control which registries developers can access through Docker Desktop via the Admin Console.