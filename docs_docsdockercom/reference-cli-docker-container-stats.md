---
title: docker container stats
url: https://docs.docker.com/reference/cli/docker/container/stats/
source: llms
fetched_at: 2026-01-24T14:35:21.379556638-03:00
rendered_js: false
word_count: 636
summary: This document provides detailed information on the docker stats command, explaining how to monitor live resource usage statistics for containers across different operating systems.
tags:
    - docker-cli
    - container-monitoring
    - resource-usage
    - performance-metrics
    - docker-stats
    - system-administration
category: reference
---

DescriptionDisplay a live stream of container(s) resource usage statisticsUsage`docker container stats [OPTIONS] [CONTAINER...]`Aliases

An alias is a short or memorable alternative for a longer command.

`docker stats`

The `docker stats` command returns a live data stream for running containers. To limit data to one or more specific containers, specify a list of container names or ids separated by a space. You can specify a stopped container but stopped containers do not return any data.

If you need more detailed information about a container's resource usage, use the `/containers/(id)/stats` API endpoint.

> On Linux, the Docker CLI reports memory usage by subtracting cache usage from the total memory usage. The API does not perform such a calculation but rather provides the total memory usage and the amount from the cache so that clients can use the data as needed. The cache usage is defined as the value of `total_inactive_file` field in the `memory.stat` file on cgroup v1 hosts.
> 
> On Docker 19.03 and older, the cache usage was defined as the value of `cache` field. On cgroup v2 hosts, the cache usage is defined as the value of `inactive_file` field.

> The `PIDS` column contains the number of processes and kernel threads created by that container. Threads is the term used by Linux kernel. Other equivalent terms are "lightweight process" or "kernel task", etc. A large number in the `PIDS` column combined with a small number of processes (as reported by `ps` or `top`) may indicate that something in the container is creating many threads.

OptionDefaultDescription`-a, --all`Show all containers (default shows just running)[`--format`](#format)Format output using a custom template:  
'table': Print output in table format with column headers (default)  
'table TEMPLATE': Print output in table format using the given Go template  
'json': Print in JSON format  
'TEMPLATE': Print output using the given Go template.  
Refer to [https://docs.docker.com/go/formatting/](https://docs.docker.com/go/formatting/) for more information about formatting output with templates`--no-stream`Disable streaming stats and only pull the first result`--no-trunc`Do not truncate output

Running `docker stats` on all running containers against a Linux daemon.

If you don't [specify a format string using `--format`](#format), the following columns are shown.

Column nameDescription`CONTAINER ID` and `Name`the ID and name of the container`CPU %` and `MEM %`the percentage of the host's CPU and memory the container is using`MEM USAGE / LIMIT`the total memory the container is using, and the total amount of memory it is allowed to use`NET I/O`The amount of data the container has received and sent over its network interface`BLOCK I/O`The amount of data the container has written to and read from block devices on the host`PIDs`the number of processes or threads the container has created

Running `docker stats` on multiple containers by name and id against a Linux daemon.

Running `docker stats` on container with name `nginx` and getting output in `json` format.

Running `docker stats` with customized format on all (running and stopped) containers.

`humble_visvesvaraya` and `big_heisenberg` are stopped containers in the above example.

Running `docker stats` on all running containers against a Windows daemon.

Running `docker stats` on multiple containers by name and id against a Windows daemon.

### [Format the output (--format)](#format)

The formatting option (`--format`) pretty prints container output using a Go template.

Valid placeholders for the Go template are listed below:

PlaceholderDescription`.Container`Container name or ID (user input)`.Name`Container name`.ID`Container ID`.CPUPerc`CPU percentage`.MemUsage`Memory usage`.NetIO`Network IO`.BlockIO`Block IO`.MemPerc`Memory percentage (Not available on Windows)`.PIDs`Number of PIDs (Not available on Windows)

When using the `--format` option, the `stats` command either outputs the data exactly as the template declares or, when using the `table` directive, includes column headers as well.

The following example uses a template without headers and outputs the `Container` and `CPUPerc` entries separated by a colon (`:`) for all images:

To list all containers statistics with their name, CPU percentage and memory usage in a table format you can use:

The default format is as follows:

On Linux:

```
"table {{.ID}}\t{{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.MemPerc}}\t{{.NetIO}}\t{{.BlockIO}}\t{{.PIDs}}"
```

On Windows:

```
"table {{.ID}}\t{{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.NetIO}}\t{{.BlockIO}}"
```