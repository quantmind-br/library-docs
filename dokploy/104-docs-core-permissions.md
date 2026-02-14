---
title: Permissions | Dokploy
url: https://docs.dokploy.com/docs/core/permissions
source: crawler
fetched_at: 2026-02-14T14:19:16.591102-03:00
rendered_js: true
word_count: 342
summary: This document describes the user management system in Dokploy, outlining the specific capabilities and restrictions for Owner, Admin, and Member roles. It details granular permissions for members, including project, service, and environment-level access controls.
tags:
    - user-management
    - role-based-access-control
    - dokploy
    - permissions
    - user-roles
    - access-control
category: reference
---

Users

Add permissions to your users to manage your applications and services.

Manage user roles and permissions within Dokploy. Dokploy handles three distinct roles with different levels of access and capabilities.

Dokploy supports three roles for managing user access:

### [Owner](#owner)

The **Owner** is the creator of the organization and has the highest level of access:

- Full administrative privileges
- Can perform all actions that admins can do
- Can delete and edit the role of admins
- **Intransferable**: The owner role cannot be transferred to another user
- Only one owner exists per organization

### [Admin](#admin)

**Admin** users have extensive administrative capabilities:

- Can perform all actions that the owner can do
- Full access to all features and settings
- **Limitations**: Cannot delete or edit the role of other admins
- **Limitations**: Cannot delete or edit the role of the owner

### [Members](#members)

**Members** are regular users who have access based on the permissions assigned to them. Members can be granted specific permissions to manage applications and services.

#### [Permissions](#permissions)

The following permissions are available for **Members** to manage your users effectively:

- **Create Projects**: Allow the user to create projects.
- **Delete Projects**: Allow the user to delete projects.
- **Create Services**: Allow the user to create services.
- **Delete Services**: Allow the user to delete services.
- **Create Environments**: Allow the user to create environments.
- **Delete Environments**: Allow the user to delete environments.
- **Access to Traefik Files**: Allow the user to access to the Traefik Tab Files.
- **Access to Docker**: Allow the user to access to the Docker Tab.
- **Access to API/CLI**: Allow the user to access to the API/CLI.
- **Access to SSH Keys**: Allow to users to access to the SSH Keys section.
- **Access to Git Providers**: Allow to users to access to the Git Providers section.

You can also grant permissions to specific users for accessing particular projects or services.

#### [Project Permissions](#project-permissions)

Based on your projects and services, you can assign permissions to specific users to give them access to particular projects or services. You can also select specific environments within projects, allowing you to grant granular access control at the environment level.