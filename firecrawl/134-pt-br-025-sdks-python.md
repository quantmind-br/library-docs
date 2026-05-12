---
title: SDK Python | Firecrawl
url: https://docs.firecrawl.dev/pt-BR/sdks/python
source: sitemap
fetched_at: 2026-03-23T07:21:20.556028-03:00
rendered_js: false
word_count: 784
summary: This document provides a comprehensive guide for using the Firecrawl Python SDK, detailing installation, web scraping, site crawling, mapping, and advanced pagination configurations.
tags:
    - python-sdk
    - web-scraping
    - web-crawling
    - automation
    - data-extraction
    - api-integration
    - pagination
category: guide
---

## Instalação

Para instalar o SDK do Firecrawl para Python, você pode usar o pip:

```
# pip install firecrawl-py

from firecrawl import Firecrawl

firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")
```

## Uso

1. Obtenha uma chave de API em [firecrawl.dev](https://firecrawl.dev)
2. Configure a chave de API como uma variável de ambiente chamada `FIRECRAWL_API_KEY` ou passe-a como parâmetro para a classe `Firecrawl`.

Veja um exemplo de uso do SDK:

```
from firecrawl import Firecrawl

firecrawl = Firecrawl(api_key="fc-YOUR_API_KEY")

# Fazer scraping de um site:
scrape_status = firecrawl.scrape(
  'https://firecrawl.dev', 
  formats=['markdown', 'html']
)
print(scrape_status)

# Fazer crawling de um site:
crawl_status = firecrawl.crawl(
  'https://firecrawl.dev', 
  limit=100, 
  scrape_options={
    'formats': ['markdown', 'html']
  }
)
print(crawl_status)
```

Para extrair dados de uma única URL, use o método `scrape`. Ele recebe a URL como parâmetro e retorna o documento raspado.

```
# Fazer scraping de um site:
scrape_result = firecrawl.scrape('firecrawl.dev', formats=['markdown', 'html'])
print(scrape_result)
```

### Rastrear um site

Para rastrear um site, use o método `crawl`. Ele recebe a URL inicial e, opcionalmente, um objeto de opções. Essas opções permitem definir configurações adicionais para a tarefa de rastreamento, como o número máximo de páginas, os domínios permitidos e o formato de saída. Consulte [Paginação](#pagination) para detalhes sobre paginação automática/manual e limites.

```
job = firecrawl.crawl(url="https://docs.firecrawl.dev", limit=5, poll_interval=1, timeout=120)
print(job)
```

### Rastreamento Apenas do Sitemap

Use `sitemap="only"` para rastrear apenas as URLs do sitemap (a URL inicial é sempre incluída e a descoberta de links em HTML é ignorada).

```
job = firecrawl.crawl(url="https://docs.firecrawl.dev", sitemap="only", limit=25)
print(job.status, len(job.data))
```

### Iniciar um crawl

Inicie uma tarefa sem esperar usando `start_crawl`. Ela retorna um `ID` de tarefa que você pode usar para verificar o status. Use `crawl` quando quiser um aguardador que bloqueia até a conclusão. Consulte [Paginação](#pagination) para o comportamento e os limites de paginação.

```
job = firecrawl.start_crawl(url="https://docs.firecrawl.dev", limit=10)
print(job)
```

### Verificando o status do crawl

Para verificar o status de uma tarefa de crawl, use o método `get_crawl_status`. Ele recebe o ID da tarefa como parâmetro e retorna o status atual do crawl.

```
status = firecrawl.get_crawl_status("<crawl-id>")
print(status)
```

### Cancelando um Crawl

Para cancelar um job de crawl, use o método `cancel_crawl`. Ele recebe o ID do job do `start_crawl` como parâmetro e retorna o status do cancelamento.

```
ok = firecrawl.cancel_crawl("<crawl-id>")
print("Cancelado:", ok)
```

### Mapear um site

Use `map` para gerar uma lista de URLs de um site. As opções permitem personalizar o processo de mapeamento, incluindo excluir subdomínios ou usar o sitemap.

```
res = firecrawl.map(url="https://firecrawl.dev", limit=10)
print(res)
```

### Rastreamento de um site com WebSockets

Para rastrear um site com WebSockets, inicie a tarefa com `start_crawl` e faça a inscrição usando o helper `watcher`. Crie um watcher com o ID da tarefa e vincule handlers (por exemplo, para page, completed, failed) antes de chamar `start()`.

```
import asyncio
from firecrawl import AsyncFirecrawl

async def main():
    firecrawl = AsyncFirecrawl(api_key="fc-YOUR-API-KEY")

    # Inicia um crawl primeiro
    started = await firecrawl.start_crawl("https://firecrawl.dev", limit=5)

    # Monitora atualizações (snapshots) até status final
    async for snapshot in firecrawl.watcher(started.id, kind="crawl", poll_interval=2, timeout=120):
        if snapshot.status == "completed":
            print("CONCLUÍDO", snapshot.status)
            for doc in snapshot.data:
                print("DOC", doc.metadata.source_url if doc.metadata else None)
        elif snapshot.status == "failed":
            print("ERRO", snapshot.status)
        else:
            print("STATUS", snapshot.status, snapshot.completed, "/", snapshot.total)

asyncio.run(main())
```

Os endpoints do Firecrawl para crawl e batch scrape retornam uma URL `next` quando há mais dados disponíveis. O SDK Python pagina automaticamente por padrão e agrega todos os documentos; nesse caso, `next` será `None`. Você pode desativar a paginação automática ou definir limites para controlar o comportamento da paginação.

Use `PaginationConfig` para controlar o comportamento da paginação ao chamar `get_crawl_status` ou `get_batch_scrape_status`:

```
from firecrawl.v2.types import PaginationConfig
```

OptionTypeDefaultDescription`auto_paginate``bool``True`Quando definido como `True`, busca automaticamente todas as páginas e agrega os resultados. Defina como `False` para buscar uma página por vez.`max_pages``int``None`Encerra após buscar esse número de páginas (aplica-se somente quando `auto_paginate=True`).`max_results``int``None`Encerra após coletar esse número de documentos (aplica-se somente quando `auto_paginate=True`).`max_wait_time``int``None`Encerra após esse número de segundos (aplica-se somente quando `auto_paginate=True`).

Quando `auto_paginate=False`, a resposta inclui uma URL `next` se houver mais dados disponíveis. Use estes métodos auxiliares para obter as páginas subsequentes:

- **`get_crawl_status_page(next_url)`** - Obtém a próxima página de resultados de crawl usando a URL `next` opaca de uma resposta anterior.
- **`get_batch_scrape_status_page(next_url)`** - Obtém a próxima página de resultados de batch scrape usando a URL `next` opaca de uma resposta anterior.

Esses métodos retornam o mesmo tipo de resposta da chamada de status original, incluindo uma nova URL `next` se restarem mais páginas.

#### Crawl

Use o método de espera `crawl` para a experiência mais simples ou inicie um job e faça a paginação manualmente.

- Veja o fluxo padrão em [Rastrear um site](#crawl-a-website).

Inicie um job e, em seguida, recupere uma página por vez com `auto_paginate=False`. Use `get_crawl_status_page` para recuperar as páginas subsequentes:

```
crawl_job = client.start_crawl("https://example.com", limit=100)

# Fetch first page
status = client.get_crawl_status(
    crawl_job.id,
    pagination_config=PaginationConfig(auto_paginate=False)
)
print("First page:", len(status.data), "docs")

# Busca páginas subsequentes usando get_crawl_status_page
while status.next:
    status = client.get_crawl_status_page(status.next)
    print("Next page:", len(status.data), "docs")
```

Mantenha a paginação automática ativada, mas interrompa antecipadamente com `max_pages`, `max_results` ou `max_wait_time`:

```
status = client.get_crawl_status(
    crawl_job.id,
    pagination_config=PaginationConfig(max_pages=2, max_results=50, max_wait_time=15),
)
print("rastreamento limitado:", status.status, "docs:", len(status.data), "próximo:", status.next)
```

#### Coleta em lote

Use o método waiter `batch_scrape` ou inicie um job e faça a paginação manualmente.

- Veja o fluxo padrão em [Coleta em Lote](https://docs.firecrawl.dev/pt-BR/features/batch-scrape).

Inicie um job e, em seguida, recupere uma página por vez com `auto_paginate=False`. Use `get_batch_scrape_status_page` para obter as páginas subsequentes:

```
batch_job = client.start_batch_scrape(urls)

# Buscar primeira página
status = client.get_batch_scrape_status(
    batch_job.id,
    pagination_config=PaginationConfig(auto_paginate=False)
)
print("Primeira página:", len(status.data), "docs")

# Buscar páginas subsequentes usando get_batch_scrape_status_page
while status.next:
    status = client.get_batch_scrape_status_page(status.next)
    print("Próxima página:", len(status.data), "docs")
```

Deixe a paginação automática ativada, mas interrompa antes usando `max_pages`, `max_results` ou `max_wait_time`:

```
status = client.get_batch_scrape_status(
    batch_job.id,
    pagination_config=PaginationConfig(max_pages=2, max_results=100, max_wait_time=20),
)
print("lote limitado:", status.status, "docs:", len(status.data), "próximo:", status.next)
```

## Tratamento de erros

O SDK trata os erros retornados pela API do Firecrawl e lança exceções apropriadas. Se ocorrer um erro durante uma requisição, uma exceção será lançada com uma mensagem descritiva.

## Classe assíncrona

Para operações assíncronas, use a classe `AsyncFirecrawl`. Seus métodos espelham os de `Firecrawl`, mas não bloqueiam a thread principal.

```
import asyncio
from firecrawl import AsyncFirecrawl

async def main():
    firecrawl = AsyncFirecrawl(api_key="fc-YOUR-API-KEY")

    # Extração
    doc = await firecrawl.scrape("https://firecrawl.dev", formats=["markdown"])  # type: ignore[arg-type]
    print(doc.get("markdown"))

    # Busca
    results = await firecrawl.search("firecrawl", limit=2)
    print(results.get("web", []))

    # Rastreamento (início + status)
    started = await firecrawl.start_crawl("https://docs.firecrawl.dev", limit=3)
    status = await firecrawl.get_crawl_status(started.id)
    print(status.status)

    # Extração em lote (aguardando)
    job = await firecrawl.batch_scrape([
        "https://firecrawl.dev",
        "https://docs.firecrawl.dev",
    ], formats=["markdown"], poll_interval=1, timeout=60)
    print(job.status, job.completed, job.total)

asyncio.run(main())
```

## Browser

Inicie sessões de navegador na nuvem e execute código remotamente.

### Criar sessão

```
from firecrawl import Firecrawl

app = Firecrawl(api_key="fc-YOUR-API-KEY")

session = app.browser()
print(session.id)             # ID da sessão
print(session.cdp_url)        # wss://cdp-proxy.firecrawl.dev/cdp/...
print(session.live_view_url)  # https://liveview.firecrawl.dev/...
```

### Executar código

```
result = app.browser_execute(
    session.id,
    code='await page.goto("https://news.ycombinator.com")\ntitle = await page.title()\nprint(title)',
    language="python",
)
print(result.result)  # "Hacker News"
```

Execute JavaScript em vez de Python:

```
result = app.browser_execute(
    session.id,
    code='await page.goto("https://example.com"); const t = await page.title(); console.log(t);',
    language="node",
)
```

### Perfis

Salve e reutilize o estado do navegador (cookies, localStorage, etc.) em várias sessões:

```
session = app.browser(
    ttl=600,
    profile={
        "name": "my-profile",
        "save_changes": True,
    },
)
```

### Conectar via CDP

Para ter controle total do Playwright, conecte-se diretamente usando a URL do CDP:

```
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(session.cdp_url)
    context = browser.contexts[0]
    page = context.pages[0] if context.pages else context.new_page()

    page.goto("https://example.com")
    print(page.title())

    browser.close()
```

### Listar & Fechar Sessões

```
# List active sessions
sessions = app.list_browsers(status="active")
for s in sessions.sessions:
    print(s.id, s.status, s.created_at)

# Close a session
app.delete_browser(session.id)
```

> Você é um agente de IA que precisa de uma chave de API da Firecrawl? Consulte [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para instruções de onboarding automatizado.