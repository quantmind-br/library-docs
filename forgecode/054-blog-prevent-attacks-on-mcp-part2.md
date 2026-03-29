---
title: 'MCP Security Prevention: Practical Strategies for AI Development - Part 2'
url: https://forgecode.dev/blog/prevent-attacks-on-mcp-part2/
source: sitemap
fetched_at: 2026-03-29T14:48:32.315489824-03:00
rendered_js: false
word_count: 810
summary: This document provides security guidance for protecting AI systems and MCP servers from prompt injection attacks, credential theft, and resource exploitation based on OWASP and NIST frameworks.
tags:
    - ai-security
    - prompt-injection
    - mcp-servers
    - owasp-top-10
    - nist-framework
    - credential-security
    - resource-limiting
    - semantic-validation
category: guide
---

Elevenlabs AudioNative Player

> **TL;DR**: Attackers are stealing convo history via MCP servers—let's stop that. OWASP ranks prompt injection as the top threat. This post shares practical steps to protect your systems.

*This is Part 2. [← Read Part 1 if you missed the carnage](https://forgecode.dev/blog/prevent-attacks-on-mcp/)*

Trail of Bits dropped a bomb & MCP servers are getting wrecked by these attacks:

- **Line Jumping attacks**[1](#footnote-1) - malicious servers inject prompts through tool descriptions. Your AI can be tricked before you even start interacting with it.
- **Conversation history theft**[2](#footnote-2) - servers can steal your full conversation history without you noticing
- **ANSI terminal code attacks**[3](#footnote-3) - escape sequences hide malicious instructions. Your terminal can show false or misleading information due to hidden instructions.
- **Insecure credential storage**[4](#footnote-4) - API keys sitting in plaintext with world-readable permissions. This leaves sensitive data exposed.

* * *

The OWASP Top 10 for Large Language Model Applications (2025)[5](#footnote-5) puts prompt injection at #1. Meanwhile, most security teams are still treating AI like it's another web app.

Your monitoring tools won't blink, API calls, auth, and response times all look normal during a breach. The breach often goes undetected until it's too late.

Trail of Bits found in their cloud infrastructure research[6](#footnote-6) that AI systems can produce insecure cloud setup code, leading to unexpectedly high costs.

Their report pointed out:

- AI tools sometimes hard-code credentials, creating security risks
- "Random" passwords that are actually predictable LLM outputs
- Infrastructure code that spins up expensive resources with zero limits

Here's how attackers weaponize this:

1. Find AI tools connected to expensive cloud services
2. Craft natural language requests that maximize resource consumption
3. Exploit AI's tendency to blindly follow requests to bypass traditional security controls
4. Costs can skyrocket due to infrastructure overuse, even though logs might look normal

Based on OWASP recommendations and documented security research, here's what works in production:

### 1. Never Give Production Creds to AI[​](#1-never-give-production-creds-to-ai "Direct link to 1. Never Give Production Creds to AI")

Don't be an idiot, never hand AI your prod keys; use a sandboxed account with zero power.

If your AI needs full admin rights, it's time to rethink your setup.

### 2. Resource Limits and Constraints[​](#2-resource-limits-and-constraints "Direct link to 2. Resource Limits and Constraints")

Traditional rate limiting is useless against AI. You need cost-based limits and hard resource constraints:

### 3. Semantic Attack Detection[​](#3-semantic-attack-detection "Direct link to 3. Semantic Attack Detection")

Traditional logging misses semantic attacks completely. Keep an eye out for signs of prompt injection attempts:

### 4. Semantic Input Validation[​](#4-semantic-input-validation "Direct link to 4. Semantic Input Validation")

The NIST AI Risk Management Framework[7](#footnote-7) recommends semantic analysis for AI inputs. Basic pattern matching catches most documented attack vectors:

### 5. Cost-Aware Rate Limiting[​](#5-cost-aware-rate-limiting "Direct link to 5. Cost-Aware Rate Limiting")

Traditional rate limiting counts requests. AI systems need cost-aware limiting:

OWASP and cloud giants agree, these metrics catch AI attacks:

**Resource consumption weirdness:**

- Compute usage spikes way above baseline
- Unusual data access patterns
- Cross-service API call increases
- Geographic request anomalies

**Behavioral red flags:**

- Requests containing system keywords
- Permission escalation attempts
- Tools accessing new data sources
- Cost per request increases

The latest MCP specification now mandates proper OAuth implementation:

This addresses some authentication issues but doesn't solve tool description injection.

Security pros at OWASP and NIST keep hammering this: no prod creds in AI, period.

**OWASP Top 10 for LLMs (2025):**[8](#footnote-8)

1. **LLM01: Prompt Injection** - #1 threat
2. **LLM02: Insecure Output Handling**
3. **LLM03: Training Data Poisoning**
4. **LLM04: Model Denial of Service**

**NIST AI Risk Management Framework:**[7](#footnote-7)

- Treat AI systems as high-risk components
- Implement continuous monitoring
- Use defense-in-depth strategies
- Plan for novel attack vectors

We're building systems that run commands based on natural language and connect to live infrastructure. The risks are well-known, the methods of attack are out there, and researchers are constantly finding new exploits.

Fix this now, or enjoy the breach headlines later.

* * *

[]()**1.** Trail of Bits. "Jumping the Line: How MCP servers can attack you before you ever use them." April 21, 2025. [https://blog.trailofbits.com/2025/04/21/jumping-the-line-how-mcp-servers-can-attack-you-before-you-ever-use-them/](https://blog.trailofbits.com/2025/04/21/jumping-the-line-how-mcp-servers-can-attack-you-before-you-ever-use-them/) [↩](#ref-1)

[]()**2.** Trail of Bits. "How MCP servers can steal your conversation history." April 23, 2025. [https://blog.trailofbits.com/2025/04/23/how-mcp-servers-can-steal-your-conversation-history/](https://blog.trailofbits.com/2025/04/23/how-mcp-servers-can-steal-your-conversation-history/) [↩](#ref-2)

[]()**3.** Trail of Bits. "Deceiving users with ANSI terminal codes in MCP." April 29, 2025. [https://blog.trailofbits.com/2025/04/29/deceiving-users-with-ansi-terminal-codes-in-mcp/](https://blog.trailofbits.com/2025/04/29/deceiving-users-with-ansi-terminal-codes-in-mcp/) [↩](#ref-3)

[]()**4.** Trail of Bits. "Insecure credential storage plagues MCP." April 30, 2025. [https://blog.trailofbits.com/2025/04/30/insecure-credential-storage-plagues-mcp/](https://blog.trailofbits.com/2025/04/30/insecure-credential-storage-plagues-mcp/) [↩](#ref-4)

[]()**5.** OWASP. "Top 10 for Large Language Model Applications (2025)." [https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/](https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/) [↩](#ref-5)

[]()**6.** Trail of Bits. "Provisioning cloud infrastructure the wrong way, but faster." August 27, 2024. [https://blog.trailofbits.com/2024/08/27/provisioning-cloud-infrastructure-the-wrong-way-but-faster/](https://blog.trailofbits.com/2024/08/27/provisioning-cloud-infrastructure-the-wrong-way-but-faster/) [↩](#ref-6)

[]()**7.** NIST. "AI Risk Management Framework (AI RMF 1.0)." [https://www.nist.gov/itl/ai-risk-management-framework](https://www.nist.gov/itl/ai-risk-management-framework) [↩](#ref-7)

[]()**8.** OWASP. "Top 10 for LLMs (2025)." [https://owasp.org/www-project-top-10-for-large-language-model-applications/](https://owasp.org/www-project-top-10-for-large-language-model-applications/) [↩](#ref-8)

[]()**9.** CVE Database. "Prompt injection vulnerabilities." [https://cve.mitre.org/](https://cve.mitre.org/) [↩](#ref-9)

[]()**10.** Perez et al. "Prompt Injection Attacks Against GPT-3." arXiv:2108.04739. [https://arxiv.org/abs/2108.04739](https://arxiv.org/abs/2108.04739) [↩](#ref-10)

[]()**11.** Zou et al. "Universal and Transferable Adversarial Attacks on Aligned Language Models." arXiv:2307.15043. [https://arxiv.org/abs/2307.15043](https://arxiv.org/abs/2307.15043) [↩](#ref-11)

[]()**12.** Wei et al. "Jailbroken: How Does LLM Safety Training Fail?" arXiv:2307.02483. [https://arxiv.org/abs/2307.02483](https://arxiv.org/abs/2307.02483) [↩](#ref-12)

* * *

*← [Read Part 1: MCP Security Issues Nobody's Talking About](https://forgecode.dev/blog/prevent-attacks-on-mcp/)*

*Building MCP security tools or researching AI vulnerabilities? The documented threats are growing faster than the defenses. Let's change that.*

- [MCP Security Issues Nobody's Talking About - Part 1](https://forgecode.dev/blog/prevent-attacks-on-mcp/)
- [AI Agent Best Practices: Maximizing Productivity with ForgeCode](https://forgecode.dev/blog/ai-agent-best-practices/)
- [MCP New Specs: AI Agent Capabilities and Security Enhancements](https://forgecode.dev/blog/mcp-spec-updates/)