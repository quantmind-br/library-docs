---
title: AI Plugins | Moodle Developer Resources
url: https://moodledev.io/docs/5.1/apis/plugintypes/ai
source: sitemap
fetched_at: 2026-02-17T15:34:38.160702-03:00
rendered_js: false
word_count: 228
summary: This document explains the architecture of the Moodle AI subsystem, detailing the decoupled relationship between provider plugins for AI service integration and placement plugins for user interaction.
tags:
    - moodle-lms
    - ai-subsystem
    - provider-plugins
    - placement-plugins
    - plugin-architecture
    - external-ai
category: concept
---

The [AI subsystem](https://moodledev.io/docs/5.1/apis/subsystems/ai) provides a way for developers to integrate external AI services into Moodle LMS.

The design of the AI subsystem features two distinct plugin types:

- [Provider plugins](https://moodledev.io/docs/5.1/apis/plugintypes/ai/provider)
- [Placement plugins](https://moodledev.io/docs/5.1/apis/plugintypes/ai/placement)

This design allows for independent development of each plugin. The Provider plugin is not aware of the Placement plugin, and the Placement plugin is not aware of the Provider plugin. All communication between the two plugins travels through the Manager.

### Provider plugins[​](#provider-plugins "Direct link to Provider plugins")

Providers are the interface between the [AI subsystem](https://moodledev.io/docs/5.1/apis/subsystems/ai) and external AI. Their focus is on formatting actions, passing them to the external AI system, and providing the response.

Currently, Moodle supports the following AI Providers in core:

- OpenAI `aiprovider_openai`
- Azure AI `aiprovider_azureai`

See the [Providers](https://moodledev.io/docs/5.1/apis/plugintypes/ai/provider) documentation for more information on developing Provider plugins.

### Placement plugins[​](#placement-plugins "Direct link to Placement plugins")

Placements provide a consistent UX and UI for users when they use AI backed functionality (e.g. generating an image).

Placement plugins leverage the functionality of the other components of the [AI subsystem](https://moodledev.io/docs/5.1/apis/subsystems/ai). This means plugin authors can focus on how users interact with the AI functionality, without needing to implement the AI functionality itself.

Because Placements are plugins in their own right, it allows for greater flexibility in how AI functionality is presented to users.

Currently, Moodle supports the following AI Placements:

- Course Assistance `aiplacement_courseassist`
- HTML Text Editor `aiplacement_editor`

See the [Placements](https://moodledev.io/docs/5.1/apis/plugintypes/ai/placement) documentation for more information on developing Placement plugins.