---
title: Tracker guide | Moodle Developer Resources
url: https://moodledev.io/general/development/tracker/guide
source: sitemap
fetched_at: 2026-02-17T16:01:47.738374-03:00
rendered_js: false
word_count: 1599
summary: This document provides an overview of the Moodle Tracker system, outlining user permissions, group roles, and the specific fields used to manage bugs, improvements, and feature requests.
tags:
    - moodle-tracker
    - issue-tracking
    - development-process
    - jira
    - bug-reporting
    - user-roles
category: guide
---

The [Moodle Tracker](http://moodle.atlassian.net/) is our database for recording and managing all Moodle development issues - bugs, improvements and feature requests.

To do anything more than browsing and searching in the tracker, you'll need to [create an account](http://moodle.atlassian.net/secure/Signup%21default.jspa) and then login.

## Tracker groups and permissions[​](#tracker-groups-and-permissions "Direct link to Tracker groups and permissions")

There are a number of groups used to define the potential of users in Tracker. Here are some important ones.

NameJira groupPotentialHow to become one**Users**jira-usersUsers can create new issues, comment on issues, vote for issues, link issues, attach files, create sub-tasks and watch issues.Anyone who creates a tracker account becomes a member of the Users group.**Moodle Security**moodle-securityTrusted developers and administrators who need to work on security issues that are hidden from normal users. See [Moodle security procedures](https://moodledev.io/general/development/process/security).This is generally limited to developers at Moodle HQ and Partner organisations. People wishing join the Moodle Security group should email [security@moodle.org](mailto:security@moodle.org) with the reasons for your request.**Developers**jira-developersDevelopers can edit issues and assign issues to themselves. They are also able to request peer reviews. They cannot submit code directly for integration review, but an HQ staff member or component lead can do this after a satisfactory peer review. See [Process](https://moodledev.io/general/development/process).People wishing to join the Developers group should be able to demonstrate a history of contributing patches to issues.

When a developer's first patch is integrated, tested and the issue is closed, they are added to the group and set as issue assignee.

If that doesn't happen automatically, please send an email to [integration@moodle.com](mailto:integration@moodle.com) with your tracker username and links to issues where you have contributed patches.

**Integration requesters**pull-requestersDevelopers can send issues for integration review. See [Process](https://moodledev.io/general/development/process).This role is reserved for Moodle HQ developers and component leads.**Integration testers**pull-testersUsers that can tests issues under integration and pass/fail them. See [Process](https://moodledev.io/general/development/process).Usually reserved for HQ developers and external testers.

note

You can browse a project without being logged in to Tracker, however you will be to unable edit or comment on bugs.

## Tracker fields[​](#tracker-fields "Direct link to Tracker fields")

### When creating an issue[​](#when-creating-an-issue "Direct link to When creating an issue")

FieldValuesNotes**Project**

- **Moodle**  
  For an issue relating to the Moodle codebase.
- **Moodle Community Sites**  
  For an issue on moodle.atlassian.net, docs.moodle.org, demo.moodle.org, download.moodle.org, moodle.org, etc.
- **Non-core contributed modules**  
  For an issue with a contributed plugin.

There are a few more projects, but these are the main ones.Tracker is used for multiple projects.**Issue Type**

- **Bug**  
  A problem which impairs or prevents Moodle from functioning correctly.
- **Improvement**  
  An enhancement to an existing Moodle feature.
- **New Feature**  
  A new Moodle feature which has yet to be developed.
- **Task**  
  A task that needs to be completed, usually apart from coding.
- **Sub-Task**  
  Part of a greater task

**Summary**A brief, concise description of the problem.When the issue is about applying an existing solution to another, usually older, branch (namely "[backport](https://moodledev.io/general/development/policies/backporting)"), please use the summary of the existing solution plus its issue number (i.e. "Fix forum alignment (backport of [MDL-99999](https://moodle.atlassian.net/browse/MDL-99999))").**Description**A full and complete description of the issue including:

- replication steps,
- the expected result,
- the actual result,
- any error messages shown with [debugging](https://docs.moodle.org//en/Debugging) turned on, and
- any other relevant information.

**Affects Version/s**

- For bugs: the latest released version in which the bug is found
- For improvements: the latest released version
- For new features: Use 'Future dev'

**Component/s**The area(s) in Moodle which is affected by the issue.Select `Unknown` if you are unsure.**Security Level**

- **None**  
  Viewable by everyone, including non-logged-in users
- **Could be a security issue**  
  Viewable by members of the jira-developers group
- **Minor security issue**  
  Viewable by members of the security team only
- **Serious security issue**  
  Viewable by members of the security team only

<!--THE END-->

- The reporter can view the issue they reported, regardless of the security level set.
- The higher the security level, the fewer people who can view the issue.
- The `Could be a security issue` should only be used temporarily when the issue is reported. A decision should be made as soon as possible to set another level.

### When editing an issue[​](#when-editing-an-issue "Direct link to When editing an issue")

Once an issue has been created, the following additional fields are able to be changed/set by editing the issue. Not all users can edit all fields.

FieldValuesNotes**Fixed Version/s**

- Prior to integration, this will be blank or set to a backlog (a queue of development work), for example `Must fix for X`.
- After integration, this will be set to the Moodle version(s) the issue was fixed in, for example `4.0.1`.
- For more detailed information, look to the **Resolution** field below.

<!--THE END-->

- This is usually set by an integrator.
- Not to be confused with `Affected version`, which is used to define the Moodle version where the issue can be reproduced.
- If you resolve the bug as anything but `Fixed` and, sometimes, `Done` (like `Cannot Reproduce`, `Won't Fix`, etc.) leave **Fix Version/s** blank.
- **Fix version/s** are used to automatically build release notes (see the tabs on [http://moodle.atlassian.net/browse/MDL](http://moodle.atlassian.net/browse/MDL))

**Priority**

- **Blocker**  
  Blocks development or testing, prevents Moodle from running. Applicable to bugs only.
- **Critical**  
  Crashes server, loss of data, severe memory leak
- **Major**  
  Major loss of function, incorrect output
- **Minor**  
  Minor loss of function where workaround is possible
- **Trivial**  
  Cosmetic problem like misspelt words or misaligned text

<!--THE END-->

- When it is reported, the priority level represents the severity of a bug.
- After being reported, the priority may be promoted by HQ developers and component leads as an issue escalates.
- Other users wishing to influence the priority of issues should do so by voting for the issue.
- The priority of new features and improvements should generally remain at the default (Minor) level.

**Reporter**The person who logs the bug.  
This field is automatically filled by Tracker.**Assignee**The person who will fix the issue. The assignee should be set when there is a definite intention to complete the issue.

- Developers or QA Testers can reassign issues.
- Please note that even though a person may be assigned to an issue, this does not mean they are currently working on the issue, although they are likely to in future.

**Peer reviewer**The person who will check the fix at the code level. See [Peer-review](https://moodledev.io/general/development/process/peer-review).**Integrator**The person who will integrate the code into the Moodle codebase. See [Integration-review](https://moodledev.io/general/development/process/integration).**Tester**The person who will test the solution at a functional level, according to the test instructions provided. See [Testing](https://moodledev.io/general/development/process/testing).**Environment**The operating system, server and/or browser specifications if applicable to this bug.Note that the database is specified separately in the database field below.**Database**If applicable to the bug, identify the database type.**Testing instructions**The steps that a tester should follow to achieve the expected behaviour after the issue has been resolved.

- This may be different to the replication steps reported in the description.
- These instructions are written by the developer working on the issue.

**Workaround**A way to achieve the desired functionality by other means.

- This will be very useful to other Moodle users who have the same problem, until the issue is resolved.
- If the issue can be resolved by a simple code change, say one line, then you can give that as a workaround, although patches and Git branches are preferred.

**Attachment**Patch files, Screenshots, example backups and other related files

- Attaching a file will help developers and testers better understand the bug.
- Maximum attachment size is 512Kb.

**URL**If possible, provide a URL address that demonstrates an example of this bug.**Epic Name**A short name given to an issue of type Epic so that linked issues can be grouped by this name. It should only be a few words at most.Only applies to issues of type Epic.**Epic Link**A link to an Epic issue. This can be added by providing the issue ID or Epic name. It is a way of organising related issues as part of a project.Only applies to issues that need to be collected together for a project.**Labels**See [Tracker issue labels](https://moodledev.io/general/development/tracker/labels).

- Labels should be specific values used in filters and searches.
- This is not a field for including generic keywords.

**Pull...**Links to a code solution in a Git repository.

- These fields are used by developers.
- There may be multiple solutions if the problem affects multiple Moodle versions.

**Documentation link**URL of related documentation.When changes require documentation to be updated, this field should be filled.**Comment**

- Notes made by all interested parties.
- A detailed register of all changes that relate to this bug.

### When closing an issue[​](#when-closing-an-issue "Direct link to When closing an issue")

FieldValuesNotes**Resolution**Issues that may/must have the **Fixed versions** field filled:

- **Fixed**  
  Issue has been fixed; a code change has been integrated into Moodle code. It's **mandatory** to set the *Fixed versions* field for these issues.
- **Done**  
  Normally used for tasks, epics... issues that don't "own" code changes in Moodle, but still have required actions (planning, review, adjust some related system...). When relevant or clearly related with any release it's **recommended** to set the *Fixed versions* to them.

Issues that must not have the **Fixed versions** field filled:

- **Won't Fix**  
  The problem described is an issue which will never be fixed. Specific reasons should be given.
- **Not a bug**  
  This issue is not a bug. The issue may have been logged in error. Use this code if the bug was fixed by another bug report or in some earlier Moodle version.
- **Duplicate**  
  The problem is a duplicate of an existing issue
- **Incomplete**  
  More information was needed to understand this bug, but it was not provided.
- **Can't Reproduce**  
  Attempts at reproduce the issue failed. If more information appears later, please open a new issue.
- **Deferred**  
  The resolution to this bug will be deferred to a later release or to a fix in a third-party plugin used in Moodle.

This field is only displayed when resolving or closing a bug.

## See also[​](#see-also "Direct link to See also")

- [Tracker introduction](https://moodledev.io/general/development/tracker/) - less scary version of this page for new users.
- [Process](https://moodledev.io/general/development/process)
- [Bug triage](https://moodledev.io/general/development/process/triage)
- [Tracker issue labels](https://moodledev.io/general/development/tracker/labels)
- [Testing of integrated issues](https://moodledev.io/general/development/process/testing/integrated-issues)
- Using Moodle [How to manipulate Moodle developers](http://moodle.org/mod/forum/discuss.php?d=43952) forum discussion
- Wikipedia [Definition of a bug](http://en.wikipedia.org/wiki/Software_bug)