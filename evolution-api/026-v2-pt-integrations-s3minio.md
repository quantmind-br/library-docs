---
title: S3/Minio - Evolution API Documentation
url: https://doc.evolution-api.com/v2/pt/integrations/s3minio
source: sitemap
fetched_at: 2026-04-12T18:45:39.040671385-03:00
rendered_js: false
word_count: 405
summary: This document provides a comprehensive guide on integrating the Evolution API with Amazon S3 or Minio for secure media storage of WhatsApp files like images and audio. It details the necessary environment variables, their functions, and how the resulting file URLs are provided in webhooks.
tags:
    - s3-integration
    - minio-storage
    - environment-variables
    - whatsapp-media
    - webhook-setup
category: guide
---

A Evolution API suporta a integração com Amazon S3 ou Minio para armazenar arquivos de mídia do WhatsApp, como imagens, áudios e documentos. Essa integração permite que os arquivos sejam armazenados de forma segura e acessível, com links gerados automaticamente e incluídos nos webhooks enviados pela API.

## Configuração de Variáveis de Ambiente

Para habilitar o armazenamento S3 ou Minio, você deve definir as variáveis de ambiente adequadas no arquivo `.env` da Evolution API. Abaixo estão as variáveis necessárias e suas funções:

### Variáveis de Configuração para S3

```
S3_ENABLED=true
S3_ACCESS_KEY=lJiKQSKlco6UfSUJSnZt
S3_SECRET_KEY=gZXkzkXQwhME8XEmZVNF0ImSWxIpbXeJ5UoPy4s1
S3_BUCKET=evolution
S3_PORT=443
S3_ENDPOINT=s3.eu-west-3.amazonaws.com
S3_USE_SSL=true
S3_REGION=eu-west-3
```

### Explicação das Variáveis

- **`S3_ENABLED`** : Ativa (`true`) ou desativa (`false`) o uso do S3 ou Minio para armazenamento de arquivos.
- **`S3_ACCESS_KEY`** : Chave de acesso fornecida pelo provedor do serviço (AWS ou Minio).
- **`S3_SECRET_KEY`** : Chave secreta correspondente à chave de acesso, usada para autenticação.
- **`S3_BUCKET`** : Nome do bucket onde os arquivos serão armazenados.
- **`S3_PORT`** : Porta utilizada para a conexão. Normalmente `443` para conexões SSL.
- **`S3_ENDPOINT`** : Endpoint do serviço S3 ou Minio. Para Amazon S3, é necessário incluir a região no formato `region: s3.[region].amazonaws.com`, por exemplo, `s3.eu-west-3.amazonaws.com`.
- **`S3_USE_SSL`** : Define se a conexão deve usar SSL (`true` ou `false`).
- **`S3_REGION`** : A região do bucket S3 (padrão é `us-east-1`).

### Exemplos de Configuração

#### Amazon S3

Ao utilizar o Amazon S3, é essencial especificar o endpoint corretamente, incluindo a região. Aqui está um exemplo:

```
S3_ENABLED=true
S3_ACCESS_KEY=your-aws-access-key
S3_SECRET_KEY=your-aws-secret-key
S3_BUCKET=my-s3-bucket
S3_PORT=443
S3_ENDPOINT=s3.eu-west-3.amazonaws.com
S3_USE_SSL=true
S3_REGION=eu-west-3
```

#### Minio

Para Minio, o endpoint pode ser o domínio personalizado do serviço:

```
S3_ENABLED=true
S3_ACCESS_KEY=your-minio-access-key
S3_SECRET_KEY=your-minio-secret-key
S3_BUCKET=my-minio-bucket
S3_PORT=443
S3_ENDPOINT=minio.mycompany.com
S3_USE_SSL=true
```

## Como Funciona o Armazenamento de Mídia

Quando o armazenamento S3 ou Minio é configurado corretamente, todos os arquivos de mídia recebidos do WhatsApp (como imagens, vídeos, áudios, etc.) são automaticamente enviados para o bucket configurado. A URL pública do arquivo armazenado é então gerada e incluída no webhook da Evolution API.

### Webhook com `mediaUrl`

Quando um arquivo de mídia é recebido e armazenado, o webhook enviado pela Evolution API incluirá o `mediaUrl` no corpo da mensagem. Isso permite que sua aplicação acesse diretamente o arquivo armazenado no S3 ou Minio.

### Exemplo de Webhook

Aqui está um exemplo de como o webhook com `mediaUrl` pode aparecer:

```
{
    "event": "messages.upsert",
    "data": {
        "message": {
            ...
            "mediaUrl": "https://files.evolution-api-pro.com/bucket/path/to/media/file.jpg",
            ...
        }
    }
}
```

## Considerações Finais

Integrar a Evolution API com Amazon S3 ou Minio para o armazenamento de arquivos de mídia oferece uma solução escalável e segura para gerenciar conteúdos de mídia do WhatsApp. Ao configurar as variáveis de ambiente corretamente, você garante que todos os arquivos de mídia sejam armazenados e acessíveis conforme necessário, proporcionando maior controle sobre os dados e a capacidade de integrá-los facilmente em suas aplicações.