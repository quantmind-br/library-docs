---
title: Django
url: https://coolify.io/docs/applications/django.md
source: llms
fetched_at: 2026-02-17T14:38:51.126495-03:00
rendered_js: false
word_count: 65
summary: This document outlines the necessary configuration steps and requirements for setting up and deploying a Django web application.
tags:
    - django
    - python
    - deployment-setup
    - gunicorn
    - web-framework
    - environment-configuration
category: configuration
---

# Django

Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.

## Requirements

1. Set the base directory where your `requirements.txt` and `manage.py` files are located.

> In the example repository, it is `/coolify`.

2. Add `gunicorn` to the `requirements.txt` file, [official docs](https://docs.gunicorn.org/en/stable/install.html).
3. Add `localhost` and your `domain` to `ALLOWED_HOSTS` in `settings.py` file, [ official docs](https://docs.djangoproject.com/en/4.2/ref/settings/#allowed-hosts).

> `Localhost` is required for health checks to work properly.