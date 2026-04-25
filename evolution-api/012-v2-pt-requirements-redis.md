---
title: Redis - Evolution API Documentation
url: https://doc.evolution-api.com/v2/pt/requirements/redis
source: sitemap
fetched_at: 2026-04-12T18:45:35.05142962-03:00
rendered_js: false
word_count: 243
summary: This document provides comprehensive instructions on how to install and configure Redis for use as a caching system with the Evolution API v2, detailing methods using Docker Compose, setting environment variables, and manual local installation.
tags:
    - redis-caching
    - evolution-api
    - docker-setup
    - environment-variables
    - performance-optimization
category: guide
---

O Redis é utilizado pela Evolution API v2 como um sistema de cache para otimizar o desempenho e a velocidade da aplicação. Ele pode ser configurado para armazenar informações temporárias e melhorar a eficiência das operações.

## Instalação e Configuração

### Utilizando Docker

A maneira mais fácil e rápida de configurar o Redis para a Evolution API v2 é através do Docker. Abaixo estão as instruções para configurar o Redis usando Docker Compose.

#### Redis

Para configurar o Redis via Docker, siga os passos abaixo:

1. Baixe o arquivo `docker-compose.yaml` para o Redis disponível [aqui](https://github.com/EvolutionAPI/evolution-api/blob/v2.0.0/Docker/redis/docker-compose.yaml).
2. Navegue até o diretório onde o arquivo foi baixado e execute o comando:

<!--THE END-->

3. A instância do Redis estará disponível no endereço `localhost` na porta `6379`.

### Configuração das Variáveis de Ambiente

Após configurar o Redis, defina as seguintes variáveis de ambiente no seu arquivo `.env`:

```
# Habilitar o cache Redis
CACHE_REDIS_ENABLED=true

# URI de conexão com o Redis
CACHE_REDIS_URI=redis://localhost:6379/6

# Prefixo para diferenciar os dados de diferentes instalações que utilizam o mesmo Redis
CACHE_REDIS_PREFIX_KEY=evolution

# Habilitar para salvar as informações de conexão no Redis ao invés do banco de dados
CACHE_REDIS_SAVE_INSTANCES=false

# Habilitar o cache local
CACHE_LOCAL_ENABLED=false
```

### Instalação Local

Caso prefira configurar o Redis localmente sem utilizar Docker, siga as instruções abaixo:

#### Redis

1. Instale o Redis na sua máquina. Em sistemas baseados em Ubuntu, por exemplo, você pode usar:

```
sudo apt-get update
sudo apt-get install redis-server
```

2. Inicie o serviço do Redis:

```
sudo service redis-server start
```

3. Verifique se o Redis está rodando corretamente com o comando:

Se tudo estiver funcionando corretamente, você verá a resposta `PONG`.

### Configuração do Cache na Evolution API v2

Após a instalação e configuração do Redis, a próxima etapa é configurar o cache na Evolution API v2 utilizando as variáveis de ambiente. Isso permitirá que a API utilize o Redis para cachear dados importantes e melhorar a performance geral da aplicação.