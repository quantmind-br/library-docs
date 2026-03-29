---
title: Via Administração do HV
url: https://developers.olx.com.br/hv/rotas_api_hv.html
source: crawler
fetched_at: 2026-02-07T15:17:38.661877238-03:00
rendered_js: false
word_count: 489
summary: This document provides technical documentation for the Vehicle History API, detailing how to activate, query, and remove vehicle history information from advertisements.
tags:
    - api-reference
    - vehicle-history
    - endpoint-documentation
    - http-methods
    - integration-guide
category: api
---

## Rotas da API - Histórico Veicular

As rotas abaixo são utilizadas para ativação, remoção e consulta do **Histórico Veicular (HV)**, uma funcionalidade que permite adicionar o histórico de um veículo a um anúncio, fornecendo mais segurança e informações para compradores e vendedores.

### Consulta do Histórico Veicular

Essa rota permite consultar o histórico de um veículo por meio do **clientAdId**.

Exemplo de Requisição:

```
curl --location 'https://apps.olx.com.br/autoupload/vehicle-histories/:clientAdId' \
--header 'Authorization: <access_token>'
```

Parâmetros:

ParâmetroValoresObrigatórioDescrição`clientAdId``string`simIdentificador único do anúncio no sistema do integrador`access_token``string`simToken de autenticação

### Formato da Resposta

Em caso de sucesso, a API retornará o status `200 OK` com um payload JSON contendo o estado atual do Histórico Veicular.

**Estrutura do Objeto de Resposta:**

```
{
  "data": {
    "list_id": "string | null",
    "status": "string",
    "vehicle_tag": "string | null"
  }
}
```

**Campos da Resposta:**

CampoDescrição`list_id`ID do anúncio na OLX. Pode estar vazio se o anúncio ainda não foi processado ou se o HV está pendente de dados.`status`O estado atual do processo do Histórico Veicular. Este é o campo principal para entender o andamento da solicitação.`vehicle_tag`Placa do veículo associada ao Histórico Veicular.

### Possíveis Status do Histórico Veicular

A tabela abaixo descreve todos os valores possíveis para o campo `status` e o que cada um significa.

StatusDescrição`pending_vehicle_data`**Aguardando dados do veículo:** O processo foi iniciado, mas são necessários os dados do veículo (RENAVAM, placa e CPF/CNPJ) para prosseguir com a consulta.`pending`**Consulta em andamento:** Os dados foram recebidos e o sistema está aguardando o retorno das vistoriadoras para confirmar a existência de um Histórico Veicular.`available`**Disponível:** O Histórico Veicular foi encontrado, aprovado e está ativo no anúncio.`user_excluded`**Removido pelo usuário:** O usuário (vendedor) optou por remover o Histórico Veicular do anúncio.`ad_excluded`**Anúncio removido:** O anúncio ao qual o Histórico Veicular estava vinculado foi deletado.`error`**Erro na consulta:** Ocorreu um erro inesperado durante o processo de consulta do Histórico Veicular.

### Exemplos de Resposta por Status

**Status: `pending_vehicle_data`(HV necessita de dados para ser validado)**

```
{
    "data": {
        "list_id": "",
        "status": "pending_vehicle_data",
        "vehicle_tag": ""
    }
}
```

**Status: `pending`(Aguardando retorno das vistoriadoras)**

```
{
    "data": {
        "list_id": "12345678",
        "status": "pending",
        "vehicle_tag": "ABC1234"
    }
}
```

**Status: `available`(HV ativo e aprovado no anúncio)**

```
{
    "data": {
        "list_id": "12345678",
        "status": "available",
        "vehicle_tag": "ABC1234"
    }
}
```

**Status: `user_excluded`(HV removido pelo usuário)**

```
{
    "data": {
        "list_id": "12345678",
        "status": "user_excluded",
        "vehicle_tag": "ABC1234"
    }
}
```

**Status: `ad_excluded`(Anúncio com HV foi deletado)**

```
{
    "data": {
        "list_id": "12345678",
        "status": "ad_excluded",
        "vehicle_tag": "ABC1234"
    }
}
```

**Status: `error`(Erro na consulta do HV)**

```
{
    "data": {
        "list_id": "12345678",
        "status": "error",
        "vehicle_tag": "ABC1234"
    }
}
```

* * *

### Ativação do Histórico Veicular

Essa rota permite ativar o histórico veicular em um anúncio. O histórico é associado ao veículo utilizando o **clientAdId**.

Exemplo de Requisição:

```
curl --location --request PATCH 'https://apps.olx.com.br/autoupload/vehicle-histories/:clientAdId' \
--header 'Content-Type: application/json' \
--header 'Authorization: <access_token>' \
--data '{
    "renavam": "0987654321",
    "vehicle_tag": "ABC1234",
    "cpf_cnpj": "12345678909"
}'
```

Parâmetros:

ParâmetroValoresObrigatórioDescrição`clientAdId``string`simIdentificador único do anúncio no sistema do integrador`access_token``string`simToken de autenticação`renavam``string`simNúmero do RENAVAM do veículo`vehicle_tag``string`simPlaca do veículo`cpf_cnpj``string`simCPF ou CNPJ do proprietário

#### Respostas da Ativação `PATCH`

Status CodeMotivoDescrição da Resposta`200`SucessoA ativação foi processada com sucesso. **Nenhum corpo (body) é retornado.**`200`Nada alteradoO anúncio já possui um Histórico Veicular nos status `pending` ou `available`.

#### Exemplos de Resposta

**Anúncio já possui HV :**

```
{
    "message": "Vehicle History Status is already available or pending"
}
```

* * *

### Remoção do Histórico Veicular

Essa rota permite remover o histórico veicular de um anúncio.

Exemplo de Requisição:

```
curl --location --request DELETE 'https://apps.olx.com.br/autoupload/vehicle-histories/:clientAdId' \
--header 'Authorization: <access_token>'
```

Parâmetros:

ParâmetroValoresObrigatórioDescrição`clientAdId``string`simIdentificador único do anúncio no sistema do integrador`access_token``string`simToken de autenticação

#### Respostas da Remoção `DELETE`

Status CodeMotivoDescrição da Resposta`200 OK`SucessoA remoção foi processada com sucesso. **Nenhum corpo (body) é retornado.**

#### Respostas de Erro Comuns

Os erros abaixo podem ser retornados por **qualquer uma** das rotas.

Ocorre quando o `access_token` não é fornecido, é inválido ou expirou.

```
{
    "reason": "ACCESS_TOKEN_NOT_FOUND",
    "message": "Check the client authentication token."
}
```

#### `404 Not Found`

Ocorre quando o `clientAdId` fornecido na URL não corresponde a nenhum anúncio existente.

```
{
    "reason": "NOT_FOUND",
    "message": "Ad not found."
}
```