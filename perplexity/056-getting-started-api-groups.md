---
title: API Groups & Billing
url: https://docs.perplexity.ai/docs/getting-started/api-groups.md
source: llms
fetched_at: 2026-02-04T07:22:52.855783677-03:00
rendered_js: false
word_count: 651
summary: This document explains how to set up and manage API Groups, organization details, and credit-based billing within the Perplexity API Portal.
tags:
    - api-portal
    - api-groups
    - billing
    - payment-methods
    - usage-monitoring
    - account-management
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# API Groups & Billing

> Learn how to use the Perplexity API Portal to manage access, usage, billing, and team collaboration.

## What is an API Group?

An **API Group** is your organization's workspace in the Perplexity API Portal. It allows you to:

* **Manage billing** and payment methods for API usage
* **Create and control API keys** for accessing the Perplexity API
* **Invite team members** and control their permissions (optional)
* **Monitor usage and costs** across all your API keys

## Prerequisites

Before getting started, make sure you have:

* A Perplexity account (sign up at [perplexity.ai](https://perplexity.ai))
* **Admin permissions** for billing and API key management
* A **credit card** ready for payment setup (you won't be charged initially)

<Note>
  If you're joining an existing team, you'll need an invitation from an Admin. Contact your team lead to get access.
</Note>

## Accessing the API Portal

Once signed in, navigate to the left-hand sidebar and expand the **API** section to access your API group and related settings.

<Frame>
  <img src="https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/api_group_location.png?fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=2f973650a8668a7ca088b6292875361c" alt="API Group Location" data-og-width="202" width="202" data-og-height="180" height="180" data-path="docs/assets/images/api_portal/api_group_location.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/api_group_location.png?w=280&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=f5be204cff10d93fba140c6fbd7ece8e 280w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/api_group_location.png?w=560&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=94970ac6773ac872f4cffa3b16e20a7e 560w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/api_group_location.png?w=840&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=dedffe27a08375b82455b39fa993b1a4 840w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/api_group_location.png?w=1100&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=70826f8ea6eb38288f925a435a5368a2 1100w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/api_group_location.png?w=1650&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=54a6f4972ffc44738547cb775b4fbd55 1650w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/api_group_location.png?w=2500&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=5d16da31ac9d77c19615cb6d3977a131 2500w" />
</Frame>

***

## Creating and Managing an API Group

To set up your organization:

<Steps>
  <Step title="Access API Group Settings">
    Click **API Group** in the left sidebar.
  </Step>

  <Step title="Complete Organization Details">
    Fill out your organization's name, address, and tax details.

    <Info>
      Your organization name and address will appear on invoices and help us support you better.
    </Info>

    **Fields include:**

    * Organization name and description
    * Address (Line 1, Line 2, City, State, Zip, Country)
    * Tax ID

    <Frame>
      <img src="https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/api_group_details.png?fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=13ffb9e9b89d4a491ec2ebce628531cc" alt="API Group Details" data-og-width="821" width="821" data-og-height="842" height="842" data-path="docs/assets/images/api_portal/api_group_details.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/api_group_details.png?w=280&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=fce4da0a840de2f2f64c67cd7c59b97f 280w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/api_group_details.png?w=560&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=a6b6faab83320d973cfcaf2635c26948 560w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/api_group_details.png?w=840&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=16373f18d90969cc3ddad2bc22a04165 840w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/api_group_details.png?w=1100&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=4f83089009d9020d7c514bcb6b903ead 1100w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/api_group_details.png?w=1650&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=a6719529574bbe9aea336d792cf97537 1650w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/api_group_details.png?w=2500&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=beaa4ce3031f670bf3bb7abaa1abeb92 2500w" />
    </Frame>
  </Step>
</Steps>

***

## Billing and Payment Methods

### How Billing Works

The Perplexity API uses a **credit-based billing system**:

* **Credits** are purchased in advance and used for API calls
* **Different models** consume different amounts of credits per request
* **Usage is charged** based on tokens processed and search queries made
* **Automatic top-up** can be enabled to avoid service interruptions

<Info>
  See our [Pricing page](./pricing) for detailed cost information per model and usage type.
</Info>

### Setting Up Payment

<Card title="Access Billing Dashboard" icon="credit-card" arrow="True" horizontal="True" iconType="solid" cta="Go to Billing" href="https://www.perplexity.ai/account/api/billing">
  Navigate directly to your API billing dashboard to manage payment methods, view usage, and configure billing settings.
</Card>

<Steps>
  <Step title="Navigate to Billing">
    Go to the **API Billing** tab in your API Portal.

    <Frame>
      <img src="https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/api_billing.png?fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=1097738622cc99e6118401234d2336e2" alt="API Billing" data-og-width="731" width="731" data-og-height="288" height="288" data-path="docs/assets/images/api_portal/api_billing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/api_billing.png?w=280&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=bb63d5b9fcac599271b79482d759e3aa 280w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/api_billing.png?w=560&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=d1a09aaf698b8408b98da138cfa01a6b 560w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/api_billing.png?w=840&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=8f3ab18531fda72bbdb6922fd5b6ad36 840w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/api_billing.png?w=1100&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=eef08afac98afcc0046b9faa6cff7248 1100w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/api_billing.png?w=1650&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=0387f3b0c79b56533b3a1812bb9e3ee5 1650w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/api_billing.png?w=2500&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=353a3786a9c7e2f1bb1b034bf7c17f06 2500w" />
    </Frame>
  </Step>

  <Step title="Add Payment Method">
    Click **Add Payment Method** and enter your credit card information.

    <Note>
      This step will not charge your credit card. It just stores payment information for future API usage.
    </Note>
  </Step>

  <Step title="Configure Auto Top-Up (Recommended)">
    Enable automatic credit top-up to avoid service interruptions.

    <Frame>
      <img src="https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/auto_reload.png?fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=8098883c0cee70e2aad31ec6098c8a23" alt="Auto Reload" data-og-width="708" width="708" data-og-height="227" height="227" data-path="docs/assets/images/api_portal/auto_reload.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/auto_reload.png?w=280&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=f43c7930bc417b993d087d763b1117f4 280w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/auto_reload.png?w=560&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=705ec834f1c85c3e317f82594f336600 560w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/auto_reload.png?w=840&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=55c431281d45b612a5d41b9ce7799459 840w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/auto_reload.png?w=1100&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=fd945476bf8dbf7832882319e408a39b 1100w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/auto_reload.png?w=1650&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=be7b717cb7cc332e022665d39ded42fc 1650w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/auto_reload.png?w=2500&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=24d52402614936988e8f8f1a18e55068 2500w" />
    </Frame>

    <Warning>
      If you run out of credits, your API keys will be blocked until you add to your credit balance. Auto top-up prevents this by automatically adding credits when your balance drops below a threshold.
    </Warning>
  </Step>
</Steps>

***

## Managing API Keys

### What are API Keys?

API keys are your credentials for accessing the Perplexity API. Each key:

* **Authenticates your requests** to the Perplexity API
* **Tracks usage and billing** for cost attribution
* **Can be revoked or regenerated** for security purposes
* **Should be kept secure** and never shared publicly

<Info>
  You'll need to include your API key in the Authorization header of every API request: `Authorization: Bearer YOUR_API_KEY`
</Info>

### Creating an API Key

<Steps>
  <Step title="Navigate to API Keys">
    Go to the **API Keys** tab in your API Portal.
  </Step>

  <Step title="Generate New Key">
    Click **+ Create Key** to generate a new API key.

    <Frame>
      <img src="https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/generate_api_keys.png?fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=0897ceb61302037b3630d6fabaa080a9" alt="Generate API Keys" data-og-width="737" width="737" data-og-height="158" height="158" data-path="docs/assets/images/api_portal/generate_api_keys.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/generate_api_keys.png?w=280&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=2f3b84f9032536451c24c516cbb5df03 280w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/generate_api_keys.png?w=560&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=11ef51e27c539a0dcadc22833bf41fd6 560w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/generate_api_keys.png?w=840&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=c86da88e0b966a6ece8d277c2a763be8 840w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/generate_api_keys.png?w=1100&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=c84411adb640b92abad76d4542f07b8d 1100w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/generate_api_keys.png?w=1650&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=ffea12fe75485804dc48a2bd00046617 1650w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/generate_api_keys.png?w=2500&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=0839dc4d344e91653602e87c986c172d 2500w" />
    </Frame>
  </Step>

  <Step title="Secure Your Key">
    Copy and securely store your API key immediately.

    <Warning>
      API keys are sensitive credentials. Never expose them in client-side code or share them in public repositories.
    </Warning>
  </Step>
</Steps>

***

## Adding and Managing Members

Admins can invite team members to the organization with specific roles: **Admin** or **Member**.

### Adding a Member

<Steps>
  <Step title="Initiate Member Invitation">
    Click **+ Add Member**.

    <Frame>
      <img src="https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/click_on_add_member.png?fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=b747a3ffd121f74eeb36621bd605449e" alt="Click on Add Member" data-og-width="746" width="746" data-og-height="154" height="154" data-path="docs/assets/images/api_portal/click_on_add_member.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/click_on_add_member.png?w=280&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=5729b4821c95115276336ea5122e76d1 280w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/click_on_add_member.png?w=560&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=df51113b91b5b3f45f67dddd63683b8a 560w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/click_on_add_member.png?w=840&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=dd4046d5c51e229e74df213279302174 840w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/click_on_add_member.png?w=1100&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=efce0acd601042d770b121dc8b6ed809 1100w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/click_on_add_member.png?w=1650&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=f168d3a41f00dd51bca79c338a2bd743 1650w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/click_on_add_member.png?w=2500&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=fbcf348ebe93198a42afc71475a60656 2500w" />
    </Frame>
  </Step>

  <Step title="Enter Member Details">
    Enter the user's email address and click **Invite**.

    <Frame>
      <img src="https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/enter_new_member_email.png?fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=fa913ab5e5c00e5180a76fa2bc39dfb1" alt="Enter New Member Email" data-og-width="549" width="549" data-og-height="258" height="258" data-path="docs/assets/images/api_portal/enter_new_member_email.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/enter_new_member_email.png?w=280&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=c9a598e2ffed96e81b6f9be8e511f907 280w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/enter_new_member_email.png?w=560&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=829d23a52cb20fff8e44313cabf7f700 560w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/enter_new_member_email.png?w=840&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=d31dcab570671e2e0822de3bba7030a8 840w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/enter_new_member_email.png?w=1100&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=fd77be40463afce8695edfb1a4824e6f 1100w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/enter_new_member_email.png?w=1650&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=cd24f1ad534d66024a22f67cfa43e200 1650w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/enter_new_member_email.png?w=2500&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=6731b844f7e94da1ae71c09f291c0c54 2500w" />
    </Frame>
  </Step>

  <Step title="Member Receives Invitation">
    The invited user will receive an email with a link to join your group.

    <Check>
      Once they accept, they'll appear in your member list with their assigned role.
    </Check>
  </Step>
</Steps>

### Filtering Members by Role

Use the dropdown to filter your list of team members by role.

<Frame>
  <img src="https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/filter_members_by_role.png?fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=b2b794439ae3486730727655433a3517" alt="Filter Members by Role" data-og-width="379" width="379" data-og-height="236" height="236" data-path="docs/assets/images/api_portal/filter_members_by_role.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/filter_members_by_role.png?w=280&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=2218a7ab464979a8b0b37cf381f88a3a 280w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/filter_members_by_role.png?w=560&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=90e1a1f77d0bb3b3379c26eed5a6fd7e 560w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/filter_members_by_role.png?w=840&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=572ad5fcdcd3a83ad5de2345faa6e9b1 840w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/filter_members_by_role.png?w=1100&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=7afcc219cc7f2d2aee8a8ac09c6e024c 1100w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/filter_members_by_role.png?w=1650&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=0ec5bdccbea212eb2b7cf487743cb4af 1650w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/api_portal/filter_members_by_role.png?w=2500&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=fb066f54d1b56626b1e06f865a457674 2500w" />
</Frame>

### Roles

* **Admin**: Full access to invite/remove members, manage billing, and view usage data.
* **Member**: Can view usage and account limits but cannot modify settings.

<Warning>
  Only Admins can make changes to billing and member permissions.
</Warning>

***

## Viewing Usage Metrics

All members can view API usage by selecting **Usage Metrics** from the sidebar.

Features include:

* Total API call trends over time
* Breakdown by API model and key
* Optional date range filters

<Check>
  Usage metrics help you monitor API activity and optimize for cost or performance.
</Check>

### Tracking Spend Per API Key

You can track billing for each of your API keys by following these steps:

<Steps>
  <Step title="Navigate to Usage Metrics">
    Navigate to the [API section](https://www.perplexity.ai/account/api) of your **Settings** and click on **Usage Metrics**

    <Frame>
      <img src="https://mintlify.s3.us-west-1.amazonaws.com/perplexity/guides/assets/pricing/view_dashboard.png" alt="Navigate to dashboard" />
    </Frame>
  </Step>

  <Step title="Access Invoice History">
    Select **Invoice history** > **Invoices**

    <Frame>
      <img src="https://mintlify.s3.us-west-1.amazonaws.com/perplexity/guides/assets/pricing/view_invoice_history.png" alt="View invoice history" />
    </Frame>
  </Step>

  <Step title="View Invoice Details">
    Click on any invoice to view details

    <Frame>
      <img src="https://mintlify.s3.us-west-1.amazonaws.com/perplexity/guides/assets/pricing/view_spend_per_api_key.png" alt="View spend per API key" />
    </Frame>
  </Step>

  <Step title="Identify API Key Charges">
    Each item from the total bill will have a code at the end (e.g., pro (743S))

    * The 4 characters in parentheses are the last 4 characters of your API key
  </Step>
</Steps>