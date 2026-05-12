---
title: Cobrança | Firecrawl
url: https://docs.firecrawl.dev/pt-BR/billing
source: sitemap
fetched_at: 2026-03-23T07:26:53.581999-03:00
rendered_js: false
word_count: 1326
summary: This document explains the Firecrawl billing system, covering credit consumption per API endpoint, subscription plans, automatic top-up mechanisms, and coupon management.
tags:
    - billing-system
    - api-usage
    - credit-management
    - subscription-plans
    - firecrawl
    - account-limits
category: reference
---

## Visão geral

Firecrawl utiliza um **sistema de faturamento baseado em créditos**. Cada chamada de API que você faz consome créditos, e a quantidade de créditos consumidos depende do endpoint e das opções que você utiliza. Você recebe uma cota mensal de créditos com base no seu plano e pode comprar créditos adicionais por meio de pacotes de recarga automática, caso precise de mais. Para ver os preços atuais dos planos, visite a [página de preços do Firecrawl](https://www.firecrawl.dev/pricing).

## Créditos

Créditos são a unidade de consumo no Firecrawl. Cada plano inclui uma cota mensal de créditos que é renovada no início de cada ciclo de cobrança. Diferentes endpoints da API consomem quantidades diferentes de créditos.

### Custos de crédito por endpoint

EndpointCusto de créditoObservações**Scrape**1 crédito / páginaConverte uma única URL em markdown limpo, HTML ou dados estruturados. Créditos adicionais se aplicam ao usar opções de scraping (consulte abaixo).**Crawl**1 crédito / páginaFaz o scraping de um site inteiro seguindo links a partir de uma URL inicial. Os mesmos custos das opções de scraping por página se aplicam a cada página rastreada.**Map**1 crédito / chamadaDescobre todas as URLs em um site sem fazer scraping do conteúdo.**Search**2 créditos / 10 resultadosFaz uma busca na web e, opcionalmente, realiza o scraping dos resultados. Custos adicionais de scraping por página se aplicam a cada resultado que for raspado. A busca ZDR Enterprise custa 10 créditos / 10 resultados (consulte [ZDR Search](https://docs.firecrawl.dev/pt-BR/features/search#zero-data-retention-zdr)).**Browser**2 créditos / minuto de navegadorSessão interativa de sandbox de navegador, cobrada por minuto.**Agent**DinâmicoAgente autônomo de pesquisa na web. 5 execuções diárias gratuitas; cobrança baseada em uso após isso.

### Custos adicionais de crédito para opções de scraping

Certas opções de scraping adicionam créditos além do custo base por página:

OpçãoCusto adicionalDescriçãoPDF parsing+1 crédito / página de PDFExtrair conteúdo de documentos PDFJSON format (LLM extraction)+4 créditos / páginaUsar um LLM para extrair dados JSON estruturados da páginaEnhanced Mode+4 créditos / páginaScraping aprimorado para páginas que são difíceis de acessarZero Data Retention (ZDR)+1 crédito / páginaGarante que nenhum dado seja persistido além da requisição (veja [Scrape ZDR](https://docs.firecrawl.dev/pt-BR/features/scrape#zero-data-retention-zdr))

Esses modificadores se acumulam. Por exemplo, fazer scraping de uma página com JSON format e Enhanced Mode custa **1 + 4 + 4 = 9 créditos** por página. Esses mesmos modificadores se aplicam aos endpoints Crawl e Search, já que eles usam scraping internamente para cada página.

### Quando os créditos são debitados

Para jobs de **batch scrape** e **crawl**, os créditos são debitados de forma assíncrona à medida que cada página conclui o processamento — não quando o job é submetido. Isso significa que pode haver um atraso entre a submissão de um job e ver o custo total de créditos refletido na sua conta. Se um batch contiver muitas URLs ou se as páginas forem enfileiradas durante períodos de alto tráfego, os créditos podem continuar aparecendo minutos ou horas após a submissão. Realizar polling ou verificar o status do batch não consome créditos.

### Monitorando seu uso

Você pode acompanhar o uso de créditos de duas maneiras:

- **Dashboard**: Veja seu uso atual e histórico em [firecrawl.dev/app](https://www.firecrawl.dev/app)
- **API**: Use os endpoints [Credit Usage](https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/credit-usage) e [Credit Usage Historical](https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/credit-usage-historical) para verificar seu uso programaticamente

## Planos

Firecrawl oferece planos mensais por assinatura. Não há uma opção pura de pague‑conforme‑o‑uso (pay-as-you-go), mas a recarga automática (descrita abaixo) oferece escalabilidade flexível adicional ao seu plano base.

### Planos disponíveis

PlanoCréditos mensaisNavegadores simultâneos**Free**500 (créditos únicos)2**Hobby**3,0005**Standard**100,00050**Growth**500,000100

Todos os planos pagos estão disponíveis com cobrança **mensal** ou **anual**. A cobrança anual oferece um desconto em comparação ao pagamento mês a mês. Para preços atualizados de cada plano, visite a [página de preços](https://www.firecrawl.dev/pricing).

### Navegadores simultâneos

Navegadores simultâneos representam quantas páginas da web o Firecrawl pode processar para você ao mesmo tempo. Seu plano determina esse limite. Se você o exceder, tarefas adicionais ficam em uma fila de espera até que uma vaga seja liberada. Consulte [Limites de Taxa](https://docs.firecrawl.dev/pt-BR/rate-limits) para ver todos os detalhes sobre concorrência e limites de taxa da API.

## Recarga automática

Se você ocasionalmente precisar de mais créditos do que o seu plano inclui, pode ativar a **recarga automática** no dashboard. Quando seus créditos restantes caírem abaixo de um limite configurável, Firecrawl compra automaticamente um pacote adicional de créditos e o adiciona ao seu saldo.

- Pacotes de recarga automática estão disponíveis em todos os planos pagos
- Os tamanhos dos pacotes e os preços variam conforme o plano (visíveis na [página de preços](https://www.firecrawl.dev/pricing))
- Você pode configurar o limite de recarga e ativar ou desativar a recarga automática a qualquer momento
- A recarga automática é limitada a **4 pacotes por mês**
- Os créditos dos pacotes de recarga automática **não são restaurados mensalmente** — eles permanecem na sua conta entre ciclos de cobrança e expiram **1 ano** após a compra, ao contrário dos créditos mensais do seu plano, que são restaurados a cada período.

A recarga automática é ideal para lidar com picos pontuais de uso. Se você perceber que está excedendo de forma consistente a cota do seu plano, fazer upgrade para um plano superior oferecerá um melhor custo-benefício por crédito.

## Cupons

A Firecrawl oferece dois tipos de cupons:

- **Cupons de assinatura** aplicam um desconto à assinatura do seu plano (por exemplo, uma porcentagem de desconto no valor mensal ou anual). Eles **só** podem ser aplicados durante o fluxo de checkout do Stripe, quando você assina um plano pago pela primeira vez ou muda de plano. Não é possível aplicar um cupom de assinatura depois que o checkout for concluído.
- **Cupons de crédito** adicionam créditos bônus à sua conta. Eles podem ser resgatados na seção **cobrança** do seu dashboard em [firecrawl.dev/app/billing](https://www.firecrawl.dev/app/billing). Procure o campo de cupom na página de cobrança para aplicar seu código. Os créditos bônus de cupons de crédito são separados da cota mensal do seu plano e permanecem mesmo se você fizer upgrade ou downgrade do seu plano.

Se você tiver um código de cupom e não souber de que tipo ele é, tente aplicá-lo primeiro na seção de cobrança do seu dashboard. Se for um cupom de assinatura, você precisará usá-lo na página de checkout do Stripe.

## Ciclo de cobrança

- **Planos mensais**: Os créditos são restaurados na sua data de renovação mensal
- **Planos anuais**: A cobrança é anual, mas os créditos ainda são restaurados todo mês na sua data de renovação mensal virtual
- **Créditos do plano não utilizados não são acumulados** — sua cota mensal é restaurada para o valor do plano no início de cada período de cobrança. Créditos de pacotes de recarga automática não estão vinculados ao seu ciclo de cobrança — eles permanecem e expiram **1 ano** a partir da data da compra.

## Upgrades e downgrades de plano

- **Upgrades** entram em vigor imediatamente. Você é cobrado proporcionalmente pelo restante do período de faturamento atual, e sua franquia de créditos e limites é atualizada na hora.
- **Downgrades** são agendados para entrar em vigor na sua próxima data de renovação. Você mantém os créditos e limites do seu plano atual até lá.

## O que acontece quando você fica sem créditos

Se você esgotar sua cota de créditos e não tiver a recarga automática ativada, solicitações à API que consomem créditos retornarão um erro **HTTP 402 (Payment Required)**. Se você tiver a recarga automática ativada, o uso continuará enquanto pacotes de recarga forem comprados automaticamente — mas, se o limite mensal de pacotes for atingido ou uma recarga falhar, seu saldo pode ficar negativo até o próximo ciclo de cobrança ou até que uma recarga manual seja feita. Para retomar o uso após uma interrupção total, você pode:

1. Ativar a recarga automática para comprar mais créditos automaticamente
2. Atualizar para um plano superior
3. Aguardar seus créditos serem renovados no próximo ciclo de cobrança

## Plano Gratuito

O plano gratuito oferece uma **cota única de 500 créditos**, sem necessidade de cartão de crédito. Esses créditos não se renovam — depois que forem usados, você precisará fazer upgrade para um plano pago para continuar usando o Firecrawl. O plano gratuito também possui limites de taxa e de concorrência menores em comparação aos planos pagos (consulte [Limites de Taxa](https://docs.firecrawl.dev/pt-BR/rate-limits)).

## Perguntas frequentes