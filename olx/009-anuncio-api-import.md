---
title: Importação de Anúncios (Inserção/Edição/Deleção)
url: https://developers.olx.com.br/anuncio/api/import.html
source: crawler
fetched_at: 2026-02-07T15:17:31.498792507-03:00
rendered_js: false
word_count: 1403
summary: This document provides technical instructions for programmatically inserting, updating, and deleting advertisements on the OLX platform using their JSON-based API and oAuth authentication.
tags:
    - olx-api
    - ad-management
    - oauth-authentication
    - json-import
    - api-integration
    - payload-specification
category: api
---

## Importação de Anúncios (Inserção/Edição/Deleção)

## Autenticação oAuth no OLX

Para utilizar a integração de anúncios via API, é necessário autenticar-se em nome de um usuário do OLX através do protocolo oAuth. A documentação da autenticação oAuth encontra-se [aqui](https://developers.olx.com.br/anuncio/api/oauth.html).

Na autenticação, o sistema solicitante receberá o `client_id` e o `client_secret` que deverão ser usados na URL de conexão. Durante o fluxo oAuth será requisitado que o usuário dê permissão ao integrador para gerenciar seus anúncios na OLX. No *handshake* do oAuth, é requisitado também o `scope` que a aplicação-cliente necessitará. Para utilizar o sistema de integração de anúncios via API, é preciso o `scope` `autoupload`.

## Importação de Anúncios

O processo de integração de anúncios via API consiste no envio de um arquivo no formato JSON descrevendo um ou mais anúncios para inserção, edição ou deleção.

A URL usada para envio da requisição é: [https://apps.olx.com.br/autoupload/import]()

O nosso servidor deve receber a chamada com método do tipo `PUT` e o header enviado deverá ser: `Content-type: application/json`. O formato do *encode* do JSON deverá ser `UTF-8` e o tamanho do payload não pode ultrapassar 1 MB.

## Inserção ou Edição de Anúncios

Para uma inserção ou edição de anúncios, é necessário montar o JSON com parâmetros **básicos** para qualquer categorias, além de **específicos** de cada categoria e/ou subcategoria.

### Parâmetros básicos

ParâmetroValoresTipoObrigatórioDescrição`access_token`stringsimToken de acesso`id`Regular expression: \[A-Za-z0-9\_{}-]{1,19}simO identificador do anúncio. Deve ser único no JSON (caso haja mais de um anúncio no JSON).`operation``insert` ou `delete`stringsimValores para identificar qual será a operação a ser feita:  
`insert` para inserir ou editar anúncios  
`delete` para despublicar anúncios.`category`integersimCategoria do anúncio.`Subject`5stringsimTítulo do anúncio. Mínimo de 2 e máximo de 90 caracteres. (Atenção as notas para [Carros vans e utilitários](https://developers.olx.com.br/anuncio/api/autos/sub_auto.html))`Body`stringsimDescrição do anúncio. Mínimo de 2 e máximo de 6 mil caracteres`Phone`integersimTelefone para contato. Mínimo de 10 e máximo de 11 caracteres. Enviar DDD + Telefone sem caracteres especiais ou espaços.`type``s` ou `u`stringsimTipo de oferta do anúncio. `s` para venda e `u` para aluguel.`price`4integersimPreço do anúncio (não aceita centavos)`zipcode`string numéricasimO CEP do anúncio.`phone_hidden``true` ou `false`booleannão1Ocultar telefone? `true` para ocultar e `false` para mostrar o telefone no anúncio. Caso não envie o comando, o mesmo será interpretado como `false` e o telefone será exibido.`params`arraynão1Lista de parâmetros com as características do anúncio. Os valores dessa lista variam de acordo com a categoria do anúncio.`images`4URL da imagemarray de stringsimURL de imagens que serão inseridas no anúncio do olx.com.br. Não pode haver URLs repetidas neste array. Máximo de 20 imagens. Importante: a primeira imagem da lista será a imagem principal do anúncio!`videos`2URL do vídeoarray de stringnão1URL de vídeo3. que será inserida no anúncio do olx.com.br deve ser apenas do https://www.youtube.com/. Aceito 1 vídeo por anúncio!

> #### Notas
> 
> 1 Se você não quer enviar um parâmetro não-obrigatório, deixe de enviar o parâmetro no payload. Se você enviar o parâmetro com valor vazio ou `0`, a operação vai falhar (a menos, é claro, que o valor `0` seja esperado para esse parâmetro).  
> 2 **Se atentar no formato URL, qualquer coisa diferente de uma URL receberá um erro ERROR\_VIDEOS\_URL\_INVALID**  
> 3 Formato recomendado de URL: https://www.youtube.com/watch?v=Vt&28raiI1q5  
> 4 Os campos `price` e `images` passaram a serem obrigatórios desde o dia `05/08/2025`.  
> 5 O campo `Subject` para categoria de [Carros vans e utilitários](https://developers.olx.com.br/anuncio/api/autos/sub_auto.html) é preenchido automaticamente pela OLX.

Segue um exemplo de envio de vídeo:

```
{
    "videos": [
        "https://www.youtube.com/watch?v=Vt&28raiI1q5"
    ]
},
```

Segue um exemplo para remover o vídeo de um anúncio:

> #### Observações
> 
> - Caso seja necessário alterar o vídeo do anúncio, deve-se alterar a URL e realizar uma edição em outro campo, por exemplo: Descrição e título.
> - Caso seja **enviado mais de um link** de vídeo no anúncio **será publicado apenas o primeiro da listagem.**
> - Em caso de **dúvidas entre em contato: video.experience@olxbr.com**

### Parâmetros específicos

CategoriaSubcategoria[Imóveis](https://developers.olx.com.br/anuncio/api/real_estate/home.html)[Apartamentos](https://developers.olx.com.br/anuncio/api/real_estate/sub_apartment.html)[Imóveis](https://developers.olx.com.br/anuncio/api/real_estate/home.html)[Casas](https://developers.olx.com.br/anuncio/api/real_estate/sub_house.html)[Imóveis](https://developers.olx.com.br/anuncio/api/real_estate/home.html)[Aluguel de quartos](https://developers.olx.com.br/anuncio/api/real_estate/sub_roomrent.html)[Imóveis](https://developers.olx.com.br/anuncio/api/real_estate/home.html)[Temporada](https://developers.olx.com.br/anuncio/api/real_estate/sub_season.html)[Imóveis](https://developers.olx.com.br/anuncio/api/real_estate/home.html)[Terrenos sítios e fazendas](https://developers.olx.com.br/anuncio/api/real_estate/sub_land.html)[Imóveis](https://developers.olx.com.br/anuncio/api/real_estate/home.html)[Comércio e indústria](https://developers.olx.com.br/anuncio/api/real_estate/sub_commercial.html)[Autos e peças](https://developers.olx.com.br/anuncio/api/autos/home.html)[Carros vans e utilitários](https://developers.olx.com.br/anuncio/api/autos/sub_auto.html)[Autos e peças](https://developers.olx.com.br/anuncio/api/autos/home.html)[Motos](https://developers.olx.com.br/anuncio/api/autos/sub_motorcycle.html)[Autos e peças](https://developers.olx.com.br/anuncio/api/autos/home.html)[Ônibus](https://developers.olx.com.br/anuncio/api/autos/sub_bus.html)[Autos e peças](https://developers.olx.com.br/anuncio/api/autos/home.html)[Caminhões](https://developers.olx.com.br/anuncio/api/autos/sub_truck.html)[Autos e peças](https://developers.olx.com.br/anuncio/api/autos/home.html)[Barcos e aeronaves](https://developers.olx.com.br/anuncio/api/autos/sub_boat_plane.html)[Peças e acessórios](https://developers.olx.com.br/anuncio/api/autoparts/home.html)[Carros vans e utilitários](https://developers.olx.com.br/anuncio/api/autoparts/sub_autos.html)[Peças e acessórios](https://developers.olx.com.br/anuncio/api/autoparts/home.html)[Motos](https://developers.olx.com.br/anuncio/api/autoparts/sub_motorcycle.html)[Peças e acessórios](https://developers.olx.com.br/anuncio/api/autoparts/home.html)[Ônibus](https://developers.olx.com.br/anuncio/api/autoparts/sub_bus.html)[Peças e acessórios](https://developers.olx.com.br/anuncio/api/autoparts/home.html)[Caminhões](https://developers.olx.com.br/anuncio/api/autoparts/sub_truck.html)[Peças e acessórios](https://developers.olx.com.br/anuncio/api/autoparts/home.html)[Barcos e aeronaves](https://developers.olx.com.br/anuncio/api/autoparts/sub_boat_plane.html)[Agro e indústria](https://developers.olx.com.br/anuncio/api/agro/home.html)[Tratores e máquinas agrícolas](https://developers.olx.com.br/anuncio/api/agro/agro.html)[Agro e indústria](https://developers.olx.com.br/anuncio/api/agro/home.html)[Máquinas pesadas para construção](https://developers.olx.com.br/anuncio/api/agro/agro.html)[Agro e indústria](https://developers.olx.com.br/anuncio/api/agro/home.html)[Máquinas para produção industrial](https://developers.olx.com.br/anuncio/api/agro/agro.html)[Agro e indústria](https://developers.olx.com.br/anuncio/api/agro/home.html)[Peças para tratores e máquinas](https://developers.olx.com.br/anuncio/api/agro/agro.html)[Agro e indústria](https://developers.olx.com.br/anuncio/api/agro/home.html)[Animais para agropecuária](https://developers.olx.com.br/anuncio/api/agro/agro.html)[Agro e indústria](https://developers.olx.com.br/anuncio/api/agro/home.html)[Produção Rural](https://developers.olx.com.br/anuncio/api/agro/rural_production.html)[Agro e indústria](https://developers.olx.com.br/anuncio/api/agro/home.html)[Outros itens para agro e indústria](https://developers.olx.com.br/anuncio/api/agro/agro.html)[Eletrônicos e celulares](https://developers.olx.com.br/anuncio/api/electronics/home.html)[Celulares e telefonia](https://developers.olx.com.br/anuncio/api/electronics/sub_cellphone.html)Eletrônicos e celulares1Videogames1Eletrônicos e celulares1Computadores e acessórios1Eletrônicos e celulares1Áudio TV vídeo e fotografia1Para a sua casa1Móveis1Para a sua casa1Eletrodomésticos1Para a sua casa1Materiais de construção e jardim1Para a sua casa1Utilidades domésticas1Para a sua casa1Objetos de decoração1Música e hobbies1Instrumentos musicais1Música e hobbies1CDs DVDs etc1Música e hobbies1Livros e revistas1Música e hobbies1Antiguidades1Música e hobbies1Hobbies e coleções1Esportes e lazer1Esportes e ginástica1Esportes e lazer1Ciclismo1Artigos infantis1Animais de estimação1Cachorros e acessórios1Animais de estimação1Gatos e acessórios1Animais de estimação1Cavalos e acessórios1Animais de estimação1Aquários e acessórios1Animais de estimação1Roedores e acessórios1Animais de estimação1Outros animais e acessórios1Moda e beleza1Beleza e saúde1Moda e beleza1Roupas e calçados1Moda e beleza1Bolsas malas e mochilas1Moda e beleza1Bijouterias relógios e acessórios1Comércio e escritório1Equipamentos e mobiliário1Comércio e escritório1Trailers e carrinhos comerciais1Comércio e escritório1Outros itens para comércio e escritório1Serviços1Vagas de emprego1

1 Categoria não suportada atualmente pela API de Importação de Anúncios da OLX

## Deleção de Anúncios

Para uma deleção, basta enviar o `id` e a operação `delete`.

A seguir um JSON de exemplo com uma deleção:

```
{
    "access_token": "ca18abccaadd282490e75173f98b8ec6f0c1c6c8",
    "ad_list": [
        {
            "id": "444444444",
            "operation": "delete"
        }
    ]
}
```

O anúncio permanecerá publicado a menos que uma operação de deleção seja enviada para a OLX com o `id` utilizado em sua inserção. Portanto recomendamos atenção redobrada para o integrador enviar a deleção para a OLX, para evitar que anúncios de produtos já vendidos continuem publicados - prejudicando a experiência do anunciante e do comprador.

## Retorno Esperado

O formato do retorno de nosso servidor será do tipo JSON, que contém a seguinte estrutura:

ParamêtroValorDescrição`token`Retorna uma string com um token a ser usado para posteriormente acessar o status da importação`statusMessage`Explica o retorno síncrono da importação, com detalhamento de erros da validação síncrona.`statusCode`Identifica o retorno síncrono da importação.`errors``array`Retorna uma lista de erros

Os `statusCode` e `statusMessage` possíveis são os seguintes:

CódigoMensagemDescrição`0``The ads were imported and will be processed`No caso, os anúncios foram validados sincronamente. Não é garantia de publicação, dado que há a validação assíncrona posterior (moderação, etc).`-1``Unexpected error`Erro inesperado.`-2``The request was blocked`Usuário não pode importar pois está bloqueado temporariamente por excesso de requisições.`-3``There is no ad to import`Não há anúncios para importar.`-4``An ad had problems on import`Se um anúncio falhar em sua validação, a importação é cancelada.`-5``Import is down`O serviço de importação está desativado.`-6``Without permission`Usuário sem permissão.`-7``Trying to import "n" ad(s), but user just have slot for "f" more.`O usuário está tentando importar "n" anúncios mas só podem importar mais "f".`-8``Trying to import "n" ad(s), only "f" were imported and will be processed. The following ads were ignored due to limit exceeded: "t"`Tentando importar "n" anúncios, só "f" foram importados e serão processados. Os seguintes anúncios foram ignorados devido ao limite tempo "t" excedido.

No caso do erro tipo `-6`, verifique se a conta OLX possui um plano profissional ativo e compatível/habilitado para realização de integração de anúncios.

- A partir de Janeiro/2025 passamos a comercializar novos planos profissionais para anunciantes de veículos. Com isso, agora passamos a oferecer diferentes opções planos para vendedores autônomos e empresas.
  
  - Planos para vendedores autônomos: `Essencial` e `Plus`
  - Planos para empresas: `Essencial Empresa`, `Plus Empresa` e `Premium Empresa`
- Importante: Para as opções de planos para vendedores autônomos, não será permitida a utilização da API de integração de anúncios para qualquer ferramenta de integração. Anunciantes que necessitem realizar integração de anúncios deverão procurar a OLX para contratação (ou alteração) dos planos para Empresas.
  
  - Se precisar entrar em contato conosco, ligue para [0800 022 9800](tel:08000229800) (segunda à sexta das 09h às 18h) ou nos envie uma mensagem através da nossa [Central de Ajudaopen in new window](https://ajuda.olx.com.br/fale-conosco)
  - Quer conhecer as opções de planos para Empresa? Confira [aquiopen in new window](https://adquirir.olx.com.br/planos-veiculos-empresa?referral=DOC_INTEGRATIONS)

No caso do erro do tipo `-4`, alguma validação síncrona aconteceu e, por isso, algum dos anúncios deixou de ser importado com sucesso. Os possíveis motivos são os seguintes:

CódigoDescrição`UNDEFINED_AD_ID`Anúncio enviado sem ID`NO_IMAGE`Anúncio enviado sem imagens`NO_REGION`CEP enviado corresponde a região inválida`NO_REGION`CEP enviado em formato inválido`ERROR_FUEL_4_DEPRECATED`Tentando enviar o valor `4 - Gás Natural` ou outro valor inválido no campo `fuel``ERROR_FINANCIAL_INVALID`Tentando enviar o valor `1 - Financiado` ou outro valor inválido no parâmetro `financial``ERROR_CAR_FEATURE_2_INVALID`Tentando enviar o valor `2 - Direção hidráulica` no parâmetro `car_features``ERROR_CAR_TYPE_1_OR_4_INVALID`Tentando enviar o valor 1 ou 4 no parâmetro `cartype``ERROR_VEHICLE_TAG_INVALID`Placa não enviada ou em formato inválido`ERROR_VEHICLE_BRAND_INVALID`Marca não enviada ou em formato inválido`ERROR_VEHICLE_MODEL_INVALID`Modelo não enviado ou em formato inválido`ERROR_VEHICLE_VERSION_INVALID`Versão não enviada ou em formato inválido`ERROR_VEHICLE_BRAND_MODEL_VERSION_INVALID`O anúncio foi rejeitado porque os valores fornecidos para `Marca`, `Modelo` e/ou `Versão` não correspondem aos dados cadastrados no [Catálogo de Autos da OLX](https://developers.olx.com.br/anuncio/api/autos/car_models.html).

Eis exemplos de JSONs de retorno da API.

```
{
    "token": "06fb235e216f3095ba913654d10afee2f55eae35",
    "statusCode": 0,
    "statusMessage": "The ads were imported and will be processed",
    "errors": []
}
```

```
{
    "token": null,
    "statusCode": -4,
    "statusMessage": "An ad had problems on import",
    "errors": [
        {
            "id": "78192371",
            "status": "error",
            "messages": [
                {
                    "category": "NO_REGION"
                }
            ]
        }
    ]
}
```

```
{
    "token": null,
    "statusCode": -6,
    "statusMessage": "Without permission",
    "errors": []
}
```