---
title: Notificação de Status de Anúncios
url: https://developers.olx.com.br/webhooks/notifications_ad_status.html
source: crawler
fetched_at: 2026-02-07T15:17:22.246531221-03:00
rendered_js: false
word_count: 372
summary: This document describes the structure and field definitions for advertisement status notifications, including a comprehensive list of possible status values and refusal reasons for integrators.
tags:
    - ad-status
    - notifications
    - api-reference
    - integration
    - olx-api
    - webhook-payload
category: reference
---

## Notificação de Status de Anúncios

Este tipo de notificação é enviado sempre que o status de um anúncio importado é alterado. O status dos anúncios possíveis estão listados na tabela [Status de Anúncio](#status-de-anuncio).

## Detalhes da Notificação

A notificação de status de anúncio contém os seguintes campos:

ParâmetroValoresTipoObrigatórioDescrição`id`stringstringSimO identificador único da notificação.`topic`stringstringSimO tópico da notificação. Atualmente, apenas o tópico `AD_STATUS` é suportado.`created_at`stringstringSimA data e hora em que a notificação foi criada, no formato `YYYY-MM-DDTHH:MM:SS.SSS`.`data`objectobjectSimOs dados da notificação.`data.ad`objectobjectSimOs dados do anúncio.`data.ad.id`stringstringSimO identificador único do anúncio no integrador.`data.ad.list_id`stringstringSimO identificador único do anúncio na OLX.`data.ad.category`stringstringSimO identificador da categoria do anúncio.`data.ad.status`stringstringSimO status do anúncio (consultar tabela de status abaixo).`data.ad.operation`stringstringSimA operação que foi realizada no anúncio. Pode ser `"INSERT"`, `"MODIFY"` ou `"DELETE"`.`data.ad.reason_tag`stringstringNãoA tag de motivo associada ao status do anúncio quando recusado (`refused`). Veja [Tabela Motivos de Recusa](#tabela-de-motivos-de-recusa) para mais detalhes.`data.ad.message`stringstringNãoMensagem contendo o motivo da recusa. Veja [Tabela Motivos de Recusa](#tabela-de-motivos-de-recusa) para mais detalhes.`data.actions`objectobjectNãoEstrutura contendo urls para atividades que poderão ser executadas sobre o anúncio.`data.actions.view`stringstringNãoA URL para visualizar o anúncio na OLX.

## Status de Anúncio

O status do anúncio pode ser um dos seguintes:

StatusDescrição`pending_pay`O anúncio está aguardando pagamento por ter sido inserido fora do limite de contrato.`pending_review`O anúncio está aguardando revisão para publicação.`accepted`O anúncio foi aceito.`refused`O anúncio foi recusado. O motivo será enviado junto as informações do anúncio.`published`O anúncio foi publicado e está disponível para visualização no portal da OLX.`published_pending_review`A nova versão do anúncio está aguardando revisão.`deleted`O anúncio foi excluído.`sold`O anúncio foi vendido via OLX Pay.`deleted_sold`O anúncio foi vendido via OLX Pay e foi excluído.`expired`O anúncio expirou.`undeleted`O anúncio foi restaurado após ter sido excluído.`expired_reviewed`O anúncio foi renovado e está aguardando revisão.

## Tabela de motivos de recusa

A tag de motivo (`reason_tag`) associada ao status do anúncio quando recusado (`refused`) pode ser uma das seguintes:

reason\_tagmessageGENERIC\_REFUSEDRecusado por motivo não identificadoREFUSED\_SUSPECT\_CARTCorpo de telefone suspeitoAUTOS\_FRAUD\_MODELModelo de fraude automotivaREFUSED\_DENOUNCEDDenúncia - Backlog  
Denúncia - Controle de reincidentesREFUSED\_SUSPECT\_AUTOSDenúncia - Veículos SuspeitosREFUSED\_SUSPECT\_EMAILDomínio de emails suspeitosREFUSED\_SUSPECT\_IPDomínio de IPs suspeitosREFUSED\_SUSPECT\_ELECTRONICDenúncia - Eletrônicos suspeitos  
Fraude de eletrônicosREFUSED\_SUSPECT\_USERFraude de usuárioREFUSED\_SUSPECT\_PROPERTIESFraude do imóveis  
Revisão do ZAPREFUSED\_SUSPECT\_CATEGORYCategoria suspeita  
Denúncia - Categorias médio riscoREFUSED\_SUSPECT\_DUPLICATESSuspeita de duplicação  
Suspeita de anúncios duplicados por atributosREFUSED\_SUSPECT\_FRAUDSuspeita de fraudeREFUSED\_SUSPECT\_ITEMSSuspeita de itens proibidosREFUSED\_SUSPECT\_LINK\_TAGSSuspeita de tags / linkREFUSED\_SUSPECT\_PRICESuspeita no preçoAWAITING\_PROCESSINGAguardando processamento

## Exemplo de Notificação de Status de Anúncio

Aqui está um exemplo de notificação de status de anúncio:

```
{
  "id":"191389c3-d42a-464d-9c3f-4edfb6c1fc05",
  "topic":"AD_STATUS",
  "created_at":"2024-05-29T18:00:00.123",
  "data":{
    "ad":{
      "id":"12345",
      "list_id":1234553,
      "category":11020,
      "status":"published",
      "operation":"INSERT"
    },
    "actions":{
      "view":"https://www.olx.com.br/vi/1223432423.htm"
    }
  }
}
```