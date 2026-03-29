---
title: Role-Based Access Control
url: https://docs.getbifrost.ai/enterprise/rbac.md
source: llms
fetched_at: 2026-01-21T19:43:31.482509854-03:00
rendered_js: false
word_count: 909
summary: Explains how to implement and manage Role-Based Access Control (RBAC) in Bifrost to provide fine-grained access management for users and resources.
tags:
    - rbac
    - access-control
    - permissions
    - user-management
    - governance
    - enterprise-security
category: guide
---

# Role-Based Access Control

> Manage user access with fine-grained permissions across Bifrost resources using roles and permissions.

## Overview

Role-Based Access Control (RBAC) in Bifrost Enterprise provides fine-grained access management for your organization. RBAC allows you to define roles with specific permissions, controlling what users can view, create, update, or delete across all Bifrost resources.

**Key Benefits:**

* **Principle of Least Privilege** - Grant users only the permissions they need
* **Centralized Access Management** - Manage all permissions from a single interface
* **Audit-Ready** - Track who has access to what for compliance requirements
* **Flexible Role Design** - Use system roles or create custom roles for your organization

RBAC integrates seamlessly with [Identity Provider authentication](./advanced-governance#identity-provider-integration), automatically assigning roles based on your IdP groups and claims.

***

## Roles & Permissions

Navigate to **Governance** → **Roles & Permissions** in the Bifrost dashboard to manage roles.

<Frame>
  <img src="https://mintcdn.com/bifrost/YVPOKLjzRQBF-BaY/media/rbac/rbac-list.png?fit=max&auto=format&n=YVPOKLjzRQBF-BaY&q=85&s=71a3815ef0024cea85fc7b7a77e50aef" alt="Roles & Permissions management interface showing system roles" data-og-width="3504" width="3504" data-og-height="2120" height="2120" data-path="media/rbac/rbac-list.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/YVPOKLjzRQBF-BaY/media/rbac/rbac-list.png?w=280&fit=max&auto=format&n=YVPOKLjzRQBF-BaY&q=85&s=103c339597dd9680b30c4d00ae7dd36d 280w, https://mintcdn.com/bifrost/YVPOKLjzRQBF-BaY/media/rbac/rbac-list.png?w=560&fit=max&auto=format&n=YVPOKLjzRQBF-BaY&q=85&s=f3ab2f78c097a04f2651e1859cbf857f 560w, https://mintcdn.com/bifrost/YVPOKLjzRQBF-BaY/media/rbac/rbac-list.png?w=840&fit=max&auto=format&n=YVPOKLjzRQBF-BaY&q=85&s=bc394b287fc52c49e044c93399cb5946 840w, https://mintcdn.com/bifrost/YVPOKLjzRQBF-BaY/media/rbac/rbac-list.png?w=1100&fit=max&auto=format&n=YVPOKLjzRQBF-BaY&q=85&s=4855ca50a477ee74fd17e8661832a426 1100w, https://mintcdn.com/bifrost/YVPOKLjzRQBF-BaY/media/rbac/rbac-list.png?w=1650&fit=max&auto=format&n=YVPOKLjzRQBF-BaY&q=85&s=4ed21aab750d27fd418a5c1bfe64cb28 1650w, https://mintcdn.com/bifrost/YVPOKLjzRQBF-BaY/media/rbac/rbac-list.png?w=2500&fit=max&auto=format&n=YVPOKLjzRQBF-BaY&q=85&s=022210f1737e50e8cbd942c272f4ebb3 2500w" />
</Frame>

### System Roles

Bifrost includes three pre-configured system roles that cover common access patterns:

| Role          | Permissions | Description                                                         |
| ------------- | ----------- | ------------------------------------------------------------------- |
| **Admin**     | 42          | Full access to all resources and operations                         |
| **Developer** | 27          | CRUD access to technical resources, view access to logs and cluster |
| **Viewer**    | 14          | Read-only access to all resources                                   |

System roles cannot be deleted, but their permissions can be customized to fit your organization's needs.

### Custom Roles

Create custom roles when system roles don't match your organizational structure. Custom roles are useful for:

* **Specialized Teams** - Create roles for QA, Security, or Compliance teams
* **Project-Based Access** - Limit access to specific resources per project
* **Temporary Access** - Grant limited permissions for contractors or auditors

**To create a custom role:**

1. Click **Add Role** in the top-right corner
2. Enter a **Role Name** (e.g., "Auditor", "QA Team")
3. Add a **Description** explaining the role's purpose
4. Click **Create Role**
5. Assign permissions using the Manage Permissions dialog

***

## Resources & Operations

RBAC permissions are defined as combinations of **Resources** and **Operations**.

### Protected Resources

Bifrost protects access to the following resources:

| Resource             | Description                          |
| -------------------- | ------------------------------------ |
| **Logs**             | Request and response logs            |
| **ModelProvider**    | AI model provider configurations     |
| **Observability**    | Monitoring and metrics dashboards    |
| **Plugins**          | Plugin configurations and management |
| **VirtualKeys**      | Virtual key management               |
| **UserProvisioning** | User and group provisioning settings |
| **Users**            | User account management              |
| **AuditLogs**        | Audit trail and compliance logs      |
| **GuardrailsConfig** | Guardrail configurations             |
| **GuardrailRules**   | Individual guardrail rules           |
| **Cluster**          | Cluster configuration and nodes      |
| **Settings**         | Workspace settings                   |
| **MCPGateway**       | MCP Gateway configurations           |
| **AdaptiveRouter**   | Adaptive routing settings            |

### Operations

Each resource supports up to four operations:

| Operation  | Description                                     |
| ---------- | ----------------------------------------------- |
| **View**   | Read-only access to view the resource           |
| **Create** | Ability to create new instances of the resource |
| **Update** | Ability to modify existing resources            |
| **Delete** | Ability to remove resources                     |

***

## Managing Permissions

To assign or modify permissions for a role:

1. Navigate to **Governance** → **Roles & Permissions**
2. Click the **menu icon** (•••) on the role you want to modify
3. Select **Manage Permissions**

<Frame>
  <img src="https://mintcdn.com/bifrost/YVPOKLjzRQBF-BaY/media/rbac/rbac-edit-role.png?fit=max&auto=format&n=YVPOKLjzRQBF-BaY&q=85&s=0963a9d03f605399dd8c9fa84195ab5e" alt="Manage Permissions dialog showing resource-based permission assignment" data-og-width="3504" width="3504" data-og-height="2126" height="2126" data-path="media/rbac/rbac-edit-role.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/YVPOKLjzRQBF-BaY/media/rbac/rbac-edit-role.png?w=280&fit=max&auto=format&n=YVPOKLjzRQBF-BaY&q=85&s=5bebffc86b274eff6d3f881d889e4f08 280w, https://mintcdn.com/bifrost/YVPOKLjzRQBF-BaY/media/rbac/rbac-edit-role.png?w=560&fit=max&auto=format&n=YVPOKLjzRQBF-BaY&q=85&s=e0a3e729f2bd670bffc786b7a7c8b884 560w, https://mintcdn.com/bifrost/YVPOKLjzRQBF-BaY/media/rbac/rbac-edit-role.png?w=840&fit=max&auto=format&n=YVPOKLjzRQBF-BaY&q=85&s=b3ff161524ab9083d853fb158806659f 840w, https://mintcdn.com/bifrost/YVPOKLjzRQBF-BaY/media/rbac/rbac-edit-role.png?w=1100&fit=max&auto=format&n=YVPOKLjzRQBF-BaY&q=85&s=105b967ceba370b99a3c37ff449219ab 1100w, https://mintcdn.com/bifrost/YVPOKLjzRQBF-BaY/media/rbac/rbac-edit-role.png?w=1650&fit=max&auto=format&n=YVPOKLjzRQBF-BaY&q=85&s=406c990524f6a01583bfd55311d1736a 1650w, https://mintcdn.com/bifrost/YVPOKLjzRQBF-BaY/media/rbac/rbac-edit-role.png?w=2500&fit=max&auto=format&n=YVPOKLjzRQBF-BaY&q=85&s=cb2ca9d2114f535a7a75414f2bb3cccd 2500w" />
</Frame>

The Manage Permissions dialog provides a two-panel interface:

**Left Panel - Resources:**

* Lists all available resources
* Shows the count of enabled permissions per resource (e.g., "4/4 permissions")
* Click a resource to view its permissions

**Right Panel - Permissions:**

* Displays available operations for the selected resource
* Toggle switches to enable/disable each permission
* Shows operation descriptions for clarity

### Assigning Permissions

1. Select a **Resource** from the left panel
2. Toggle the **operations** you want to enable for this role
3. Repeat for other resources as needed
4. Click **Save Permissions** to apply changes

The footer shows the total permissions count (e.g., "42 of 42 permissions selected") to help track the role's access level.

***

## Best Practices

### Role Design

* **Start with System Roles** - Use Admin, Developer, and Viewer as templates
* **Follow Least Privilege** - Only grant permissions that are necessary
* **Document Role Purpose** - Use clear descriptions to explain each role's intent
* **Review Regularly** - Audit role assignments quarterly

### Permission Strategies

**For Development Teams:**

```
Developer role + specific resource access based on team focus
- Frontend team: VirtualKeys (View), Logs (View), Observability (View)
- Backend team: ModelProvider (CRUD), Plugins (CRUD), Logs (View)
```

**For Security/Compliance Teams:**

```
Custom "Auditor" role with:
- AuditLogs (View)
- Logs (View)
- GuardrailsConfig (View)
- Users (View)
```

**For Operations Teams:**

```
Custom "Ops" role with:
- Cluster (CRUD)
- Observability (View)
- Logs (View)
- Settings (View, Update)
```

***

## Integration with Identity Providers

When using [Okta](./setting-up-okta) or [Microsoft Entra](./setting-up-entra) for authentication, roles can be automatically assigned based on:

* **IdP Groups** - Map identity provider groups to Bifrost roles
* **App Roles** - Sync application roles from your IdP
* **Claims** - Use custom claims to determine role assignment

Users authenticated via SSO receive their role assignments automatically on first login, with permissions synchronized on each session.

***

## API Access

Roles and permissions can also be managed via the API:

**List all roles:**

```bash  theme={null}
curl -X GET http://localhost:8080/api/roles \
  -H "Authorization: Bearer <admin_token>"
```

**Get role permissions:**

```bash  theme={null}
curl -X GET http://localhost:8080/api/roles/{role_id}/permissions \
  -H "Authorization: Bearer <admin_token>"
```

**Update role permissions:**

```bash  theme={null}
curl -X PUT http://localhost:8080/api/roles/{role_id}/permissions \
  -H "Authorization: Bearer <admin_token>" \
  -H "Content-Type: application/json" \
  -d '{
    "permission_ids": [1, 2, 3, 4, 5]
  }'
```

**Create a custom role:**

```bash  theme={null}
curl -X POST http://localhost:8080/api/roles \
  -H "Authorization: Bearer <admin_token>" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Auditor",
    "description": "Read-only access for compliance auditing"
  }'
```

***

## Next Steps

* **[Setting up Okta](./setting-up-okta)** - Configure Okta for SSO with role sync
* **[Setting up Microsoft Entra](./setting-up-entra)** - Configure Entra ID for SSO with role sync
* **[Audit Logs](./audit-logs)** - Track permission usage and access patterns
* **[Advanced Governance](./advanced-governance)** - Learn about the complete governance framework


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt