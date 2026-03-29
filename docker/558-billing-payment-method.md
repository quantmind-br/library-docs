---
title: Add or update a payment method
url: https://docs.docker.com/billing/payment-method/
source: llms
fetched_at: 2026-01-24T14:14:46.432903712-03:00
rendered_js: false
word_count: 257
summary: This document provides instructions on how to add or update payment methods for personal and organization accounts, while outlining policies for taxes, invoices, and failed payments.
tags:
    - billing-management
    - payment-methods
    - subscription-billing
    - sales-tax
    - vat-information
    - invoice-processing
    - payment-recovery
category: guide
---

This page describes how to add or update a payment method for your personal account or for an organization.

You can add a payment method or update your account's existing payment method at any time.

All charges are in United States dollars (USD).

For United States customers, Docker began collecting sales tax on July 1, 2024. For European customers, Docker began collecting VAT on March 1, 2025. For United Kingdom customers, Docker began collecting VAT on May 1, 2025.

To ensure that tax assessments are correct, make sure that your [billing information](https://docs.docker.com/billing/details/) and VAT/Tax ID, if applicable, are updated. If you're exempt from sales tax, see [Register a tax certificate](https://docs.docker.com/billing/tax-certificate/).

Pay by invoice is available for Teams and Business customers with annual subscriptions, starting with your first renewal. When you select this payment method, you'll pay upfront for your first subscription period using a payment card or ACH bank transfer.

At renewal time, instead of automatic payment, you'll receive an invoice via email that you must pay manually. Pay by invoice is not available for subscription upgrades or changes.

If your subscription payment fails, there is a grace period of 15 days, including the due date. Docker retries to collect the payment 3 times using the following schedule:

Docker also sends an email notification `Action Required - Credit Card Payment Failed` with an attached unpaid invoice after each failed payment attempt.

Once the grace period is over and the invoice is still not paid, the subscription downgrades to a free subscription and all paid features are disabled.