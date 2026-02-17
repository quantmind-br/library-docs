---
title: Mediawiki
url: https://coolify.io/docs/services/mediawiki.md
source: llms
fetched_at: 2026-02-17T14:45:51.918014-03:00
rendered_js: false
word_count: 97
summary: This document provides a step-by-step guide for installing and configuring MediaWiki within a containerized environment using its web-based setup wizard. It focuses on the specific process of generating and mounting the LocalSettings.php configuration file to finalize the installation.
tags:
    - mediawiki
    - installation
    - containerization
    - localsettings-php
    - setup-wizard
    - open-source
category: guide
---

![Mediawiki](https://www.mediawiki.org/static/images/icons/mediawikiwiki.svg)

## What is Mediawiki?

Free and open source collaborative space for managing and sharing knowledge.

## Installation Steps

1. Comment out the shared volume for LocalSettings in your configuration.
2. Start the container.
3. Go to `http(s)://your-domain` to access the MediaWiki installation wizard.
4. Configure MediaWiki according to your needs through the wizard.
5. Download the generated `LocalSettings.php` file.
6. Stop the container.
7. Move the downloaded `LocalSettings.php` file to the specified file mount path on your server.
8. Uncomment the shared volume configuration to mount the `LocalSettings.php` file to the specified file mount path on your server.
9. Restart the container.

## Links

* [The official website](https://www.mediawiki.org/wiki/MediaWiki)
* [GitHub](https://github.com/wikimedia/mediawiki)