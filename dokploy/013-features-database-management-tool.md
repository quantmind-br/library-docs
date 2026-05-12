---
title: Dokploy - Deploy your applications with ease
url: https://dokploy.com/features/database-management-tool
source: sitemap
fetched_at: 2026-04-26T08:39:47.375127362-03:00
rendered_js: false
word_count: 779
summary: This document outlines the database management capabilities of Dokploy, covering support for multiple database engines, real-time monitoring, automated backups, and granular infrastructure control.
tags:
    - database-management
    - containerization
    - docker
    - backups
    - monitoring
    - infrastructure
    - devops
category: guide
---

## Database Management, Done Right

Create, manage, and back up databases easily with Dokploy's database tool, and customize the process to suit your project needs. Deploy in minutes, maintain full control over your stored data, and recover fast when it matters.

## Deploy the database you already use

Dokploy's database management tool supports five widely used database systems out of the box, so you're not locked into a single technology. You pick what fits your stack and your data management needs.

### PostgreSQL

A robust, SQL-compliant relational database with high reliability—a solid choice for production workloads that handle structured and transactional data and demand consistency and standards compliance.

### MySQL

A widely used open source relational database known for its high performance and flexibility, with broad ecosystem support across frameworks and hosting environments.

### MariaDB

A free and open source fork of MySQL with additional features and improved performance, maintained by an active community and great for MySQL applications.

### MongoDB

A NoSQL database built for high scalability and flexibility, well-suited to applications with unstructured or semi-structured data and evolving data sources.

### Redis

An in-memory key-value store often used as a database, cache, and message broker—fast by design and easy to integrate for high-performance operations.

## Watch your databases in real time

Dokploy surfaces live monitoring graphs for memory, CPU, disk, and network directly in the dashboard. The data updates as you view it, so you can see exactly what your database is doing and catch problems before they become incidents.

## Protect, recover, and connect with confidence

Automated backups, transparent logs, straightforward restores, and flexible connection options. Everything you need to manage a database reliably, all in one place.

### Backups

Schedule automated backups for any database and route them directly to an S3 bucket of your choice. Set a cron schedule, define a prefix, and test your configuration before relying on it so you know your stored data is secure before you ever need to recover it.

### Logs

View real-time logs from any running database directly in your Dokploy dashboard. Spot errors as they happen, trace unexpected behavior back to its source, and keep a clear record of what’s happening inside your containers.

### Restore

Restore any database from a backup stored in your S3 bucket in a few clicks—critical for disaster recovery when you need to act fast. Select the source bucket, search for your backup file with autocomplete, and kick off the restoration process—Dokploy handles the correct restore commands automatically.

### Connections

Connect to databases internally within your network or expose them externally via a generated connection URL. Use internal credentials for applications running in the same environment, and configure external access only when needed, with security controls in place to protect sensitive data.

## Advanced options, your way

Dokploy goes beyond the basics, giving you granular control over how each database runs, from the image it uses to the resources it consumes and everything in between.

### Custom Docker Image

Swap out the default Docker image for any database with one that fits your exact requirements and database development workflow.

### Run Command

Execute custom commands directly inside the container for advanced management, complex queries, or troubleshooting.

### Volumes

Configure persistent storage volumes to make sure your data survives deployments and restarts.

### Resources

Adjust CPU and memory allocation per database to optimize database performance and keep resource usage predictable as your infrastructure grows.

### Keyboard Shortcuts

Navigate between database tabs instantly with built-in keyboard shortcuts, keeping your workflow fast.

### Danger Zone

When you need a clean slate, the Danger Zone lets you wipe all data, tables, and configuration in one controlled action.

## Your data stays secure

Your database data is stored on your own server. Dokploy creates Docker containers on your infrastructure, so you have full control over your data—no third parties, no external dependencies.

### Your server, your data

Dokploy creates Docker containers on your own server. Your database data never leaves your infrastructure—you have full ownership and control over where it lives.

### Isolated containers

Each database runs in its own Docker container, isolated from other services. You control networking, access, and exposure—nothing is shared unless you configure it.

### No third-party access

Dokploy doesn’t store or proxy your data. Everything runs on your machine, so there’s no middleman between your applications and your databases.

## Start managing databases smarter

Dokploy gives you everything you need to deploy, monitor, and protect your databases—without the complexity. Create your account and have your first database running in minutes with our database management tool.

## Database management tool FAQs

## Unlock Your Deployment Potential with Dokploy Cloud

Say goodbye to infrastructure hassles—Dokploy Cloud handles it all. Effortlessly deploy, manage Docker containers, and secure your traffic with Traefik. Focus on building, we'll handle the rest.

[Create an account](https://app.dokploy.com/register)