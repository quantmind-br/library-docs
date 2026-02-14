---
description: Auto-generated documentation index for Dokploy
generated: 2026-02-14T17:25:00Z
source: https://docs.dokploy.com/
total_docs: 104
categories: 16
---

# Dokploy Documentation Index

> Organized index for AI agent consumption. Documents follow logical learning sequence from introduction to advanced topics.

## Metadata Summary

| Property | Value |
|----------|-------|
| **Source** | https://docs.dokploy.com/ |
| **Generated** | 2026-02-14 |
| **Total Documents** | 104 |
| **Categories** | 16 |
| **Organization Method** | Sequential Numbering |

---

## Document Index

### 1. Introduction & Overview (001-007)
*Core concepts, architecture, and fundamental understanding of Dokploy*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 001 | `001-docs-core.md` | Welcome to Dokploy | Open-source deployment platform using Docker and Traefik | deployment, open-source, docker, traefik, self-hosting, paas |
| 002 | `002-docs-core-architecture.md` | Architecture of Dokploy | Core architectural components: Next.js, PostgreSQL, Redis, Traefik | dokploy-architecture, next-js, postgresql, redis, traefik, reverse-proxy |
| 003 | `003-docs-core-features.md` | Features | Comprehensive overview of deployment and management features | dokploy, application-deployment, docker-compose, database-management, monitoring |
| 004 | `004-docs-core-comparison.md` | Comparison | Feature comparison with CapRover, Dokku, and Coolify | deployment-tools, dokploy, caprover, dokku, coolify, paas-comparison |
| 005 | `005-docs-core-cloud.md` | Dokploy Cloud | Remote deployment service for multiple servers | dokploy-cloud, remote-deployment, multi-server, scalability, high-availability |
| 006 | `006-docs-core-overview.md` | Overview | General notifications configuration and providers | dokploy, notifications, deployment-alerts, monitoring, webhook |
| 007 | `007-docs-core-videos.md` | Videos | Video tutorials and external resources for Dokploy | dokploy, self-hosting, vps-deployment, docker-compose, server-management |

### 2. Installation & Quick Start (008-014)
*Getting Dokploy up and running on your server*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 008 | `008-docs-core-installation.md` | Installation | Step-by-step VPS installation and initial setup | dokploy-installation, docker-deployment, vps-setup, self-hosted |
| 009 | `009-docs-core-manual-installation.md` | Manual Installation | Comprehensive bash script for manual Linux installation | dokploy-installation, linux-server, docker-swarm, bash-script |
| 010 | `010-docs-core-uninstall.md` | Uninstall | Complete uninstallation of Dokploy and Docker services | dokploy, uninstallation, docker-swarm, server-maintenance |
| 011 | `011-docs-core-reset-password.md` | Reset Password & 2FA | Password reset and 2FA disable via CLI | dokploy, password-reset, 2fa-reset, docker-commands, account-recovery |
| 012 | `012-docs-core-troubleshooting.md` | Troubleshooting | Solutions for common domain, port, volume, and routing issues | dokploy, troubleshooting, docker-compose, networking, traefik |
| 013 | `013-docs-core-goodies.md` | Goodies | Community tools, GitHub Actions, SDKs, and templates | dokploy, community-tools, github-actions, deployment-automation |

### 3. Core Concepts & Fundamentals (014-022)
*Essential concepts for understanding Dokploy's capabilities*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 014 | `014-docs-core-applications.md` | Applications | Managing applications: deployment methods, monitoring, domains | dokploy, application-management, deployment-methods, docker-swarm |
| 015 | `015-docs-core-databases.md` | Databases | Creating, managing, and backing up database systems | dokploy, database-management, automated-backups, container-configuration |
| 016 | `016-docs-core-docker-compose.md` | Docker Compose | Using Docker Compose and Docker Stack with Dokploy | dokploy, docker-compose, docker-stack, container-orchestration |
| 017 | `017-docs-core-domains.md` | Domains | Configuring custom URLs and routing for applications | dokploy, domain-management, traefik-configuration, https-setup |
| 018 | `018-docs-core-variables.md` | Environment Variables | Managing shared and service-level environment variables | dokploy, environment-variables, configuration-management, secrets-management |
| 019 | `019-docs-core-providers.md` | Providers | Git repos, Docker registries, and file upload configuration | dokploy, deployment-providers, git-integration, docker-registry |
| 020 | `020-docs-core-ssh-keys.md` | SSH Keys | Configuring SSH for private repos and remote servers | ssh-keys, dokploy, private-repositories, server-access, security |
| 021 | `021-docs-core-registry.md` | Registry | Docker registry settings for image and artifact storage | docker-registry, dokploy, image-storage, authentication |
| 022 | `022-docs-core-certificates.md` | Certificates | SSL/TLS certificate management for HTTPS | dokploy, ssl-certificates, traefik-configuration, https-setup |

