---
title: Email Routing analytics · Cloudflare Email Routing docs
url: https://developers.cloudflare.com/email-routing/get-started/email-routing-analytics/index.md
source: llms
fetched_at: 2026-01-24T15:13:50.626341422-03:00
rendered_js: false
word_count: 145
summary: This document explains how to use the Email Routing Overview page to monitor account metrics, track routing activity, and verify security statuses such as SPF and DKIM.
tags:
    - email-routing
    - dashboard-overview
    - activity-log
    - email-metrics
    - security-protocols
    - spf
    - dkim
    - dmarc
category: guide
---

The Overview page shows you a summary of your account. You can check details such as how many custom and destination addresses you have configured, as well as the status of your routing service.

## Email Routing summary

In Email Routing summary you can check metrics related the number of emails received, forwarded, dropped, and rejected. To filter this information by time interval, select the drop-down menu. You can choose preset periods between the previous 30 minutes and 30 days, as well as a custom date range.

## Activity Log

This section allows you to sort through emails received, and check Email Routing actions - for example, `Forwarded`, `Dropped`, or `Rejected`. Select a specific email to expand its details and check information regarding the [SPF](https://datatracker.ietf.org/doc/html/rfc7208), [DKIM](https://datatracker.ietf.org/doc/html/rfc6376), and [DMARC](https://datatracker.ietf.org/doc/html/rfc7489) statuses. Depending on the information shown, you can opt to mark an email as spam or block the sender.