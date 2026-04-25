---
title: NVM - Evolution API Documentation
url: https://doc.evolution-api.com/v2/en/install/nvm
source: sitemap
fetched_at: 2026-04-12T18:46:26.27875792-03:00
rendered_js: false
word_count: 243
summary: This document provides a comprehensive, step-by-step guide for setting up and deploying the Evolution API v2, covering prerequisites like database and Redis configuration through to process management with PM2.
tags:
    - setup-guide
    - installation
    - api-deployment
    - environment-variables
    - prerequisites
    - nvm
    - database
category: guide
---

## Prerequisites

Before starting the installation of Evolution API v2, ensure that you have already configured the necessary services, such as PostgreSQL and Redis. Follow the links below for more details:

- [Database Configuration](https://doc.evolution-api.com/v2/pt/requirements/database)
- [Redis Configuration](https://doc.evolution-api.com/v2/pt/requirements/redis)

## NVM Installation

Evolution API can be easily installed using Node Version Manager (NVM). Follow these steps to set up your environment and start the Evolution API on your server.

### Install NVM

First, download and install Node.js with the following commands:

```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
```

Now, load the environment and install Node.js:

```
# Load NVM into the current environment
source ~/.bashrc

# Install and use the required Node.js version
nvm install v20.10.0 && nvm use v20.10.0
```

Confirm that NVM was successfully installed:

## Cloning the Repository and Installing Dependencies

Clone the official Evolution API v2 repository from the correct branch:

```
git clone -b v2.0.0 https://github.com/EvolutionAPI/evolution-api.git
```

Navigate to the project directory and install the dependencies:

```
cd evolution-api
npm install
```

## Environment Variables Configuration

Now let’s configure the environment variables. First, copy the `.env.example` file to `.env`:

Edit the `.env` file with your specific settings:

Replace the default values with your configurations, such as database connection strings, API keys, server ports, etc.

## Database Generation and Deployment

After setting up the environment, you will need to generate the Prisma client files and deploy the migrations to the database. Use the following commands, depending on the database you are using (PostgreSQL or MySQL):

1. Generate the Prisma client files:
2. Deploy the migrations:

## Starting the Evolution API

After configuration, you can start the Evolution API with the following command:

```
npm run build
npm run start:prod
```

## PM2 Installation and Configuration

Use PM2 to manage the API process:

```
npm install pm2 -g
pm2 start 'npm run start:prod' --name ApiEvolution
pm2 startup
pm2 save --force
```

To verify that the API is running, visit [http://localhost:8080](http://localhost:8080). You should see the following response:

```
{
  "status": 200,
  "message": "Welcome to the Evolution API, it is working!",
  "version": "2.0.10",
  "clientName": "evolution01",
  "manager": "https://evo2.site.com/manager",
  "documentation": "https://doc.evolution-api.com"
}
```