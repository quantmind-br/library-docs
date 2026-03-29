---
title: How We Build
url: https://ampcode.com/notes/how-we-build
source: crawler
fetched_at: 2026-02-06T02:08:56.3662858-03:00
rendered_js: false
word_count: 549
summary: This document outlines the core engineering philosophy and cultural values of a development team, emphasizing shipping speed, individual accountability, and minimalist design standards.
tags:
    - engineering-culture
    - shipping-fast
    - ownership
    - design-philosophy
    - product-development
    - software-principles
category: guide
---

- We want to be [a team that ships](https://nav.al/build-a-team-that-ships). Most importantly:
  
  - “People choose what to work on. Better they ship what they want than not ship what you want.”
  - “No tasks longer than one week. You have to ship something into live production every week – worst case, two weeks. If you just joined, ship something.”
  - “Peer-management. Promise what you’ll do in the coming week on internal \[chat]. Deliver – or publicly break your promise – next week.”
  - “One person per project. Get help from others, but you and you alone are accountable.”
- Fixing bugs takes priority over everything else.
- We have to optimize for speed. Why? Because everything is changing — constantly. If we’re too slow, we fall behind.
- Optimizing for speed means: keeping the surface area small (less features that allow you to do more; when in doubt: no feature; see [FIF](https://ampcode.com/fif)), shipping constantly, asking “how will we debug this?” and “how easy to remove is it?” from the start.
- We have to optimize for robustness. Every pixel matters and every millisecond matters.
- We don’t do big releases. We constantly merge and constantly release.
- No code reviews for core committers. You merge it, you own it. Owning it means: you make sure it works, you keep fixing it, you are *responsible* for it. Conversely: don’t merge things you can’t own.
- We must build for where the puck is going, not for where it is.
- Every member of this team must talk to customers and users. Join the Discord, reply in the Discord.
- People on this team share and promote their work. The product *is* how we sell this. It’s not only marketing’s job to make sure you have a product that users want to use.
- Treat this as if it were your own project.
- Dogfooding is a superpower. Ship, *use*, iterate.
- No magic. Avoid “magic” solutions that infer user intent behind the scenes. When they fail, debugging becomes nearly impossible. Clear, debuggable functionality is essential to maintaining speed.
- Embrace how AI is changing how we develop software. Prototypes over RFCs and discussions.
- Hours and days over weeks and months. Instead of “next week”, why not “this week”? Instead of “tomorrow”, why not “today”?
- Before you post an Amp-related *announcement* to [/news](https://ampcode.com/news) or similar (including personal posts that will be seen as Amp announcements), get feedback on the language from other core team members for tone and consistency.
- Everyone here designs, not just designers:
  
  - Great design is the responsibility of everyone, not just people with “designer” in their title
  - Design is how it works, feels, and performs
  - If it’s user-facing, the first version of something should still feel good
  - We make decisions based on giving things a go and seeing how it feels, not just on screenshots/videos/chats
  - If you see something that sucks, speak up
  - Innovation over familiarity (tacky or janky does not count as innovative)
  - Less is more. Less screens. Less pages. Less color. Less UI. We take away more than we add.
  - We design in code — static design is an optional napkin scribble
  - Great ideas can come from anywhere and anyone
  - If you don’t know where to start, go find something great and use it as reference
  - (But don’t use the design and layout of [/manual](https://ampcode.com/manual) for anything other than [/manual](https://ampcode.com/manual))
- No emojis in the UI