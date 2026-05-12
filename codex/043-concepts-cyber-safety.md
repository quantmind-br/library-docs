---
title: Cyber Safety
url: https://developers.openai.com/codex/concepts/cyber-safety.md
source: llms
fetched_at: 2026-04-30T10:15:23.060146068-03:00
rendered_js: false
word_count: 337
summary: This document outlines the security safeguards and monitoring protocols implemented for GPT-5.3-Codex to prevent malicious cyber activity. It details how legitimate cybersecurity professionals can maintain access to advanced capabilities through the Trusted Access program.
tags:
    - cybersecurity
    - model-safety
    - risk-mitigation
    - trusted-access
    - ai-governance
    - threat-detection
category: concept
optimized: true
optimized_at: 2026-04-30T13:30:00Z
---
# Cyber Safety

[GPT-5.3-Codex](https://openai.com/index/introducing-gpt-5-3-codex/) is the first model treated as High cybersecurity capability under OpenAI's [Preparedness Framework](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf). Additional safeguards include:
- Training the model to refuse clearly malicious requests (e.g., stealing credentials)
- Automated classifier-based monitors detecting signals of suspicious cyber activity
- Routing high-risk traffic to a less cyber-capable model (GPT-5.2)

A very small portion of traffic is expected to be affected. OpenAI is refining policies, classifiers, and in-product notifications.

## Why

Models have improved at cybersecurity tasks like vulnerability discovery, benefiting developers and security professionals. As capabilities improve, OpenAI is taking a precautionary approach: expanding protections to support legitimate research while slowing misuse.

Cyber capabilities are dual-use. The same knowledge underpinning defensive work (penetration testing, vulnerability research, high-scale scanning, malware analysis, threat intelligence) can also enable real-world harm.

## How it works

Developers and security professionals doing cybersecurity-related work may have requests rerouted to GPT-5.2 as a fallback. Automated detection may [mistake](#false-positives) legitimate activity.

The latest alpha version of the Codex CLI includes in-product messaging for reroutes. Support for all clients is coming soon.

Accounts impacted can regain access to GPT-5.3-Codex by joining [Trusted Access for Cyber](#trusted-access-for-cyber).

OpenAI plans to move from account-level safety checks to request-level checks in most cases as mitigations scale.

## Trusted Access for Cyber

Pilot program allowing developers to retain advanced capabilities while policies and classifiers are calibrated. Goal: very few users need to join.

To use models for potentially high-risk cybersecurity work:
- **Users**: verify identity at [chatgpt.com/cyber](https://chatgpt.com/cyber)
- **Enterprises**: request [trusted access](https://openai.com/form/enterprise-trusted-access-for-cyber/) for entire team through OpenAI representative

Security researchers needing even more cyber-capable or permissive models for legitimate defensive work can express interest in the [invite-only program](https://docs.google.com/forms/d/e/1FAIpQLSea_ptovrS3xZeZ9FoZFkKtEJFWGxNrZb1c52GW4BVjB2KVNA/viewform?usp=header).

Users with trusted access must still abide by [Usage Policies](https://openai.com/policies/usage-policies/) and [Terms of Use](https://openai.com/policies/row-terms-of-use/).

## False positives

Legitimate or non-cybersecurity activity may occasionally be flagged. When rerouting occurs, the responding model is visible in API request logs and via in-product notice in the CLI (soon all surfaces).

If you believe rerouting is incorrect, report via `/feedback`.

#cybersecurity #safety #trusted-access #gpt-5-3-codex