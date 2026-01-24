---
title: Pause Docker Desktop
url: https://docs.docker.com/desktop/use-desktop/pause/
source: llms
fetched_at: 2026-01-24T14:19:26.237044607-03:00
rendered_js: false
word_count: 135
summary: Explains how to manually pause and resume Docker Desktop to reduce CPU and memory usage by suspending the underlying Linux VM and its running containers.
tags:
    - docker-desktop
    - resource-management
    - container-states
    - performance-optimization
    - linux-vm
category: guide
---

Pausing Docker Desktop temporarily suspends the Linux VM running Docker Engine. This saves the current state of all containers in memory and freezes all running processes, significantly reducing CPU and memory usage which is helpful for conserving battery on laptops.

To pause Docker Desktop, select the **Pause** icon to the left of the footer in the Docker Dashboard. To manually resume Docker Desktop, select the **Resume** option in the Docker menu, or run any Docker CLI command.

When you manually pause Docker Desktop, a paused status displays on the Docker menu and on the Docker Desktop Dashboard. You can still access the **Settings** and the **Troubleshoot** menu.

> Tip
> 
> The Resource Saver feature is enabled by default and provides better CPU and memory savings than the manual Pause feature. See [Resource Saver mode](https://docs.docker.com/desktop/use-desktop/resource-saver/) for more info.