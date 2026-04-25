---
title: Domain Intel — Passive domain reconnaissance using Python stdlib | Hermes Agent
url: https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/research/research-domain-intel
source: crawler
fetched_at: 2026-04-24T17:01:31.229146039-03:00
rendered_js: false
word_count: 89
summary: This document describes a collection of tools built using only Python's standard library to perform passive domain reconnaissance without requiring external API keys or dependencies.
tags:
    - domain-reconnaissance
    - python-stdlib
    - subdomain-discovery
    - dns-lookup
    - whois
    - ssl-inspection
category: tutorial
---

Passive domain reconnaissance using Python stdlib. Subdomain discovery, SSL certificate inspection, WHOIS lookups, DNS records, domain availability checks, and bulk multi-domain analysis. No API keys required.

Passive domain reconnaissance using only Python stdlib. **Zero dependencies. Zero API keys. Works on Linux, macOS, and Windows.**

This skill includes `scripts/domain_intel.py` — a complete CLI tool for all domain intelligence operations.

```bash
# Subdomain discovery via Certificate Transparency logs
python3 SKILL_DIR/scripts/domain_intel.py subdomains example.com

# SSL certificate inspection (expiry, cipher, SANs, issuer)
python3 SKILL_DIR/scripts/domain_intel.py ssl example.com

# WHOIS lookup (registrar, dates, name servers — 100+ TLDs)
python3 SKILL_DIR/scripts/domain_intel.py whois example.com

# DNS records (A, AAAA, MX, NS, TXT, CNAME)
python3 SKILL_DIR/scripts/domain_intel.py dns example.com

# Domain availability check (passive: DNS + WHOIS + SSL signals)
python3 SKILL_DIR/scripts/domain_intel.py available coolstartup.io

# Bulk analysis — multiple domains, multiple checks in parallel
python3 SKILL_DIR/scripts/domain_intel.py bulk example.com github.com google.com
python3 SKILL_DIR/scripts/domain_intel.py bulk example.com github.com --checks ssl,dns
```

`SKILL_DIR` is the directory containing this SKILL.md file. All output is structured JSON.

Pure Python stdlib (`socket`, `ssl`, `urllib`, `json`, `concurrent.futures`). Works identically on Linux, macOS, and Windows with no dependencies.