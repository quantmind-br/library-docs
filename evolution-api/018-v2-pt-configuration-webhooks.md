---
title: Webhooks - Evolution API Documentation
url: https://doc.evolution-api.com/v2/pt/configuration/webhooks
source: sitemap
fetched_at: 2026-04-12T18:46:03.70811821-03:00
rendered_js: false
word_count: 451
summary: This document explains how to implement and configure webhooks with the Evolution API for real-time WhatsApp integration. It details activation methods (global vs. instance), available event types, required parameters, and provides endpoints for managing or locating active webhook settings.
tags:
    - webhooks
    - whatsapp-api
    - integration
    - real-time
    - event-handling
    - configuration
category: guide
---

Os Webhooks permitem integração em tempo real entre a Evolution API e o WhatsApp™, permitindo sincronização e compartilhamento automatizados de dados. É exatamente esse recurso que possibilita a criação de bots de autoatendimento e sistemas multi-serviço.

## Ativando Webhooks

Existem duas maneiras de ativar o webhook:

- No arquivo `.env` com eventos globais
- Chamando o endpoint `/webhook/instance`

### Eventos de webhook da instância

A maioria dos usuários preferirá a ativação por instância, desta forma é mais fácil controlar os eventos recebidos, no entanto em alguns casos é necessário um webhook global, isso pode ser feito usando a variável de webhook global. Aqui está um exemplo com alguns eventos comuns ouvidos:

```
{
  "url": "{{webhookUrl}}",
  "webhook_by_events": false,
  "webhook_base64": false,
  "events": [
      "QRCODE_UPDATED",
      "MESSAGES_UPSERT",
      "MESSAGES_UPDATE",
      "MESSAGES_DELETE",
      "SEND_MESSAGE",
      "CONNECTION_UPDATE",
      "TYPEBOT_START",
      "TYPEBOT_CHANGE_STATUS"
  ]    
}
```

### Parâmetros

ParâmetroTipoObrigatórioDescriçãoenabledbooleanSimInsira “true” para criar ou alterar dados do Webhook, ou “false” se quiser parar de usá-lo.urlstringSimURL do Webhook para receber dados do evento.webhook\_by\_eventsbooleanNãoDeseja gerar uma URL específica do Webhook para cada um dos seus eventos.eventsarrayNãoLista de eventos a serem processados. Se você não quiser usar alguns desses eventos, apenas remova-os da lista.

### Eventos Globais de Webhook

Cada URL e eventos de Webhook da instância serão solicitados no momento em que forem criados Defina um webhook global que ouvirá eventos habilitados de todas as instâncias

```
WEBHOOK_GLOBAL_URL=''
WEBHOOK_GLOBAL_ENABLED=false

# Com esta opção ativada, você trabalha com uma URL por evento de webhook, respeitando a URL global e o nome de cada evento
WEBHOOK_GLOBAL_WEBHOOK_BY_EVENTS=false

## Defina os eventos que você deseja ouvir, todos os eventos listados abaixo são suportados
WEBHOOK_EVENTS_APPLICATION_STARTUP=false
WEBHOOK_EVENTS_QRCODE_UPDATED=true

# Alguns eventos extras para erros
WEBHOOK_EVENTS_ERRORS=false
WEBHOOK_EVENTS_ERRORS_WEBHOOK=
```

## Eventos Suportados

Estes são os eventos de webhook disponíveis e suportados:

**Variável de ambiente****URL****Descrição**APPLICATION\_STARTUP/application-startupNotifica quando uma inicialização de aplicativo ocorreQRCODE\_UPDATED/qrcode-updatedEnvia o base64 do qrcode para leituraCONNECTION\_UPDATE/connection-updateInforma o status da conexão com o WhatsAppMESSAGES\_SET/messages-setEnvia uma lista de todas as suas mensagens carregadas no WhatsApp. Este evento ocorre apenas uma vezMESSAGES\_UPSERT/messages-upsertNotifica quando uma mensagem é recebidaMESSAGES\_UPDATE/messages-updateInforma quando uma mensagem é atualizadaMESSAGES\_DELETE/messages-deleteInforma quando uma mensagem é excluídaSEND\_MESSAGE/send-messageNotifica quando uma mensagem é enviadaCONTACTS\_SET/contacts-setRealiza o carregamento inicial de todos os contatos. Este evento ocorre apenas uma vezCONTACTS\_UPSERT/contacts-upsertRecarrega todos os contatos com informações adicionais. Este evento ocorre apenas uma vezCONTACTS\_UPDATE/contacts-updateInforma quando o contato é atualizadoPRESENCE\_UPDATE/presence-updateInforma se o usuário está online, se ele está realizando alguma ação como escrever ou gravar e seu último visto: ‘indisponível’, ‘disponível’, ‘compondo’, ‘gravando’, ‘pausado’CHATS\_SET/chats-setEnvia uma lista de todos os chats carregadosCHATS\_UPDATE/chats-updateInforma quando o chat é atualizadoCHATS\_UPSERT/chats-upsertEnvia qualquer nova informação de chatCHATS\_DELETE/chats-deleteNotifica quando um chat é excluídoGROUPS\_UPSERT/groups-upsertNotifica quando um grupo é criadoGROUPS\_UPDATE/groups-updateNotifica quando um grupo tem suas informações atualizadasGROUP\_PARTICIPANTS\_UPDATE/group-participants-updateNotifica quando uma ação ocorre envolvendo um participante: ‘adicionar’, ‘remover’, ‘promover’, ‘rebaixar’NEW\_TOKEN/new-jwtNotifica quando o token (jwt) é atualizado

## Webhook por eventos

Ao habilitar as opções WEBHOOK\_BY\_EVENTS nos webhooks globais e locais, os seguintes caminhos serão adicionados ao final do webhook.

### Exemplo

Supondo que sua URL de webhook fosse `https://sub.domain.com/webhook/`. A Evolution adicionará automaticamente ao final da URL o nome do evento quando `webhook_by_events` estiver definido como verdadeiro.

## Localizando Webhook

Se necessário, há uma opção para localizar qualquer webhook ativo na instância específica.

MétodoEndpointGET\[baseUrl]/webhook/find/\[instance]

### Dados retornados da solicitação:

Chamando o endpoint retornará todas as informações sobre o webhook que está sendo usado pela instância.

```
{
  "enabled": true,
  "url": "[url]",
  "webhookByEvents": false,
  "events": [
    [eventos]
  ]
}
```