---
title: Inferência de operações
url: https://developers.olx.com.br/faq/xml_json_insertion.html
source: crawler
fetched_at: 2026-02-07T15:17:17.734817185-03:00
rendered_js: false
word_count: 213
summary: This document explains the logic used by OLX to process advertisement insertions, updates, and deletions based on unique identifiers within XML and JSON integration files.
tags:
    - olx-integration
    - xml-import
    - json-import
    - ad-management
    - data-synchronization
category: guide
---

## Inferência de Inserção, Edição e Deleção de Anúncios em Integrações via XML ou JSON

A OLX funciona com um modelo de inserção paga de anúncios. Para a importação de anúncios via arquivo, a OLX vai inferir que há uma nova inserção quando houver um anúncio com identificador inédito. Para importação via JSON, o identificador é o parâmetro `id` existente em cada anúncio. No caso de XML, o parâmetro é `CodigoImovel`.

Se um anúncio com um identificador já existente estiver no arquivo em uma nova importação, não realizaremos nenhuma operação, a menos que haja alguma alteração nas outras informações desses anúncio. Nesse caso, trataremos a operação como uma edição (e não inserção).

Para que ocorra a deleção de um anúncio, basta que ele deixe de existir no arquivo e, no próximo processamento dessa carga vamos inferir que esse anúncio deve ser removido.

**IMPORTANTE**: se um anúncio for removido e no próximo processamento ele voltar a aparecer no arquivo (ou, especificamente, se um determinado identificador deixar de existir no arquivo e, em outra importação, voltar a aparecer, vamos inferir (e, portanto, contabilizar) uma nova inserção. Por isso é crítico que um anúncio sempre esteja disponível com o mesmo identificador no arquivo e só deixe de aparecer quando de fato tivermos que removê-lo do seu inventário.