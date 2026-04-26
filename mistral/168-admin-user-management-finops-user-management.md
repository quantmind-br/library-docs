---
title: User management | Mistral Docs
url: https://docs.mistral.ai/admin/user-management-finops/user-management
source: sitemap
fetched_at: 2026-04-26T04:01:11.707594196-03:00
rendered_js: false
word_count: 568
summary: This document provides instructions for managing organization members, including inviting users, assigning roles, managing product seats, and removing or deactivating accounts.
tags:
    - user-management
    - admin-panel
    - access-control
    - role-based-access
    - subscription-management
    - organization-administration
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# User Management

Add, manage, and remove users within your Organization. Assign roles to control access to products and administrative functions, and manage seats to grant access to paid features.

> [!info]
> Available on **Team** and **Enterprise** plans. Requires the **Admin** role.

## Inviting Members

1. Open [Admin Members](https://admin.mistral.ai).
2. Click **Invite members**.
3. Enter one or more email addresses (comma-separated).
4. Choose a role (**Admin**, **Billing**, or **Member**) for all invitees.
5. Assign product seats based on your subscription.
6. Send the invitations.

Invitees receive an email with instructions to join. You can resend or revoke an invitation before acceptance.

With [email domain authentication](https://docs.mistral.ai/admin/security-access/email-domain-auth) enabled, users with matching domain emails join automatically on sign-up.

## Invitation Flow

1. Invitee receives email from Mistral with a **Join Organization** link.
2. Clicking the link opens sign-up/sign-in. Existing users sign in; new users create an account.
3. After authenticating, invitee joins the Organization with the assigned role.
4. Assigned product seats activate immediately.

> [!note]
> Invitations expire after **7 days**. Resend from the **Members** panel if needed.

### Managing Pending Invitations

| Action | How |
|--------|-----|
| **Resend** | Click the resend icon. Original link is invalidated. |
| **Revoke** | Click the revoke icon. Original link stops working. |
| **Re-invite removed user** | Previously removed users can be re-invited with fresh role and seat. |

## Managing Product Seats

Seats control access to paid products (Le Chat Team/Enterprise, Mistral Code).

1. Find the user in [Admin Members](https://admin.mistral.ai) (search by name or email).
2. In the product column, set dropdown to **Active** to grant access, or **Inactive** to revoke.
3. Changes apply immediately.

> [!info]
> Number of available seats appears at the top of each product column. If you need more seats, contact [support](https://help.mistral.ai).

- **Reassignment**: set user's seat to **Inactive** to free it, then assign to another user.
- **Role independence**: product seats are separate from Organization roles.
- **Deactivation**: deactivating a seat removes product access but keeps Organization membership.

## Roles

The system assigns **Member** role by default. Change roles from the **Members** panel. Role changes take effect immediately.

Workspace roles are independent from Organization roles. A user with **Billing** role at Organization level can be an **Admin** within a specific workspace. See [Organizations and workspaces](https://docs.mistral.ai/admin/security-access/organization).

## Removing Members

To remove a member, click **Remove** next to their name and confirm.

> [!warning]
> Removal is immediate. The user loses access to the Organization and all its resources. Resources they created remain available to other Organization members. You cannot remove the last **Admin**.

Removed members can rejoin if re-invited.

## Leaving an Organization

Any user can leave (unless they are the last **Admin**):

1. Go to [Admin Members](https://admin.mistral.ai).
2. Find your own entry.
3. Click **Remove** next to your name and confirm.

> [!warning]
> Leaving is permanent. You must be re-invited to rejoin.

#user-management #admin-panel #access-control #role-based-access
