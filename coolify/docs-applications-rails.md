---
title: Ruby on Rails
url: https://coolify.io/docs/applications/rails.md
source: llms
fetched_at: 2026-02-17T14:38:58.103547-03:00
rendered_js: false
word_count: 49
summary: This document provides configuration instructions for deploying Ruby on Rails applications using the NIXPACKS build pack, specifically focusing on database migration commands.
tags:
    - ruby-on-rails
    - nixpacks
    - deployment
    - database-migration
    - mvc-pattern
category: configuration
---

# Ruby on Rails

Ruby on Rails is a web-application framework that includes everything needed to create database-backend web applications according to the Model-View-Controller (MVC) pattern.

## Requirements

If you would like to migrate the database during the deployment with `NIXPACKS` build pack, you need to set the following `Start Command`:

```bash
bundle exec rake db:migrate && bundle exec bin/rails server -b 0.0.0.0 -p ${PORT:-3000} -e $RAILS_ENV
```