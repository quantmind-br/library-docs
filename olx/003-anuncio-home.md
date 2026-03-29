---
title: Documentação para a Importação de Anúncios da OLX
url: https://developers.olx.com.br/anuncio/home.html
source: crawler
fetched_at: 2026-02-07T15:17:06.174674446-03:00
rendered_js: false
word_count: 259
summary: This document outlines the available methods for third-party ad integration on OLX, detailing supported categories and technical models for API, XML, and JSON imports.
tags:
    - olx-integration
    - ad-import
    - api-reference
    - xml-integration
    - json-integration
    - inventory-management
    - real-estate-ads
category: guide
---

## Documentação para a Importação de Anúncios da OLX

A OLX hoje suporta dois tipos de importação de anúncios, para anunciantes que querem gerenciar seus anúncios a partir de um software terceiro (ou seja, sem passar pelas interfaces nativas da OLX para gestão de inventário): via API ou via arquivo (JSON ou XML).

## Status das Integrações da OLX

Modelo de IntegraçãoVersão em produçãoCategorias atendidasPróximos passos[API](https://developers.olx.com.br/anuncio/api/home.html)EstávelAutos, Imóveis, Peças e AgroEscrever documentação de categorias não-documentadas. Preparar comunicação e rollout da Fase 2 da nova API de Integração de Anúncios.[XML](https://developers.olx.com.br/anuncio/xml/real_estate/home.html)EstávelImóveisNenhuma evolução prevista. Documentação atualizada.[JSON](https://developers.olx.com.br/anuncio/json/home.html)EstávelAutos, Imóveis, Peças e AgroNenhuma evolução prevista. Documentação atualizada.

## Categorias Suportadas por cada Modelo de Integração

Nem todas as categorias de anúncios na OLX são suportadas pelas integrações existentes:

CategoriaSubcategoriaXMLJSONAPIImóveisApartamentos[Sim](https://developers.olx.com.br/anuncio/xml/real_estate/home.html)[Sim](https://developers.olx.com.br/anuncio/json/real_estate/home.html)[Sim](https://developers.olx.com.br/anuncio/api/real_estate/home.html)ImóveisCasas[Sim](https://developers.olx.com.br/anuncio/xml/real_estate/home.html)[Sim](https://developers.olx.com.br/anuncio/json/real_estate/home.html)[Sim](https://developers.olx.com.br/anuncio/api/real_estate/home.html)ImóveisAluguel de quartosNãoSimSimImóveisTemporadaNãoSimSimImóveisTerrenos sítios e fazendas[Sim](https://developers.olx.com.br/anuncio/xml/real_estate/home.html)[Sim](https://developers.olx.com.br/anuncio/json/real_estate/home.html)[Sim](https://developers.olx.com.br/anuncio/api/real_estate/home.html)ImóveisComércio e indústria[Sim](https://developers.olx.com.br/anuncio/xml/real_estate/home.html)[Sim](https://developers.olx.com.br/anuncio/json/real_estate/home.html)[Sim](https://developers.olx.com.br/anuncio/api/real_estate/home.html)Autos e peçasCarros vans e utilitáriosNão[Sim](https://developers.olx.com.br/anuncio/json/autos/home.html)[Sim](https://developers.olx.com.br/anuncio/api/autos/home.html)Autos e peçasMotosNão[Sim](https://developers.olx.com.br/anuncio/json/autos/home.html)[Sim](https://developers.olx.com.br/anuncio/api/autos/home.html)Autos e peçasÔnibusNãoSimSimAutos e peçasCaminhõesNãoSimSimAutos e peçasBarcos e aeronavesNãoSimSimPeças e acessóriosCarros vans e utilitáriosNão[Sim](https://developers.olx.com.br/anuncio/json/autoparts/home.html)[Sim](https://developers.olx.com.br/anuncio/api/autoparts/home.html)Peças e acessóriosMotosNão[Sim](https://developers.olx.com.br/anuncio/json/autoparts/home.html)[Sim](https://developers.olx.com.br/anuncio/api/autoparts/home.html)Peças e acessóriosÔnibusNão[Sim](https://developers.olx.com.br/anuncio/json/autoparts/home.html)[Sim](https://developers.olx.com.br/anuncio/api/autoparts/home.html)Peças e acessóriosCaminhõesNão[Sim](https://developers.olx.com.br/anuncio/json/autoparts/home.html)[Sim](https://developers.olx.com.br/anuncio/api/autoparts/home.html)Peças e acessóriosBarcos e aeronavesNão[Sim](https://developers.olx.com.br/anuncio/json/autoparts/home.html)[Sim](https://developers.olx.com.br/anuncio/api/autoparts/home.html)Agro e indústriaTratores e máquinas agrícolasNão[Sim](https://developers.olx.com.br/anuncio/json/agro/home.html)[Sim](https://developers.olx.com.br/anuncio/api/agro/home.html)Agro e indústriaPeças para tratores e máquinasNão[Sim](https://developers.olx.com.br/anuncio/json/agro/home.html)[Sim](https://developers.olx.com.br/anuncio/api/agro/home.html)Agro e indústriaAnimais para agropecuáriaNão[Sim](https://developers.olx.com.br/anuncio/json/agro/home.html)[Sim](https://developers.olx.com.br/anuncio/api/agro/home.html)Agro e indústriaMáquinas pesadas para construçãoNão[Sim](https://developers.olx.com.br/anuncio/json/agro/home.html)[Sim](https://developers.olx.com.br/anuncio/api/agro/home.html)Agro e indústriaMáquinas para produção industrialNão[Sim](https://developers.olx.com.br/anuncio/json/agro/home.html)[Sim](https://developers.olx.com.br/anuncio/api/agro/home.html)Agro e indústriaProdução RuralNão[Sim](https://developers.olx.com.br/anuncio/json/agro/home.html)[Sim](https://developers.olx.com.br/anuncio/api/agro/home.html)Agro e indústriaOutros itens para agro e indústriaNão[Sim](https://developers.olx.com.br/anuncio/json/agro/home.html)[Sim](https://developers.olx.com.br/anuncio/api/agro/home.html)Eletrônicos e celularesCelulares e telefoniaNãoNão[Sim](https://developers.olx.com.br/anuncio/api/electronics/home.html)

## Perguntas e Dúvidas Frequentes

Algumas das principais dúvidas relativas à integração de anúncios com a OLX podem ser vistas aqui:

- [Limitação de Taxa (Rate Limit) na API](https://developers.olx.com.br/faq/rate_limit.html)
- [Alteração de categorias](https://developers.olx.com.br/faq/category.html)
- [Especificações de imagens](https://developers.olx.com.br/faq/images.html)
- [Inferência de Inserção, Edição e Deleção de Anúncios em Integrações via XML ou JSON](https://developers.olx.com.br/faq/xml_json_insertion.html)

## Dúvidas, Sugestões e Comentários

Caso você queria um suporte para sua integração, pode enviar email para suporteintegrador@olxbr.com.