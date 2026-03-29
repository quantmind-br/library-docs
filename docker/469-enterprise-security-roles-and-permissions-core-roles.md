---
title: Core roles
url: https://docs.docker.com/enterprise/security/roles-and-permissions/core-roles/
source: llms
fetched_at: 2026-01-24T14:26:58.065120242-03:00
rendered_js: false
word_count: 334
summary: This document outlines the predefined permissions and access levels for Docker's core organization roles, including Member, Editor, and Owner across repository management and administrative tasks.
tags:
    - docker-roles
    - access-control
    - organization-management
    - user-permissions
    - docker-administration
    - role-based-access
category: reference
---

Table of contents

* * *

Core roles are Docker's built-in roles with predefined permission sets. This page provides an overview of Docker's core roles and permissions for each role.

## [What are core roles?](#what-are-core-roles)

Docker organizations have three core roles:

- **Member**: Non-administrative role with basic access. Members can view other organization members and pull images from repositories they have access to.
- **Editor**: Partial administrative access. Editors can create, edit, and delete repositories. They can also manage team permissions for repositories.
- **Owner**: Full administrative access. Owners can manage all organization settings, including repositories, teams, members, billing, and security features.

> Note
> 
> A company owner has the same organization management permissions as an organization owner, but there are some content and registry permissions that company owners don't have (for example, repository pull/push). For more information, see [Company overview](https://docs.docker.com/admin/company/).

### [Content and registry permissions](#content-and-registry-permissions)

These permissions apply organization-wide, including all repositories in your organization's namespace.

PermissionMemberEditorOwnerExplore images and extensions✅✅✅Star, favorite, vote, and comment on content✅✅✅Pull images✅✅✅Create and publish an extension✅✅✅Become a Verified, Official, or Open Source publisher❌❌✅Edit and delete publisher repository logos❌✅✅Observe content engagement as a publisher❌❌✅Create public and private repositories❌✅✅Edit and delete repositories❌✅✅Manage tags❌✅✅View repository activity❌❌✅Set up Automated builds❌❌✅Edit build settings❌❌✅View teams✅✅✅Assign team permissions to repositories❌✅✅

When you add members to teams, you can grant additional repository permissions beyond their organization role:

1. Role permissions: Applied organization-wide (member or editor)
2. Team permissions: Additional permissions for specific repositories

### [Organization management permissions](#organization-management-permissions)

PermissionMemberEditorOwnerCreate teams❌❌✅Manage teams (including delete)❌❌✅Configure the organization's settings (including linked services)❌❌✅Add organizations to a company❌❌✅Invite members❌❌✅Manage members❌❌✅Manage member roles and permissions❌❌✅View member activity❌❌✅Export and reporting❌❌✅Image Access Management❌❌✅Registry Access Management❌❌✅Set up Single Sign-On (SSO) and SCIM❌❌✅ \*Require Docker Desktop sign-in❌❌✅ \*Manage billing information (for example, billing address)❌❌✅Manage payment methods (for example, credit card or invoice)❌❌✅View billing history❌❌✅Manage subscriptions❌❌✅Manage seats❌❌✅Upgrade and downgrade plans❌❌✅

** If not part of a company*

### [Docker Scout permissions](#docker-scout-permissions)

PermissionMemberEditorOwnerView and compare analysis results✅✅✅Upload analysis records✅✅✅Activate and deactivate Docker Scout for a repository❌✅✅Create environments❌❌✅Manage registry integrations❌❌✅

### [Docker Build Cloud permissions](#docker-build-cloud-permissions)

PermissionMemberEditorOwnerUse a cloud builder✅✅✅Create and remove builders✅✅✅Configure builder settings✅✅✅Buy minutes❌❌✅Manage subscription❌❌✅