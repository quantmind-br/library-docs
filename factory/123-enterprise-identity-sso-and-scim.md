---
title: Identity, Domains, SSO, and SCIM - Factory Documentation
url: https://docs.factory.ai/enterprise/identity-sso-and-scim
source: sitemap
fetched_at: 2026-01-13T19:04:02.187131472-03:00
rendered_js: false
word_count: 1979
summary: This guide explains how to configure and manage enterprise identity within Factory using WorkOS, covering domain verification, SSO/SAML integration, and automated user provisioning via Directory Sync.
tags:
    - sso
    - saml
    - scim
    - identity-management
    - domain-verification
    - provisioning
    - oidc
category: guide
---

Factory provides comprehensive enterprise identity management through Single Sign-On (SSO) using SAML/OIDC protocols and automated user provisioning via Directory Sync (SCIM). This guide covers how these systems work together to manage user identities, authentication, and access control.

## Overview

Factory uses **WorkOS** to handle enterprise identity management, supporting:

- **Domain Verification**: Establish ownership of your email domains for identity governance
- **SSO/SAML**: Authenticate users through your Identity Provider (IdP)
- **Directory Sync/SCIM**: Automatically provision and manage users from your directory
- **Just-In-Time (JIT) Provisioning**: Create users on first login via SSO
- **Group-based Access Control**: Manage permissions through directory groups

## How It Works

### Domain Verification (Required First)

Before enabling SSO or Directory Sync:

1. **Verify ownership** of your email domains through DNS validation
2. **Claim existing users** - All users with your domain automatically join your organization
3. **Set policies** - Configure MFA, session management, and access controls
4. **Enable SSO/SCIM** - Now ready for enterprise identity management

### Authentication with SSO

When SSO is enabled:

1. Users click “Sign in with SSO” instead of entering a password
2. They’re redirected to your corporate identity provider (Okta, Azure AD, etc.)
3. After authenticating with their corporate credentials, they’re logged into Factory
4. First-time users are automatically created if JIT provisioning is enabled

### User Provisioning with Directory Sync

When Directory Sync (SCIM) is enabled:

- **Adding users** to your directory automatically creates them in Factory
- **Updating** user information syncs to Factory in real-time
- **Removing users** from your directory revokes their Factory access
- **Group changes** automatically update user permissions

### Data Priority

When users exist from multiple sources (SSO, Directory Sync, manual invite), Factory follows this priority:

1. **Directory Sync data always wins** - Information from your directory overwrites other sources
2. **Users are matched by email** - We find existing users by email address (case-insensitive)
3. **Custom data is preserved** - Factory-specific settings that don’t exist in your directory are kept
4. **Soft deletes** - Removed users are deactivated, not deleted, preserving their work history

## Prerequisites

Before setting up Domains, SSO, and SCIM:

- You are on a plan that includes **enterprise SSO support**
- Your organization’s **email domains must be verified** (see Domain Verification below)
- You have **admin access** to your IdP (or a partner in IT who does)
- You have a **Factory admin** who can coordinate configuration on the Factory side
- Contact your Factory representative to initiate the setup process

## Setup Process Overview

### Initial Setup Flow

### Setup Options

During setup, you’ll configure:

## Domain Verification

### Why Domain Verification Matters

Domain verification is a **mandatory prerequisite** for enabling SSO and establishing your organization’s identity governance in Factory. It proves your organization owns and controls specific email domains, creating a secure foundation for enterprise identity management.

### What Domain Verification Enables

Once your domain is verified, your organization gains powerful administrative controls:

#### Identity Governance

- **Mandatory SSO enforcement** - Require all users with your domain to authenticate via SSO
- **Automatic user claiming** - Existing Factory users with your domain automatically join your organization
- **Email domain restrictions** - Prevent unauthorized accounts from using your domain
- **Guest user policies** - Define how external collaborators can access your organization

#### Security Policies

- **MFA requirements** - Enforce multi-factor authentication for all domain users
- **Password policies** - Set complexity requirements for non-SSO authentication methods
- **Session management** - Control session duration and idle timeout settings
- **IP restrictions** - Limit access to specific IP ranges or VPN endpoints

#### Compliance Controls

- **Audit logging** - Track all authentication events for domain users
- **Data residency** - Ensure user data stays within specified geographic regions
- **Access reviews** - Periodic certification of user access rights
- **Deprovisioning workflows** - Automated removal of access when users leave

### Configuring Domain Verification

#### What Happens After Verification

Once your domain is verified:

- **Immediate effect** - All existing users with your domain email are associated with your organization
- **Automatic claiming** - New users with your domain join your organization by default
- **Policy enforcement** - Your configured security policies apply instantly
- **SSO readiness** - You can proceed with SSO configuration for verified domains

### Multiple Domain Support

Organizations often need to verify multiple domains:

