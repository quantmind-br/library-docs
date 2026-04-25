---
title: Banco de Dados - Evolution API Documentation
url: https://doc.evolution-api.com/v2/pt/requirements/database
source: sitemap
fetched_at: 2026-04-12T18:45:34.992790543-03:00
rendered_js: false
word_count: 323
summary: This document provides comprehensive instructions on setting up the database for the Evolution API v2, detailing how to configure connections using either PostgreSQL or MySQL. It offers setup guides for both Docker and local installations, along with necessary environment variable configurations.
tags:
    - database-setup
    - postgresql
    - mysql
    - docker-compose
    - environment-variables
category: guide
---

O banco de dados é uma parte fundamental da Evolution API v2, responsável por armazenar todas as informações críticas da aplicação. A API suporta tanto PostgreSQL quanto MySQL, utilizando o Prisma como ORM (Object-Relational Mapping) para facilitar a interação com esses bancos de dados.

## Escolha do Banco de Dados

A Evolution API v2 permite a flexibilidade de escolher entre PostgreSQL e MySQL como provedor de banco de dados. A escolha pode ser configurada através da variável de ambiente `DATABASE_PROVIDER` e as conexões são gerenciadas pelo Prisma.

## Instalação e Configuração

### Utilizando Docker

A maneira mais fácil e rápida de configurar um banco de dados para a Evolution API v2 é através do Docker. Abaixo estão as instruções para configurar tanto o PostgreSQL quanto o MySQL usando Docker Compose.

#### PostgreSQL

Para configurar o PostgreSQL via Docker, siga os passos abaixo:

1. Baixe o arquivo `docker-compose.yaml` para o PostgreSQL disponível [aqui](https://github.com/EvolutionAPI/evolution-api/blob/main/Docker/postgres/docker-compose.yaml).
2. Navegue até o diretório onde o arquivo foi baixado e execute o comando:

<!--THE END-->

3. A instância do PostgreSQL estará disponível no endereço `localhost` na porta `5432`.

#### MySQL

Para configurar o MySQL via Docker, siga os passos abaixo:

1. Baixe o arquivo `docker-compose.yaml` para o MySQL disponível [aqui](https://github.com/EvolutionAPI/evolution-api/blob/v2.0.0/Docker/mysql/docker-compose.yaml).
2. Navegue até o diretório onde o arquivo foi baixado e execute o comando:

<!--THE END-->

3. A instância do MySQL estará disponível no endereço `localhost` na porta `3306`.

### Configuração das Variáveis de Ambiente

Após configurar o banco de dados, defina as seguintes variáveis de ambiente no seu arquivo `.env`:

```
# Habilitar o uso do banco de dados
DATABASE_ENABLED=true

# Escolher o provedor do banco de dados: postgresql ou mysql
DATABASE_PROVIDER=postgresql

# URI de conexão com o banco de dados
DATABASE_CONNECTION_URI='postgresql://user:pass@localhost:5432/evolution?schema=public'

# Nome do cliente para a conexão do banco de dados
DATABASE_CONNECTION_CLIENT_NAME=evolution_exchange

# Escolha os dados que você deseja salvar no banco de dados da aplicação
DATABASE_SAVE_DATA_INSTANCE=true
DATABASE_SAVE_DATA_NEW_MESSAGE=true
DATABASE_SAVE_MESSAGE_UPDATE=true
DATABASE_SAVE_DATA_CONTACTS=true
DATABASE_SAVE_DATA_CHATS=true
DATABASE_SAVE_DATA_LABELS=true
DATABASE_SAVE_DATA_HISTORIC=true
```

### Instalação Local

Caso prefira configurar o banco de dados localmente sem utilizar Docker, siga as instruções abaixo:

#### PostgreSQL

1. Instale o PostgreSQL na sua máquina. Em sistemas baseados em Ubuntu, por exemplo, você pode usar:

```
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
```

2. Inicie o serviço do PostgreSQL:

```
sudo service postgresql start
```

3. Crie um banco de dados para a Evolution API v2:

```
sudo -u postgres createdb evolution
```

#### MySQL

1. Instale o MySQL na sua máquina. Em sistemas baseados em Ubuntu, você pode usar:

```
sudo apt-get update
sudo apt-get install mysql-server
```

2. Inicie o serviço do MySQL:

<!--THE END-->

3. Crie um banco de dados para a Evolution API v2:

```
mysql -u root -p -e "CREATE DATABASE evolution;"
```