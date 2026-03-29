---
title: Casas
url: https://developers.olx.com.br/anuncio/xml/real_estate/sub_house.html
source: crawler
fetched_at: 2026-02-07T15:17:37.121942929-03:00
rendered_js: false
word_count: 173
summary: This document provides technical specifications and XML requirements for listing properties in the Casas subcategory, including mandatory parameters and valid attribute values.
tags:
    - real-estate-integration
    - xml-schema
    - olx-api
    - property-listings
    - metadata-configuration
category: reference
---

### Subcategoria `Casas`

Para esta subcategoria, é necessário preencher o parâmetro `<SubTipoImovel>` com os seguintes valores:

`<SubTipoImovel>`Título do anúncio`Casa`Casa`Casa de Rua`Casa`Casa Padrão`Casa`Casa Padrão Térrea`Casa`Casa Residencial`Casa`Sobrado`Casa`Sobrado Residencial`Casa`Village Residencial`Casa`Casa de Condomínio`Casa de condomínio`Casa em Condomínio`Casa de condomínio`Casa de Vila`Casa de vila

Além disso, há parâmetros específicos para esta subcategoria, que devem constar dentro do parâmetro `params` e preenchidos conforme a tabela a seguir:

ParâmetroValorObrigatórioDescrição`<SubTipoImovel>`Consulte tabela anteriorSimDefine a categoria onde o anúncio estará localizado na OLX`<QtdDormitorios>``0` para 0 quartos  
`1` para 1 quarto  
`2` para 2 quartos  
`3` para 3 quartos  
`4` para 4 quartos  
`5` para 5 ou mais quartos  
SimQuantidade de quartos`<QtdBanheiros>``0` para 0 banheiros  
`1` para 1 banheiro  
`2` para 2 banheiros  
`3` para 3 banheiros  
`4` para 4 banheiros  
`5` para 5 ou mais banheiros  
NãoQuantidade de banheiros`<QtdVagas>``0` para 0 vagas  
`1` para 1 vaga  
`2` para 2 vagas  
`3` para 3 vagas  
`4` para 4 vagas  
`5` para 5 ou mais vagas  
NãoQuantidade de vagas de garagem

Aqui está um exemplo de XML para inserção ou edição de anúncios na subcategoria `Casas`:

```
<?xml version="1.0" encoding="utf-8"?>
<Carga xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
    xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <Imoveis>
        <Imovel>
            <CodigoImovel>CASA001</CodigoImovel>
            <TituloAnuncio>Casa Agradável No Melhor Bairro da Cidade</TituloAnuncio>
            <SubTipoImovel>Casa Residencial</SubTipoImovel>
            <Cidade>São Paulo</Cidade>
            <Bairro>Perdizes</Bairro>
            <CEP>05018000</CEP>
            <PrecoVenda>500000</PrecoVenda>
            <ValorIPTU>500</ValorIPTU>
            <QtdDormitorios>3</QtdDormitorios>
            <QtdVagas>2</QtdVagas>
            <QtdBanheiros>2</QtdBanheiros>
            <AreaUtil>67</AreaUtil>
            <Observacao>A melhor casa do bairro, prontinha para você morar!\nFica perto de um parque bem grande, cheio de árvore.\nMuito legal, você deveria visitar!</Observacao>
            <Fotos>
                <Foto>
                    <URLArquivo> http://www.site_da_imobiliaria.com/foto_legal.jpg</URLArquivo>
                </Foto>
                <Foto>
                    <Principal>1</Principal>
                    <URLArquivo> http://www.site_da_imobiliaria.com/foto_legal2.jpg</URLArquivo>
                </Foto>
            </Fotos>
        </Imovel>
    </Imoveis>
</Carga>
```