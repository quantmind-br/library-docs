---
title: Overview | Moodle Developer Resources
url: https://moodledev.io/general/community
source: sitemap
fetched_at: 2026-02-17T15:55:35.249322-03:00
rendered_js: false
word_count: 724
summary: This document provides an overview of the Moodle development ecosystem, detailing the key contributors, release cycles, support policies, and core development standards.
tags:
    - moodle-development
    - release-cycle
    - coding-standards
    - issue-tracking
    - open-source
    - plugin-architecture
category: guide
---

This page gives an overview of the process of developing Moodle and outlines some of the basic concepts to better understand this Developer documentation.

## The key players[​](#the-key-players "Direct link to The key players")

- [**Moodle HQ**](https://moodle.com/careers/)  
  The team of developers who are directly funded by the Moodle project to work full-time on core developments.
- [**Moodle Certified Service Providers**](https://moodle.com/services/)  
  Also known as Moodle Partners, these are over 100 companies around the world that provide Moodle services. These companies often have their own developers and may contribute to Moodle directly by working on core code or by creating plugins.
- **Component leads**  
  A number of people around the world have volunteered to lead various components in Moodle. This involves maintaining existing code as well as listening to the community and improving that component with new features.

There are many other people contributing to Moodle in many ways, such as coding, testing, writing documentation, helping in the forums or translating. For a full list, see the [Moodle developer credits](http://moodle.org/dev/) page on moodle.org.

## How we develop the Roadmap[​](#how-we-develop-the-roadmap "Direct link to How we develop the Roadmap")

The [Roadmap](https://moodledev.io/general/community/roadmap) lists the new features being developed for the next major version. This list is derived mostly from issues with large numbers of votes in the Moodle [Tracker](https://moodledev.io/general/development/tracker/guide), so please vote for what you want! Other influences include general discussion, surveys and feature requests at MoodleMoots and in the Moodle forums.

Component leads decide on features in individual components, so make your case to them!

## Moodle versions[​](#moodle-versions "Direct link to Moodle versions")

Moodle major releases (with big new features) are on a regular 6-month cycle, in April and October. Each major release increments the version number by 0.1 (eg 3.4 -&gt; 3.5 -&gt; 3.6) and starts a new branch of minor releases.

Minor releases (with bug fixes only) are on a 2-month cycle, unless a security emergency occurs. They will increment the major release by 0.0.1 (eg 3.5 -&gt; 3.5.1 -&gt; 3.5.2).

The full details of these can be seen in the [Releases](https://moodledev.io/general/releases).

## Support lifetime[​](#support-lifetime "Direct link to Support lifetime")

Moodle HQ is committed to supporting major Moodle LMS releases for 12 months of general fixes (usually 6-point releases), and 18 months of security fixes.

That means we usually release minor versions for the most recent three major branches.

Some versions, every two years, are [long term supported (LTS)](https://en.wikipedia.org/wiki/Long-term_support). LTS Moodle releases are supported for 36 months, which means they have 18 additional months of security fixes compared to other versions.

## Issue tracking[​](#issue-tracking "Direct link to Issue tracking")

Issue tracking is an important part of a continuous quality control process. It involves reporting of problems (bugs), ideas for improvement, and new features. Unlike most proprietary software programs, Moodle issue reporting and tracking information is open to everyone. Moodle's issue tracking system is called the [Tracker](http://moodle.atlassian.net/).

All Moodle users are encouraged to be active participants when it comes to testing. Anyone with a Tracker user account can create, view, comment on, vote, and watch bugs.

## Processes[​](#processes "Direct link to Processes")

As you might guess, a large software project like Moodle with hundreds of contributors and varied opinions can be difficult to manage.

Over time we have developed several well-defined processes for getting code in and out of Moodle and for governing everyone's workflow in a way that is fair and clear.

See our [Process](https://moodledev.io/general/development/process) page for full information on our development processes, including how you can contribute to the project.

## Coding Standards[​](#coding-standards "Direct link to Coding Standards")

Over time we have distilled our best practice in writing code down into our [Coding Guide](https://moodledev.io/general/development/policies). These rules cover the formatting and layout of all our code to make it consistent across the code base. If you plan to write Moodle code, you need to read it thoroughly.

## Plugins and APIs[​](#plugins-and-apis "Direct link to Plugins and APIs")

Although Moodle is open source and you can change anything you want in its core code, the best and most maintainable way to extend Moodle is to write a plugin (sometimes called a module). Plugins are a directory of code that can be simply "dropped" in into any Moodle installation and it will be detected, installed and automatically made available as a tool within the Moodle interface.

See our [Plugin documentation](https://moodledev.io/docs/5.2/apis/plugintypes) for full details of the various types of plugin available.

## See also[​](#see-also "Direct link to See also")

- [Finding your way into the Moodle code](https://docs.moodle.org/dev/Finding_your_way_into_the_Moodle_code)
- [Working with the Community](https://docs.moodle.org/dev/Working_with_the_Community)
- [Plugin contribution](https://moodledev.io/general/community/plugincontribution)
- [How to guarantee your change is integrated to Moodle core](http://www.slideshare.net/poltawski/how-to-guarantee-your-change-is-integrated-to-moodle-core) presentation by Dan Poltawski

<!--THE END-->

- [The key players](#the-key-players)
- [How we develop the Roadmap](#how-we-develop-the-roadmap)
- [Moodle versions](#moodle-versions)
- [Support lifetime](#support-lifetime)
- [Issue tracking](#issue-tracking)
- [Processes](#processes)
- [Coding Standards](#coding-standards)
- [Plugins and APIs](#plugins-and-apis)
- [See also](#see-also)