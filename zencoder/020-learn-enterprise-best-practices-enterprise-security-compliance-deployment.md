---
title: Enterprise Security, Compliance, and Deployment - Zencoder Docs
url: https://docs.zencoder.ai/learn/enterprise-best-practices/enterprise-security-compliance-deployment
source: crawler
fetched_at: 2026-01-23T09:28:22.711941879-03:00
rendered_js: false
word_count: 925
summary: This document outlines Zencoder's security compliance standards, data privacy architecture, and administrative procedures for team management and billing. It provides instructions for configuring SSO, managing user roles, and monitoring organization-wide AI usage and costs.
tags:
    - security-compliance
    - user-management
    - data-privacy
    - sso-configuration
    - rbac
    - billing-management
    - ai-governance
category: guide
---

### The Security Triple Crown

SOC 2 Type II

ISO/IEC 27001

ISO/IEC 42001

What do these certifications mean for enterprise security?

Together the audits prove Zencoder’s security program is battle-tested and AI-aware: day-to-day operations are monitored, the broader org follows a global security playbook, and AI workflows get their own governance layer. SOC 2 Type II confirms an external auditor watched our production controls run for months and verified they keep customer data safe. ISO/IEC 27001 shows we operate a formal security management system with inventories, risk reviews, policies, and continual improvement. ISO/IEC 42001 extends that rigor to AI, requiring documented responsible-AI practices, data governance, monitoring, and human oversight from model design through deployment.

ISO 42001 is AI-specific; what does it mean?

ISO/IEC 42001 is the world’s first management standard written for AI systems. It forces vendors to document every AI use case, govern the datasets feeding their models, and keep humans in the loop for approvals, monitoring, and incident response. Achieving it means Zencoder treats model training and deployment with the same rigor as traditional security: risk assessments, policies, audit trails, and continuous improvement for the entire AI lifecycle.

What is Zencoder’s zero-storage data privacy architecture?

Every request flows through Zencoder’s proxy, but the code, prompts, and model outputs never land on persistent media—data is encrypted in transit, processed in memory, and discarded once the response is returned. Logs retain only high-level metadata so customers can audit usage without exposing source code, and admins can pin the pipeline to their own LLM tenancy or keys for additional control. The privacy policy, terms of service, and acceptable-use policy lock this in contractually: your content is not written to disk, not mined for training, and only the minimal telemetry required for billing and abuse prevention survives.

### Configuring Single Sign-On and Team Access

How does one setup SSO with Okta or Google Workspace?

Zencoder supports SAML-based single sign-on with Okta and Google Workspace on Core plans and above. Admins simply exchange the IdP metadata with the Zencoder team (or upload it in the SSO section of the dashboard), verify the ACS URL, and flip SSO to “required” for the workspace. From that point users click “Sign in with SSO,” enter the company domain, and are routed through the IdP—no separate Zencoder password to manage.

How to add team members?

Head to Settings → Users and use the “Invite” button to add teammates up to the number of seats on your contract. Each invite captures the user’s email, role, and optional profile info, and the system enforces seat availability automatically. Need to give one engineer extra model usage? Adjust the per-user quota multiplier (1×, 2×, or 5×) before sending the invite so their allowance scales without over-subscribing the workspace.

How to configure role-based access control?

Zencoder keeps RBAC simple: every user is an Owner, Manager, or Member. Owners can manage billing, plan changes, and SSO, while Managers can invite and remove users, adjust quotas, and view org-wide settings. Members are limited to product usage only. Choose the role during the invite flow so privileged accounts stay limited to the small group that actually needs them.

How to manage permissions?

Review the Users page regularly—especially the list of Owners and Managers—so you know exactly who can spend budget or invite new teammates. If someone’s responsibilities change, reach out to Zencoder support to adjust their role (or remove the account and re-invite with the new role); the three-dot menu also lets you delete dormant users in a few clicks. Keeping that roster tidy ensures only the right people wield elevated privileges.

### Subscription Management and Cost Control

How does the per-seat licensing work in Zencoder?

Plans are sold per seat (one paid user). Buy however many seats your org needs, keep everyone on the same tier, and assign them from the Users page. Billing runs monthly; if you add seats mid-cycle you only pay the prorated remainder, then the new seat count appears on the next invoice.

How are LLM calls consumed in Zencoder?

We meter the real LLM calls instead of charging per “agent request.” Each chat run shows how many calls the agent spent and how many remain, factoring in the org plan plus any quota multiplier the user has. That keeps incentives aligned: agents can chain tools freely without silently inflating cost.

How to use BYOK (Bring Your Own Key)? Why use it?

Open the IDE extension’s three-dot menu → Custom API Keys, paste your OpenAI or Anthropic key, and flip the provider toggle. With the key + toggle active the session bills your cloud credits instead of Zencoder’s allotment, which is perfect when you already negotiated rates elsewhere. BYOK works on every plan, even free.

How can we monitor usage of Zencoder in the organization?

Head to the Analytics page in the web dashboard. Pick a 7/30/90-day window to refresh the entire view, check the top-line stats (active users, LOC accepted, LOC generated), and watch the active-users-per-day chart. The Members table breaks down usage per person and you can export it via “Download CSV,” or pull daily metrics from the Analytics API ([https://docs.zencoder.ai/features/analytics-api](https://docs.zencoder.ai/features/analytics-api)).

What if one specific user (not all) needs more usage?

Use the Quota dropdown on the Users page to boost that member to 2× or 5× the base allowance—essentially lending them extra seats. You can change multipliers anytime as long as the extra quota stays within the seats you already purchased. We can also set an account to 0× quota manually so its seat flows to someone who will use it.

[AI Coding Foundations](https://docs.zencoder.ai/learn/enterprise-best-practices/ai-coding-foundations)[Team Collaboration](https://docs.zencoder.ai/learn/enterprise-best-practices/team-collaboration-zen-agents)