---
title: Documentação para a Importação via XML para Imóveis na OLX
url: https://developers.olx.com.br/anuncio/xml/real_estate/home.html
source: crawler
fetched_at: 2026-02-07T15:17:10.86420055-03:00
rendered_js: false
word_count: 571
summary: This document provides technical instructions for importing real estate advertisements to the OLX platform via XML files, detailing required tags, data formats, and structural parameters.
tags:
    - xml-import
    - olx-integration
    - real-estate-ads
    - data-specification
    - technical-documentation
category: guide
---

## Documentação para a Importação via XML para Imóveis na OLX

Este manual tem como objetivo auxiliar a implantação de importação de anúncios de XML para o segmento de Imóveis.

Para que o cliente seja elegível à integração via XML com a OLX, seus anúncios devem ser disponibilizados num arquivo XML em uma URL pública, com o devido permissionamento para seu download a qualquer hora do dia, seguindo o seguinte encoding:

```
<?xml version="1.0" encoding="utf-8"?>
```

## Parâmetros básicos

Para a montagem do XML, é necessário respeitar parâmetros genéricos e específicos de cada categoria e/ou subcategoria. Os parâmetros básicos são os seguintes:

Tag XMLValorObrigatório?Descrição`<CodigoImovel>`String de até 20 caracteresSimTambém conhecido como `Ref` ou `External ID`, essa tag serve para te ajudar a identificar o anúncio depois de processado na OLX.`<TituloAnuncio>`Título com até 90 caracteresNãoTítulo do Imóvel, que será mostrado na listagem de resultados`<Titulo>`Título com até 90 caracteresNãoTítulo do Imóvel, que será mostrado na listagem de resultados. Se o `<TituloAnuncio>` for preenchido, a tag `<Titulo>` é ignorada.`<Bairro>`NãoEsse campo só é utilizado para formar o título do anúncio, caso as tags `<TituloAnuncio>` ou `<Titulo>` não tenham sido preenchidas. Não é usado em nenhum outro lugar da OLX atualmente.`<Cidade>`NãoEsse campo só é utilizado para formar o título do anúncio, caso as tags `<TituloAnuncio>` ou `<Titulo>` não tenham sido preenchidas. Não é usado em nenhum outro lugar da OLX atualmente.`<SubTipoImovel>`Consulte a SubCategoria para saber os valores aceitos em `<SubTipoImovel>`SimDefine a categoria onde o anúncio vai ser encontrado.`<CEP>`Para processamento, nós vamos limpar todo caractere não-numérico enviado.SimCódigo de localização espacial do imóvel.`<Observacao>`Descrição com até 6 mil caracteresSimDescrição do anúncio. Não aceita tags HTML. Para quebra de linha, use a tag `\n``<PrecoVenda>`Número inteiro, sem parte decimal, sem separador de milharesNãoValor de venda do imóvel.`<PrecoLocacao>`Número inteiro, sem parte decimal, sem separador de milharesNãoValor de aluguel do imóvel. O `<PrecoLocacao>` será ignorado, caso o campo `<PrecoVenda>` seja preenchido também.`<PrecoLocacaoTemporada>`Número inteiro, sem parte decimal, sem separador de milharesNãoValor de aluguel por temporada do imóvel. O `<PrecoLocacaoTemporada>` será ignorado, se `<PrecoLocacao>` ou `<PrecoVenda>` seja preenchido também.`<PrecoCondominio>`Número inteiro, sem parte decimal, sem separador de milharesNãoValor do condomínio do imóvel.`<ValorIPTU>`Número inteiro, sem parte decimal, sem separador de milharesNãoValor mensal do IPTU do imóvel.`<AreaTotal>`Número inteiro, sem parte decimalNãoTamanho em metros quadrados do imóvel.`<AreaUtil>`Número inteiro, sem parte decimalNãoTamanho em metros quadrados do imóvel. Se a `<AreaTotal>` for preenchida, a tag `<AreaUtil>` é ignorada.`<Foto>` `<URLArquivo>`NãoURL em que a imagem está hospedada`<Foto>` `<Principal>``1` para definir a imagem principalNãoValor `1` caso a imagem seja a imagem principal do anúncio`<Videos>` `<Video>`1NãoURL de video2 que será inserida no anúncio do olx.com.br deve ser apenas do https://www.youtube.com. Aceito 1 vídeo por anúncio.

1: **A inserção de vídeo está em fase Beta** e pode sofrer alterações com o tempo. **A disponibilidade via XML é apenas para categoria de Imóveis.**

2: Formato recomendado de URL: https://www.youtube.com/watch?v=Vt&28raiI1q5

Segue um exemplo de envio de Vídeo:

```
 <Videos>
       <Video>https://www.youtube.com/watch?v=Vt28raiI1q5</Video>
 </Videos>
```

***Observações:***

*- Caso seja necessário alterar o **vídeo** do anúncio, deve-se alterar a URL e realizar uma edição em outro campo, por exemplo: Descrição e título.*

*- A tag de `<Videos>` deve estar dentro da estrutura de `<Imovel>`. Seguir a mesma estrutura para `<Fotos>`*

*- Caso seja **enviado mais de um link** de vídeo no anúncio **será publicado apenas o primeiro** da listagem.*

*- Em caso de **dúvidas entre em contato: video.experience@olxbr.com***

Cada subcategoria pode ter parâmetros específicos para cada uma delas. A documentação destas pode ser achada na página de cada subcategoria - onde também você encontrará exemplos de XMLs para cada subcategoria.

- [Apartamentos](https://developers.olx.com.br/anuncio/xml/real_estate/sub_apartment.html)
- [Casas](https://developers.olx.com.br/anuncio/xml/real_estate/sub_house.html)
- [Terrenos, sítios e fazendas](https://developers.olx.com.br/anuncio/xml/real_estate/sub_land.html)
- [Comércio e Indústria](https://developers.olx.com.br/anuncio/xml/real_estate/sub_commercial.html)