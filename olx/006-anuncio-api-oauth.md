---
title: Autenticação na API olx.com.br
url: https://developers.olx.com.br/anuncio/api/oauth.html
source: crawler
fetched_at: 2026-02-07T15:17:21.089831227-03:00
rendered_js: false
word_count: 1941
summary: This document provides a comprehensive guide for implementing OAuth 2.0 authentication for web applications integrating with the OLX API.
tags:
    - oauth-2-0
    - api-authentication
    - olx-api
    - web-application
    - authorization-flow
    - api-integration
category: guide
---

Este documento descreve como utilizar o protocolo oAuth 2.0 como forma de autenticação na API olx.com.br por meio de aplicação web. Você vai registrar sua aplicação no olx.com.br, a aplicação vai solicitar uma chave de acesso ao servidor de autenticação do olx.com.br e então utilizar essa chave para receber as informações de um recurso da API olx.com.br que deseja acessar.

## Registro da Aplicação

Antes de iniciar o protocolo de autenticação com o servidor olx.com.br, o cliente deverá registrar sua aplicação, fornecendo os seguintes dados para suporteintegrador@olxbr.com:

- Nome do cliente
- Nome da aplicação
- Descrição da aplicação
- Website
- Telefone
- E-mail
- URIs de redirecionamento (identifica um endpoint do cliente que será alvo de redirecionamento no processo de autenticação; mínimo 1 e máximo 3)

Após receber os dados, o olx.com.br entrará em contato com o cliente para fornecer sua identificação (`client_id`) e sua chave de segurança, necessários para iniciar a sequência de autorização.

## Sequência de Autorização

A sequência de autorização tem início quando a aplicação do integrador redireciona o navegador para uma URL do olx.com.br. Nesta URL serão incluídos alguns parâmetros que indicam o tipo de acesso que está sendo requerido. O olx.com.br é o responsável pela autenticação do usuário e por confirmar a permissão de acesso a suas informações e recursos. Como resultado, o olx.com.br retorna para a aplicação um código de autorização. Após receber o código de autorização a aplicação poderá fornecê-lo (junto com sua identificação e senha) para obter em troca uma chave de acesso. A aplicação poderá então utilizar essa chave de acesso para acessar a API olx.com.br.​

## Código de Autenticação

O código de autorização é obtido utilizando o servidor de autorização do olx.com.br como intermediador entre o cliente/aplicação e o usuário.

O servidor de autenticação valida a requisição para certificar que todos os parâmetros obrigatórios estão válidos e presentes. Se a requisição for válida, o servidor de autenticação tenta autenticar o usuário (pedindo seu login e senha) e obtém dele uma decisão de autorização.

Ao invés de solicitar a autorização diretamente ao usuário, o cliente direciona-o para a página de autenticação do olx.com.br que, após autenticar o usuário com seu login e senha, redireciona o usuário de volta ao cliente junto com o código de autorização.

Este código deverá ser utilizado logo em seguida para solicitar a chave de acesso que, caso seja aceita pelo usuário, permitirá o cliente a acessar suas informações através da API olx.com.br. O código de autenticação é temporário e não pode ser reutilizado.

A URL usada para autenticar um usuário será https://auth.olx.com.br/oauth

Os parâmetros HTTP `GET` suportados pelo servidor de autenticação do olx.com.br para aplicações Web são:

ParâmetroValoresObrigatórioDescrição`response_type`codeSimDetermina que o valor esperado pela requisição será um código de autorização.`client_id`A identificação do cliente que foi fornecida pelo olx.com.br através do registro da aplicação.SimIdentifica o cliente que está enviando a requisição. O valor do parâmetro tem que ser idêntico ao valor fornecido pelo olx.com.br durante o registro da aplicação.`redirect_uri`O valor do parâmetro tem que ser idêntico a um dos URI cadastrados no registro da aplicação no olx.com.br.Sim (se integrador cadastrou múltiplas URIs)Determina para qual servidor a resposta da requisição será enviada.`scope`Conjunto de permissões que a aplicação solicita, separadas por espaço, não importa a ordem dos valores. Ver tópico Permissões.SimIdentifica o tipo de acesso a API olx.com.br que a aplicação está requisitando. Os valores passados neste parâmetro serão os mesmos`state`Qualquer valor.NãoFornece qualquer valor que pode ser útil a aplicação ao receber a resposta de requisição.

