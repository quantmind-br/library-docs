---
title: Connection Unstable
url: https://coolify.io/docs/troubleshoot/server/connection-issues.md
source: llms
fetched_at: 2026-02-17T14:41:50.316247-03:00
rendered_js: false
word_count: 206
summary: This document provides troubleshooting steps and solutions for identifying and resolving unstable server connections in Coolify caused by firewall rate-limiting on port 22.
tags:
    - coolify
    - troubleshooting
    - firewall
    - ufw
    - iptables
    - port-22
    - server-connectivity
category: guide
---

# Connection Unstable

If you're experiencing unstable connections, most of the times (90% of the cases) a firewall issue, ufw, iptables or some configuration on your server or between your Coolify instance (or Coolify Cloud) and your server.

## Symptoms

* Server is sometimes reachable, sometimes not.
* You receive a lot of failed connection lost emails.

## Diagnosis

* Check your UFW rules with `ufw status numbered` and see if you have a `LIMIT` rule for port 22.
* Check your iptables rules with `iptables -L -v -n` and see if you have a `LIMIT` rule for port 22.
* Check your server logs (`/var/log/ufw.log`, `/var/log/iptables.log`, `/var/log/auth.log`, `/var/log/kern.log`) for any firewall related errors.

## Solution

* UFW

  * `ufw status numbered` - if you have port 22 open, but with a `LIMIT` rule, this is the problem.
  * `ufw delete <rule_number>` - delete the rule - you probably have IPV4 and IPV6 rules, so you need to delete both.
    * After you deleted the rule, you need to check the status with `ufw status numbered` and see that the rule is deleted and which rule number is next.
  * `ufw allow 22/tcp` - add the rule without a limit.

  OR

  * `ufw limit 22/tcp 100/minute` - add a higher limit.

In case of Coolify Cloud, you can enable connection from Coolify Cloud IP addresses by adding the following to the UFW rules for each IP:

```sh
# For each IPv4 address
ufw allow from <ipv4> to any port 22

# For each IPv6 subnet
ufw allow from <ipv6> to any port 22
```

> You can find the current Coolify Cloud IP addresses at <https://coolify.io/ipv4.txt> and <https://coolify.io/ipv6.txt>