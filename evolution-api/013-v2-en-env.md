---
title: Environment Variables - Evolution API Documentation
url: https://doc.evolution-api.com/v2/en/env
source: sitemap
fetched_at: 2026-04-12T18:46:34.38807581-03:00
rendered_js: false
word_count: 667
summary: This document provides an extensive reference of environment variables and configuration settings for connecting the API to various services, including server details, telemetry, CORS policies, database connections, messaging queues like RabbitMQ and SQS, webhooks, and third-party integrations such as OpenAI.
tags:
    - environment-variables
    - api-configuration
    - service-integration
    - webhook-settings
    - connection-details
    - system-setup
category: reference
---

See the example env file in the [official repository](https://github.com/EvolutionAPI/evolution-api/blob/main/Docker/.env.example).

## Server

VariableValueExampleSERVER\_TYPEThe type of server (http or https)httpSERVER\_PORTPort on which the server will run8080SERVER\_URLThe address for your running server. This address is used to return data from internal requests, such as webhook links.[https://example.evolution-api.com](https://example.evolution-api.com)

## Telemetry

VariableValueExampleTELEMETRYEnables or disables telemetry (true or false)trueTELEMETRY\_URLURL of the telemetry server[https://telemetry.example.com](https://telemetry.example.com)

## CORS

VariableValueExampleCORS\_ORIGINAllowed origins for the API, separated by commas (use ”\*” to accept requests from any origin)\*CORS\_METHODSAllowed HTTP methods, separated by commasGET,POST,PUT,DELETECORS\_CREDENTIALSPermission for cookies in requests (true or false)true

## Logs

VariableValueExampleLOG\_LEVELLogs that will be displayed among: ERROR, WARN, DEBUG, INFO, LOG, VERBOSE, DARK, WEBHOOKSERROR,WARN,DEBUG,INFO,LOG,VERBOSE,DARK,WEBHOOKSLOG\_COLORWhether or not to show colors in Logs (true or false)trueLOG\_BAILEYSWhich Baileys logs will be displayed among: “fatal”, “error”, “warn”, “info”, “debug”, “trace”error

## Instances

VariableValueExampleDEL\_INSTANCEIn how many minutes an instance will be deleted if not connected. Use “false” to never deletefalse

## Persistent Storage

VariableValueExampleDATABASE\_ENABLEDWhether persistent storage is enabled (true or false)trueDATABASE\_PROVIDERDatabase provider (postgresql or mysql)postgresqlDATABASE\_CONNECTION\_URIThe database connection URIpostgresql://user:pass@localhost:5432/evolution?schema=publicDATABASE\_CONNECTION\_CLIENT\_NAMEClient name for the database connection, used to separate one API installation from another using the same databaseevolution\_exchange

### Which data will be saved (true or false)

VariableValueDATABASE\_SAVE\_DATA\_INSTANCESaves instance dataDATABASE\_SAVE\_DATA\_NEW\_MESSAGESaves new messagesDATABASE\_SAVE\_MESSAGE\_UPDATESaves message updatesDATABASE\_SAVE\_DATA\_CONTACTSSaves contactsDATABASE\_SAVE\_DATA\_CHATSSaves chatsDATABASE\_SAVE\_DATA\_LABELSSaves labelsDATABASE\_SAVE\_DATA\_HISTORICSaves event history

## RabbitMQ

VariableValueExampleRABBITMQ\_ENABLEDEnables RabbitMQ (true or false)falseRABBITMQ\_URIRabbitMQ connection URIamqp://localhostRABBITMQ\_EXCHANGE\_NAMEExchange nameevolutionRABBITMQ\_GLOBAL\_ENABLEDEnables RabbitMQ globally (true or false)false

### Choose the events you want to send to RabbitMQ

VariableValueExampleRABBITMQ\_EVENTS\_APPLICATION\_STARTUPSends an event on app startup (true or false)falseRABBITMQ\_EVENTS\_INSTANCE\_CREATESends instance creation events (true or false)falseRABBITMQ\_EVENTS\_INSTANCE\_DELETESends instance deletion events (true or false)falseRABBITMQ\_EVENTS\_QRCODE\_UPDATEDSends QR Code update events (true or false)falseRABBITMQ\_EVENTS\_MESSAGES\_SETSends message creation events (message retrieval) (true or false)falseRABBITMQ\_EVENTS\_MESSAGES\_UPSERTSends message receipt events (true or false)falseRABBITMQ\_EVENTS\_MESSAGES\_EDITEDSends message editing events (true or false)falseRABBITMQ\_EVENTS\_MESSAGES\_UPDATESends message update events (true or false)falseRABBITMQ\_EVENTS\_MESSAGES\_DELETESends message deletion events (true or false)falseRABBITMQ\_EVENTS\_SEND\_MESSAGESends message sending events (true or false)falseRABBITMQ\_EVENTS\_CONTACTS\_SETSends contact creation events (true or false)falseRABBITMQ\_EVENTS\_CONTACTS\_UPSERTSends contact retrieval events (true or false)falseRABBITMQ\_EVENTS\_CONTACTS\_UPDATESends contact update events (true or false)falseRABBITMQ\_EVENTS\_PRESENCE\_UPDATESends presence update events (“typing…” or “recording…”) (true or false)falseRABBITMQ\_EVENTS\_CHATS\_SETSends chat creation events (chat retrieval) (true or false)falseRABBITMQ\_EVENTS\_CHATS\_UPSERTSends chat creation events (receiving or sending messages in new chats) (true or false)falseRABBITMQ\_EVENTS\_CHATS\_UPDATESends chat update events (true or false)falseRABBITMQ\_EVENTS\_CHATS\_DELETESends chat deletion events (true or false)falseRABBITMQ\_EVENTS\_GROUPS\_UPSERTSends group creation events (true or false)falseRABBITMQ\_EVENTS\_GROUP\_UPDATESends group update events (true or false)falseRABBITMQ\_EVENTS\_GROUP\_PARTICIPANTS\_UPDATESends group participant update events (true or false)falseRABBITMQ\_EVENTS\_CONNECTION\_UPDATESends connection update events (true or false)falseRABBITMQ\_EVENTS\_CALLSends call events (true or false)falseRABBITMQ\_EVENTS\_TYPEBOT\_STARTSends Typebot flow start events (true or false)falseRABBITMQ\_EVENTS\_TYPEBOT\_CHANGE\_STATUSSends Typebot status update events (true or false)false

## SQS

VariableValueExampleSQS\_ENABLEDWhether SQS is enabled (true or false)falseSQS\_ACCESS\_KEY\_IDSQS key ID-SQS\_SECRET\_ACCESS\_KEYAccess key-SQS\_ACCOUNT\_IDAccount ID-SQS\_REGIONSQS region-

## WebSocket

VariableValueExampleWEBSOCKET\_ENABLEDEnables WebSocket (true or false)falseWEBSOCKET\_GLOBAL\_EVENTSEnables global events in WebSocket (true or false)false

## WhatsApp Business API

VariableValueExampleWA\_BUSINESS\_TOKEN\_WEBHOOKToken used to validate the webhook in the Facebook APPevolutionWA\_BUSINESS\_URLWhatsApp Business API URL[https://graph.facebook.com](https://graph.facebook.com)WA\_BUSINESS\_VERSIONWhatsApp Business API versionv20.0WA\_BUSINESS\_LANGUAGEWhatsApp Business API languageen\_US

## Global Webhook

VariableValueExampleWEBHOOK\_GLOBAL\_ENABLEDWhether webhooks are globally enabled (true or false)falseWEBHOOK\_GLOBAL\_URLURL that will receive webhook requests[https://webhook.example.com](https://webhook.example.com)WEBHOOK\_GLOBAL\_WEBHOOK\_BY\_EVENTSEnables webhook by event, respecting the global URL and each event’s name (true or false)false

### Webhook events with true or false value

VariableWEBHOOK\_EVENTS\_APPLICATION\_STARTUPWEBHOOK\_EVENTS\_QRCODE\_UPDATEDWEBHOOK\_EVENTS\_MESSAGES\_SETWEBHOOK\_EVENTS\_MESSAGES\_UPSERTWEBHOOK\_EVENTS\_MESSAGES\_EDITEDWEBHOOK\_EVENTS\_MESSAGES\_UPDATEWEBHOOK\_EVENTS\_MESSAGES\_DELETEWEBHOOK\_EVENTS\_SEND\_MESSAGEWEBHOOK\_EVENTS\_CONTACTS\_SETWEBHOOK\_EVENTS\_CONTACTS\_UPSERTWEBHOOK\_EVENTS\_CONTACTS\_UPDATEWEBHOOK\_EVENTS\_PRESENCE\_UPDATEWEBHOOK\_EVENTS\_CHATS\_SETWEBHOOK\_EVENTS\_CHATS\_UPSERTWEBHOOK\_EVENTS\_CHATS\_UPDATEWEBHOOK\_EVENTS\_CHATS\_DELETEWEBHOOK\_EVENTS\_GROUPS\_UPSERTWEBHOOK\_EVENTS\_GROUPS\_UPDATEWEBHOOK\_EVENTS\_GROUP\_PARTICIPANTS\_UPDATEWEBHOOK\_EVENTS\_CONNECTION\_UPDATEWEBHOOK\_EVENTS\_LABELS\_EDITWEBHOOK\_EVENTS\_LABELS\_ASSOCIATIONWEBHOOK\_EVENTS\_CALLWEBHOOK\_EVENTS\_TYPEBOT\_STARTWEBHOOK\_EVENTS\_TYPEBOT\_CHANGE\_STATUSWEBHOOK\_EVENTS\_ERRORSWEBHOOK\_EVENTS\_ERRORS\_WEBHOOK

## Session Configurations

VariableValueExampleCONFIG\_SESSION\_PHONE\_CLIENTName that will be displayed on the smartphone connectionEvolution APICONFIG\_SESSION\_PHONE\_NAMEBrowser name (Chrome, Firefox, Edge, Opera, Safari)Chrome

## QR Code

VariableValueExampleQRCODE\_LIMITHow long the QR code will last30QRCODE\_COLORColor of the generated QR code#175197

## Typebot

VariableValueExampleTYPEBOT\_API\_VERSIONAPI version (fixed

version or latest) | latest |

## Chatwoot

VariableValueExampleCHATWOOT\_ENABLEDEnables integration with Chatwoot (true or false)falseCHATWOOT\_MESSAGE\_READMarks the client’s last WhatsApp message as read when sending a message in Chatwoot (true or false)trueCHATWOOT\_MESSAGE\_DELETEDeletes the message in Chatwoot when deleted in WhatsApp (true or false)trueCHATWOOT\_IMPORT\_DATABASE\_CONNECTION\_URIDatabase connection URI for Chatwoot to import messagespostgresql://user:password@host:5432/chatwoot?sslmode=disableCHATWOOT\_IMPORT\_PLACEHOLDER\_MEDIA\_MESSAGEImports media messages as a placeholder in Chatwoot (true or false)true

## OpenAI

VariableValueExampleOPENAI\_ENABLEDEnables integration with OpenAI (true or false)false

## Dify

VariableValueExampleDIFY\_ENABLEDEnables integration with Dify (true or false)false

## Cache

VariableValueExampleCACHE\_REDIS\_ENABLEDEnables Redis cache (true or false)trueCACHE\_REDIS\_URIRedis connection URIredis://localhost:6379/6CACHE\_REDIS\_PREFIX\_KEYPrefix to differentiate data from one installation to another using the same RedisevolutionCACHE\_REDIS\_SAVE\_INSTANCESSaves WhatsApp connection credentials in Redis (true or false)falseCACHE\_LOCAL\_ENABLEDEnables local in-memory cache as an alternative to Redis (true or false)false

## Amazon S3 / MinIO

VariableValueExampleS3\_ENABLEDEnables storage on S3 (true or false)falseS3\_ACCESS\_KEYS3 access key-S3\_SECRET\_KEYS3 secret key-S3\_BUCKETS3 bucket nameevolutionS3\_PORTS3 connection port443S3\_ENDPOINTS3 (or MinIO) endpoints3.amazonaws.comS3\_USE\_SSLUses SSL for S3 connection (true or false)true

## Authentication

VariableValueExampleAUTHENTICATION\_API\_KEYAPI key used for global authentication429683C4C977415CAAFCCE10F7D57E11AUTHENTICATION\_EXPOSE\_IN\_FETCH\_INSTANCESShows instances in the fetch endpoint (true or false)true

## Language

VariableValueExampleLANGUAGEAPI languageen