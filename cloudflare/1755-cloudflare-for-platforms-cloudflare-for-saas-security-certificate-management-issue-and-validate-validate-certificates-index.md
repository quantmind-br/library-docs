---
title: Validate certificates · Cloudflare for Platforms docs
url: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/index.md
source: llms
fetched_at: 2026-01-24T15:10:57.852021947-03:00
rendered_js: false
word_count: 210
summary: This document explains the various methods and requirements for performing Domain Control Validation (DCV) to issue and renew SSL/TLS certificates for custom hostnames.
tags:
    - domain-control-validation
    - dcv
    - ssl-tls-certificates
    - cloudflare-for-saas
    - wildcard-certificates
    - dns-validation
    - certificate-renewal
category: guide
---

Before a certificate authority (CA) will issue a certificate for a domain, the requester must prove they have control over that domain. This process is known as domain control validation (DCV).



## DCV situations

### Non-wildcard certificates

Specific (non-wildcard) custom hostnames can use [HTTP based DCV](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/http/) for certificate renewals, as long as:

* The hostname is pointing to the SaaS provider.
* The hostname's traffic is proxying through the Cloudflare network.

If your custom hostnames do not meet these requirements, use another validation method.

### Wildcard certificates

Wildcard custom hostnames require TXT-based validation. As the SaaS provider, you have two options for wildcard custom hostname certificate renewals:



* [DCV Delegation](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/delegated-dcv/) (auto-issuance)
* [Manual](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/txt/)

### Minimize downtime

If you want to minimize downtime, explore one of the following methods to issue and deploy the certificate before onboarding your customers:

* [Delegated DCV](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/delegated-dcv/): Place a one-time record at your authoritative DNS that allows Cloudflare to auto-renew all future certificate orders.
* [TXT validation](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/txt/): Have your customers add a `TXT` record to their authoritative DNS.
* [Manual HTTP validation](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/http/#http-manual): Add a `TXT` record at your origin.

### Minimize customer effort

If you value simplicity and your customers can handle a few minutes of downtime, you can rely on Cloudflare [automatic HTTP validation](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/http/#http-automatic).

## Potential issues

To avoid or solve potential issues, refer to our [troubleshooting guide](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/troubleshooting/).