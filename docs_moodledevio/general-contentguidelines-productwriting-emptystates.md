---
title: Empty states | Moodle Developer Resources
url: https://moodledev.io/general/contentguidelines/productwriting/emptystates
source: sitemap
fetched_at: 2026-02-17T15:58:14.84433-03:00
rendered_js: false
word_count: 663
summary: This document provides design and content guidelines for creating effective empty states to improve user engagement and onboarding when no content is currently available in the interface.
tags:
    - ux-design
    - user-interface
    - empty-states
    - content-strategy
    - onboarding
    - design-guidelines
category: guide
---

Empty states appear when there's nothing to display to our users. They can happen in a variety of situations:

- First use: When someone first uses a product or a feature. For example, when someone creates a new Database activity.
- User-emptied: When users have completed all tasks or actions, or have cleared the interface themselves. For example, when a student has completed all upcoming actions in the Timeline block, or when someone deletes all their messages.
- No results: When users search for something or use filters that return no results.

Empty states are a good opportunity to make a human connection with users, showing them we are here to help them move forward. You can also use empty states to educate users about a new feature, or to onboard new users and show them the key tasks they can do to get started.

Depending on the part of the experience where they appear, empty states may include an image, a title, a description and one or more calls-to-action.

## Basic guidelines[​](#basic-guidelines "Direct link to Basic guidelines")

- Avoid completely empty states.
- Help users understand why there is nothing to show them.
- Guide them to take an action.
- Be clear and concise, and use friendly language.
- You can use visuals to make empty states more engaging, but don't rely on the image alone to convey your message.

## Content[​](#content "Direct link to Content")

### Title[​](#title "Direct link to Title")

The title is a short explanation of why the user is seeing an empty screen.

Do

Your search didn't match any courses

Do

You're not enrolled in any courses

Don't use punctuation in the title, unless it's a question or an exclamation.

On first use or user-emptied states, writing an encouraging title not only informs users, but it's an opportunity to create a positive user experience.

Do

**You're all caught up!** There are no upcoming activities in your timeline.

Don't

**No upcoming activities** There are no upcoming activities in your timeline.

### Description[​](#description "Direct link to Description")

The description guides users on how to move forward with the experience.

Explain briefly what users can do to fill the empty state.

Do

**Your search didn't match any courses** Try adjusting your filters or browse all courses.

Don't

**No results** There are no results for your search.

If users can't do anything themselves to fill in the empty state, explain what they will see in the screen once it has content.

Do

**You're not enrolled in any course** Once you enrol in a course, it will appear here.

Don't

**No courses** You're not enrolled in any course yet.

### Calls to action[​](#calls-to-action "Direct link to Calls to action")

The call to action (CTA) in an empty state is a button or link that tells the user what to do next to 'fill' the empty state.

Keep calls to action concise and actionable, and tell the user exactly what they will get if they follow them.

Do

**You're not enrolled in any course** Once you enrol in a course, it will appear here. CTA: **Browse courses**

Don't

**No courses** You're not enrolled in any course yet. CTA: **Search**

Do

**This database is empty** Add entries to start building your activity. CTA: **Add entry**

Don't

**Add the first entry** This database has no entries yet. CTA: **Continue**

One some occasions, you might want to use two calls to action: one to 'fill' the empty state, and one to give users more context or information.

You can include the secondary call to action as a link in the description:

Do

**Create your first course** Need help getting started? Check out our [Quick start guide](#calls-to-action). CTA: **Add course**

Or include it as a secondary call to action:

Do

**No entries yet** CTAs: Import entries | **Add entry**

### Illustration[​](#illustration "Direct link to Illustration")

Using an illustration can help users understand the context of the empty state and make the experience more engaging and delightful. However, it's important to use illustrations only when they add value to the user experience. Never rely on the image alone to convey your message, and remember to add alt text to the image if it's essential to understanding the empty state.