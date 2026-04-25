---
title: Variáveis de Ambiente - Evolution API Documentation
url: https://doc.evolution-api.com/v2/pt/env
source: sitemap
fetched_at: 2026-04-12T18:45:46.525689329-03:00
rendered_js: false
word_count: 831
summary: This document details the comprehensive environment variables required for configuring an application, covering settings for servers, telemetry, CORS policies, logging levels, persistent storage, messaging queues (RabbitMQ), cloud services (SQS), WebSockets, WhatsApp Business API integration, and various webhook configurations.
tags:
    - environment-variables
    - configuration
    - api-setup
    - webhooks
    - logging
    - database
category: guide
---

Veja o arquivo de exemplo do env no [repositório oficial](https://github.com/EvolutionAPI/evolution-api/blob/main/Docker/.env.example).

## Server

VariávelValorExemploSERVER\_TYPEO tipo de servidor (http ou https)httpSERVER\_PORTPorta em que o servidor será executado8080SERVER\_URLO endereço para seu servidor em execução. Esse endereço é utilizado para retornar dados de requisição interna, como links de webhook.[https://exemplo.evolution-api.com](https://exemplo.evolution-api.com)

## Telemetria

VariávelValorExemploTELEMETRYHabilita ou desabilita a telemetria (true ou false)trueTELEMETRY\_URLURL do servidor de telemetria[https://telemetry.example.com](https://telemetry.example.com)

## CORS

VariávelValorExemploCORS\_ORIGINAs origens permitidas pela API separadas por vírgula (utilize ”\*” para aceitar requisições de qualquer origem)\*CORS\_METHODSMétodos HTTP permitidos separados por vírgulaGET,POST,PUT,DELETECORS\_CREDENTIALSPermissão de cookies em requisições (true ou false)true

## Logs

VariávelValorExemploLOG\_LEVELLogs que serão mostrados entre: ERROR, WARN, DEBUG, INFO, LOG, VERBOSE, DARK, WEBHOOKSERROR,WARN,DEBUG,INFO,LOG,VERBOSE,DARK,WEBHOOKSLOG\_COLORMostrar ou não cores nos Logs (true ou false)trueLOG\_BAILEYSQuais logs da Baileys serão mostrados entre: “fatal”, “error”, “warn”, “info”, “debug”, “trace”error

## Instâncias

VariávelValorExemploDEL\_INSTANCEEm quantos minutos uma instância será excluída se não conectada. Use “false” para nunca excluirfalse

## Armazenamento Persistente

VariávelValorExemploDATABASE\_ENABLEDSe o armazenamento persistente está habilitado (true ou false)trueDATABASE\_PROVIDERProvedor de banco de dados (postgresql ou mysql)postgresqlDATABASE\_CONNECTION\_URIA URI de conexão do banco de dadospostgresql://user:pass@localhost:5432/evolution?schema=publicDATABASE\_CONNECTION\_CLIENT\_NAMENome do cliente para a conexão com o banco de dados, usado para separar uma instalação da API de outra que usa o mesmo bancoevolution\_exchange

### Quais dados serão salvos (true ou false)

VariávelValorDATABASE\_SAVE\_DATA\_INSTANCESalva dados de instânciasDATABASE\_SAVE\_DATA\_NEW\_MESSAGESalva novas mensagensDATABASE\_SAVE\_MESSAGE\_UPDATESalva atualizações de mensagensDATABASE\_SAVE\_DATA\_CONTACTSSalva contatosDATABASE\_SAVE\_DATA\_CHATSSalva conversasDATABASE\_SAVE\_DATA\_LABELSSalva etiquetasDATABASE\_SAVE\_DATA\_HISTORICSalva histórico de eventos

## RabbitMQ

VariávelValorExemploRABBITMQ\_ENABLEDHabilita o RabbitMQ (true ou false)falseRABBITMQ\_URIURI de conexão do RabbitMQamqp://localhostRABBITMQ\_EXCHANGE\_NAMENome do exchangeevolutionRABBITMQ\_GLOBAL\_ENABLEDHabilita o RabbitMQ de forma global (true ou false)false

### Escolha os eventos que deseja enviar para o RabbitMQ

VariávelValorExemploRABBITMQ\_EVENTS\_APPLICATION\_STARTUPEnvia um evento na inicialização do app (true ou false)falseRABBITMQ\_EVENTS\_INSTANCE\_CREATEEnvia eventos de criação de instância (true ou false)falseRABBITMQ\_EVENTS\_INSTANCE\_DELETEEnvia eventos de deleção de instância (true ou false)falseRABBITMQ\_EVENTS\_QRCODE\_UPDATEDEnvia eventos de atualização do QR Code (true ou false)falseRABBITMQ\_EVENTS\_MESSAGES\_SETEnvia eventos de criação de mensagens (recuperação de mensagens) (true ou false)falseRABBITMQ\_EVENTS\_MESSAGES\_UPSERTEnvia eventos de recebimento de mensagens (true ou false)falseRABBITMQ\_EVENTS\_MESSAGES\_EDITEDEnvia eventos de edição de mensagens (true ou false)falseRABBITMQ\_EVENTS\_MESSAGES\_UPDATEEnvia eventos de atualização de mensagens (true ou false)falseRABBITMQ\_EVENTS\_MESSAGES\_DELETEEnvia eventos de deleção de mensagens (true ou false)falseRABBITMQ\_EVENTS\_SEND\_MESSAGEEnvia eventos de envio de mensagens (true ou false)falseRABBITMQ\_EVENTS\_CONTACTS\_SETEnvia eventos de criação de contatos (true ou false)falseRABBITMQ\_EVENTS\_CONTACTS\_UPSERTEnvia eventos de recuperação de contatos (true ou false)falseRABBITMQ\_EVENTS\_CONTACTS\_UPDATEEnvia eventos de atualização de contatos (true ou false)falseRABBITMQ\_EVENTS\_PRESENCE\_UPDATEEnvia eventos de atualização de presença (“digitando…” ou “gravando…”) (true ou false)falseRABBITMQ\_EVENTS\_CHATS\_SETEnvia eventos de criação de conversas (recuperação de conversas) (true ou false)falseRABBITMQ\_EVENTS\_CHATS\_UPSERTEnvia eventos de criação de conversas (recebimento ou envio de mensagens em novos chats) (true ou false)falseRABBITMQ\_EVENTS\_CHATS\_UPDATEEnvia eventos de atualização de conversas (true ou false)falseRABBITMQ\_EVENTS\_CHATS\_DELETEEnvia eventos de deleção de conversas (true ou false)falseRABBITMQ\_EVENTS\_GROUPS\_UPSERTEnvia eventos de criação de grupos (true ou false)falseRABBITMQ\_EVENTS\_GROUP\_UPDATEEnvia eventos de atualização de grupos (true ou false)falseRABBITMQ\_EVENTS\_GROUP\_PARTICIPANTS\_UPDATEEnvia eventos de atualização nos participantes de grupos (true ou false)falseRABBITMQ\_EVENTS\_CONNECTION\_UPDATEEnvia eventos de atualização de conexão (true ou false)falseRABBITMQ\_EVENTS\_CALLEnvia eventos de chamadas (true ou false)falseRABBITMQ\_EVENTS\_TYPEBOT\_STARTEnvia eventos de início de fluxo do Typebot (true ou false)falseRABBITMQ\_EVENTS\_TYPEBOT\_CHANGE\_STATUSEnvia eventos de atualização no status do Typebot (true ou false)false

## SQS

VariávelValorExemploSQS\_ENABLEDSe o SQS está habilitado (true ou false)falseSQS\_ACCESS\_KEY\_IDO ID de chave do SQS-SQS\_SECRET\_ACCESS\_KEYChave de acesso-SQS\_ACCOUNT\_IDID da conta-SQS\_REGIONRegião do SQS-

## WebSocket

VariávelValorExemploWEBSOCKET\_ENABLEDHabilita o WebSocket (true ou false)falseWEBSOCKET\_GLOBAL\_EVENTSHabilita eventos globais no WebSocket (true ou false)false

## WhatsApp Business API

VariávelValorExemploWA\_BUSINESS\_TOKEN\_WEBHOOKToken usado para validar o webhook no Facebook APPevolutionWA\_BUSINESS\_URLURL da API do WhatsApp Business[https://graph.facebook.com](https://graph.facebook.com)WA\_BUSINESS\_VERSIONVersão da API do WhatsApp Businessv20.0WA\_BUSINESS\_LANGUAGEIdioma da API do WhatsApp Businessen\_US

## Webhook Global

VariávelValorExemploWEBHOOK\_GLOBAL\_ENABLEDSe os webhooks estão habilitados globalmente (true ou false)falseWEBHOOK\_GLOBAL\_URLURL que receberá as requisições de webhook[https://webhook.example.com](https://webhook.example.com)WEBHOOK\_GLOBAL\_WEBHOOK\_BY\_EVENTSAtiva webhook por evento, respeitando a URL global e o nome de cada evento (true ou false)false

### Eventos de webhook com valor true ou false

VariávelWEBHOOK\_EVENTS\_APPLICATION\_STARTUPWEBHOOK\_EVENTS\_QRCODE\_UPDATEDWEBHOOK\_EVENTS\_MESSAGES\_SETWEBHOOK\_EVENTS\_MESSAGES\_UPSERTWEBHOOK\_EVENTS\_MESSAGES\_EDITEDWEBHOOK\_EVENTS\_MESSAGES\_UPDATEWEBHOOK\_EVENTS\_MESSAGES\_DELETEWEBHOOK\_EVENTS\_SEND\_MESSAGEWEBHOOK\_EVENTS\_CONTACTS\_SETWEBHOOK\_EVENTS\_CONTACTS\_UPSERTWEBHOOK\_EVENTS\_CONTACTS\_UPDATEWEBHOOK\_EVENTS\_PRESENCE\_UPDATEWEBHOOK\_EVENTS\_CHATS\_SETWEBHOOK\_EVENTS\_CHATS\_UPSERT

| | WEBHOOK\_EVENTS\_CHATS\_UPDATE | | WEBHOOK\_EVENTS\_CHATS\_DELETE | | WEBHOOK\_EVENTS\_GROUPS\_UPSERT | | WEBHOOK\_EVENTS\_GROUPS\_UPDATE | | WEBHOOK\_EVENTS\_GROUP\_PARTICIPANTS\_UPDATE | | WEBHOOK\_EVENTS\_CONNECTION\_UPDATE | | WEBHOOK\_EVENTS\_LABELS\_EDIT | | WEBHOOK\_EVENTS\_LABELS\_ASSOCIATION | | WEBHOOK\_EVENTS\_CALL | | WEBHOOK\_EVENTS\_TYPEBOT\_START | | WEBHOOK\_EVENTS\_TYPEBOT\_CHANGE\_STATUS | | WEBHOOK\_EVENTS\_ERRORS | | WEBHOOK\_EVENTS\_ERRORS\_WEBHOOK |

## Configurações de Sessão

VariávelValorExemploCONFIG\_SESSION\_PHONE\_CLIENTNome que será exibido na conexão do smartphoneEvolution APICONFIG\_SESSION\_PHONE\_NAMENome do navegador (Chrome, Firefox, Edge, Opera, Safari)Chrome

## QR Code

VariávelValorExemploQRCODE\_LIMITPor quanto tempo o QR code durará30QRCODE\_COLORCor do QR code gerado#175197

## Typebot

VariávelValorExemploTYPEBOT\_API\_VERSIONVersão da API (versão fixa ou latest)latest

## Chatwoot

VariávelValorExemploCHATWOOT\_ENABLEDHabilita a integração com Chatwoot (true ou false)falseCHATWOOT\_MESSAGE\_READMarca como lida a última mensagem do cliente no WhatsApp ao enviar uma mensagem no Chatwoot (true ou false)trueCHATWOOT\_MESSAGE\_DELETEDeleta a mensagem no Chatwoot quando deletada no WhatsApp (true ou false)trueCHATWOOT\_IMPORT\_DATABASE\_CONNECTION\_URIURI de conexão com o banco de dados do Chatwoot para importar mensagenspostgresql://user:password@host:5432/chatwoot?sslmode=disableCHATWOOT\_IMPORT\_PLACEHOLDER\_MEDIA\_MESSAGEImporta as mensagens de mídia como placeholder no Chatwoot (true ou false)true

## OpenAI

VariávelValorExemploOPENAI\_ENABLEDHabilita a integração com OpenAI (true ou false)false

## Dify

VariávelValorExemploDIFY\_ENABLEDHabilita a integração com Dify (true ou false)false

## Cache

VariávelValorExemploCACHE\_REDIS\_ENABLEDHabilita o cache Redis (true ou false)trueCACHE\_REDIS\_URIA URI de conexão do Redisredis://localhost:6379/6CACHE\_REDIS\_PREFIX\_KEYPrefixo para diferenciar dados de uma instalação para outra usando o mesmo RedisevolutionCACHE\_REDIS\_SAVE\_INSTANCESSalva as credenciais de conexão do WhatsApp no Redis (true ou false)falseCACHE\_LOCAL\_ENABLEDHabilita o cache local em memória como alternativa ao Redis (true ou false)false

## Amazon S3 / MinIO

VariávelValorExemploS3\_ENABLEDHabilita o armazenamento no S3 (true ou false)falseS3\_ACCESS\_KEYChave de acesso do S3-S3\_SECRET\_KEYChave secreta do S3-S3\_BUCKETNome do bucket no S3evolutionS3\_PORTPorta de conexão ao S3443S3\_ENDPOINTEndpoint do S3 (ou MinIO)s3.amazonaws.comS3\_USE\_SSLUsa SSL para conexão ao S3 (true ou false)true

## Autenticação

VariávelValorExemploAUTHENTICATION\_API\_KEYChave da API usada para autenticação global429683C4C977415CAAFCCE10F7D57E11AUTHENTICATION\_EXPOSE\_IN\_FETCH\_INSTANCESExibe as instâncias no endpoint de fetch (true ou false)true

## Idioma

VariávelValorExemploLANGUAGEIdioma da APIen