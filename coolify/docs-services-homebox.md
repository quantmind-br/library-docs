---
title: Homebox
url: https://coolify.io/docs/services/homebox.md
source: llms
fetched_at: 2026-02-17T14:44:46.635149-03:00
rendered_js: false
word_count: 133
summary: This document introduces Homebox, a home inventory and organization system, and provides instructions for configuring initial user registration using environment variables.
tags:
    - home-inventory
    - asset-management
    - self-hosted
    - docker-configuration
    - inventory-system
category: guide
---

# Homebox

## What is Homebox?

Homebox is an inventory and organization system built specifically for home users. It allows you to catalog and track your belongings, create locations and categories, manage warranties and receipts, and keep detailed records of your household items. Homebox is perfect for insurance purposes, organizing collections, and general home inventory management with features like photo attachments, search functionality, and reporting capabilities.

## Configuration

In order to create your first account you will have to head to the environment variables for Homebox and set `HBOX_OPTIONS_ALLOW_REGISTRATION` to true and restart your docker for the change to take effect.
You are now able to create your first account, after which you can set `HBOX_OPTIONS_ALLOW_REGISTRATION` to false again to prevent new registrations, or keep them opened for other users to join your homebox.

## Links

* [GitHub](https://github.com/hay-kot/homebox?utm_source=coolify.io)