- **Primary domain** - Your main corporate email domain
- **Subsidiary domains** - Acquired companies or regional offices
- **Legacy domains** - Historical domains still in use
- **Alias domains** - Alternative spellings or shortened versions

Each domain requires separate verification but shares the same organizational policies once verified.

### Domain Verification Best Practices

### Common Issues and Solutions

IssueCauseSolutionVerification fails after 24 hoursDNS record not properly addedCheck exact formatting and placement of TXT recordUsers can’t access after verificationDomain policies too restrictiveReview and adjust enforcement settingsSubsidiary users not includedDomain not verifiedAdd and verify all subsidiary domainsExternal collaborators blockedStrict domain enforcementConfigure guest user exceptions

## Single Sign-On (SSO)

### How SSO Works

1. User attempts to log in to Factory
2. Redirected to your Identity Provider (IdP)
3. User authenticates with corporate credentials
4. IdP sends SAML assertion back to Factory
5. User is authenticated and provisioned if needed (see JIT below)

### Supported SSO Providers

Factory supports integration with all major identity providers through WorkOS. Select your provider during setup:

#### Popular SSO Providers

- SAML Providers
- OIDC Providers
- Enterprise Platforms
- Generic Options

<!--THE END-->

- **Okta** - Full SAML 2.0 and SCIM support - **Microsoft Azure AD / Entra ID** - SAML and OIDC with SCIM - **Google Workspace** - SAML 2.0 with Google Groups mapping - **OneLogin** - SAML 2.0 and SCIM provisioning - **Ping Identity / PingOne** - Enterprise SAML federation - **JumpCloud** - SAML with cross-directory support - **CyberArk** - SAML with privileged access management - **Duo (Cisco)** - SAML with MFA integration

<!--THE END-->

- **Auth0** - Universal OIDC with custom rules - **Keycloak** - Open-source OIDC provider - **AWS Cognito** - OIDC with AWS integration - **Firebase Auth** - Google’s OIDC implementation - **FusionAuth** - Developer-focused OIDC

<!--THE END-->

- **Salesforce Identity** - SAML for Salesforce orgs - **VMware Workspace ONE** - Enterprise mobility + SAML - **IBM Security Verify** - Enterprise SAML/OIDC - **Oracle Identity Cloud** - Oracle ecosystem integration - **RSA SecurID** - SAML with token-based MFA

<!--THE END-->

- **Generic SAML 2.0** - Any SAML-compliant IdP
- **Generic OIDC** - Any OpenID Connect provider
- **ADFS** - Microsoft Active Directory Federation Services
- **Shibboleth** - Academic/research institution SSO
- **SimpleSAMLphp** - Open-source SAML implementation

#### Magic Link Alternative

If your organization doesn’t use SSO, Factory also supports:

- **Magic Link Authentication** - Passwordless email-based login
- Can be used alongside SSO for external collaborators

### Just-In-Time (JIT) Provisioning

When SSO is enabled with JIT provisioning:

- Users are automatically created on first successful login
- User profile is populated from SAML attributes
- Organization membership is created automatically
- No manual user invitation required

### Configuring SSO

#### What You Need to Prepare

Before starting SSO setup:

1. **Admin access** to your identity provider
2. **Test users** - Create a pilot group (e.g., `factory-pilot-users`) to test before organization-wide rollout
3. **Group strategy** - Decide which IdP groups map to Factory roles:
   
   - Admin groups (e.g., `factory-admins`)
   - Member groups (e.g., `factory-developers`)
   - Read-only groups (e.g., `factory-viewers`)

#### How Setup Works

#### Group-to-Role Mapping

During setup, you’ll configure how your IdP groups map to Factory roles:

Your IdP GroupMaps to Factory RolePermissions`factory-admins`AdminFull access, manage users and settings`factory-developers`MemberCreate and edit content, use all features`factory-viewers`ViewerRead-only access`factory-contractors`MemberSame as developers, but easier to track

#### Testing Your Integration

After configuration, test with your pilot group:

1. Have a test user sign in via SSO from the Factory login page
2. Initiate login from the Factory sign‑in page using “Sign in with SSO” / your IdP button.
3. Verify that:
   
   - The user is redirected to the IdP, authenticates, and returns to Factory.
   - The user lands in the correct org/team with the expected role.

If anything fails, check the IdP’s logs and Factory’s error message; most issues are due to mismatched URLs, certificates, or attribute mappings.

* * *

## Directory Sync (SCIM) Provisioning

SSO controls **how users authenticate**; SCIM controls **which users and groups exist** in Factory. With SCIM enabled:

- New employees in relevant IdP groups get access to Factory automatically.
- Users removed from those groups lose access automatically.
- Group membership changes propagate into Factory without manual updates.

### Supported Directory Sync Providers

Factory supports SCIM 2.0 provisioning from these directory providers:

- Full SCIM Support
- Partial Support
- Custom Integration

**Providers with complete SCIM 2.0 implementation:**

