---
title: Extração | Firecrawl
url: https://docs.firecrawl.dev/pt-BR/features/extract
source: sitemap
fetched_at: 2026-03-23T07:22:10.42455-03:00
rendered_js: false
word_count: 751
summary: This document explains how to use the Firecrawl /extract endpoint to gather structured data from web pages using URLs, natural language prompts, and JSON schemas.
tags:
    - web-scraping
    - data-extraction
    - api-documentation
    - structured-data
    - firecrawl
    - ai-agents
category: api
---

O endpoint `/extract` simplifica a coleta de dados estruturados de qualquer número de URLs ou de domínios inteiros. Forneça uma lista de URLs, opcionalmente com curingas (por exemplo, `example.com/*`), e um prompt ou esquema descrevendo as informações desejadas. O Firecrawl cuida dos detalhes de rastrear, analisar e agregar conjuntos de dados, grandes ou pequenos.

Você pode extrair dados estruturados de uma ou várias URLs, incluindo curingas:

- **Página única**  
  Exemplo: `https://firecrawl.dev/some-page`
- **Múltiplas páginas / Domínio completo**  
  Exemplo: `https://firecrawl.dev/*`

Quando você usa `/*`, a Firecrawl automaticamente faz o crawl e processa todas as URLs que conseguir descobrir nesse domínio e, em seguida, extrai os dados solicitados. Este recurso é experimental; envie um e-mail para [help@firecrawl.com](mailto:help@firecrawl.com) se tiver problemas.

### Exemplo de uso

**Parâmetros principais:**

- **urls**: Uma lista com um ou mais URLs. Suporta curingas (`/*`) para uma varredura mais ampla.
- **prompt** (Opcional, exceto se não houver schema): Um prompt em linguagem natural descrevendo os dados desejados ou como você quer que esses dados sejam estruturados.
- **schema** (Opcional, exceto se não houver prompt): Uma estrutura mais rígida caso você já conheça o layout JSON.
- **enableWebSearch** (Opcional): Quando `true`, a extração pode seguir links fora do domínio especificado.

