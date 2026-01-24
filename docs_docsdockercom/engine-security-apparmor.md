---
title: AppArmor security profiles for Docker
url: https://docs.docker.com/engine/security/apparmor/
source: llms
fetched_at: 2026-01-24T14:25:18.21319349-03:00
rendered_js: false
word_count: 0
summary: This document defines an AppArmor security profile designed to harden a Docker-based Nginx container by restricting its access to files, network protocols, and system capabilities.
tags:
    - apparmor
    - docker
    - nginx
    - security-profile
    - container-hardening
    - access-control
category: configuration
---

```
#include <tunables/global>profile docker-nginx flags=(attach_disconnected,mediate_deleted) {
  #include <abstractions/base>  network inet tcp,
  network inet udp,
  network inet icmp,
  deny network raw,
  deny network packet,
  file,
  umount,
  deny /bin/** wl,
  deny /boot/** wl,
  deny /dev/** wl,
  deny /etc/** wl,
  deny /home/** wl,
  deny /lib/** wl,
  deny /lib64/** wl,
  deny /media/** wl,
  deny /mnt/** wl,
  deny /opt/** wl,
  deny /proc/** wl,
  deny /root/** wl,
  deny /sbin/** wl,
  deny /srv/** wl,
  deny /tmp/** wl,
  deny /sys/** wl,
  deny /usr/** wl,
  audit /** w,
  /var/run/nginx.pid w,
  /usr/sbin/nginx ix,
  deny /bin/dash mrwklx,
  deny /bin/sh mrwklx,
  deny /usr/bin/top mrwklx,
  capability chown,
  capability dac_override,
  capability setuid,
  capability setgid,
  capability net_bind_service,
  deny @{PROC}/* w,   # deny write for all files directly in /proc (not in a subdir)
  # deny write to files not in /proc/<number>/** or /proc/sys/**
  deny @{PROC}/{[^1-9],[^1-9][^0-9],[^1-9s][^0-9y][^0-9s],[^1-9][^0-9][^0-9][^0-9]*}/** w,
  deny @{PROC}/sys/[^k]** w,  # deny /proc/sys except /proc/sys/k* (effectively /proc/sys/kernel)
  deny @{PROC}/sys/kernel/{?,??,[^s][^h][^m]**} w,  # deny everything except shm* in /proc/sys/kernel/
  deny @{PROC}/sysrq-trigger rwklx,
  deny @{PROC}/mem rwklx,
  deny @{PROC}/kmem rwklx,
  deny @{PROC}/kcore rwklx,
  deny mount,
  deny /sys/[^f]*/** wklx,
  deny /sys/f[^s]*/** wklx,
  deny /sys/fs/[^c]*/** wklx,
  deny /sys/fs/c[^g]*/** wklx,
  deny /sys/fs/cg[^r]*/** wklx,
  deny /sys/firmware/** rwklx,
  deny /sys/kernel/security/** rwklx,
}
```