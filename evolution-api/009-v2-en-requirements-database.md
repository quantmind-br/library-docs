---
title: Database - Evolution API Documentation
url: https://doc.evolution-api.com/v2/en/requirements/database
source: sitemap
fetched_at: 2026-04-12T18:46:11.873179593-03:00
rendered_js: false
word_count: 281
summary: This document provides comprehensive instructions on setting up and configuring the database backend for the Evolution API v2, covering options for using PostgreSQL or MySQL via Docker Compose or local installations.
tags:
    - database-setup
    - postgresql
    - mysql
    - environment-variables
    - prisma-orm
    - api-v2
category: guide
---

The database is a fundamental part of the Evolution API v2, responsible for storing all the application’s critical information. The API supports both PostgreSQL and MySQL, using Prisma as the ORM (Object-Relational Mapping) to facilitate interaction with these databases.

## Database Choice

Evolution API v2 offers the flexibility to choose between PostgreSQL and MySQL as the database provider. The choice can be configured through the `DATABASE_PROVIDER` environment variable, and connections are managed by Prisma.

## Installation and Configuration

### Using Docker

The easiest and fastest way to set up a database for Evolution API v2 is through Docker. Below are the instructions to configure both PostgreSQL and MySQL using Docker Compose.

#### PostgreSQL

To set up PostgreSQL via Docker, follow these steps:

1. Download the `docker-compose.yaml` file for PostgreSQL available [here](https://github.com/EvolutionAPI/evolution-api/blob/v2.0.0/Docker/postgres/docker-compose.yaml).
2. Navigate to the directory where the file was downloaded and run the command:

<!--THE END-->

3. The PostgreSQL instance will be available at `localhost` on port `5432`.

#### MySQL

To set up MySQL via Docker, follow these steps:

1. Download the `docker-compose.yaml` file for MySQL available [here](https://github.com/EvolutionAPI/evolution-api/blob/v2.0.0/Docker/mysql/docker-compose.yaml).
2. Navigate to the directory where the file was downloaded and run the command:

<!--THE END-->

3. The MySQL instance will be available at `localhost` on port `3306`.

### Environment Variables Configuration

After setting up the database, define the following environment variables in your `.env` file:

```
# Enable the use of the database
DATABASE_ENABLED=true

# Choose the database provider: postgresql or mysql
DATABASE_PROVIDER=postgresql

# Database connection URI
DATABASE_CONNECTION_URI='postgresql://user:pass@localhost:5432/evolution?schema=public'

# Client name for the database connection
DATABASE_CONNECTION_CLIENT_NAME=evolution_exchange

# Choose the data you want to save in the application database
DATABASE_SAVE_DATA_INSTANCE=true
DATABASE_SAVE_DATA_NEW_MESSAGE=true
DATABASE_SAVE_MESSAGE_UPDATE=true
DATABASE_SAVE_DATA_CONTACTS=true
DATABASE_SAVE_DATA_CHATS=true
DATABASE_SAVE_DATA_LABELS=true
DATABASE_SAVE_DATA_HISTORIC=true
```

### Local Installation

If you prefer to set up the database locally without using Docker, follow the instructions below:

#### PostgreSQL

1. Install PostgreSQL on your machine. On Ubuntu-based systems, for example, you can use:

```
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
```

2. Start the PostgreSQL service:

```
sudo service postgresql start
```

3. Create a database for Evolution API v2:

```
sudo -u postgres createdb evolution
```

#### MySQL

1. Install MySQL on your machine. On Ubuntu-based systems, you can use:

```
sudo apt-get update
sudo apt-get install mysql-server
```

2. Start the MySQL service:

<!--THE END-->

3. Create a database for Evolution API v2:

```
mysql -u root -p -e "CREATE DATABASE evolution;"
```