**Exemplo de URL:**  
https://auth.olx.com.br/oauth?client\_id=​1055d3e698d289f2af8663725127bd4b&redirect\_uri=https://yourserver.com/token&response\_type=code&scope=autoupload&state=/profile

## Permissões

Ao solicitar a chave de acesso o cliente deve solicitar permissões através do parâmetro `scope`. Essas solicitações serão enviadas ao usuário para que ele possa permitir ou não o acesso.

O valor parâmetro `scope` é expressado como uma lista de valores (case sensitive) separados por espaços, não importando a ordem.

O servidor de autorização do olx.com.br pode ignorar parcial ou totalmente as permissões solicitadas pelo cliente de acordo com as políticas do servidor de autenticação ou por instrução do usuário.

Segue abaixo a lista dos possíveis valores de permissão que podem ser solicitadas ao usuário:

ValorDescriçãobasic\_user\_infoPermite acesso as informações básicas do usuário. Ex: nome completo e email.autouploadPermite acesso ao sistema de autouploads (Envio de anúncios de forma automática)autoservicePermite fazer alterações de configuração do usuário do recebimento de [leads](https://developers.olx.com.br/lead/how_to.html) e envio de [webhooks](https://developers.olx.com.br/webhooks/notifications.html)chatPermite acesso a configuração de chat e recebimento de mensagens do chat da OLX. [Clique aqui](https://developers.olx.com.br/chat/)

### Resposta da requisição

A resposta será enviada para o `redirect_uri`,conforme especificado na URL da requisição. Se o usuário aprovar o acesso, a resposta conterá um código de autorização e o parâmetro `state` (se incluído na requisição). Se o usuário não aprovar, a resposta retornará uma mensagem de erro. Todas as respostas são retornadas ao servidor web por `query string`.

### Confirmação da autorização

Se o usuário conceder a permissão solicitada o servidor de autenticação gera um código de autorização e enviao para o cliente através dos seguintes parâmetros na URI de redirecionamento:

ParâmetroValoresObrigatórioDescrição`code`Código de autorização gerado pelo servidor de autenticação.SimCódigo de autorização utilizado para solicitar permissão de acesso a recursos de um usuário. Expira 10 minutos após ter sido gerado e não pode ser reutilizado.`state`Mesmo valor enviado pelo cliente na requisição.Sim (se presente na requisição)Fornece qualquer valor que pode ser útil a aplicação ao receber a resposta de requisição.

Exemplo de resposta de confirmação: https://yourserver.com/token?state=/profile&code=4gP7q7W91aoMsCeLvIaQm6bTrgtp7

### Erros de autenticação

Se a requisição falhar devido a uma URI de redirecionamento inválida ou não enviada ou se o identificador do cliente (`client_id`) inválido ou não enviado o servidor de autenticação não irá redirecionar o usuário para o URI de redirecionamento.

Se o usuário negar acesso as permissões solicitadas ou se a requisição falhar por outros motivos o servidor de autenticação informa ao cliente qual foi o erro através de parâmetros enviados na URI de redirecionamento. Caso a URI passada seja diferente de uma das registradas no olx.com.br, o servidor de autenticação responderá com um HTTP 400 (Bad Request).

Segue abaixo a lista dos parâmetros para erros de autenticação retornados pelo servidor de autenticação:

ParâmetroValoresObrigatórioDescrição`error``invalid_request`SimA requisição tem parâmetro obrigatório faltando, inclui um parâmetro inválido ou está mal formatada por algum outro motivo.`error``unauthorized_client`SimO cliente não está autorizado a requisitar um código de autorização usando este método.`error``access_denied`SimO usuário ou servidor de autenticação negou a requisição.`error``unsupported_response_type`SimO servidor de autenticação não suporta obter um código de autorização utilizando este método.`error``invalid_scope`SimA permissão solicitada é inválida, desconhecida ou mal formatada.`error``temporarily_unavailable`SimNo momento o servidor de autenticação está indisponível para receber requisições devido a uma manutenção ou sobrecarga temporária.`error``server_error`SimO servidor de autenticação encontrou uma condição inesperada que impossibilitou a finalização da requisição.`state`Mesmo valor enviado pelo cliente na requisição.Sim (se presente na requisição)Fornece qualquer valor que pode ser útil a aplicação ao receber a resposta de requisição.

Exemplo de resposta de erro: https://yourserver.com/token?error=access\_denied&state=/profile

## Chave de acesso

Chaves de acesso são credenciais usadas para acessar recursos protegidos de um usuário. É uma string que representa uma autorização emitida ao cliente. Esta chave representa permissões específicas, concedidas pelo usuário e emitida pelo servidor de autorização.

### Requisição da chave de acesso

A URL usada para solicitar a chave de acesso será https://auth.olx.com.br/oauth/token

Após receber o código de autorização, o cliente poderá trocá-lo por uma chave de acesso através de uma nova requisição. Esta requisição deverá ser um `POST HTTPS` e conter os seguintes parâmetros:

Segue abaixo um exemplo de requisição de chave de acesso:

```
POST /oauth/token HTTP/1.1
Host: auth.olx.com.br
Content-Type: application/x-www-form-urlencoded

code=4/P7q7W91aoMsCeLvIaQm6bTrgtp7&client_id=1055d3e698d289f2af8663725127bd4b&client_secret={sua_chave_de_segurança}&redirect_uri=https://yourserver.com/token&grant_type=authorization_code
```

### Resposta de requisição

Se a solicitação da chave de acesso for válida e autorizada, o servidor de autenticação retorna um HTTP 200 (OK) com valor da chave de acesso. Se a solicitação falhar o servidor de autenticação, retorna um erro conforme seção 2​.2.2.2.​

#### Resposta bem sucedida

O servidor de autenticação gera uma chave de acesso e constrói a resposta adicionando os seguintes parâmetros no corpo da resposta HTTP 200 (OK):

ParâmetroValoresObrigatórioDescrição`access_token`A chave de acesso retornada pelo servidor de autenticação.SimA chave de acesso que será utilizada para utilizar a API olx.com.br.`token_type``Bearer`SimDefine o tipo de chave gerada.

Segue abaixo um exemplo de resposta bem sucedida em formato JSON retornada pelo servidor de autenticação:

```
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
Cache-Control: no-store
Pragma: no-cache

{ 
    "access_token":"1/fFAGRNJru1FTz70BzhT3Zg",
    "token_type":"Bearer"
}
```

#### Resposta de erro

O servidor de autenticação retorna um HTTP 400 (Bad Request) e inclui um dos seguintes valores na resposta:

ParâmetroValoresObrigatórioDescrição`error`invalid\_requestSimFalta de parâmetro obrigatório na requisição, inclui um parâmetro não suportado, inclui um parâmetro repetido, incluir múltiplas credenciais ou mal formato por algum outro motivo.`error`invalid\_clientSimFalha na autorização do cliente.`error`invalid\_grantSimCódigo de autorização inválido, expirado ou revogado, URI não é a mesma que a URI usada na requisição de autorização ou foi emitido para outro cliente.`error`unauthorized\_clientSimO cliente autenticado não está autorizado a utilizar este tipo de autorização (`grant_type`).`error`unsupported\_grant\_typeSimO tipo de autorização (`grant_type`) não é suportado pelo servidor.`error`invalid\_scopeSimA solicitação de permissão enviada é inválido, desconhecida ou excede as permissões concedidas pelo usuário.

Segue abaixo um exemplo de resposta de erro na requisição de uma chave de acesso:

```
HTTP/1.1 400 Bad Request
Content-Type: application/json;charset=UTF-8
Cache-Control: no-store
Pragma: no-cache

{
    "error":"invalid_request"
}
```

Depois que a aplicação obtiver uma chave de acesso poderá então utilizar a API olx.com.br para acessar recursos privados de um determinado usuário.

## Acesso a API

O cliente acessa os recursos protegidos do usuário apresentando a chave de acesso a API olx.com.br. O servidor valida a chave de acesso e garante que as permissões concedidas são suficientes para acessar o recurso solicitado.

Segue abaixo um exemplo de como utilizar a API olx.com.br para obter as informações básicas de um usuário:

```
POST /oauth_api/basic_user_info HTTPS/1.1 
Host: apps.olx.com.br
User-Agent: Mozilla/5.0
Content-Type: application/json;charset=UTF-8
{
    "access_token":"387266f574068c83f74942fe255e82261708f960"
}
```

Ou utilizando uma aplicação por linha de comando como, por exemplo, o CURL:

```
curl -X POST https://apps.olx.com.br/oauth_api/basic_user_info --data '{"access_token":"387266f574068c83f74942fe255e82261708f960"}' -H 'User-Agent: Mozilla/5.0'
```

## Recursos

A versão atual da API OLX fornece acesso aos seguintes recursos:

RecursoDescrição`basic_user_info`Retorna uma lista com as informações básicas do usuário.`autoupload`Sistema de envio de anúncios de forma automática

### `basic_user_info`

Retorna uma lista com as informações básicas do usuário.

**Acesso**

```
POST /oauth_api/basic_user_info HTTPS/1.1 
Host: apps.olx.com.br
```

**Permissões**

Qualquer chave de acesso com a permissão b​asic\_user\_info.

**Campos**

NomeDescriçãoTipo`user_name`Nome completo do usuário.`string``user_email`Email do usuário.`string`

**Chamada**

```
POST /oauth_api/basic_user_info HTTPS/1.1 
Host: apps.olx.com.br
Content-Type: application/json;charset=UTF-8
{
  "access_token":"1/fFAGRNJru1FTz70BzhT3Zg"
}
```

**Retorno**

```
"user_name":"José da Silva",
"user_email":"jose.silva@sample.com"
}
```

### `autoupload`

Sistema de envio de anúncios de forma automática. Para mais informações, consultar o manual de Autoupload do olx.com.br

## Exemplo de utilização

Abaixo vamos ver alguns exemplos de como se autenticar por esse nosso fluxo.

### Python

Um exemplo em Python de como utilizar nosso sistema de OAuth

```
from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import RedirectResponse
import httpx

app = FastAPI()


@app.get("/")
async def home(request: Request):
    client_id = "563247ed31d2044ee725dedcf5b0076ac14a3caf"
    response_type = "code"
    scope = "basic_user_info"
    redirect_uri = "http://127.0.0.1:8000/oauth"
    state = "test"

    auth_host = "auth.olx.com.br"

    url = f"https://{auth_host}/oauth?client_id={client_id}&response_type={response_type}&scope={scope}&redirect_uri={redirect_uri}&state={state}"
    return RedirectResponse(url)


@app.get("/oauth")
async def oauth(request: Request, code: str):
    client_id = "563247ed31d2044ee725dedcf5b0076ac14a3caf"
    client_secret = "e90f41c9ba21794c14305b5849daf03c"
    grant_type = "authorization_code"
    redirect_uri = "http://127.0.0.1:8000/oauth"

    auth_host = "auth.olx.com.br"

    async with httpx.AsyncClient() as client:
        payload = {
            "code": code,
            "client_id": client_id,
            "client_secret": client_secret,
            "redirect_uri": redirect_uri,
            "grant_type": grant_type,
        }
        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        response = await client.post(
            f"https://{auth_host}/oauth/token", data=payload, headers=headers
        )
        data = response.json()

    access_token = data["access_token"]

    payload = {"access_token": access_token}
    return payload

```

A primeira função `home` é onde iremos montar uma URL para autenticação da conta OLX, usamos os seguintes dados:

- client\_id: Token fornecido pela OLX que representa sua aplicação.
- client\_secret: Token fornecido pela OLX que garante as credenciais da sua aplicação.
- redirect\_uri: Uma das URLs que você cadastrou na sua aplicação na OLX.

Após a autenticação ser bem sucedida, iremos redirecionar para o `redirect_uri` enviado na requisição, enviando dois `query parameters`:

- state: Valor escolhido e enviado, caso sua aplicação precise de algum dado extra.
- code: O código retornado pela OLX após autenticação para que possa ser obtido o `access_token`.

A segunda função `oauth` vai receber esse redirecionamento com os dados e irá realizar a requisição para obter o `access_token` e assim finalizando o nosso fluxo de autenticação.

### Java

Um exemplo em Java (com Spring, OkHttp3, Gson) de como utilizar nosso sistema de OAuth

```
package com.oauth.tutorialoauth;

import com.google.gson.Gson;
import com.google.gson.annotations.SerializedName;
import okhttp3.*;
import org.springframework.boot.SpringApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.view.RedirectView;

import java.io.IOException;

@RestController
public class OauthController {

    private static final String CLIENT_ID = "563247ed31d2044ee725dedcf5b0076ac14a3caf";
    private static final String CLIENT_SECRET = "e90f41c9ba21794c14305b5849daf03c";
    private static final String AUTH_HOST = "auth.olx.com.br";
    private static final String REDIRECT_URI = "http://127.0.0.1:8080/oauth";
    private static final String GRANT_TYPE = "authorization_code";
    private static final String RESPONSE_TYPE = "code";
    private static final String SCOPE = "basic_user_info";
    private static final String STATE = "test";

    @GetMapping("/")
    public RedirectView home() {
        String url = String.format("https://%s/oauth?client_id=%s&response_type=%s&scope=%s&redirect_uri=%s&state=%s",
                AUTH_HOST, CLIENT_ID, RESPONSE_TYPE, SCOPE, REDIRECT_URI, STATE);
        return new RedirectView(url);
    }

    @ResponseBody
    @GetMapping("/oauth")
    public Object oauth(@RequestParam("code") String code) throws IOException {
        OkHttpClient client = new OkHttpClient();
        Gson gson = new Gson();

        MediaType mediaType = MediaType.parse("application/x-www-form-urlencoded");
        RequestBody body = okhttp3.RequestBody.create(
                "code=" + code +
                        "&client_id=" + CLIENT_ID +
                        "&client_secret=" + CLIENT_SECRET +
                        "&redirect_uri=" + REDIRECT_URI +
                        "&grant_type=" + GRANT_TYPE,
                mediaType
        );

        Request request = new Request.Builder()
                .url("https://" + AUTH_HOST + "/oauth/token")
                .post(body)
                .addHeader("Content-Type", "application/x-www-form-urlencoded")
                .build();

        try (Response response = client.newCall(request).execute()) {
            assert response.body() != null;
            String responseBody = response.body().string();

            // Desserializar a resposta JSON em uma instância de AccessTokenResponse
            AccessTokenResponse accessTokenResponse = gson.fromJson(responseBody, AccessTokenResponse.class);

            // Retornar o access_token
            return accessTokenResponse.getAccessToken();
        }
    }

    public static class AccessTokenResponse {
        @SerializedName("access_token")
        private String accessToken;

        public String getAccessToken() {
            return accessToken;
        }
    }
}
```

A primeira função `home` é onde iremos montar uma URL para autenticação da conta OLX, usamos os seguintes dados:

- client\_id: Token fornecido pela OLX que representa sua aplicação.
- client\_secret: Token fornecido pela OLX que garante as credenciais da sua aplicação.
- redirect\_uri: Uma das URLs que você cadastrou na sua aplicação na OLX.

Após a autenticação ser bem sucedida, iremos redirecionar para o `redirect_uri` enviado na requisição, enviando dois `query parameters`:

- state: Valor escolhido e enviado, caso sua aplicação precise de algum dado extra.
- code: O código retornado pela OLX após autenticação para que possa ser obtido o `access_token`.

A segunda função `oauth` vai receber esse redirecionamento com os dados e irá realizar a requisição para obter o `access_token` e assim finalizando o nosso fluxo de autenticação.

### PHP

Um exemplo em PHP de como utilizar nosso sistema de OAuth: oauth.php

```
<?php
    # antes de usar este script, você deve registrar sua aplicação na OLX
    /*
    *
    *   @client_id         - token fornecido pelo OLXque representa sua aplicação
    *   @client_secret     - token fornecido pelo OLXque garante as credenciais da sua aplicação
    *
    */
    # utilizar seu client_id e client_secret fornecido pelo OLX 
    $client_id = '52e213308e9d882584498ed90074bba58250c54e'; 
    $client_secret = 'db016607c4395f05df1eeb1f18e93ae2';

    $response_type = 'code';
    $scope = 'basic_user_info'; 
    $redirect_uri ='http://127.0.0.1/oauth.php';
    $state  = 'bla';
    $grant_type = 'authorization_code';

    $auth_host = 'dev04c6.srv.office:22406';
    $apps_host = 'dev04c6.srv.office:22406';
    $url = "https://{$auth_host}/oauth?client_id={$client_id}&response_type={$response_type}&scope={$sc ope}&redirect_uri={$redirect_uri}&state={$state}";
?>


<!-- Requisição do código de autenticação - Como explicado na seção 2.1.1 do Manual do OAuth -->
<!-- O usuário deve clicar no link para iniciar o 'oauth login' -->
<a href="<?php echo $url; ?>">Fazer login no olx.com.br</a><br><br>
<!-- uma vez clicado, o usuário deverá se autenticar no OLX e autorizar a sua aplicação a acessar seus dados -->

<?php
    # isso só deve ocorrer após o recebimento do 'code' no redirect do oauth 
    if (isset($_GET['code'])) {
            $code = $_GET['code'];

            # dados necessários para a requisição do token de acesso
            $fields = array(
                'code' => $code,
                'client_id' => $client_id,
                'client_secret' => $client_secret,
                'redirect_uri' => $redirect_uri,
                'grant_type' => $grant_type
            );

            # Requisição da chave de acesso - Como explicado na seção 2.2.1 do Manual do OAuth 
            # para utilizar o método 'http_post_fields', instalar o pacote: pecl_http 
            $response = http_post_fields("https://{$auth_host}/oauth/token",$fields);

            # separa o header do body do pacote http
            $res = preg_split("#\n\\s*?\n#", $response, 2);
            $data = json_decode($res[1]);
            echo "access_token: {$data->access_token}<br />";

            # salvar access_token
            #
            # O access_token deve ser salvo para evitar a necessidade de fazer novamente o handshake do OAuth 
            //$generic_database->saveAccessToken($data->access_token); // comando de exemplo

            $request_data =array('access_token'=>$data->access_token);

            # Acesso à API - Como explicado na seção 3.1 do Manual do OAuth neste exemplo, estamos acessando o resource basic_user_info que simplesmente retorna informações básicas do usuário para utilizar o método 'http_post_data', instalar o pacote: pecl_http 
            $response = http_post_data("https://{$apps_host}/oauth_api/basic_user_info", json_encode($request_data));

            # separa o header do body do pacote http
            $res = preg_split("#\n\\s*?\n#", $response, 2); echo "basic_user_info: {$res[1]}";
        }
?>
```

## Referências

- \[RFC6749] [The OAuth 2.0 Authorization Frameworkopen in new window](http://tools.ietf.org/html/rfc6749)
- [Using OAuto 2.0 for Web Server Applicationsopen in new window](https://developers.google.com/accounts/docs/OAuth2WebServer?hl=pt-BR)