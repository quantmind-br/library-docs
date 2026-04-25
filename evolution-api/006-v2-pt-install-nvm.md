---
title: NVM - Evolution API Documentation
url: https://doc.evolution-api.com/v2/pt/install/nvm
source: sitemap
fetched_at: 2026-04-12T18:45:52.412697694-03:00
rendered_js: false
word_count: 278
summary: This document provides a comprehensive, step-by-step guide on setting up and deploying the Evolution API v2. It covers prerequisites like database setup, installing Node versions using NVM, cloning the repository, configuring environment variables, running migrations, and finally starting and managing the service with PM2.
tags:
    - installation-guide
    - api-setup
    - node-js
    - deployment
    - prerequisites
    - environment-variables
category: tutorial
---

## Pré-requisitos

Antes de iniciar a instalação da Evolution API v2, certifique-se de que você já configurou os serviços necessários, como PostgreSQL e Redis. Siga os links abaixo para mais detalhes:

- [Configuração do Banco de Dados](https://doc.evolution-api.com/v2/pt/requirements/database)
- [Configuração do Redis](https://doc.evolution-api.com/v2/pt/requirements/redis)

## Instalação do NVM

A Evolution API pode ser facilmente instalada usando o Node Version Manager (NVM). Siga estas etapas para configurar seu ambiente e iniciar a Evolution API em seu servidor.

### Instalar NVM

Primeiro, baixe e instale o Node.js com os seguintes comandos:

```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
```

Agora, carregue o ambiente e instale o Node.js:

```
# Carregar o NVM no ambiente atual
source ~/.bashrc

# Instalar e usar a versão necessária do Node.js
nvm install v20.10.0 && nvm use v20.10.0
```

Confirme que o NVM foi instalado com sucesso:

## Clonando o Repositório e Instalando Dependências

Clone o repositório oficial da Evolution API v2 a partir da branch correta:

```
git clone -b v2.0.0 https://github.com/EvolutionAPI/evolution-api.git
```

Acesse o diretório do projeto e instale as dependências:

```
cd evolution-api
npm install
```

## Configuração de Variáveis de Ambiente

Agora vamos configurar as variáveis de ambiente. Primeiro, copie o arquivo `.env.example` para `.env`:

Edite o arquivo `.env` com suas configurações específicas:

Substitua os valores padrão pelas suas configurações, como strings de conexão de banco de dados, chaves de API, portas do servidor, etc.

## Geração e Deploy do Banco de Dados

Após configurar o ambiente, você precisará realizar a geração dos arquivos do cliente Prisma e o deploy das migrations no banco de dados. Utilize os comandos abaixo, dependendo do banco de dados que você está utilizando (PostgreSQL ou MySQL):

1. Gerar os arquivos do cliente Prisma:
2. Realizar o deploy das migrations:

## Inicializando a Evolution API

Após a configuração, você pode iniciar a Evolution API com o seguinte comando:

```
npm run build
npm run start:prod
```

## Instalação e Configuração do PM2

Use o PM2 para gerenciar o processo da API:

```
npm install pm2 -g
pm2 start 'npm run start:prod' --name ApiEvolution
pm2 startup
pm2 save --force
```

Para verificar se a API está em execução, acesse [http://localhost:8080](http://localhost:8080). Você deve ver a seguinte resposta:

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