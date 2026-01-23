---
title: Email Notifications | liteLLM
url: https://docs.litellm.ai/docs/proxy/email
source: sitemap
fetched_at: 2026-01-21T19:51:50.474939616-03:00
rendered_js: false
word_count: 921
summary: This document provides instructions for configuring and customizing automated email notifications for LiteLLM Proxy events like user creation, API key management, and budget alerts.
tags:
    - litellm
    - email-notifications
    - smtp-configuration
    - budget-alerts
    - branding-customization
    - security-settings
category: guide
---

LiteLLM Email Notifications

## Overview[​](#overview "Direct link to Overview")

Send LiteLLM Proxy users emails for specific events.

CategoryDetailsSupported Events• User added as a user on LiteLLM Proxy  
• Proxy API Key created for user  
• Proxy API Key rotated for userSupported Email Integrations• Resend API  
• SMTP

## Usage[​](#usage "Direct link to Usage")

info

LiteLLM Cloud: This feature is enabled for all LiteLLM Cloud users, there's no need to configure anything.

### 1. Configure email integration[​](#1-configure-email-integration "Direct link to 1. Configure email integration")

- SMTP
- Resend API
- SendGrid API

Get SMTP credentials to set this up

proxy\_config.yaml

```
litellm_settings:
callbacks:["smtp_email"]
```

Add the following to your proxy env

```
SMTP_HOST="smtp.resend.com"
SMTP_TLS="True"
SMTP_PORT="587"
SMTP_USERNAME="resend"
SMTP_SENDER_EMAIL="notifications@alerts.litellm.ai"
SMTP_PASSWORD="xxxxx"
```

### 2. Create a new user[​](#2-create-a-new-user "Direct link to 2. Create a new user")

On the LiteLLM Proxy UI, go to users &gt; create a new user.

After creating a new user, they will receive an email invite a the email you specified when creating the user.

### 3. Configure Budget Alerts (Optional)[​](#3-configure-budget-alerts-optional "Direct link to 3. Configure Budget Alerts (Optional)")

Enable budget alert emails by adding "email" to the `alerts` list in your proxy configuration:

proxy\_config.yaml

```
general_settings:
alerts:["email"]
```

#### Budget Alert Types[​](#budget-alert-types "Direct link to Budget Alert Types")

**Soft Budget Alerts**: Automatically triggered when a key exceeds its soft budget limit. These alerts help you monitor spending before reaching critical thresholds.

**Max Budget Alerts**: Automatically triggered when a key reaches a specified percentage of its maximum budget (default: 80%). These alerts warn you when you're approaching budget exhaustion.

Both alert types send a maximum of one email per 24-hour period to prevent spam.

#### Configuration Options[​](#configuration-options "Direct link to Configuration Options")

Customize budget alert behavior using these environment variables:

.env

```
# Percentage of max budget that triggers alerts (as decimal: 0.8 = 80%)
EMAIL_BUDGET_ALERT_MAX_SPEND_ALERT_PERCENTAGE=0.8

# Time-to-live for alert deduplication in seconds (default: 24 hours)
EMAIL_BUDGET_ALERT_TTL=86400
```

## Email Templates[​](#email-templates "Direct link to Email Templates")

### 1. User added as a user on LiteLLM Proxy[​](#1-user-added-as-a-user-on-litellm-proxy "Direct link to 1. User added as a user on LiteLLM Proxy")

This email is send when you create a new user on LiteLLM Proxy.

**How to trigger this event**

On the LiteLLM Proxy UI, go to Users &gt; Create User &gt; Enter the user's email address &gt; Create User.

### 2. Proxy API Key created for user[​](#2-proxy-api-key-created-for-user "Direct link to 2. Proxy API Key created for user")

This email is sent when you create a new API key for a user on LiteLLM Proxy.

**How to trigger this event**

On the LiteLLM Proxy UI, go to Virtual Keys &gt; Create API Key &gt; Select User ID

