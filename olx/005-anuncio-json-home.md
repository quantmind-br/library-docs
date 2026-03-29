---
title: Importação de Anúncios via Arquivo JSON
url: https://developers.olx.com.br/anuncio/json/home.html
source: crawler
fetched_at: 2026-02-07T15:17:11.609038919-03:00
rendered_js: false
word_count: 459
summary: This document outlines the technical requirements and procedures for importing advertisements to OLX using a JSON file, including parameter definitions and synchronization logic for insertions and updates.
tags:
    - olx-integration
    - json-import
    - ad-management
    - data-synchronization
    - bulk-upload
category: guide
---

## Importação de Anúncios via Arquivo JSON

Para a integração via Arquivo, a OLX vai consultar periodicamente (mínimo de uma vez por dia) o arquivo disponibilizado pelo anunciante. Para isso, caberá ao anunciante (junto com seu integrador, quando isso for aplicável) disponibilizar uma URL onde esse arquivo estará sempre disponível.

### Parâmetros básicos

Para a montagem do JSON, é necessário respeitar parâmetros genéricos e específicos de cada categoria e/ou subcategoria. Os parâmetros básicos são os seguintes:

ParâmetroValorTipoObrigatórioDescrição`subject`stringsimTítulo do anúncio Mínimo: 2 Máximo: 90`body`stringsimDescrição do anúncio Mínimo: 2 Máximo: 6000`category`stringsimCódigo que define onde o anúncio vai ser exibido na OLX. Verifique a documentação da categoria (ou subcategoria) para saber qual valor inserir para o parâmetro.`id`stringsimIdentificador do anúncio.  
Regular expression : \[A-Za-z0- 9\_{}- ]{1,19}  
Atenção: o campo id deve ser único no arquivo.`images`URL das imagensArray de stringnãoURL das imagens do anúncio. Não pode haver URLs repetidas neste array. Máximo de 20 imagens por anúncio.  
Importante: a primeira imagem da lista será a imagem principal do anúncio.`price`integernãoPreço do anúncio (não aceita centavos)`zipcode`string numéricasimCEP do local onde o produto está disponível.`type``s`stringsimTipo de oferta do anúncio. O valor `s` indica que o produto está à venda.

1: Se você não quer enviar um parâmetro não-obrigatório, deixe de enviar o parâmetro no payload. Se você enviar o parâmetro com valor vazio ou `0`, a operação vai falhar (a menos, é claro, que o valor `0` seja esperado para esse parâmetro).

Exemplos de JSONs de cada categoria podem ser achados na documentação específica por categoria.

### Categorias Suportadas

Atualmente temos a documentação escrita para as seguintes categorias:

- [Autopeças](https://developers.olx.com.br/anuncio/json/autoparts/)
- [Veículos](https://developers.olx.com.br/anuncio/json/autos/)
- [Imóveis](https://developers.olx.com.br/anuncio/json/real_estate/)
- [Agro & Indústria](https://developers.olx.com.br/anuncio/json/agro/)

### Inferência de Inserção, Edição e Deleção de Anúncios

A OLX funciona com um modelo de inserção paga de anúncios. Para a importação de anúncios via arquivo, a OLX vai inferir que há uma nova inserção quando houver um anúncio com identificador inédito. Para JSONs, o identificador é o parâmetro `id`, contido no JSON.

Se um anúncio com um identificador já existente estiver no arquivo em uma nova importação, não realizaremos nenhuma operação, a menos que haja alguma alteração nas outras informações desses anúncio. Nesse caso, trataremos a operação como uma edição (e não inserção).

Para que ocorra a deleção de um anúncio, basta que ele deixe de existir no arquivo e, no próximo processamento dessa carga vamos inferir que esse anúncio deve ser removido.

**Importante**: se um anúncio for removido e no próximo processamento ele voltar a aparecer no arquivo (ou, especificamente, se um determinado identificador deixar de existir no arquivo e, em outra importação, voltar a aparecer, vamos inferir (e, portanto, contabilizar) uma nova inserção. Por isso é crítico que um anúncio sempre esteja disponível com o mesmo identificador no arquivo e só deixe de aparecer quando de fato tivermos que removê-lo do seu inventário.