- **Okta** - Real-time provisioning with Okta Universal Directory
- **Microsoft Azure AD / Entra ID** - Enterprise directory sync
- **OneLogin** - User and group provisioning
- **JumpCloud** - Cross-platform directory services
- **Google Workspace** - Google Groups and organizational units
- **PingOne** - PingDirectory integration
- **CyberArk** - Privileged access provisioning

**Providers with limited SCIM features:**

- **Rippling** - HR-driven provisioning
- **BambooHR** - Employee lifecycle management
- **Workday** - HCM-based provisioning
- **AWS SSO** - AWS Identity Center provisioning

Note: These providers may require additional configuration or have limitations on group management.

**Build your own SCIM integration:**

- **Generic SCIM 2.0** - Any SCIM-compliant directory
- **Custom SCIM Endpoint** - Your internal user directory
- **LDAP Bridge** - Connect legacy LDAP/AD via SCIM gateway
- **CSV Upload** - Manual bulk provisioning (not real-time)

### SCIM Features by Provider

ProviderUsersGroupsReal-timeNested GroupsCustom AttributesOkta✅✅✅✅✅Azure AD / Entra ID✅✅✅✅✅Google Workspace✅✅✅❌PartialOneLogin✅✅✅❌✅JumpCloud✅✅✅✅✅Rippling✅Partial✅❌PartialGeneric SCIM✅✅VariesVariesVaries

### Configuring Directory Sync

#### What You Need to Prepare

Before enabling SCIM:

1. **Decide which groups to sync** - Not all IdP groups need Factory access
2. **Plan your group structure** - Consider teams, roles, and access levels
3. **Identify service accounts** - Separate human users from CI/CD accounts
4. **Review existing users** - Understand how they’ll be affected when SCIM takes over

Treat the SCIM token as a secret; store it only in your IdP’s application configuration.

#### How SCIM Setup Works

#### Configuring SCIM in Your IdP

In your IdP’s SCIM settings for the Factory application:

1. Enable **automatic provisioning**.
2. Paste the **SCIM base URL** and **SCIM token** from Factory.
3. Choose which users and groups to sync (for example, only `factory-*` groups).
4. Configure attribute mappings if required (for example, `userName` → email, `displayName` → name).

Once enabled, your IdP will start pushing users and groups to Factory and keep them synchronized.

#### What Happens When SCIM is Enabled

With SCIM in place, group management should happen **only in your IdP**. Use group naming and mapping rules such as:

- `factory-org-owners` → Factory org Owners.
- `factory-org-admins` → Factory org Admins.
- `factory-users` → Factory Members.
- `factory-ci-bots` → machine/service accounts with restricted permissions.

This keeps RBAC definitions in one place (your IdP) and lets you audit them alongside other enterprise apps.

## Data Management and Merging

### User Identity Sources

Factory users can originate from multiple sources:

- **Directory Sync**: Automatically provisioned via SCIM
- **SSO JIT**: Created on first SSO login
- **Manual Invitation**: Added by administrators
- **API**: Created programmatically

### Merging Strategy

When users exist from multiple sources, Factory follows these rules:

1. **Directory data takes precedence** - SCIM attributes override all other sources
2. **Email-based matching** - Users matched by email (case-insensitive)
3. **Soft deletes only** - Users deactivated, not deleted, preserving audit trails
4. **Profile preservation** - Non-directory fields retained during updates

## Conflict Resolution

### SSO vs Directory Sync

When both are enabled, potential conflicts include: **Scenario**: User logs in via SSO before directory provisions them  
**Resolution**: Directory sync merges with SSO user on next sync **Best Practice**: Choose one primary method:

- **Directory-first**: Disable JIT, require directory provisioning
- **SSO-first**: Use JIT for creation, directory for updates

### Email Case Sensitivity

All email matching is case-insensitive:

- `John.Doe@company.com` = `john.doe@company.com`
- Prevents duplicate users from case variations
- Emails normalized to lowercase for comparison

* * *

## Troubleshooting & best practices

Common issues and recommendations:

- **Login loops or failures**
  
  - Verify ACS / redirect URLs exactly match what Factory provided.
  - Confirm certificates or signing keys have not expired or been rotated without updating Factory.
- **User lands in wrong org or role**
  
  - Check group memberships and mapping rules.
  - Ensure the intended groups are included in SAML assertions or ID tokens.
- **Provisioning not working**
  
  - Confirm SCIM is enabled in both Factory and your IdP.
  - Check SCIM logs in your IdP for errors (invalid token, URL, or schema).

Best practices:

- Keep a **small pilot group** for initial rollout and future changes.
- Use **clear, prefix‑based group names** (for example, `factory-*`) to keep IdP configuration maintainable.
- Manage all role changes and access reviews in your IdP to leverage existing governance processes.

Once SSO and SCIM are in place, the **Identity & Access Management** overview explains how these identities are enforced at runtime for Droids.