### 4. Configuration - Git Providers (023-028)
*Integrating Git repositories for automated deployments*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 023 | `023-docs-core-github.md` | GitHub | GitHub App integration for automated deployments | github-integration, git-sources, automated-deployment, github-app |
| 024 | `024-docs-core-gitlab.md` | Gitlab | GitLab repository connection and webhook setup | dokploy, gitlab-integration, automated-deployments, webhooks |
| 025 | `025-docs-core-bitbucket.md` | Bitbucket | Bitbucket integration with app passwords and webhooks | dokploy, bitbucket, deployment-automation, webhooks |
| 026 | `026-docs-core-gitea.md` | Gitea | Gitea repository connection and OAuth2 setup | gitea, dokploy, deployments, git-integration, webhooks |
| 027 | `027-docs-core-Docker.md` | Docker Registry | Docker Hub, GHCR, and public registry authentication | docker-registry, dokploy, docker-hub, ghcr, authentication |
| 028 | `028-docs-core-auto-deploy.md` | Auto Deploy | Webhook and API-based automated deployments | dokploy, deployment-automation, webhooks, api-deployment |

### 5. Configuration - Registry Providers (029-031)
*External container registry integrations*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 029 | `029-docs-core-registry-dockerhub.md` | Docker Hub | Docker Hub registry configuration with access tokens | docker-hub, registry-configuration, access-token, container-images |
| 030 | `030-docs-core-registry-ghcr.md` | GHCR | GitHub Container Registry setup and configuration | github-container-registry, ghcr, registry-configuration |
| 031 | `031-docs-core-registry-digital-ocean.md` | Digital Ocean | Digital Ocean Container Registry integration | digital-ocean, container-registry, docker, cloud-storage |

### 6. Configuration - Storage & Backups (032-038)
*S3-compatible storage for backups and volume management*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 032 | `032-docs-core-actions.md` | Actions (S3) | S3 destination management for database backups | s3-destinations, database-backups, cloud-storage |
| 033 | `033-docs-core-aws-s3.md` | AWS S3 | AWS S3 bucket and IAM configuration for backups | aws-s3, backup-storage, iam-policy, access-keys |
| 034 | `034-docs-core-cloudflare-r2.md` | Cloudflare R2 | R2 bucket configuration for S3-compatible backups | cloudflare-r2, s3-storage, backup-configuration |
| 035 | `035-docs-core-cloud-storage.md` | Google Cloud Storage | GCS bucket and HMAC key setup for backups | google-cloud-storage, backup-configuration, hmac-keys |
| 036 | `036-docs-core-backblaze-b2.md` | Backblaze B2 | B2 bucket configuration for backup storage | backblaze-b2, s3-storage, backup-configuration |
| 037 | `037-docs-core-backups.md` | Backups | Creating, scheduling, and restoring system backups | dokploy, backup-and-restore, s3-storage, postgresql |
| 038 | `038-docs-core-volume-backups.md` | Volume Backups | Docker named volume backup and restore | dokploy, docker-volumes, volume-backups, s3-storage |

