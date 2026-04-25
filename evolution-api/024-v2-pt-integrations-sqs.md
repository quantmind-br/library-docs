---
title: Amazon SQS - Evolution API Documentation
url: https://doc.evolution-api.com/v2/pt/integrations/sqs
source: sitemap
fetched_at: 2026-04-12T18:45:40.990541614-03:00
rendered_js: false
word_count: 334
summary: This document details how to integrate and configure Amazon SQS with the Evolution API for managing events and message queues in a scalable manner, covering both global and instance-specific setup methods.
tags:
    - amazon-sqs
    - event-management
    - api-integration
    - configuration
    - aws-sdk
category: guide
---

A Evolution API permite a integração com o **Amazon SQS (Simple Queue Service)** para gerenciar eventos e filas de mensagens de forma escalável e confiável. Assim como no RabbitMQ, o SQS na Evolution API pode ser configurado tanto de maneira global quanto para instâncias individuais.

## Configuração Global do SQS

Para habilitar o SQS e configurar o processamento de eventos de forma centralizada, utilize as seguintes variáveis de ambiente:

### Configuração de Variáveis de Ambiente

```
SQS_ENABLED=true
SQS_ACCESS_KEY_ID=your-access-key-id
SQS_SECRET_ACCESS_KEY=your-secret-access-key
SQS_ACCOUNT_ID=your-account-id
SQS_REGION=your-region
```

### Explicação das Variáveis

- **`SQS_ENABLED`** : Ativa (`true`) ou desativa (`false`) a integração com o Amazon SQS.
- **`SQS_ACCESS_KEY_ID`** : Chave de acesso da AWS para autenticação.
- **`SQS_SECRET_ACCESS_KEY`** : Chave secreta correspondente à chave de acesso para autenticação.
- **`SQS_ACCOUNT_ID`** : ID da conta AWS onde o SQS está configurado.
- **`SQS_REGION`** : Região da AWS onde suas filas SQS estão localizadas (por exemplo, `us-east-1`).

### Funcionamento

- **Fila por Evento**: No modo global, todos os eventos são enfileirados em filas específicas para cada tipo de evento. Isso significa que eventos de diferentes instâncias são centralizados em filas unificadas por evento, simplificando o processamento e o monitoramento.

## Configuração do SQS para Instâncias Individuais

Embora a configuração global seja recomendada para centralizar o processamento de eventos, você pode configurar o SQS para instâncias individuais caso precise segmentar as filas por instância.

### Endpoint para Configuração Individual

Para configurar o SQS para uma instância específica do WhatsApp na Evolution API, utilize o seguinte endpoint:

```
POST [baseUrl]/sqs/set/[instance_name]
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

### Funcionamento

- **Segmentação por Instância**: Ao configurar o SQS para instâncias individuais, cada instância pode ter suas próprias filas específicas para os eventos configurados. Isso permite maior controle e segmentação dos eventos, caso você precise separar o processamento por instância.

## Considerações Finais

A integração com o Amazon SQS na Evolution API oferece uma solução poderosa para gerenciar eventos de forma escalável e confiável, tanto de maneira centralizada quanto segmentada por instância. Utilize a configuração global para simplificar o processamento em ambientes complexos, ou configure individualmente para um controle mais granular.