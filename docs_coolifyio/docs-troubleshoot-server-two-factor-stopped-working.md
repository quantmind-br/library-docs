---
title: 2FA Stopped Working
url: https://coolify.io/docs/troubleshoot/server/two-factor-stopped-working.md
source: llms
fetched_at: 2026-02-17T14:41:53.750089-03:00
rendered_js: false
word_count: 105
summary: This document provides diagnostic steps and solutions for resolving two-factor authentication failures caused by server time synchronization issues.
tags:
    - 2fa
    - time-synchronization
    - ntp
    - troubleshooting
    - linux-server
    - authentication
category: guide
---

# 2FA Stopped Working

It is usually a time synchronization issue.

## Diagnosis

* Check your server's time with `date` - if the time is off, you need to synchronize it.
* Check your NTP configuration with `cat /etc/ntp.conf`.
* Check with `systemctl status systemd-timesyncd.service` if your operating system is using systemd to synchronize time.
* Check your firewall (`ufw`, `iptables`) rules to see if you have any rules that block time synchronization ports (`123/udp, 123/tcp`).

## Solution

* If your operating system is using systemd, you can synchronize the time with `sudo timedatectl set-ntp true`.
* If your operating system is not using systemd, you can synchronize the time with `sudo ntpdate ntp.ubuntu.com`.