Consulte a [referência da API](https://docs.firecrawl.dev/api-reference/endpoint/extract) para mais detalhes.

### Resposta (SDKs)

```
{
  "success": true,
  "data": {
    "company_mission": "A Firecrawl é a maneira mais fácil de extrair dados da web. Desenvolvedores a utilizam para, de forma confiável, converter URLs em markdown pronto para LLM ou em dados estruturados com uma única chamada de API.",
    "supports_sso": false,
    "is_open_source": true,
    "is_in_yc": true
  }
}
```

## Status do job e conclusão

Ao enviar um job de extração—diretamente via API ou pelos métodos iniciais—você receberá um ID de job. Você pode usar esse ID para:

- Obter o status do job: Envie uma solicitação para o endpoint /extract/ para ver se o job ainda está em execução ou se foi concluído.
- Aguardar resultados: Se você usar o método padrão `extract` (Python/Node), o SDK aguarda e retorna os resultados finais.
- Iniciar e depois consultar: Se você usar os métodos de início—`start_extract` (Python) ou `startExtract` (Node)—o SDK retorna um ID de job imediatamente. Use `get_extract_status` (Python) ou `getExtractStatus` (Node) para verificar o progresso.

Abaixo estão exemplos de código para verificar o status de um job de extração usando Python, Node.js e cURL:

### Estados possíveis

- **completed**: A extração foi concluída com sucesso.
- **processing**: O Firecrawl ainda está processando sua solicitação.
- **failed**: Ocorreu um erro; os dados não foram totalmente extraídos.
- **cancelled**: A tarefa foi cancelada pelo usuário.

#### Exemplo pendente

```
{
  "success": true,
  "data": [],
  "status": "em processamento",
  "expiresAt": "2025-01-08T20:58:12.000Z"
}
```

#### Exemplo concluído

```
{
  "success": true,
  "data": {
      "company_mission": "A Firecrawl é a maneira mais simples de extrair dados da web. Desenvolvedores a utilizam para converter URLs, com confiabilidade, em markdown pronto para LLM ou dados estruturados com uma única chamada à API.",
      "supports_sso": false,
      "is_open_source": true,
      "is_in_yc": true
    },
  "status": "concluído",
  "expiresAt": "2025-01-08T20:58:12.000Z"
}
```

Se você preferir não definir uma estrutura rígida, pode simplesmente fornecer um `prompt`. O modelo subjacente escolherá uma estrutura para você, o que pode ser útil para solicitações mais exploratórias ou flexíveis.

```
{
  "success": true,
  "data": {
    "company_mission": "Transforme sites em dados prontos para LLMs. Impulsione seus apps de IA com dados limpos coletados de qualquer site."
  }
}
```

Definir `enableWebSearch = true` na sua requisição expandirá o crawl além do conjunto de URLs fornecido. Isso pode capturar informações de suporte ou relacionadas a partir de páginas linkadas. Veja um exemplo que extrai informações sobre dash cams, enriquecendo os resultados com dados de páginas relacionadas:

### Exemplo de resposta com pesquisa na web

```
{
  "success": true,
  "data": {
    "dash_cams": [
      {
        "name": "Nextbase 622GW",
        "price": "$399.99",
        "features": [
          "Gravação de vídeo em 4K",
          "Estabilização de imagem",
          "Alexa integrada",
          "Integração com What3Words"
        ],
        /* Informações abaixo enriquecidas com outros sites, como 
        https://www.techradar.com/best/best-dash-cam, encontradas 
        via o parâmetro enableWebSearch */
        "pros": [
          "Excelente qualidade de vídeo",
          "Ótima visão noturna",
          "GPS integrado"
        ],
        "cons": ["Preço elevado", "O app pode ser instável"]
      }
    ],
  }

```

A resposta inclui contexto adicional obtido de páginas relacionadas, oferecendo informações mais completas e precisas.

O endpoint /extract agora permite extrair dados estruturados usando um prompt, sem a necessidade de URLs específicas. Isso é útil para pesquisa ou quando as URLs exatas são desconhecidas. Atualmente em alpha.

## Limitações Conhecidas (Beta)

1. **Cobertura de Sites em Grande Escala**  
   A cobertura completa de sites muito grandes (por exemplo, “todos os produtos da Amazon”) em uma única requisição ainda não é suportada.
2. **Consultas Lógicas Complexas**  
   Pedidos como “encontrar todas as postagens de 2025” podem não retornar de forma confiável todos os dados esperados. Capacidades de consulta mais avançadas estão em desenvolvimento.
3. **Inconsistências Ocasionais**  
   Os resultados podem variar entre execuções, especialmente em sites muito grandes ou dinâmicos. Geralmente os detalhes essenciais são capturados, mas alguma variação é possível.
4. **Estado Beta**  
   Como o endpoint `/extract` ainda está em Beta, recursos e desempenho continuarão evoluindo. Agradecemos relatos de bugs e feedback para nos ajudar a melhorar.

## Usando o FIRE-1

O FIRE-1 é um agente de IA que amplia as capacidades de scraping do Firecrawl. Ele pode controlar ações do navegador e navegar por estruturas complexas de sites para viabilizar a extração de dados além do scraping tradicional. Você pode usar o agente FIRE-1 com o endpoint `/extract` para tarefas de extração complexas que exigem navegar por várias páginas ou interagir com elementos. **Exemplo (cURL):**

```
curl -X POST https://api.firecrawl.dev/v2/extract \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer SUA_CHAVE_DE_API' \
    -d '{
      "urls": ["https://example-forum.com/topic/123"],
      "prompt": "Extraia todos os comentários de usuários deste tópico do fórum.",
      "schema": {
        "type": "object",
        "properties": {
          "comments": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "author": {"type": "string"},
                "comment_text": {"type": "string"}
              },
              "required": ["author", "comment_text"]
            }
          }
        },
        "required": ["comments"]
      },
      "agent": {
        "model": "FIRE-1"
      }
    }'
```

> O FIRE-1 já está disponível e em versão de prévia.

## Cobrança e acompanhamento de uso

Simplificamos a cobrança: o Extract agora usa créditos, assim como os demais endpoints. Cada crédito equivale a 15 tokens. Você pode acompanhar o uso do Extract pelo [dashboard](https://www.firecrawl.dev/app/extract). Tem alguma sugestão ou precisa de ajuda? Envie um e-mail para [help@firecrawl.com](mailto:help@firecrawl.com).

> Você é um agente de IA que precisa de uma API key da Firecrawl? Consulte [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para instruções automatizadas de onboarding.