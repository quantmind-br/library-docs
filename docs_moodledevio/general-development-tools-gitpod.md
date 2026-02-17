---
title: Gitpod | Moodle Developer Resources
url: https://moodledev.io/general/development/tools/gitpod
source: sitemap
fetched_at: 2026-02-17T16:01:32.23958-03:00
rendered_js: false
word_count: 419
summary: This document explains how to set up and use Gitpod to create cloud-based development environments for Moodle, including integration with the Moodle Tracker for simplified testing and development.
tags:
    - gitpod
    - moodle
    - moodle-docker
    - cloud-ide
    - development-environment
    - testing
    - tampermonkey
category: guide
---

[Gitpod](https://www.gitpod.io/) is a free, cloud-based platform with IDE integration that provides a suitable development environment directly in a browser.

It has been integrated with [moodle-docker](https://github.com/moodlehq/moodle-docker/) so that you can open any Moodle repository/branch in a Gitpod workspace.

When launching a workspace in Gitpod, it will automatically:

1. Clone the Moodle repo into the `<workspace>/moodle` folder.
2. Initialise the Moodle database.
3. Start the Moodle webserver.

More information about the Gitpod integration with moodle-docker, like the parameters it supports, can be found in the [project's page](https://github.com/moodlehq/moodle-docker/#quick-start-with-gitpod).

## How to use Gitpod with Moodle?[​](#how-to-use-gitpod-with-moodle "Direct link to How to use Gitpod with Moodle?")

A [Tampermonkey](https://www.tampermonkey.net/) script has been created to facilitate the initiation of a Gitpod workspace from any Moodle repository/branch. When the script is installed, a button is displayed near each branch in the [Moodle tracker](https://moodle.atlassian.net/) within the Moodle repository, facilitating the initiation of a Gitpod workspace. It can be used for testing any Moodle repository/branch without requiring a local environment installed.

![Gitpod integration with Moodle tracker](https://moodledev.io/assets/images/trackerintegration-baa834069354ce8b7a27d64d2cc70cf3.png)

To use it, follow these steps:

1. Install the [Tampermonkey extension](https://www.tampermonkey.net/) for your preferred browser.
2. Go to **Dashboard** in the Tampermonkey extension and access the **Utilities** tab.
3. In the **Import from URL** field, paste the following Gitpod script: [https://gist.githubusercontent.com/sarjona/9fc728eb2d2b41a783ea03afd6a6161e/raw/gitpod.js](https://gist.githubusercontent.com/sarjona/9fc728eb2d2b41a783ea03afd6a6161e/raw/gitpod.js)
4. Go to the [Moodle Tracker](https://moodle.atlassian.net/) and open any issue.
5. Click the **Open in Gitpod** button that should appear near any of the branches in the issue.

The first time you open a workspace, you will need to register in [gitpod.io](https://www.gitpod.io/) (you can use your Github account).

After waiting for 5-8 minutes, a Moodle site will open in your IDE (web VSCode by default) and you'll be able to start playing with it!!

info

The password for the `admin` user is `test` ;-)

## About the Gitpod workspaces[​](#about-the-gitpod-workspaces "Direct link to About the Gitpod workspaces")

- By default, all Gitpod workspaces become inactive after 30 minutes of no activity. They can be reopened from the [Gitpod dashboard](https://gitpod.io/workspaces/).
- Workspaces are automatically deleted after 14 days.
- You can view a list of your workspaces on the [Gitpod dashboard](https://gitpod.io/workspaces/). From there, you can open any existing workspaces, which will be resumed with the Moodle site displayed in the IDE just as it was when it became inactive.
- It's recommended to rename workspaces manually to something more meaningful (like the tracker issue).

## What can be done with this integration?[​](#what-can-be-done-with-this-integration "Direct link to What can be done with this integration?")

The following list is just a sample of the things that can be done with the integration of Gitpod with Moodle:

- Test Moodle Tracker issues easily. Especially useful for non-developers or QA testers.
- Test third-party plugins.
- Remote development environment.
- Run tests (behat, PHPUnit…).

## See also[​](#see-also "Direct link to See also")

- [Moodle docker](https://github.com/moodlehq/moodle-docker/#quick-start-with-gitpod)
- [Gitpod samples](https://github.com/gitpod-samples)
  
  - [gitpod.yml](https://www.gitpod.io/docs/references/gitpod-yml)
  - [gitpod-cli](https://www.gitpod.io/docs/references/gitpod-cli)
  - [Environment variables](https://www.gitpod.io/docs/configure/projects/environment-variables)