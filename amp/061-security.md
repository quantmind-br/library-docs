---
title: Amp Security Reference
url: https://ampcode.com/security
source: crawler
fetched_at: 2026-02-06T02:07:47.838403592-03:00
rendered_js: false
word_count: 2652
summary: This document outlines the security architecture, compliance certifications, and data handling practices for the Amp AI coding agent to assist enterprises with risk assessments. It details how code data is processed by third-party providers and explains encryption, retention, and authentication standards.
tags:
    - security-compliance
    - data-privacy
    - soc2-type-ii
    - data-retention
    - encryption-standards
    - enterprise-security
    - infrastructure-security
category: guide
---

## Keeping your code and development workflow secure is important to us. Amp is built with the security of our *enterprise customers* in mind.

Frontier coding agents such as Amp are more powerful than the previous generation of AI coding tools. This document explains the security characteristics of Amp and helps enterprises make an educated risk assessment.

For any security-related questions, email [security@ampcode.com](mailto:security@ampcode.com).

If you have identified a security vulnerability in Amp, we operate a [bug bounty program](#bug-bounty-program).

## Certifications & Third-Party Assessments[#](#certifications-and-third-party-assessments)[#](#certifications-and-third-party-assessments)

Amp is SOC 2 Type II certified, and we perform annual pentesting of our entire stack, covering clients, backend, and infrastructure.

In addition, Sourcegraph is ISO 27001 certified, and has maintained GDPR and CCPA compliance for several years.

Visit our [Security Trust Portal](https://trust.ampcode.com/) to request a copy of our reports.

## Infrastructure & Service Providers[#](#infrastructure-and-service-providers)[#](#infrastructure-and-service-providers)

Amp uses the following infrastructure and service providers:

- [Google Cloud Platform (GCP)](https://cloud.google.com/) Sees & stores partial code data Our primary infrastructure is hosted on Google Cloud Platform in the US. This infrastructure serves ampcode.com, including storing user and thread data (including partial code data, but not the entire codebase) and providing LLM inference proxied via other providers listed below.
- [Anthropic](https://anthropic.com/) Sees partial code data Anthropic's Claude models hosted on Anthropic's US-based servers are currently used for the majority of LLM inference.
- [OpenAI](https://openai.com/) Sees partial code data OpenAI's models hosted on OpenAI's US-based servers may be used for some LLM inference.
- [xAI](https://x.ai/) Sees partial code data xAI's models hosted on xAI's US-based servers may be used for some LLM inference.
- [Google Cloud Vertex AI](https://cloud.google.com/vertex-ai) Sees partial code data Google Gemini and Anthropic Claude models hosted on Google Cloud Vertex AI (on US servers) may be used for some LLM inference.
- [Amazon Bedrock](https://aws.amazon.com/bedrock/) Sees partial code data Amazon's Bedrock (on US servers) may be used for some LLM inference for Anthropic Claude models.
- [Fireworks](https://fireworks.ai/) Sees partial code data Proprietary Amp models for certain features are hosted on Fireworks servers in the US.
- [Baseten](https://www.baseten.co/) Sees partial code data Proprietary Amp models for certain features are hosted on Baseten servers in the US.
- [Parallel](https://parallel.ai/) Sees no code data Parallel powers web search and web page retrieval tools used by the agent.
- [Sparkpost](https://sparkpost.com/) (now [Bird](https://bird.com/)) Sees no code data All email delivery is handled by Sparkpost. Sparkpost has 10-day retention of email address, header, and diagnostic information but does not retain the email contents.
- [WorkOS](https://workos.com/) Sees no code data WorkOS is used for authentication and user management and stores some personal data (name and email address).
- [Stripe](https://stripe.com/) Sees no code data All billing is handled through Stripe, except for custom enterprise invoicing. Stripe stores personal data (name, email address, payment information) for the purpose of facilitating payment.
- [Google Workspace](https://google.com) Sees no code data We use Google Workspace for internal communication and documents. We may communicate with you about your account over email and to help you use Amp.
- [Slack](https://slack.com) Sees no code data We use Slack for internal communication. We may communicate with you on shared Slack channels about your account and to help you use Amp.
- [Zendesk](https://zendesk.com) Sees no code data We use Zendesk for managing support tickets. We may use Zendesk to communicate with you about support tickets.
- [PostHog](https://posthog.com/) Sees no code data PostHog collects analytics on non-[Enterprise](https://ampcode.com/manual#enterprise) Amp usage and pageviews.

“Partial code data” means snippets of or entire code files that are selected as context for the LLM requests, but not the entire codebase.

We have no infrastructure or service providers based in China.

## Data Security & Retention[#](#data-security-retention)[#](#data-security-retention)

Data such as threads, user information and telemetry on Amp Server is stored in a multi-tenant Google Cloud Platform project, where all service accounts are exclusive to this project.

The Amp Client and Amp Server do not see, store, clone, or index the entire codebase.

The Amp [Enterprise](https://ampcode.com/manual#enterprise) plan (paid or trial) provides zero data retention for text inputs on all LLM providers, which means that any text (including code) sent to LLMs will not retain any input or output beyond the time it takes to generate an output. Images are subject to extremely limited retention periods by LLM providers to ensure compliance with law and the provider’s acceptable usage policy (AUP).

### Thread Data[#](#thread-data)[#](#thread-data)

Thread data includes user messages, LLM responses, snippets of or entire code files used as context for the LLM requests, tool call results, and attachments. When a thread is explicitly deleted, all data for that thread is removed within 30 days of thread deletion.

When a user is deleted, thread data corresponding to that user is handled as follows:

- **Threads in Enterprise workspaces**: Threads created within an [Enterprise workspace](https://ampcode.com/manual#enterprise) are owned by the enterprise that owns the workspace, not the individual user who created the thread. If a user leaves that workspace or deletes their account, their threads (and thread author attribution data, including user names and emails) remain in the workspace. We only delete workspace threads and associated user data when the enterprise’s contract with us ends.
- **Threads in non-Enterprise workspaces**: If the user is in a non-Enterprise workspace and deletes their account, the user’s threads will be deleted along with the user’s account information, pursuant to our [Privacy Policy](https://sourcegraph.com/terms/privacy).
- **Threads created outside any workspace**: Threads created outside of a workspace are deleted when the user deletes their account along with their account information, pursuant to our Privacy Policy. Note that when joining a workspace with the same account as an individual user has used to create personal threads, the user understands and acknowledges that existing personal threads will be visible in the workspace to all workspace members unless: (a) the user makes those threads [“private”](https://ampcode.com/manual#privacy-and-permissions), or (b) the user signs up to the workspace with a separate account under a separate email.

### Encryption Standards[#](#encryption-standards)[#](#encryption-standards)

Amp uses industry-standard encryption practices to protect data:

- **In Transit**: All traffic in transit is encrypted using TLS 1.2+.
- **At Rest**: All data stored by Amp Server is encrypted at the volume level using AES-256. Backups are similarly encrypted.

## Models in Use[#](#models)[#](#models)

See the [Models](https://ampcode.com/models) page for a list of which LLMs are currently used by Amp. All model inference is performed on the [infrastructure & service providers](#infrastructure-and-service-providers) documented above.

Enterprise workspaces can disable ad-supported free usage (Daily Grant) for all members of their workspace.

## User Authentication[#](#user-authentication)[#](#user-authentication)

[Amp Enterprise](https://ampcode.com/manual#enterprise) supports **Single Sign-On** (SSO) and **Directory Sync** through various identity providers, including Okta, for user authentication. We use [WorkOS](https://workos.com) to provide this capability and the SSO configuration and management dashboard for Workspace Admins.

SSO can be configured to be the exclusive authentication method for your workspace, preventing the use of password-based authentication.

Directory Sync (e.g. SCIM) can be used for automatic provisioning and de-provisioning of user accounts and groups. This allows organizations to automatically manage user access based on their identity provider’s user directory, ensuring that access is granted or revoked when users join or leave the organization.

To set up SSO and Directory Sync, go to your [Workspace Settings](https://ampcode.com/workspace) page.

## Audit Logging[#](#audit-logging)[#](#audit-logging)

Audit logs for [user authentication-related events](https://workos.com/docs/events/authentication) are available to Workspace Admins in [Enterprise](https://ampcode.com/manual#enterprise) workspaces.

Amp maintains comprehensive application audit logs for security and monitoring purposes. Logs are structured and include key fields such as timestamps, actor IDs, request details, and event information. These logs are collected internally and monitored by the Amp security team, but are not currently exposed to Workspace Admins.

Application audit logs can be provided for Enterprise workspaces upon request, for example during customer audits or incidents.

Audit logs are retained for a minimum of 30 days.

## Model Training[#](#model-training)[#](#model-training)

Amp does not train models on your data, unless you have explicitly opted into training.

If you’re on an Amp workspace, turning training on requires the approval of the Workspace Admin.

On an [Amp Enterprise](https://ampcode.com/manual#enterprise) workspace plan (paid or trial) training can *never* be enabled.

To enable or disable training, go to [User Settings](https://ampcode.com/settings#training).

Ad-supported free usage (Daily Grant) does not require opting into training.

## System Components[#](#system-components)[#](#system-components)

Amp consists of two components:

1. **Amp Client:** The end-user application that is used as a [VS Code extension](https://marketplace.visualstudio.com/items?itemName=sourcegraph.amp) (in VS Code or a compatible fork) or a [CLI program](https://www.npmjs.com/package/@sourcegraph/amp). The client provides the user interface, local code and context management, local settings, and local thread history. It communicates with and executes tools as requested by Amp Server (ampcode.com).
2. **Amp Server:** A multi-tenant cloud service at ampcode.com, hosted on Google Cloud Platform. It handles authentication, user accounts, workspaces, thread syncing and storage, and usage tracking. It also acts as a proxy for LLM inference between the Amp Client and the LLM providers listed above.

Amp doesn’t support [Bring Your Own Key](https://ampcode.com/news/no-more-byok) or self-hosted deployments.

## User Interaction Example[#](#user-interaction-example)[#](#user-interaction-example)

When users use Amp, they create and send messages in threads to the agent. A thread is a single conversation between the user and the agent, with any number of back-and-forths among the user, tools, and LLM.

When a developer starts a new thread in an Amp Client, the client collects local contextual information such as code snippets, metadata about open files, and relevant editor state. For additional context, the agent may use built-in tools such as `Bash` or MCP servers (Model Context Protocol) to provide additional information. The collected context, along with the user’s prompt and conversation history, if applicable, is sent to Amp Server and then to the LLM inference provider.

After processing, the LLM’s response is returned through Amp Server back to the Amp Client. The Amp Client displays the response and takes additional actions based on the response, such as reading files requested by the LLM and sending them back to Amp Server for the next step in the agentic loop.

Amp Server stores these conversations in its PostgreSQL database in Google Cloud Platform, which enables team collaboration features such as thread sharing and auditing. Users can mark a thread as *private* to prevent it from being shared with other workspace members.

## Client Security[#](#client-security)[#](#client-security)

- The VS Code extension stores credentials using VS Code’s built-in `SecretStorage` API, which uses the system’s native credential store (Keychain on macOS, Credential Manager on Windows, libsecret on Linux).
  
  - Thread history is cached locally by the extension and stored in the extension’s VS Code `globalStorage` directory.
- The Amp Client makes HTTP requests to the following domains. If you’re behind a corporate proxy, please allowlist these domains to ensure that Amp works correctly.
  
  - [`ampcode.com`](https://ampcode.com/): For the Amp Server service.
  - [`auth.ampcode.com`](https://auth.ampcode.com/) and [`authapi.ampcode.com`](https://authapi.ampcode.com/): For authentication to ampcode.com.
- The Amp CLI stores credentials in `~/.local/share/amp/secrets.json` on Linux and macOS, and `%USERPROFILE%\.local\share\amp\secrets.json` on Windows.
- The Amp Client makes a best effort to avoid reading `.env` files and other credentials files.

## Secret Redaction[#](#secret-redaction)[#](#secret-redaction)

Amp automatically detects and redacts secrets before they can enter threads or be transmitted to any external service. This protection operates at the lowest level of the system to ensure that detected secrets are never visible to the LLM, stored in local cache, transmitted to LLM providers, or saved on ampcode.com.

When a secret is detected, it is replaced with a redaction marker like `[REDACTED:amp]` that indicates the type of secret found without exposing the actual value.

**Supported secret types:** Amp detects many common secrets including:

- **Cloud providers:** AWS, Google Cloud, and Azure credentials.
- **Development platforms:** GitHub, GitLab, Sourcegraph, and Amp access tokens.
- **LLM providers:** OpenAI, Anthropic, and HuggingFace API keys.
- **Common services:** Stripe, Slack, and npm tokens.
- **Generic patterns:** API keys, webhook secrets, and password fields.

**Limitations:** Secret redaction is best-effort and may not catch all possible secret formats, especially:

- Secrets in non-standard formats or custom internal systems.
- Secrets that don’t follow recognizable patterns.
- Encoded or obfuscated secrets.

**If a secret is not automatically redacted:**

- Edit the message that precedes the secret being read and resend it, which will overwrite the thread contents on ampcode.com.
- Mark the thread as private (this prevents workspace sharing but does not remove the secret from ampcode.com).
- Consider rotating the exposed secret as a security precaution.

Supported secret types are regularly updated to cover new services and formats. Contact Support if you would like a new secret type to be added.

## Bug Bounty Program[#](#bug-bounty-program)[#](#bug-bounty-program)

Amp operates an open bug bounty program to compensate researchers for their work to make Amp more secure. We welcome reports from security researchers and the general public.

If you believe you have discovered a security issue:

- Familiarize yourself with the following terms of our bug bounty program.
- Report the issue to [disclosure@ampcode.com](mailto:disclosure@ampcode.com), providing all relevant information. The more details you provide, the easier it will be for us to triage and fix the issue.

### In Scope[#](#in-scope)[#](#in-scope)

- [ampcode.com](https://ampcode.com) and related digital assets owned, operated, or maintained by Amp.
- The Amp CLI and editor extensions for VS Code, Cursor, JetBrains, Neovim, and other editors.

### Out of Scope[#](#out-of-scope)[#](#out-of-scope)

- We’re interested in prompt injection and LLM security research—please report findings to us. However, due to LLMs’ inherent nature and Amp’s code execution capabilities, these vulnerabilities aren’t typically eligible for bug bounty rewards.
- Assets not related to Amp, or not owned by Amp or Sourcegraph.

Vulnerabilities discovered or suspected in out-of-scope systems should be reported to the appropriate vendor or authority.

### Our Commitments[#](#our-commitments)[#](#our-commitments)

When working with us, according to this policy, you can expect us to:

- Respond to your report promptly, and work with you to understand and validate your report;
- Keep you informed about the progress of a vulnerability as it is processed;
- Work to remediate discovered vulnerabilities in a timely manner, within our operational constraints; and
- Extend Safe Harbor for your vulnerability research that is related to this policy.

### Our Expectations[#](#our-expectations)[#](#our-expectations)

In participating in our vulnerability disclosure program in good faith, we ask that you:

- Play by the rules, including following this policy and any other relevant agreements. If there is any inconsistency between this policy and any other applicable terms, the terms of this policy will prevail;
- Report any vulnerability you’ve discovered promptly;
- Avoid violating the privacy of others, disrupting our systems, destroying data, and/or harming user experience;
- Use only the Official Channels to discuss vulnerability information with us;
- Provide us a reasonable amount of time (at least 30 days from the initial report) to resolve the issue before you disclose it publicly;
- Perform testing only on in-scope systems, and respect systems and activities which are out-of-scope;
- If a vulnerability provides unintended access to data: Limit the amount of data you access to the minimum required for effectively demonstrating a Proof of Concept; and cease testing and submit a report immediately if you encounter any user data during testing, such as Personally Identifiable Information (PII) or proprietary information;
- Interact only with test accounts you own or with explicit permission from the account holder; and
- Do not engage in extortion.

### Official Channels[#](#official-channels)[#](#official-channels)

Security issues should only be reported via [disclosure@ampcode.com](mailto:disclosure@ampcode.com).

### Safe Harbor[#](#safe-harbor)[#](#safe-harbor)

When conducting vulnerability research, according to this policy, we consider this research conducted under this policy to be:

- Authorized under any applicable anti-hacking laws, and we will not initiate or support legal action against you for accidental, good-faith violations of this policy;
- Authorized under any relevant anti-circumvention laws, and we will not bring a claim against you for circumvention of technology controls;
- Exempt from restrictions in our Terms of Service (TOS) and/or Acceptable Usage Policy (AUP) that would interfere with conducting security research, and we waive those restrictions on a limited basis; and
- Lawful, helpful to the overall security of the Internet, and conducted in good faith.

You are expected, as always, to comply with all applicable laws. If legal action is initiated by a third party against you and you have complied with this policy, we will take steps to make it known that your actions were conducted in compliance with this policy.

If at any time you have concerns or are uncertain whether your security research is consistent with this policy, please submit a report through one of our Official Channels before going any further.

*Note that the Safe Harbor applies only to legal claims under the control of the organization participating in this policy, and that the policy does not bind independent third parties.*