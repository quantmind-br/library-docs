---
title: Configure
url: https://docs.docker.com/enterprise/security/single-sign-on/configure/
source: llms
fetched_at: 2026-01-24T14:27:03.34529561-03:00
rendered_js: false
word_count: 389
summary: Provides instructions for administrators to set up single sign-on (SSO) for Docker organizations by adding and verifying domains using DNS TXT records.
tags:
    - docker-sso
    - domain-verification
    - dns-configuration
    - single-sign-on
    - identity-provider
    - docker-admin
category: guide
---

## Configure single sign-on

Subscription: Business

Requires: Docker Desktop [4.42](https://docs.docker.com/desktop/release-notes/#4420) and later

For: Administrators

Learn how to set up single sign-on (SSO) for your Docker organization by adding and verifying the domains your members use to sign in.

## [Step one: Add a domain](#step-one-add-a-domain)

> Note
> 
> Docker supports multiple identity provider (IdP) configurations. You can associate one domain with more than one IdP.

To add a domain:

1. Sign in to [Docker Home](https://app.docker.com) and choose your organization. If it's part of a company, select the company first to manage the domain at that level.
2. Select **Admin Console**, then **Domain management**.
3. Select **Add a domain**.
4. Enter your domain in the text box and select **Add domain**.
5. In the modal, copy the **TXT Record Value** provided for domain verification.

## [Step two: Verify your domain](#step-two-verify-your-domain)

To confirm domain ownership, add a TXT record to your Domain Name System (DNS) host using the TXT Record Value from Docker. DNS propagation can take up to 72 hours. Docker automatically checks for the record during this time.

> Tip
> 
> When adding a record name, **use `@` or leave it empty** for root domains like `example.com`. **Avoid common values** like `docker`, `docker-verification`, `www`, or your domain name itself. Always **check your DNS provider's documentation** to verify their specific record name requirements.

1. To add your TXT record to AWS, see [Creating records by using the Amazon Route 53 console](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-creating.html).
2. Wait up to 72 hours for TXT record verification.
3. After the record is live, go to **Domain management** in the [Admin Console](https://app.docker.com/admin) and select **Verify**.

<!--THE END-->

1. To add your TXT record to Google Cloud DNS, see [Verifying your domain with a TXT record](https://cloud.google.com/identity/docs/verify-domain-txt).
2. Wait up to 72 hours for TXT record verification.
3. After the record is live, go to **Domain management** in the [Admin Console](https://app.docker.com/admin) and select **Verify**.

<!--THE END-->

1. To add your TXT record to GoDaddy, see [Add a TXT record](https://www.godaddy.com/help/add-a-txt-record-19232).
2. Wait up to 72 hours for TXT record verification.
3. After the record is live, go to **Domain management** in the [Admin Console](https://app.docker.com/admin) and select **Verify**.

<!--THE END-->

1. Sign in to your domain host.
2. Add a TXT record to your DNS settings and save the record.
3. Wait up to 72 hours for TXT record verification.
4. After the record is live, go to **Domain management** in the [Admin Console](https://app.docker.com/admin) and select **Verify**.

## [Next steps](#next-steps)

- [Connect Docker and your IdP](https://docs.docker.com/enterprise/security/single-sign-on/connect/).
- [Troubleshoot](https://docs.docker.com/enterprise/troubleshoot/troubleshoot-sso/) SSO issues.