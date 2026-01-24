---
title: Activity logs
url: https://docs.docker.com/admin/organization/activity-logs/
source: llms
fetched_at: 2026-01-24T14:13:06.95929088-03:00
rendered_js: false
word_count: 938
summary: This document explains how Docker administrators can access and filter activity logs to monitor organizational, repository, and billing-related events. It provides a comprehensive reference of trackable actions and instructions for viewing logs within Docker Home.
tags:
    - docker-hub
    - activity-logs
    - administration
    - audit-logs
    - organization-management
    - repository-tracking
    - billing-events
category: guide
---

Subscription: Team Business

For: Administrators

Activity logs display a chronological list of activities that occur at organization and repository levels. The activity log provides organization owners with a record of all member activities.

With activity logs, owners can view and track:

- What changes were made
- The date when a change was made
- Who initiated the change

For example, activity logs display activities such as the date when a repository was created or deleted, the member who created the repository, the name of the repository, and when there was a change to the privacy settings.

Owners can also see the activity logs for their repository if the repository is part of the organization subscribed to a Docker Business or Team subscription.

To view activity logs in Docker Home:

1. Sign in to [Docker Home](https://app.docker.com) and select your organization.
2. Select **Admin Console**, then **Activity logs**.

> Docker Home retains activity logs for 30 days. To retrieve activities beyond 30 days, you must use the [Docker Hub API](https://docs.docker.com/reference/api/hub/latest/#tag/audit-logs).

By default, the **Activity** tab displays all recorded events within the last 30 days. To narrow your view, use the calendar to select a specific date range. The log updates to show only the activities that occurred during that period.

You can also filter by activity type. Use the **All Activities** drop-down to focus on organization-level, repository-level, or billing-related events. In Docker Hub, when viewing a repository, the **Activities** tab only shows events for that repository.

After selecting a category—**Organization**, **Repository**, or **Billing**—use the **All Actions** drop-down to refine the results even further by specific event type.

> Events triggered by Docker Support appear under the username **dockersupport**.

Refer to the following section for a list of events and their descriptions:

### [Organization events](#organization-events)

EventDescriptionTeam CreatedActivities related to the creation of a teamTeam UpdatedActivities related to the modification of a teamTeam DeletedActivities related to the deletion of a teamTeam Member AddedDetails of the member added to your teamTeam Member RemovedDetails of the member removed from your teamTeam Member InvitedDetails of the member invited to your teamOrganization Member AddedDetails of the member added to your organizationOrganization Member RemovedDetails about the member removed from your organizationMember Role ChangedDetails about the role changed for a member in your organizationOrganization CreatedActivities related to the creation of a new organizationOrganization Settings UpdatedDetails related to the organization setting that was updatedRegistry Access Management enabledActivities related to enabling Registry Access ManagementRegistry Access Management disabledActivities related to disabling Registry Access ManagementRegistry Access Management registry addedActivities related to the addition of a registryRegistry Access Management registry removedActivities related to the removal of a registryRegistry Access Management registry updatedDetails related to the registry that was updatedSingle Sign-On domain addedDetails of the single sign-on domain added to your organizationSingle Sign-On domain removedDetails of the single sign-on domain removed from your organizationSingle Sign-On domain verifiedDetails of the single sign-on domain verified for your organizationAccess token createdAccess token created in organizationAccess token updatedAccess token updated in organizationAccess token deletedAccess token deleted in organizationPolicy createdDetails of adding a settings policyPolicy updatedDetails of updating a settings policyPolicy deletedDetails of deleting a settings policyPolicy transferredDetails of transferring a settings policy to another ownerCreate SSO ConnectionDetails of creating a new org/company SSO connectionUpdate SSO ConnectionDetails of updating an existing org/company SSO connectionDelete SSO ConnectionDetails of deleting an existing org/company SSO connectionEnforce SSODetails of toggling enforcement on an existing org/company SSO connectionEnforce SCIMDetails of toggling SCIM on an existing org/company SSO connectionRefresh SCIM TokenDetails of a SCIM token refresh on an existing org/company SSO connectionChange SSO Connection TypeDetails of a connection type change on an existing org/company SSO connectionToggle JIT provisioningDetails of a JIT toggle on an existing org/company SSO connection

### [Repository events](#repository-events)

> Event descriptions that include a user action can refer to a Docker username, personal access token (PAT) or organization access token (OAT). For example, if a user pushes a tag to a repository, the event would include the description: `<user-access-token>` pushed the tag to the repository.

EventDescriptionRepository CreatedActivities related to the creation of a new repositoryRepository DeletedActivities related to the deletion of a repositoryRepository UpdatedActivities related to updating the description, full description, or status of a repositoryPrivacy ChangedDetails related to the privacy policies that were updatedTag PushedActivities related to the tags pushedTag DeletedActivities related to the tags deletedCategories UpdatedActivities related to setting or updating categories of a repository

### [Billing events](#billing-events)

EventDescriptionPlan UpgradedOccurs when your organization’s billing plan is upgraded to a higher tier plan.Plan DowngradedOccurs when your organization’s billing plan is downgraded to a lower tier plan.Seat AddedOccurs when a seat is added to your organization’s billing plan.Seat RemovedOccurs when a seat is removed from your organization’s billing plan.Billing Cycle ChangedOccurs when there is a change in the recurring interval that your organization is charged.Plan Downgrade CanceledOccurs when a scheduled plan downgrade for your organization is canceled.Seat Removal CanceledOccurs when a scheduled seat removal for an organization’s billing plan is canceled.Plan Upgrade RequestedOccurs when a user in your organization requests a plan upgrade.Plan Downgrade RequestedOccurs when a user in your organization requests a plan downgrade.Seat Addition RequestedOccurs when a user in your organization requests an increase in the number of seats.Seat Removal RequestedOccurs when a user in your organization requests a decrease in the number of seats.Billing Cycle Change RequestedOccurs when a user in your organization requests a change in the billing cycle.Plan Downgrade Cancellation RequestedOccurs when a user in your organization requests a cancellation of a scheduled plan downgrade.Seat Removal Cancellation RequestedOccurs when a user in your organization requests a cancellation of a scheduled seat removal.

### [Offload events](#offload-events)

EventDescriptionOffload Lease StartOccurs when an Offload lease is started in your organization.Offload Lease EndOccurs when an Offload lease is ended in your organization.