---
title: Organization
url: https://docs.docker.com/admin/faqs/organization-faqs/
source: llms
fetched_at: 2026-01-24T14:13:05.955289223-03:00
rendered_js: false
word_count: 382
summary: This document provides answers to common questions regarding Docker organization management, covering topics such as user identification, authentication enforcement, and seat allocation rules.
tags:
    - docker-organizations
    - user-management
    - seat-allocation
    - authentication
    - docker-desktop
    - account-administration
category: reference
---

## FAQs on organizations

Table of contents

* * *

### [How can I see how many active users are in my organization?](#how-can-i-see-how-many-active-users-are-in-my-organization)

If your organization uses a Software Asset Management tool, you can use it to find out how many users have Docker Desktop installed. If your organization doesn't use this software, you can run an internal survey to find out who is using Docker Desktop.

For more information, see [Identify your Docker users and their Docker accounts](https://docs.docker.com/admin/organization/onboard/#step-1-identify-your-docker-users-and-their-docker-accounts).

### [Do users need to authenticate with Docker before an owner can add them to an organization?](#do-users-need-to-authenticate-with-docker-before-an-owner-can-add-them-to-an-organization)

No. Organization owners can invite users with their email addresses, and also assign them to a team during the invite process.

### [Can I force my organization's members to authenticate before using Docker Desktop and are there any benefits?](#can-i-force-my-organizations-members-to-authenticate-before-using-docker-desktop-and-are-there-any-benefits)

Yes. You can [enforce sign-in](https://docs.docker.com/enterprise/security/enforce-sign-in/).

Some benefits of enforcing sign-in are:

- Administrators can enforce features like [Image Access Management](https://docs.docker.com/enterprise/security/hardened-desktop/image-access-management/) and [Registry Access Management](https://docs.docker.com/enterprise/security/hardened-desktop/registry-access-management/).
- Administrators can ensure compliance by blocking Docker Desktop usage for users who don't sign in as members of the organization.

### [Can I convert my personal Docker ID to an organization account?](#can-i-convert-my-personal-docker-id-to-an-organization-account)

Yes. You can convert your user account to an organization account. Once you convert a user account into an organization, it's not possible to revert it to a personal user account.

For prerequisites and instructions, see [Convert an account into an organization](https://docs.docker.com/admin/organization/convert-account/).

### [Do organization invitees take up seats?](#do-organization-invitees-take-up-seats)

Yes. A user invited to an organization will take up one of the provisioned seats, even if that user hasn’t accepted their invitation yet.

To manage invites, see [Manage organization members](https://docs.docker.com/admin/organization/members/).

### [Do organization owners take a seat?](#do-organization-owners-take-a-seat)

Yes. Organization owners occupy a seat.

### [What is the difference between user, invitee, seat, and member?](#what-is-the-difference-between-user-invitee-seat-and-member)

- User: Docker user with a Docker ID.
- Invitee: A user that an administrator has invited to join an organization but has not yet accepted their invitation.
- Seats: The number of purchased seats in an organization.
- Member: A user who has received and accepted an invitation to join an organization. Member can also refer to a member of a team within an organization.

### [If I have two organizations and a user belongs to both organizations, do they take up two seats?](#if-i-have-two-organizations-and-a-user-belongs-to-both-organizations-do-they-take-up-two-seats)

Yes. In a scenario where a user belongs to two organizations, they take up one seat in each organization.