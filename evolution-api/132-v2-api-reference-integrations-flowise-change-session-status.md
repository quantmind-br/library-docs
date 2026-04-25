---
title: Change Status Session - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/flowise/change-session-status
source: sitemap
fetched_at: 2026-04-12T18:48:59.672808478-03:00
rendered_js: false
word_count: 65
summary: This document explains the necessary structure and parameters to update the status of a specific Flowise instance via an API request.
tags:
    - api-update
    - flowise-status
    - whatsapp-jid
    - authorization-key
category: reference
---

Atualiza o status de uma instância Flowise

#### Authorizations

Your authorization key header

#### Path Parameters

#### Body

Corpo da requisição contendo o identificador remoto e o status a ser atualizado

Identificador remoto do WhatsApp no formato JID

Example:

`"5511912345678@s.whatsapp.net"`

Novo status para a instância

Available options:

`opened`,

`paused`,

`closed`

#### Response

Status da instância Flowise atualizado com sucesso

Example:

`"Status alterado com sucesso"`

[Find Flowise settings](https://doc.evolution-api.com/v2/api-reference/integrations/flowise/find-settings)[Find Sessions Flowise](https://doc.evolution-api.com/v2/api-reference/integrations/flowise/find-sessions)