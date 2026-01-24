---
title: Domains
url: https://docs.docker.com/enterprise/security/single-sign-on/faqs/domain-faqs/
source: llms
fetched_at: 2026-01-24T14:27:05.102760363-03:00
rendered_js: false
word_count: 137
summary: This document provides answers to frequently asked questions about managing and verifying domains for Single Sign-On (SSO), including sub-domain support and DNS record retention.
tags:
    - sso-configuration
    - domain-verification
    - dns-records
    - identity-management
    - docker-business
category: reference
---

## SSO domain FAQs

## [Can I add sub-domains?](#can-i-add-sub-domains)

Yes, you can add sub-domains to your SSO connection. All email addresses must use domains you've added to the connection. Verify that your DNS provider supports multiple TXT records for the same domain.

## [Do I need to keep the DNS TXT record permanently?](#do-i-need-to-keep-the-dns-txt-record-permanently)

You can remove the TXT record after one-time verification to add the domain. However, if your organization changes identity providers and needs to set up SSO again, you'll need to verify the domain again.

## [Can I verify the same domain for multiple organizations?](#can-i-verify-the-same-domain-for-multiple-organizations)

You can't verify the same domain for multiple organizations at the organization level. To verify one domain for multiple organizations, you must have a Docker Business subscription and create a company. Companies allow centralized management of organizations and domain verification at the company level.