### 7. Configuration - Monitoring & Notifications (039-048)
*Alerting and monitoring integrations*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 039 | `039-docs-core-monitoring.md` | Monitoring | Server and application monitoring setup | dokploy, server-monitoring, metrics-collection, alert-thresholds |
| 040 | `040-docs-core-webhook.md` | Webhook | HTTP webhook notifications configuration | dokploy, webhooks, notifications, http-endpoints |
| 041 | `041-docs-core-telegram.md` | Telegram | Telegram Bot notifications for application events | dokploy, telegram-notifications, botfather, alerting |
| 042 | `042-docs-core-discord.md` | Discord | Discord webhook notifications setup | discord, notifications, webhooks, server-monitoring |
| 043 | `043-docs-core-slack.md` | Slack | Slack webhook integration for real-time alerts | dokploy, slack-integration, notifications, webhooks |
| 044 | `044-docs-core-email.md` | Email | SMTP email notifications configuration | dokploy, email-notifications, smtp-configuration |
| 045 | `045-docs-core-pushover.md` | Pushover | Pushover mobile notification setup | pushover, notifications, dokploy, alerting |
| 046 | `046-docs-core-gotify.md` | Gotify | Gotify self-hosted notification setup | dokploy, gotify, notifications, server-alerts |
| 047 | `047-docs-core-ntfy.md` | Ntfy | Ntfy notification configuration | dokploy, ntfy, notifications, alerting |
| 048 | `048-docs-core-lark.md` | Lark | Lark webhook notifications for events | dokploy, lark, notifications, webhook-integration |

### 8. Application Management (049-056)
*Advanced application deployment and lifecycle management*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 049 | `049-docs-core-applications-build-type.md` | Build Type | Nixpacks, Railpack, Dockerfile, Buildpack options | dokploy, build-types, nixpacks, railpack, dockerfile |
| 050 | `050-docs-core-applications-advanced.md` | Advanced | Docker Swarm orchestration and resource management | dokploy, docker-swarm, resource-management, container-scaling |
| 051 | `051-docs-core-applications-preview-deployments.md` | Preview Deployments | GitHub PR-based isolated testing environments | dokploy, preview-deployments, github-integration, pull-requests |
| 052 | `052-docs-core-applications-rollbacks.md` | Rollbacks | Automatic and manual deployment rollbacks | dokploy, rollback, docker-swarm, health-checks |
| 053 | `053-docs-core-applications-zero-downtime.md` | Zero Downtime | Health check configuration for seamless updates | dokploy, zero-downtime, docker-swarm, health-check |
| 054 | `054-docs-core-applications-going-production.md` | Going Production | CI/CD optimization and production deployment | dokploy, ci-cd, github-actions, production-deployment |
| 055 | `055-docs-core-watch-paths.md` | Watch Paths | Automated deployments based on file changes | watch-paths, auto-deploy, glob-patterns, deployment-automation |
| 056 | `056-docs-core-schedule-jobs.md` | Schedule Jobs | Cron-based automated task scheduling | dokploy, scheduled-jobs, automation, cron-expressions |

### 9. Database Management (057-063)
*Database backup, restore, and connection management*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 057 | `057-docs-core-databases-backups.md` | Database Backups | Scheduled S3 backups for databases | dokploy, database-backups, s3-storage, cron-scheduling |
| 058 | `058-docs-core-databases-restore.md` | Restore | Database restoration from S3 backups | dokploy, database-restoration, s3-backup, postgresql |
| 059 | `059-docs-core-databases-connection.md` | Connection | Internal and external database connection setup | dokploy, database-connection, networking, security |
| 060 | `060-docs-core-databases-connection-mariadb.md` | MariaDB | Beekeeper Studio connection to MariaDB | dokploy, mariadb, beekeeper-studio, external-access |
| 061 | `061-docs-core-databases-connection-mysql.md` | MySQL | Beekeeper Studio connection to MySQL | dokploy, mysql, beekeeper-studio, database-management |
| 062 | `062-docs-core-databases-connection-mongo-atlas.md` | Mongo Compass | MongoDB Compass connection configuration | mongodb, mongo-compass, dokploy, database-connection |
| 063 | `063-docs-core-databases-connection-pg-admin.md` | PG Admin | pgAdmin connection to PostgreSQL | dokploy, postgresql, pgadmin, database-management |

### 10. Docker Compose Deep Dive (064-066)
*Advanced Docker Compose configuration and utilities*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 064 | `064-docs-core-docker-compose-example.md` | Example | Docker Compose deployment tutorial with Traefik | dokploy, docker-compose, traefik, deployment, networking |
| 065 | `065-docs-core-docker-compose-utilities.md` | Utilities | Isolated deployments and networking utilities | dokploy, docker-compose, isolated-deployments, networking |
| 066 | `066-docs-core-docker-compose-domains.md` | Domains | Domain configuration for Docker Compose apps | dokploy, docker-compose, domain-configuration, traefik-labels |

