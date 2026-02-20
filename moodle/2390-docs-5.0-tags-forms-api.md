---
title: 4 docs tagged with "Forms API" | Moodle Developer Resources
url: https://moodledev.io/docs/5.0/tags/forms-api
source: sitemap
fetched_at: 2026-02-17T15:19:04.940492-03:00
rendered_js: false
word_count: 191
summary: This document explains advanced features of the Moodle Form API, including hidden advanced elements, checkbox controllers, non-submitting action buttons, and repeatable form components.
tags:
    - moodle-development
    - form-api
    - ui-components
    - advanced-elements
    - checkbox-grouping
    - repeatable-fields
category: guide
---

## [Advanced elements](https://moodledev.io/docs/5.0/apis/subsystems/form/advanced/advanced-elements)

Form elements can be marked as 'advanced'. This has the effect that they are hidden initially.

## [Checkbox controller](https://moodledev.io/docs/5.0/apis/subsystems/form/advanced/checkbox-controller)

The checkbox controller allows developers to group checkboxes together and add a link or button to check, or uncheck, all of the checkboxes at once.

## [No submit button](https://moodledev.io/docs/5.0/apis/subsystems/form/advanced/no-submit-button)

The moodleform 'nosubmitbutton\_pressed()' method allows you to detect if a button on your form has been pressed that is a submit button but that has been defined as a button that doesn't result in a processing of all the form data but will result in some form 'sub action' and then having the form redisplayed. This is useful for example to have an 'Add' button to add some option to a select box in the form etc. You define a button as a no submit button as in the example below (in definition()). This example adds a text box and a submit button in a group.

## [Repeat elements](https://moodledev.io/docs/5.0/apis/subsystems/form/advanced/repeat-elements)

The Form API includes the ability to repeat a group of form elements. This is useful where you need to have an unknown quantity of item data, for example possible answers in a quiz question.