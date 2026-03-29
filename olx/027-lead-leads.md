---
title: Envio de Leads
url: https://developers.olx.com.br/lead/leads.html
source: crawler
fetched_at: 2026-02-07T15:17:29.272341423-03:00
rendered_js: false
word_count: 330
summary: This document outlines the technical specifications for integrating OLX leads via HTTP POST requests, detailing the required JSON payload structure, parameters, and status code handling.
tags:
    - api-integration
    - lead-generation
    - json-payload
    - olx-platform
    - webhook
    - http-post
category: api
---

## Documentação da API de integração de Leads

As informações dos leads serão enviados via protocolo HTTP ou HTTPS com o verbo POST com payload em formato JSON para o endpoint especificado para o cliente.

Cada lead será enviado de forma individual, a medida que forem gerados na plataforma OLX, contendo os seguintes campos:

ParâmetroObrigatórioDescrição`source`SimOrigem do lead. Valores possíveis: `whatsapp`, `telefone`, `chat`, `financing` (simulação de financiamento), `olx` (outras origens).`adId`**1**NãoIdentificador do anúncio no software de gestão (integrador).`listId`SimIdentificador do anúncio na OLX`linkAd`SimLink do anúncio na OLX`name`SimNome do cliente que entrou em contato.`email`SimEmail do cliente que entrou em contato.`phone`NãoTelefone do cliente que entrou em contato. Sequência numérica de até 13 caracteres. Telefones podem vir com ou sem DDD.`message`SimMensagem enviada pelo cliente.`createdAt`SimData e hora da geração do lead.`adsInfo`**2**NãoInformações adicionais de anúncios. Disponível apenas para algumas categorias.`externalId`NãoIdentificador único do lead.

> **1** Caso o campo `adId` for enviado vazio, significa que o anúncio do cliente foi inserido manualmente (diretamente no portal OLX) e não pela nossa API de integração de anúncios
> 
> **2** Para mais informações detalhadas de anúncio, consultar a documentação [Envio de leads com informações detalhadas de anúncio](https://developers.olx.com.br/lead/leads_enriched.html)

Segue um exemplo de um JSON para um lead enviado:

```
{
  "source": "financing",
  "adId": "a1234",
  "listId": "12345689",
  "linkAd": "https://www.olx.com.br/vi/12345689",
  "name": "Nome do cliente",
  "email": "email.docliente@gmail.com",
  "phone": "2199999999",
  "message": "Olá, gostaria de saber mais informações sobre o anúncio a1234", 
  "createdAt": "2019-02-12T14:30:00.500Z",
  "adsInfo": {
    "category": 2020,
    "subject": "Harley Davidson",
    "body": "Harley Davidson fat boy carburada, frente cabeça de touro",
    "type": "sell",
    "price": "90000",
    "zipcode": "25964000",
    "regdate": "90000",
    "mileage": "43000",
    "carcolor": "1",
    "fuel": "1",
    "car_steering": "1",
    "exchange": "1",
    "owner": "1",
    "financial": "2|3|4",
    "financial_status": "1",
    "vehicle_brand": "28",
    "vehicle_model": "7",
    "vehicle_version": "2",
    "cubiccms": "21",
    "moto_features": "1|2|3|4|5|6|7|8|9"
  },
  "externalId": "123jdanjkdna-danjndaada"
}
```

### Restrições atuais

Atualmente, a OLX só suporta envio de leads via integração para algumas de suas categorias:

CategoriaSubcategoriaCódigo da CategoriaAutosCarros, vans e utilitários`2020`AutosMotos`2060`AutosCaminhões`2040`

### Status code

Nosso controle de entrega de leads será feito com base no status code do protocolo HTTP:

- `2XX`: Indica que o lead foi recebido com sucesso.
- `3XX`, `4XX` ou `5XX`: Indica que houve erro no recebimento do lead.

A OLX guardará a resposta da entrega do lead para eventual *troubleshoot*. A priori, a OLX não tem política de reenvio ou reprocessamento de leads que não forem recebidos.

É recomendável que seja enviada um `responseId`, para identificar o recebimento do lead e a resposta devolvida referente a esse lead recebido.

### Timeout

As requisições para o endpoint estão configuradas com timeout de 5 segundos. Caso a requisição que demore mais que 5 segundos, será considerada ERRO.