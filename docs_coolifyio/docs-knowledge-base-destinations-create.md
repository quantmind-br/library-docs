---
title: Creating Destinations
url: https://coolify.io/docs/knowledge-base/destinations/create.md
source: llms
fetched_at: 2026-02-17T14:40:24.425267-03:00
rendered_js: false
word_count: 423
summary: This document provides instructions for creating and configuring destinations in Coolify, covering manual creation methods, Docker network settings, and scanning existing server networks.
tags:
    - coolify
    - docker-networking
    - server-management
    - deployment-destinations
    - docker-swarm
    - container-orchestration
category: guide
---

# Creating Destinations

This guide shows you how to create new destinations in Coolify for deploying your applications and databases.

## Prerequisites

Before creating a destination, ensure you have:

* At least one server connected to Coolify
* Appropriate permissions to manage destinations
* Basic understanding of [Docker networks](https://docs.docker.com/engine/network/)

## Creating a New Destination

### Method 1: From Destinations Page

1. Navigate to **Destinations** in the main navigation
2. Click on **+ Add**
3. Fill in the destination details.

### Method 2: From Server Management

1. Go to **Servers** and select your server
2. Navigate to the **Destinations** tab
3. Click **+ Add**
4. Fill in the destination details.

## Configuration Options

### Destination Name

* Auto-generated based on server name and network ID
* Can be customized to be more descriptive

### Network Name

* Must be unique per server
* Auto-generated unique identifier (CUID2 format)
* Can be customized to be more descriptive
* Cannot be changed after creation
* Used as the actual Docker network name

### Server Selection

* Choose from available servers in your team
* Server must be online and accessible
* Can not be a [build server](/knowledge-base/server/build-server)
* Determines where the Docker network will be created

### Destination Type

The destination type is **automatically determined** based on your selected server's configuration:

#### Standalone Docker

* **Automatically selected** when the server is configured as a standalone Docker host
* Creates a standard Docker network
* Suitable for single-server deployments
* Supports bridge and custom networks

#### Docker Swarm

* **Automatically selected** when the server is configured as a Docker Swarm manager or worker
* Creates overlay networks for multi-node communication
* Server must have Docker Swarm mode enabled during server setup
* Advanced feature for clustered deployments

::: tip Server Configuration Determines Type
You cannot manually choose between Standalone Docker and Docker Swarm when creating a destination. The type is determined by how your server was configured when it was added to Coolify.
:::

## Automatic Network Creation

When you create a destination, Coolify automatically:

1. **Creates the Docker network** on the target server
2. **Connects the proxy** (Traefik/Caddy) to the network
3. **Configures network settings** for proper isolation
4. **Enables inter-container communication** within the network

## Network Scanning

You can also scan existing Docker networks on a server and add them as destinations:

1. Go to **Server** and select your server
2. Navigate to **Destinations**
3. Click **Scan for Destinations**
4. Select existing networks to import and Coolify will create destination entries for them

## Validation and Errors

Common errors when creating destinations:

* **Network already added to this server**: The network name conflicts with an existing one

## After Creation

Once created, your destination will:

* Appear in the destinations list
* Be available for deploying applications and databases
* Have network connectivity configured automatically
* Be ready to host your containerized resources