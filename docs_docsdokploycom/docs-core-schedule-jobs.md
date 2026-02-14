---
title: Schedule Jobs | Dokploy
url: https://docs.dokploy.com/docs/core/schedule-jobs
source: crawler
fetched_at: 2026-02-14T14:18:09.755856-03:00
rendered_js: true
word_count: 452
summary: This document explains how to configure and manage automated tasks in Dokploy using the Schedule Jobs feature, covering various job types including application, compose, and server-level scripts.
tags:
    - dokploy
    - scheduled-jobs
    - automation
    - cron-expressions
    - docker-exec
    - server-management
category: guide
---

Learn how to automate tasks using Dokploy's Schedule Jobs feature

Schedule Jobs in Dokploy allows you to create and manage automated tasks that run on a specified schedule using cron expressions. Each job execution creates a log entry where you can monitor the output and execution status.

Dokploy supports four types of scheduled jobs:

1. **Application Jobs**: Run commands inside specific application containers
2. **Compose Jobs**: Execute commands in Docker Compose services
3. **Server Jobs**: Run scripts on remote servers (executed on the host)
4. **Dokploy Server Jobs**: Execute tasks at the container level within the Dokploy container. These jobs can interact with commands inside the Dokploy container (e.g., `docker ps`, `docker image prune`), but they are not executed directly on the host system

For application and compose jobs, you can run single commands that will be executed inside the target container. Dokploy internally uses Docker exec to run these commands:

```
docker exec -it <container_id> <command>
```

### [Example](#example)

Assuming you with a nginx container and you want to check the nginx version in a container:

1. Create a new schedule job
2. Set the command to: `nginx -v`
3. Configure your desired schedule using cron syntax
4. Save and monitor the execution logs

The target container must be running for the job to execute successfully.

For docker compose jobs, is required to not change the COMPOSE\_PROJECT\_NAME environment variable, since this is used to identify the project.

### [Server Jobs](#server-jobs)

For remote servers, you can write bash scripts to perform various tasks. These scripts are executed directly on the host system and can use any command or tool available on the target server.

### [Dokploy Server Jobs](#dokploy-server-jobs)

Dokploy Server Jobs are executed at the container level within the Dokploy container. This means:

- Commands run inside the Dokploy container environment
- You can interact with Docker commands (e.g., `docker ps`, `docker image prune`, `docker system prune`)
- Scripts have access to the Docker socket and can manage containers and images
- Jobs do not execute directly on the host system, but within the containerized Dokploy environment

**Example**: You can create a scheduled job to clean up unused Docker images:

```
#!/bin/bash
docker image prune -af
```

This command will run inside the Dokploy container and can interact with Docker to clean up images.

Make sure any required dependencies are installed on the target server before using them in your scripts.

### [Example 1: Automatic Docker Cleanup](#example-1-automatic-docker-cleanup)

This script cleans up unused Docker containers. You could schedule it to run every 15 minutes using the cron expression `*/15 * * * *`:

```
#!/bin/bash
docker system prune --force
```

### [Example 2: Custom Database Backup](#example-2-custom-database-backup)

You can create scripts to backup databases that aren't natively supported by Dokploy. Here's an example structure for a custom backup script:

```
#!/bin/bash
# Backup script for custom database
backup_date=$(date +%Y%m%d_%H%M%S)
backup_file="database_${backup_date}.backup"

# search the container name
container_name=$(docker ps --filter "name=clickhouse" --format "{{.Names}}")

# Add your backup commands here
docker exec -it $container_name clickhouse-client --query "BACKUP DATABASE mydb TO '/backups/$backup_file'"

# Upload to S3 (if needed)
# aws s3 cp /backups/$backup_file s3://your-bucket/backups/
```

1. Always test your commands or scripts manually before scheduling them
2. Use appropriate error handling in your scripts
3. Consider the impact of scheduled jobs on system resources