On the Create Key Modal, Select Advanced Settings &gt; Set Send Email to True.

### 3. Proxy API Key Rotated for User[​](#3-proxy-api-key-rotated-for-user "Direct link to 3. Proxy API Key Rotated for User")

This email is sent when you rotate an API key for a user on LiteLLM Proxy.

**How to trigger this event**

On the LiteLLM Proxy UI, go to Virtual Keys &gt; Click on a key &gt; Click "Regenerate Key"

info

Ensure there is a `user_id` attached to the key. This would have been set when creating the key.

After regenerating the key, the user will receive an email notification with:

- Security-focused messaging about the rotation
- The new API key (or a placeholder if `EMAIL_INCLUDE_API_KEY=false`)
- Instructions to update their applications
- Security best practices

## Email Customization[​](#email-customization "Direct link to Email Customization")

LiteLLM allows you to customize various aspects of your email notifications. Below is a complete reference of all customizable fields:

FieldEnvironment VariableTypeDefault ValueExampleDescriptionLogo URL`EMAIL_LOGO_URL`stringLiteLLM logo`"https://your-company.com/logo.png"`Public URL to your company logoSupport Contact`EMAIL_SUPPORT_CONTACT`string[support@berri.ai](mailto:support@berri.ai)`"support@your-company.com"`Email address for user supportEmail Signature`EMAIL_SIGNATURE`string (HTML)Standard LiteLLM footer`"<p>Best regards,<br/>Your Team</p><p><a href='https://your-company.com'>Visit us</a></p>"`HTML-formatted footer for all emailsInvitation Subject`EMAIL_SUBJECT_INVITATION`string"LiteLLM: New User Invitation"`"Welcome to Your Company!"`Subject line for invitation emailsKey Creation Subject`EMAIL_SUBJECT_KEY_CREATED`string"LiteLLM: API Key Created"`"Your New API Key is Ready"`Subject line for key creation emailsKey Rotation Subject`EMAIL_SUBJECT_KEY_ROTATED`string"LiteLLM: API Key Rotated"`"Your API Key Has Been Rotated"`Subject line for key rotation emailsInclude API Key`EMAIL_INCLUDE_API_KEY`booleantrue`"false"`Whether to include the actual API key in emails (set to false for enhanced security)Proxy Base URL`PROXY_BASE_URL`string[http://0.0.0.0:4000](http://0.0.0.0:4000)`"https://proxy.your-company.com"`Base URL for the LiteLLM Proxy (used in email links)

## HTML Support in Email Signature[​](#html-support-in-email-signature "Direct link to HTML Support in Email Signature")

The `EMAIL_SIGNATURE` field supports HTML formatting for rich, branded email footers. Here's an example of what you can include:

```
<p>Best regards,<br/>The LiteLLM Team</p>
<p>
<ahref='https://docs.litellm.ai'>Documentation</a> |
<ahref='https://github.com/BerriAI/litellm'>GitHub</a>
</p>
<pstyle='font-size:12px;color:#666;'>
  This is an automated message from LiteLLM Proxy
</p>
```

Supported HTML features:

- Text formatting (bold, italic, etc.)
- Line breaks (`<br/>`)
- Links (`<a href='...'>`)
- Paragraphs (`<p>`)
- Basic inline styling
- Company information and social media links
- Legal disclaimers or terms of service links

## Environment Variables[​](#environment-variables "Direct link to Environment Variables")

You can customize the following aspects of emails through environment variables:

```
# Email Branding
EMAIL_LOGO_URL="https://your-company.com/logo.png"  # Custom logo URL
EMAIL_SUPPORT_CONTACT="support@your-company.com"     # Support contact email
EMAIL_SIGNATURE="<p>Best regards,<br/>Your Company Team</p><p><a href='https://your-company.com'>Visit our website</a></p>"  # Custom HTML footer/signature

# Email Subject Lines
EMAIL_SUBJECT_INVITATION="Welcome to Your Company!"  # Subject for invitation emails
EMAIL_SUBJECT_KEY_CREATED="Your API Key is Ready"    # Subject for key creation emails
EMAIL_SUBJECT_KEY_ROTATED="Your API Key Has Been Rotated"  # Subject for key rotation emails

# Security Settings
EMAIL_INCLUDE_API_KEY="false"  # Set to false to hide API keys in emails (default: true)

# Proxy Configuration
PROXY_BASE_URL="https://proxy.your-company.com"      # Base URL for the LiteLLM Proxy (used in email links)
```

## Security: Hiding API Keys in Emails[​](#security-hiding-api-keys-in-emails "Direct link to Security: Hiding API Keys in Emails")

For enhanced security, you can configure LiteLLM to **not** include actual API keys in email notifications. This is useful when:

- You want to reduce the risk of key exposure via email interception
- Your security policy requires keys to only be retrieved from the secure dashboard
- You're concerned about email forwarding or storage security

When disabled, emails will show: `[Key hidden for security - retrieve from dashboard]` instead of the actual API key.

**Configuration:**

```
# Hide API keys in emails (enhanced security)
EMAIL_INCLUDE_API_KEY="false"

# Include API keys in emails (default behavior)
EMAIL_INCLUDE_API_KEY="true"  # or omit this variable
```

**Behavior:**

SettingKey Created EmailKey Rotated Email`true` (default)Shows actual `sk-xxxxx` keyShows actual `sk-xxxxx` key`false`Shows placeholder messageShows placeholder message

Users can always retrieve their keys from the LiteLLM Proxy dashboard.

## HTML Support in Email Signature[​](#html-support-in-email-signature-1 "Direct link to HTML Support in Email Signature")

The `EMAIL_SIGNATURE` environment variable supports HTML formatting, allowing you to create rich, branded email footers. You can include:

- Text formatting (bold, italic, etc.)
- Line breaks using `<br/>`
- Links using `<a href='...'>`
- Paragraphs using `<p>`
- Company information and social media links
- Legal disclaimers or terms of service links

Example HTML signature:

```
<p>Best regards,<br/>The LiteLLM Team</p>
<p>
<ahref='https://docs.litellm.ai'>Documentation</a> |
<ahref='https://github.com/BerriAI/litellm'>GitHub</a>
</p>
<pstyle='font-size:12px;color:#666;'>
  This is an automated message from LiteLLM Proxy
</p>
```

## Default Templates[​](#default-templates "Direct link to Default Templates")

If environment variables are not set, LiteLLM will use default templates:

- Default logo: LiteLLM logo
- Default support contact: [support@berri.ai](mailto:support@berri.ai)
- Default signature: Standard LiteLLM footer
- Default subjects: "LiteLLM: {event\_message}" (replaced with actual event message)

## Template Variables[​](#template-variables "Direct link to Template Variables")

When setting custom email subjects, you can use template variables that will be replaced with actual values:

```
# Examples of template variable usage
EMAIL_SUBJECT_INVITATION="Welcome to \{company_name\}!"
EMAIL_SUBJECT_KEY_CREATED="Your \{company_name\} API Key"
```

The system will automatically replace `\{event_message\}` and other template variables with their actual values when sending emails.

## FAQ[​](#faq "Direct link to FAQ")

### Why do I see "[http://0.0.0.0:4000](http://0.0.0.0:4000)" in the email links?[​](#why-do-i-see-http00004000-in-the-email-links "Direct link to why-do-i-see-http00004000-in-the-email-links")

The `PROXY_BASE_URL` environment variable is used to construct email links. If you are using the LiteLLM Proxy in a local environment, you will see "[http://0.0.0.0:4000](http://0.0.0.0:4000)" in the email links.

If you are using the LiteLLM Proxy in a production environment, you will see the actual base URL of the LiteLLM Proxy.

You can set the `PROXY_BASE_URL` environment variable to the actual base URL of the LiteLLM Proxy.

```
PROXY_BASE_URL="https://proxy.your-company.com"
```