### 11. Domains & SSL Configuration (067-069)
*Custom domain and SSL certificate management*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 067 | `067-docs-core-domains-generated.md` | Generated Domains | Free HTTP domains using traefik.me | dokploy, domain-configuration, traefik-me, free-domains |
| 068 | `068-docs-core-domains-cloudflare.md` | Cloudflare | Cloudflare domain and SSL/TLS configuration | cloudflare, ssl-tls, lets-encrypt, https |
| 069 | `069-docs-core-domains-others.md` | Other Providers | External provider DNS and SSL setup | dokploy, dns-configuration, custom-domain, lets-encrypt |

### 12. Remote Servers & Clustering (070-076)
*Multi-server deployment and Docker Swarm clustering*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 070 | `070-docs-core-remote-servers.md` | Introduction | Remote server deployment and build servers overview | dokploy, remote-deployment, build-servers, infrastructure-management |
| 071 | `071-docs-core-remote-servers-instructions.md` | Deploy Server | Complete VPS deployment workflow | dokploy, remote-server, vps-deployment, ssh-keys |
| 072 | `072-docs-core-remote-servers-deployments.md` | Deployments | Remote server deployment configuration | remote-server, server-setup, deployment, bash-configuration |
| 073 | `073-docs-core-remote-servers-validate.md` | Validate | Server validation requirements and checks | dokploy, server-validation, deployment-server, docker-swarm |
| 074 | `074-docs-core-remote-servers-security.md` | Security | Firewall, SSH hardening, and Fail2Ban setup | dokploy, server-security, ufw, ssh-hardening, fail2ban |
| 075 | `075-docs-core-remote-servers-build-server.md` | Build Server | Dedicated build server configuration | dokploy, build-server, docker-registry, remote-servers |
| 076 | `076-docs-core-cluster.md` | Cluster | Docker Swarm horizontal and vertical scaling | dokploy, docker-swarm, horizontal-scaling, cluster-management |

### 13. Tutorials - Framework Deployment (077-093)
*Step-by-step deployment guides for popular frameworks*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 077 | `077-docs-core-html.md` | HTML | Static HTML site deployment | dokploy, html-deployment, static-site, git-integration |
| 078 | `078-docs-core-vuejs.md` | Vue.js | Vue.js application deployment | vuejs, deployment, git-provider, nixpacks |
| 079 | `079-docs-core-nextjs.md` | Next.js | Next.js application deployment | nextjs, deployment, git-integration, dokploy |
| 080 | `080-docs-core-astro.md` | Astro | Astro static site deployment | astro, deployment, git-integration, nixpacks |
| 081 | `081-docs-core-astro-ssr.md` | Astro SSR | Astro server-side rendering deployment | astro, ssr, dokploy, deployment, nixpacks |
| 082 | `082-docs-core-remix.md` | Remix | Remix application deployment | remix, deployment, git-integration, dokploy |
| 083 | `083-docs-core-nestjs.md` | Nest.js | Nest.js backend deployment | nest-js, deployment, git-provider, domain-setup |
| 084 | `084-docs-core-deno.md` | Deno | Deno application deployment | deno, deployment, dokploy, dockerfile |
| 085 | `085-docs-core-preact.md` | Preact | Preact application deployment | preact, deployment-guide, git-integration, nixpacks |
| 086 | `086-docs-core-solidjs.md` | Solid.js | Solid.js application deployment | solid-js, deployment, git-integration, nixpacks |
| 087 | `087-docs-core-svelte.md` | Svelte | Svelte application deployment | dokploy, svelte, deployment, git-integration |
| 088 | `088-docs-core-tanstack.md` | Tanstack | Tanstack application deployment | tanstack, deployment, git-provider, nixpacks |
| 089 | `089-docs-core-lit.md` | Lit | Lit web components deployment | lit, deployment, git-provider, nixpacks |
| 090 | `090-docs-core-qwik.md` | Qwik | Qwik application deployment | qwik, deployment, git-integration, environment-variables |
| 091 | `091-docs-core-turborepo.md` | Turborepo | Turborepo monorepo deployment | dokploy, turborepo, nixpacks, deployment, monorepo |
| 092 | `092-docs-core-vite-react.md` | Vite React | Vite React application deployment | vite, react, deployment, git-integration |
| 093 | `093-docs-core-11ty.md` | 11ty | Eleventy static site deployment | 11ty, deployment, static-site, git-integration |

