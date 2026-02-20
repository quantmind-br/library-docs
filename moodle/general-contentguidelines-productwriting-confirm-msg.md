---
title: Confirmation messages | Moodle Developer Resources
url: https://moodledev.io/general/contentguidelines/productwriting/confirm-msg
source: sitemap
fetched_at: 2026-02-17T15:58:10.984412-03:00
rendered_js: false
word_count: 447
summary: This document provides design and content guidelines for creating clear and effective confirmation messages that help users verify actions with significant consequences.
tags:
    - ux-writing
    - confirmation-messages
    - content-guidelines
    - moodle-development
    - user-interface
    - accessibility
category: guide
---

Confirmation messages prompt people to confirm actions that have significant consequences or are difficult to undo. They can also help prevent errors or unexpected results by verifying user intent before proceeding with an action.

Clear and concise confirmation messages help people feel more confident and in control of their actions within the Moodle products.

[HTML modal](https://componentlibrary.moodle.com/admin/tool/componentlibrary/docspage.php/moodle/components/dom-modal/)

## Basic guidelines[​](#basic-guidelines "Direct link to Basic guidelines")

- Address a single task.
- Ask a clear, specific question.
- Provide clear options to either confirm or cancel the action.
- Explain the consequences of the action so people can make an informed decision.

## Content[​](#content "Direct link to Content")

### Title[​](#title "Direct link to Title")

The title or heading of a confirmation message should focus only on one task, and mention the specific action that the user wants to perform.

Write your title as a clear, unambiguous question. This helps users understand that they're making a choice.

Don't include articles like 'a', 'an' or 'the', so that the question is short and easy to scan.

### Description[​](#description "Direct link to Description")

The description should explain the consequences of the action and share additional details that enable people to make a confident decision.

Do

**Delete entry?** This will delete the entry 'My first blog post'.

Don't

**Delete entry?** Are you sure you want to delete the blog post?

Don't repeat information from the title.

Do

**Remove account 'Barbara Gardner'?** This account and its data on the site \[site name] will be removed from the app on this device.

Don't

**Remove account 'Barbara Gardner'?** Are you sure you want to remove this account?

Save "Are you sure?" for actions that have very serious consequences. For example, actions that could prevent a course or activity from working properly, or deleting something that can't be retrieved from the recycle bin.

Do

**Delete tool?** This tool is currently being used in at least one activity in your course. If you delete this tool, the activities that use it will no longer work. Are you sure you want to delete the tool?

Don't

**Delete activity?** Are you sure you want to delete the activity?

### Calls to action[​](#calls-to-action "Direct link to Calls to action")

Calls to action (CTAs) should be clear and simple, and offer a straightforward way out.

Do

**Delete downloaded data?** Cancel | **Delete**

Don't

**Delete downloaded data?** Cancel | **Continue**

Do

**Log out from this device?** Cancel | **Log out**

Don't

**Log out from this device?** No | **Ok**

Use the same verb in both the title and the confirmation button to make the content more scannable and summarise outcomes.

Do

**Move** selected activities? Cancel | **Move**

Don't

**Move** selected activities? Cancel | **Continue**

Don't

**Delete** tool? Cancel | **Delete**

Don't

**Delete** tool? Cancel | **Remove**

Avoid 'cancelling cancellations'

Do

**Cancel booking?** Keep my booking | Cancel booking

Don't

**Cancel subscription?** Cancel | Confirm cancellation