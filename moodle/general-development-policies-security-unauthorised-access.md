---
title: Unauthorised access | Moodle Developer Resources
url: https://moodledev.io/general/development/policies/security/unauthorised-access
source: sitemap
fetched_at: 2026-02-17T15:59:56.95613-03:00
rendered_js: false
word_count: 427
summary: Explains Moodle's permission system using roles, capabilities, and contexts, providing guidance on how to implement access control within custom code.
tags:
    - moodle-security
    - authorization
    - roles-and-capabilities
    - access-control
    - php-development
    - permissions
category: guide
---

## What is the danger?[​](#what-is-the-danger "Direct link to What is the danger?")

Assuming you have dealt with the issue of [Authentication](https://moodledev.io/general/development/policies/security/unauthenticated-access), so you know who is accessing your Moodle script, the next issue is that different users should only be allowed to do certain things. For example, as student should be allowed to post to a forum, but they should not be allowed to grade their own assignment as 100%.

However, in a system as complex as Moodle, different situations require different users to have different permissions to do, or not do, various things. Therefore, permissions need to be configurable and flexible.

## How Moodle avoids this problem[​](#how-moodle-avoids-this-problem "Direct link to How Moodle avoids this problem")

### Roles and capabilities[​](#roles-and-capabilities "Direct link to Roles and capabilities")

Moodle has a flexible roles system, build around the concepts of

- **contexts** - "Different situations", for example within a course (`CONTEXT_COURSE`), within a particular activity (`CONTEXT_MODULE`).
- **capabilities** - "Various things" a user might do, for example `mod/forum:replypost`, `mod/assignment:grade`.
- **roles** - Roles let administrators and teachers control which users get which capabilities in which contexts. For example, Sam might be a student in course Security 101, and Students are allowed to `mod/forum:replypost`, so Sam can reply to any post in any forum in the Security 101 course. Different role assignments and role definitions give administrators a lot of flexibility.

info

Follow the [Roles](https://moodledev.io/docs/5.2/apis/subsystems/roles) link to get a full description of the roles and capabilities.

### Groups[​](#groups "Direct link to Groups")

Moodle also allows users to be put in groups. Different groups may have access to different activities, and may or may not be able to see the actions of people in other groups.

## What you need to do in your code[​](#what-you-need-to-do-in-your-code "Direct link to What you need to do in your code")

- Before allowing the user to see anything or do anything, make a call to has\_capability or require\_capability, testing the appropriate capability in the appropriate context.
  
  - Get the appropriate context using a call to `get_context_instance`.
- For this to work in custom code, you may need to define additional capabilities. For example, `block/myblock:viewsecretthing`. You can define extra capabilities by creating a [db/access.php](https://moodledev.io/docs/5.2/apis/commonfiles#dbaccessphp) file in your plugin.
- If appropriate, use the [groups API](https://moodledev.io/docs/5.2/apis/subsystems/group) to check group membership, and only show users information from groups they should be able to see.
  
  - Note that `require_login` checks basic groups access permissions for you.
- It is very important to check capabilities when printing UI, but also after data submission before it is processed.

## What you need to do as an administrator[​](#what-you-need-to-do-as-an-administrator "Direct link to What you need to do as an administrator")

- Think carefully before changing the default role definitions.
- Always review capability risks before giving permissions to users that are not trusted.
- Use the various reports, especially the [Security overview](https://docs.moodle.org/en/Security_overview) report, to ensure that users do not have more capabilities than they should.

## See also[​](#see-also "Direct link to See also")

- [Security](https://moodledev.io/general/development/policies/security)
- [Coding](https://moodledev.io/general/development/policies)