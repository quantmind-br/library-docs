---
title: Registry Access Management
url: https://docs.docker.com/enterprise/security/hardened-desktop/registry-access-management/
source: llms
fetched_at: 2026-01-24T14:26:39.388791807-03:00
rendered_js: false
word_count: 657
summary: This document explains how administrators can use Registry Access Management to restrict Docker Desktop users to specific approved container registries. It details the configuration process, security requirements, and technical limitations for organizations using Docker Business.
tags:
    - docker-desktop
    - registry-access-management
    - container-security
    - docker-business
    - administration
category: configuration
---

Subscription: Business

For: Administrators

Registry Access Management (RAM) lets administrators control which container registries developers can access through Docker Desktop. This DNS-level filtering ensures developers only pull and push images from approved registries, improving supply chain security.

RAM works with all registry types including cloud services, on-premises registries, and registry mirrors. You can allow any hostname or domain, but must include redirect domains (like `s3.amazonaws.com` for some registries) in your allowlist.

Registry Access Management works with any container registry, including:

- Docker Hub (allowed by default)
- Cloud registries: Amazon ECR, Google Container Registry, Azure Container Registry
- Git-based registries: GitHub Container Registry, GitLab Container Registry
- On-premises solutions: Nexus, Artifactory, Harbor
- Registry mirrors: Including Docker Hub mirrors

Before configuring Registry Access Management, you must:

- [Enforce sign-in](https://docs.docker.com/enterprise/security/enforce-sign-in/) to ensure users authenticate with your organization
- Use [personal access tokens (PATs)](https://docs.docker.com/security/access-tokens/) for authentication (Organization access tokens aren't supported)
- Have a Docker Business subscription

> Registry Access Management only takes effect when users are signed in to Docker Desktop with organization credentials.

To configure registry permissions:

1. Sign in to [Docker Home](https://app.docker.com) and select your organization from the top-left account drop-down.
2. Select **Admin Console**, then **Registry access**.
3. Use the **toggle** to enable registry access. By default, Docker Hub is enabled in the registry list.
4. To add additional registries, select **Add registry** and provide a **Registry address** and **Registry nickname**.
5. Select **Create**. You can add up to 100 registries.
6. Verify your registry appears in the registry list and select **Save changes**.

Changes can take up to 24 hours to take effect. To apply them sooner, have developers sign out and back in to Docker Desktop.

> Starting with Docker Desktop 4.36, if a developer belongs to multiple organizations with different RAM policies, only the policy for the first organization in the configuration file is enforced.

> RAM restrictions also apply to Dockerfile `ADD` instructions that fetch content via URL. Include trusted registry domains in your allowlist when using `ADD` with URLs.
> 
> RAM is designed for container registries, not general-purpose URLs like package mirrors or storage services. Adding too many domains may cause errors or hit system limits.

After users sign in to Docker Desktop with their organization credentials, Registry Access Management takes effect immediately.

When users try to pull from a blocked registry:

Allowed registry access works normally:

Registry restrictions apply to all Docker operations including pulls, pushes, and builds that reference external registries.

Registry Access Management has these limits and platform-specific behaviors:

- Maximum allowlist size: 100 registries or domains per organization
- DNS-based filtering: Restrictions work at the hostname level, not IP addresses
- Redirect domains required: Must include all domains a registry redirects to (CDN endpoints, storage services)
- Windows containers: Windows image operations aren't restricted by default. Turn on **Use proxy for Windows Docker daemon** in Docker Desktop settings to apply restrictions
- WSL 2 requirements: Requires Linux kernel 5.4 or later, restrictions apply to all WSL 2 distributions

These scenarios are not restricted by Registry Access Management:

- Docker buildx with Kubernetes driver
- Docker buildx with custom docker-container driver
- Some Docker Debug and Kubernetes image pulls (even if Docker Hub is blocked)
- Images previously cached by registry mirrors may still be blocked if the source registry is restricted

Users can potentially bypass Registry Access Management through:

- Local proxies or DNS manipulation
- Signing out of Docker Desktop (unless sign-in is enforced)
- Network-level modifications outside Docker Desktop's control

To maximize security effectiveness:

- [Enforce sign-in](https://docs.docker.com/enterprise/security/enforce-sign-in/) to prevent bypass through sign-out
- Implement additional network-level controls for complete protection
- Use Registry Access Management as part of a broader security strategy

<!--THE END-->

- Include all registry domains: Some registries redirect to multiple domains. For AWS ECR, include:
- Practice regular allowlist maintenance:
  
  - Remove unused registries periodically
  - Add newly approved registries as needed
  - Update domain names that may have changed
  - Monitor registry usage through Docker Desktop analytics
- Test configuration changes:
  
  - Verify registry access after making allowlist updates
  - Check that all necessary redirect domains are included
  - Ensure development workflows aren't disrupted
  - Combine with [Enhanced Container Isolation](https://docs.docker.com/enterprise/security/hardened-desktop/enhanced-container-isolation/) for comprehensive protection