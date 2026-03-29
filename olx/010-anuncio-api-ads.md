---
title: Consulta de status da publicação
url: https://developers.olx.com.br/anuncio/api/ads.html
source: crawler
fetched_at: 2026-02-07T15:17:07.556728453-03:00
rendered_js: false
word_count: 323
summary: This document explains how to monitor and query the status of advertisements published via the OLX API, detailing the differences between import processes and final ad states.
tags:
    - olx-api
    - ad-status
    - import-process
    - webhooks
    - api-integration
    - ad-publishing
category: api
---

## Anúncios Publicados por API

Essa pagina de consultar o status do anúncio é apenas para processos via API.

Uma vez finalizado o processo de importação na plataforma, existem 3 endpoints para consultar informações relacionadas as publicações. O primeiro é uma [Listagem de Publicação](https://developers.olx.com.br/anuncio/api/published_ads.html) de todos os anúncios ativos que foram publicados passando um `access_token`. O segundo é [Consulta de status da Importação](https://developers.olx.com.br/anuncio/api/publishing_status.html) a partir do token que é gerado toda vez que um processo de importação de anúncio se inicia. Já o terceiro é uma [Consulta do status de Anúncios Publicados](https://developers.olx.com.br/anuncio/api/published_ads_status.html) de um anúncio passando o `list_id` e o `access_token`.

## Qual a diferença entre consultar o status da importação de um anúncio e o status do anúncio?

Consultar o status do *processo de importação de um anúncio* envolve verificar em que etapa o anúncio está durante o processo de publicação, como "done" ou "pending". Já consultar o status do anúncio refere-se à condição atual do anúncio após a publicação, como "accepted", "refused","deleted", "pending" ou "queued". O primeiro foca na jornada até o anúncio ser publicado, enquanto o segundo foca na situação do anúncio já publicado.  
O Token de importação, tem o prazo e a duração de uso de no maximo `7 dias` após esse periodo a requisição passa a retornar 404. Ja a consulta do status do anúncio não tem expiração.

Para mais [detalhes consulta do status da importação](https://developers.olx.com.br/anuncio/api/publishing_status.html).

Para mais [detalhes consulta do status do anúncio](https://developers.olx.com.br/anuncio/api/publishing_ads_status.html).

## Você sabia que podemos enviar qualquer modificação realizada no anúncio por API?

SIM, É ISSO MESMO!  
Confira nossa documentação de [Notificação via Webhooks](https://developers.olx.com.br/webhooks/home.html) que faz com que através de uma API cadastrada com a gente, enviamos notificações referentes a varios temas para essa configuração de API. E toda modificação do anúncio realizado pela OLX, **pelo integrador, ou pelo cliente** vamos enviar um evento para essa URL. Lembrando que esta funcionalidade está em BETA, então modificações de contratos podem ser realizadas e precisamos muito do seu feedback.