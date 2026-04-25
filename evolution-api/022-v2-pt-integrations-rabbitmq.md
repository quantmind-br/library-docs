---
title: RabbitMQ - Evolution API Documentation
url: https://doc.evolution-api.com/v2/pt/integrations/rabbitmq
source: sitemap
fetched_at: 2026-04-12T18:45:45.624812585-03:00
rendered_js: false
word_count: 373
summary: This document details how to configure the RabbitMQ integration with the Evolution API for managing and processing system events efficiently. It explains both centralized global configuration via environment variables and instance-specific configuration using an API endpoint.
tags:
    - rabbitmq
    - event-management
    - api-configuration
    - global-setup
    - instance-settings
    - message-queuing
category: guide
---

A Evolution API permite a integração com o **RabbitMQ** para gerenciar eventos e filas de mensagens, facilitando a comunicação e processamento de tarefas de forma eficiente e escalável. A seguir, você encontrará informações sobre como configurar o RabbitMQ tanto em modo global quanto em instâncias individuais.

## Configuração Global do RabbitMQ

Com a nova configuração global, é possível centralizar o processamento de eventos em filas unificadas, em vez de configurar filas separadas para cada instância. Isso simplifica a gestão de eventos, pois todos os eventos do sistema passam por filas específicas de acordo com o tipo de evento.

### Configuração de Variáveis de Ambiente

Aqui estão as variáveis de ambiente necessárias para habilitar e configurar o RabbitMQ em modo global:

```
RABBITMQ_ENABLED=true
RABBITMQ_URI=amqp://admin:admin@localhost:5672/default
RABBITMQ_EXCHANGE_NAME=evolution_exchange
RABBITMQ_GLOBAL_ENABLED=true
```

### Eventos Configuráveis

Com o modo global habilitado (`RABBITMQ_GLOBAL_ENABLED=true`), todos os eventos são enfileirados em filas específicas por tipo de evento, em vez de por instância. Aqui está a lista de eventos que você pode ativar globalmente:

```
RABBITMQ_EVENTS_APPLICATION_STARTUP=true
RABBITMQ_EVENTS_INSTANCE_CREATE=true
RABBITMQ_EVENTS_INSTANCE_DELETE=true
RABBITMQ_EVENTS_QRCODE_UPDATED=true
RABBITMQ_EVENTS_MESSAGES_SET=true
RABBITMQ_EVENTS_MESSAGES_UPSERT=true
RABBITMQ_EVENTS_MESSAGES_EDITED=true
RABBITMQ_EVENTS_MESSAGES_UPDATE=true
RABBITMQ_EVENTS_MESSAGES_DELETE=true
RABBITMQ_EVENTS_SEND_MESSAGE=true
RABBITMQ_EVENTS_CONTACTS_SET=true
RABBITMQ_EVENTS_CONTACTS_UPSERT=true
RABBITMQ_EVENTS_CONTACTS_UPDATE=true
RABBITMQ_EVENTS_PRESENCE_UPDATE=true
RABBITMQ_EVENTS_CHATS_SET=true
RABBITMQ_EVENTS_CHATS_UPSERT=true
RABBITMQ_EVENTS_CHATS_UPDATE=true
RABBITMQ_EVENTS_CHATS_DELETE=true
RABBITMQ_EVENTS_GROUPS_UPSERT=true
RABBITMQ_EVENTS_GROUP_UPDATE=true
RABBITMQ_EVENTS_GROUP_PARTICIPANTS_UPDATE=true
RABBITMQ_EVENTS_CONNECTION_UPDATE=true
RABBITMQ_EVENTS_CALL=true
RABBITMQ_EVENTS_TYPEBOT_START=true
RABBITMQ_EVENTS_TYPEBOT_CHANGE_STATUS=true
```

### Funcionamento

- **Fila por Evento**: No modo global, os eventos são enfileirados em filas específicas para cada tipo de evento. Por exemplo, todos os eventos de atualização de mensagens (`MESSAGES_UPDATE`) serão enfileirados na mesma fila, independentemente da instância de origem.
- **Facilidade de Gerenciamento**: Essa abordagem facilita o gerenciamento e monitoramento dos eventos, permitindo uma centralização das operações e simplificando a lógica de consumo de mensagens no seu sistema.

## Configuração do RabbitMQ para Instâncias Individuais

Embora a configuração global seja recomendada para centralizar o processamento de eventos, ainda é possível configurar o RabbitMQ para instâncias individuais, caso haja necessidade de segmentação por instância.

### Endpoint para Configuração Individual

Para configurar o RabbitMQ para uma instância específica do WhatsApp na Evolution API, utilize o seguinte endpoint:

```
POST [baseUrl]/rabbitmq/set/[instance_name]
```

### Corpo da Requisição

Aqui está um exemplo do corpo JSON para configurar eventos em uma instância específica:

```
{
    "enabled": true,
    "events": [
        "APPLICATION_STARTUP",
        "QRCODE_UPDATED",
        "MESSAGES_SET",
        "MESSAGES_UPSERT",
        "MESSAGES_UPDATE",
        "MESSAGES_DELETE",
        "SEND_MESSAGE",
        "CONTACTS_SET",
        "CONTACTS_UPSERT",
        "CONTACTS_UPDATE",
        "PRESENCE_UPDATE",
        "CHATS_SET",
        "CHATS_UPSERT",
        "CHATS_UPDATE",
        "CHATS_DELETE",
        "GROUPS_UPSERT",
        "GROUP_UPDATE",
        "GROUP_PARTICIPANTS_UPDATE",
        "CONNECTION_UPDATE",
        "CALL",
        "NEW_JWT_TOKEN"
    ]
}
```

Ao configurar a integração com o RabbitMQ para instâncias individuais, ajuste o array de eventos no corpo JSON para incluir apenas os eventos relevantes para aquela instância.

## Considerações Finais

A configuração do RabbitMQ na Evolution API oferece flexibilidade para gerenciar eventos de forma centralizada com a configuração global, ou de forma segmentada por instância, dependendo das necessidades do seu sistema. Utilize a configuração global para simplificar a gestão de eventos em ambientes complexos, ou configure individualmente para controle mais granular.