### 14. Enterprise Features (094-100)
*SSO, licensing, and enterprise-grade features*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 094 | `094-docs-core-enterprise.md` | Introduction | Enterprise SSO, whitelabeling, audit logs overview | enterprise-features, sso, whitelabeling, audit-logs |
| 095 | `095-docs-core-enterprise-license-keys.md` | License Keys | Enterprise license activation and validation | dokploy, enterprise-license, license-activation |
| 096 | `096-docs-core-enterprise-sso.md` | Single Sign-On | OIDC and SAML SSO overview and providers | sso, oidc, saml, identity-management |
| 097 | `097-docs-core-enterprise-sso-auth0.md` | Auth0 | Auth0 SAML/OIDC SSO configuration | dokploy, auth0, saml, sso, identity-provider |
| 098 | `098-docs-core-enterprise-sso-azure.md` | Azure AD | Microsoft Entra ID OIDC/SAML SSO setup | sso, azure-ad, microsoft-entra-id, oidc, saml |
| 099 | `099-docs-core-enterprise-sso-keycloak.md` | Keycloak | Keycloak OpenID Connect SSO configuration | sso, keycloak, openid-connect, identity-provider |
| 100 | `100-docs-core-enterprise-sso-okta.md` | Okta | Okta OIDC/SAML SSO setup | sso, okta, oidc, saml, authentication |

### 15. Guides & Advanced Networking (101-103)
*Cloud provider integrations and advanced networking*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 101 | `101-docs-core-guides-ec2-instructions.md` | EC2 Instructions | AWS EC2 setup and Dokploy integration | aws-ec2, dokploy, ssh-keys, server-setup, cloud-hosting |
| 102 | `102-docs-core-guides-tailscale.md` | Tailscale | VPN-based secure server access | tailscale, dokploy, vpn, wireguard, networking |
| 103 | `103-docs-core-guides-cloudflare-tunnels.md` | Cloudflare Tunnels | Secure tunneling without open ports | cloudflare-tunnel, dokploy, zero-trust, networking, traefik |

### 16. Permissions & Reference (104)
*User management and role-based access control*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 104 | `104-docs-core-permissions.md` | Permissions | User roles and access control management | user-management, role-based-access-control, permissions, user-roles |

---

## Quick Reference

### By Topic

| Topic | File Range |
|-------|------------|
| **Getting Started** | 001-014 |
| **Core Concepts** | 014-022 |
| **Git Integration** | 023-028 |
| **Storage & Backups** | 032-038 |
| **Notifications** | 039-048 |
| **Application Management** | 049-056 |
| **Database Operations** | 057-063 |
| **Docker Compose** | 064-066 |
| **Domain Configuration** | 067-069 |
| **Multi-Server** | 070-076 |
| **Framework Tutorials** | 077-093 |
| **Enterprise** | 094-100 |

### By Category (Original)

| Category | Files |
|----------|-------|
| **concept** | 001, 002, 005 |
| **reference** | 003, 004, 007, 104 |
| **tutorial** | 008, 064, 077-093 |
| **guide** | 009-013, 015-019, 025-028, 037, 051, 054, 057-058, 070-076, 094, 101-103 |
| **configuration** | 020-024, 029-036, 038-050, 052-053, 055-056, 059-063, 065-069, 095-100 |

---

## Learning Path

### Level 1: Foundation (Start Here)
- Read files **001-007** for introduction and overview
- Complete files **008-014** for installation and setup

### Level 2: Core Understanding
- Learn core concepts from files **014-022**
- Configure providers with files **019-028**

### Level 3: Practical Application
- Set up storage and backups: **032-038**
- Configure notifications: **039-048**
- Follow framework tutorials: **077-093**

### Level 4: Advanced Usage
- Master application management: **049-056**
- Configure multi-server deployments: **070-076**
- Set up Docker Compose: **064-066**

### Level 5: Enterprise & Reference
- Configure enterprise features: **094-100**
- Review permissions: **104**
- Consult guides: **101-103**

---

*This index is auto-generated and optimized for AI agent search. Files are numbered sequentially following a logical learning progression.*