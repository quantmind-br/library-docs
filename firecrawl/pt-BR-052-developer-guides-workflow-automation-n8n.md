---
title: Firecrawl + n8n - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/developer-guides/workflow-automation/n8n
source: sitemap
fetched_at: 2026-03-23T07:27:23.259121-03:00
rendered_js: false
word_count: 3559
summary: This guide provides instructions on setting up Firecrawl and n8n to build automated web scraping workflows without writing custom code.
tags:
    - web-scraping
    - n8n-automation
    - firecrawl
    - workflow-automation
    - data-extraction
    - api-integration
category: guide
---

## Introdução ao Firecrawl e n8n

A automação de web scraping se tornou essencial para empresas modernas. Seja para monitorar preços de concorrentes, agregar conteúdo, gerar leads ou alimentar aplicações de IA com dados em tempo real, a combinação de Firecrawl e n8n oferece uma solução poderosa sem exigir conhecimentos de programação. ![Integração do Firecrawl com n8n](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/firecrawl-n8n-integration-hero.png?fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=cb863000a893ef260cfe023e2455c88c) **O que é o n8n?** O n8n é uma plataforma de automação de fluxos de trabalho de código aberto que conecta diferentes ferramentas e serviços. Pense nele como um ambiente de programação visual em que você arrasta e solta nós em uma tela, conecta-os e cria fluxos automatizados. Com mais de 400 integrações, o n8n permite criar automações complexas sem escrever código.

A extração tradicional de dados da web apresenta vários desafios. Scripts personalizados falham quando os sites atualizam sua estrutura. Sistemas antibot bloqueiam solicitações automatizadas. Sites com muito JavaScript não são renderizados corretamente. A infraestrutura exige manutenção constante. O Firecrawl cuida dessas complexidades técnicas na parte de extração, enquanto o n8n fornece o framework de automação. Juntos, eles permitem criar fluxos de trabalho prontos para produção que:

- Extraem dados de qualquer site com confiabilidade
- Conectam os dados extraídos a outras ferramentas de negócio
- Roda em agendas programadas ou acionados por eventos
- Escalam de tarefas simples a pipelines complexos

Este guia vai orientá-lo na configuração de ambas as plataformas e na criação do seu primeiro fluxo de trabalho de extração do zero.

## Etapa 1: Crie sua conta na Firecrawl

A Firecrawl fornece recursos de web scraping para seus fluxos de trabalho. Vamos configurar sua conta e obter suas credenciais de API.

### Crie sua conta no Firecrawl

1. Acesse [firecrawl.dev](https://firecrawl.dev) no seu navegador
2. Clique no botão “Get Started” ou “Sign Up”
3. Crie uma conta usando seu e-mail ou o login do GitHub
4. Verifique seu e-mail, se for solicitado

### Obtenha sua chave de API

Depois de fazer login, você precisa de uma chave de API para conectar o Firecrawl ao n8n:

1. Acesse seu dashboard do Firecrawl
2. Vá até a [página de API Keys](https://www.firecrawl.dev/app/api-keys)
3. Clique em “Create New API Key”
4. Dê um nome descritivo à sua chave (por exemplo, “Integração n8n”)
5. Copie a chave de API gerada e guarde-a em um local seguro

![Firecrawl api key section](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/firecrawl-api-key-creation-dashboard.gif?s=2c04559b9027dfe825e3ba7d78af8527)

O Firecrawl oferece créditos gratuitos ao se cadastrar, suficientes para testar seus fluxos de trabalho e concluir este tutorial.

## Etapa 2: Configurar o n8n

O n8n oferece duas opções de implantação: hospedado na nuvem ou autogerenciado. Para iniciantes, a versão em nuvem é a forma mais rápida de começar.

### Escolha a sua versão do n8n

**n8n Cloud (recomendado para iniciantes):**

- Nenhuma instalação necessária
- Plano gratuito disponível
- Infraestrutura gerenciada
- Atualizações automáticas

**Self-Hosted:**

- Controle total dos dados
- Execução nos seus próprios servidores
- Exige instalação do Docker
- Ideal para usuários avançados com requisitos específicos de segurança

Escolha a opção que melhor atenda às suas necessidades. Ambos os caminhos levam à mesma interface do editor de fluxos de trabalho.

### Opção A: n8n Cloud (Recomendado para iniciantes)

1. Acesse [n8n.cloud](https://n8n.cloud)
2. Clique em “Start Free” ou “Sign Up”
3. Cadastre-se usando seu e-mail ou GitHub
4. Conclua a verificação
5. Você será redirecionado ao seu painel do n8n

![Página inicial do n8n Cloud mostrando as opções de cadastro](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-cloud-signup-homepage.png?fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=7965f6fab8bd1d48b81db7c1dbed1e7f) O plano gratuito oferece tudo o que você precisa para criar e testar fluxos de trabalho. Você pode fazer upgrade depois se precisar de mais tempo de execução ou recursos avançados.

### Opção B: Self-hosted com Docker

Se preferir executar o n8n na sua própria infraestrutura, você pode configurá-lo rapidamente usando Docker. **Pré-requisitos:**

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado no computador
- Familiaridade básica com o terminal/linha de comando

**Etapas de instalação:**

1. Abra o terminal ou o prompt de comando
2. Crie um volume do Docker para manter os dados dos seus workflows:

```
docker volume create n8n_data
```

Este volume armazena seus fluxos de trabalho, credenciais e histórico de execução, garantindo que persistam mesmo se você reiniciar o contêiner.

3. Execute o contêiner Docker do n8n:

```
docker run -it --rm --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
```

![Terminal exibindo os comandos do Docker sendo executados com o n8n iniciando](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-docker-self-hosted-installation.gif?s=4968ecd0996ef3e76dc0abb886ae52ca)

4. Aguarde o n8n iniciar. Você verá uma saída indicando que o servidor está em execução.
5. Abra seu navegador e acesse `http://localhost:5678`.
6. Crie sua conta no n8n registrando um e-mail.

![Tela de boas-vindas do n8n self-hosted em localhost:5678](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-localhost-registration-form.gif?fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=163949933d76425a68ec728639e767ea) Sua instância self-hosted do n8n agora está sendo executada localmente. A interface é idêntica à do n8n Cloud, então você pode seguir o restante deste guia, independentemente da opção escolhida.

### Entendendo a interface do n8n

Ao fazer login no n8n pela primeira vez, você verá o painel principal: ![n8n dashboard showing the workflow list view with "Create new workflow" button](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-dashboard-workflow-list.png?fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=5d92092b94fd021c2cebf163c2ef4d01) Principais elementos da interface:

- **Workflows**: Suas automações salvas aparecem aqui
- **Executions**: Histórico de execuções de workflows
- **Credentials**: Chaves de API e tokens de autenticação armazenados
- **Settings**: Configurações da conta e do workspace

Clique em “Create New Workflow” para abrir o editor de workflows.

### A Tela do Workflow

O editor de workflow é onde você vai criar suas automações: ![Canvas de workflow vazio do n8n com o botão "+" visível no centro](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-empty-workflow-canvas.png?fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=7508078e88b57ccedc2a4d4a258fddf8) Elementos importantes:

- **Canvas**: A área principal onde você posiciona e conecta nós
- **Botão Adicionar Nó (+)**: Clique para adicionar novos nós ao seu workflow
- **Painel de Nós**: Abre ao clicar em ”+”, exibindo todos os nós disponíveis
- **Executar Workflow**: Executa seu workflow manualmente para testes
- **Salvar**: Salva a configuração do seu workflow

Vamos criar seu primeiro workflow adicionando o nó Firecrawl.

## Etapa 3: Instalar e configurar o nó do Firecrawl

O n8n tem suporte nativo ao Firecrawl. Instale o nó e conecte-o à sua conta do Firecrawl usando a chave de API criada anteriormente.

### Adicione o nó do Firecrawl ao seu fluxo de trabalho

1. No novo canvas do seu fluxo de trabalho, clique no botão ”**+**” no centro
2. O painel de seleção de nós abrirá no lado direito
3. Na caixa de pesquisa no topo, digite “**Firecrawl**”
4. Você verá o nó do Firecrawl aparecer nos resultados da pesquisa

<!--THE END-->

![Clicando no botão +, digitando "Firecrawl" na pesquisa e o nó do Firecrawl aparecendo](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-search-install-firecrawl-node.gif?s=6d81f8bf967429cfaf2bcf22c3976fbf)

5. Clique em “**Install**” ao lado do nó do Firecrawl
6. Aguarde a conclusão da instalação (isso leva alguns segundos)
7. Após a instalação, clique no nó do Firecrawl para adicioná-lo ao seu canvas

![Nó do Firecrawl agora adicionado ao canvas, exibido como uma caixa com o logo do Firecrawl](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-firecrawl-node-added-canvas.gif?s=d7480ebf8ef357fba9a0c5ee5123ffc8) O nó do Firecrawl aparecerá no seu canvas como uma caixa com o logo do Firecrawl. Esse nó representa uma única operação do Firecrawl no seu fluxo de trabalho.

### Conecte sua chave de API do Firecrawl

Antes de usar o nó do Firecrawl, você precisa autenticá-lo com sua chave de API:

1. Clique na caixa do nó do Firecrawl para abrir o painel de configuração à direita
2. No topo, você verá um menu suspenso “Credential to connect with”
3. Como esta é sua primeira vez, clique em “**Create New Credential**”

<!--THE END-->

![Painel de configuração do nó Firecrawl mostrando o menu suspenso de credenciais com a opção "Create New Credential"](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-firecrawl-api-credentials-setup.gif?s=547bda13daeb17dd963160a8ef4bbf48)

4. Uma janela de configuração de credenciais será aberta
5. Insira um nome para essa credencial (por exemplo, “Minha conta Firecrawl”)
6. Cole sua chave de API do Firecrawl no campo “API Key”
7. Clique em “**Save**” na parte inferior

A credencial agora está salva no n8n. Você não precisará inserir sua chave de API novamente nos próximos nós do Firecrawl.

### Teste sua conexão

Vamos verificar se seu nó do Firecrawl está corretamente conectado:

1. Com o nó do Firecrawl ainda selecionado, veja o painel de configuração
2. No menu suspenso “Resource”, selecione “**Scrape a url and get its content**”
3. No campo “URL”, insira: `https://firecrawl.dev`
4. Deixe as outras configurações nos padrões por enquanto
5. Clique no botão “**Test step**” no canto inferior direito do nó

![Selecionando a operação Scrape, inserindo a URL example.com e clicando no botão Test step](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-firecrawl-test-connection-scrape.gif?s=a5a832a971778744a6ceaf9d2ff0cdb1) Se tudo estiver configurado corretamente, o conteúdo extraído de example.com aparecerá no painel de saída abaixo do nó. Parabéns! Seu nó do Firecrawl está conectado e funcionando.

## Etapa 4: Crie seu bot no Telegram

Antes de montar seu primeiro workflow, você precisará de um bot no Telegram para receber notificações. Bots do Telegram são gratuitos e fáceis de criar com o BotFather.

### Crie um bot com o BotFather

1. Abra o Telegram no seu celular ou no desktop
2. Procure por “**@BotFather**” (o bot oficial do Telegram)
3. Inicie uma conversa com o BotFather clicando em “**Start**”
4. Envie o comando `/newbot` para criar um novo bot
5. O BotFather pedirá que você escolha um nome para o seu bot (é o nome exibido para os usuários)
6. Insira um nome como “**My Firecrawl Bot**”
7. Em seguida, escolha um nome de usuário para o seu bot. Ele deve terminar com “bot” (por exemplo, “**my\_firecrawl\_updates\_bot**”)
8. Se o nome de usuário estiver disponível, o BotFather criará seu bot e enviará uma mensagem com o token do bot

![Criando um bot com o BotFather, mostrando todo o fluxo da conversa](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/telegram-botfather-create-new-bot.png?fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=45ee39deae96fbc3eac5fdb2eeba2e0b)

### Obtenha seu Chat ID

Para enviar mensagens para si mesmo, você precisa do seu chat ID do Telegram:

1. Abra o navegador e acesse esta URL (substitua `YOUR_BOT_TOKEN` pelo token real do seu bot):
   
   ```
   https://api.telegram.org/botYOUR_BOT_TOKEN/getUpdates
   ```
2. Mantenha essa aba do navegador aberta
3. Agora, procure pelo nome de usuário do seu bot no Telegram (o que você acabou de criar)
4. Inicie uma conversa com o bot clicando em “**Start**”
5. Envie qualquer mensagem para o bot (por exemplo, “hello”)
6. Volte para a aba do navegador e atualize a página
7. Procure pelo campo `"chat":{"id":` na resposta JSON
8. O número ao lado de `"id":` é o seu chat ID (por exemplo, `123456789`)
9. Guarde esse chat ID para usar depois

![Browser showing Telegram API getUpdates response with chat ID highlighted](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/telegram-api-get-chat-id-browser.gif?s=e074ecf1a659bdfa7284e86c923be06f)

Agora você tem tudo o que precisa para integrar o Telegram aos seus fluxos no n8n.

Agora, vamos montar três fluxos de trabalho reais que enviam informações diretamente para o seu Telegram. Esses exemplos mostram diferentes operações do Firecrawl e como integrá-las com notificações no Telegram.

### Exemplo 1: Resumo diário das atualizações do produto Firecrawl

Receba um resumo diário das atualizações do produto Firecrawl no seu Telegram todas as manhãs. **O que você vai construir:**

- Faz o scraping do blog de atualizações de produto do Firecrawl diariamente às 9h
- Usa IA para gerar um resumo do conteúdo
- Envia o resumo para o seu Telegram

**Passo a passo:**

1. Crie um novo workflow no n8n
2. Adicione um nó **Schedule Trigger**:
   
   - Clique no botão ”**+**” no canvas
   - Pesquise por “**Schedule Trigger**”
   - Configure: Todos os dias às 9:00

<!--THE END-->

![Schedule Trigger configured for daily 9 AM execution](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-schedule-trigger-daily-cron.gif?s=ae68cd74cdf14a1d012861df8319b245)

3. Adicione o nó **Firecrawl**:
   
   - Clique em ”**+**” ao lado de Schedule Trigger
   - Pesquise e adicione “**Firecrawl**”
   - Selecione sua credencial do Firecrawl
   - Configure:
     
     - **Resource**: Scrape a URL e obtenha seu conteúdo
     - **URL**: `https://www.firecrawl.dev/blog/category/product-updates`
     - **Formats**: Selecione “Summary”

<!--THE END-->

![Adding and configuring Firecrawl node with the blog URL and Summary format selected](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-firecrawl-scrape-blog-summary.gif?s=ad1684f165aacd7ab5d1530cdac73962)

4. Adicione o nó **Telegram**:
   
   - Clique em ”**+**” ao lado de Firecrawl
   - Pesquise por “**Telegram**”
   - Clique em “**Send a text message**” para adicioná-lo ao canvas
5. Configure as credenciais do Telegram:
   
   - Clique no nó do Telegram para abrir sua configuração
   - No menu “Credential to connect with”, clique em “**Create New Credential**”
   - Cole o token do seu bot do BotFather
   - Clique em “**Save**”

<!--THE END-->

![Telegram credential configuration with bot token field](https://mintlify.s3.us-west-1.amazonaws.com/firecrawl/images/guides/n8n/n8n-telegram-bot-token-credentials.gif)

6. Configure a mensagem do Telegram:
   
   - **Operation**: Send Message
   - **Chat ID**: Insira seu chat ID
   - **Text**: Deixe com uma mensagem “hello” por enquanto
   - Clique em **Execute step** para testar o envio de uma mensagem enquanto recebe o resumo do Firecrawl.

<!--THE END-->

![Configuring Telegram node and mapping the summary field to the message text](https://mintlify.s3.us-west-1.amazonaws.com/firecrawl/images/guides/n8n/n8n-test-telegram-message-firecrawl.gif)

- Agora, com a estrutura de resumo do Firecrawl, adicione o resumo ao texto da mensagem arrastando o campo `summary` da saída do nó do Firecrawl.

<!--THE END-->

7. Teste o workflow:
   
   - Clique em “**Execute Workflow**”
   - Verifique no seu Telegram a mensagem com o resumo

<!--THE END-->

![Complete workflow showing Schedule Trigger → Firecrawl → Telegram with all nodes connected](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-workflow-complete-firecrawl-telegram.png?fit=max&auto=format&n=ATrkZnTEGYY5UO9D&q=85&s=1c3eacbcb705c21c6265ae3ecbd59d59)

8. Ative o workflow alternando a chave “**Active**”

Seu bot do Telegram agora enviará um resumo diário das atualizações do produto Firecrawl todas as manhãs às 9h.

### Exemplo 2: Pesquisa de notícias de IA para o Telegram

Este fluxo usa a operação Search do Firecrawl para encontrar notícias de IA e enviar resultados formatados para o Telegram. **Principais diferenças em relação ao Exemplo 1:**

- Usa um **Manual Trigger** em vez de Schedule (executa sob demanda)
- Usa a operação **Search** em vez de Scrape
- Inclui um nó **Code** para formatar múltiplos resultados

**Crie o fluxo:**

1. Crie um novo fluxo e adicione um nó **Manual Trigger**
2. Adicione o nó **Firecrawl** com estas configurações:
   
   - **Resource**: Search and optionally scrape search results
   - **Query**: `ai news`
   - **Limit**: 5

<!--THE END-->

![Firecrawl Search node configuration with "ai news" query](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-firecrawl-search-ai-news-results.gif?s=23eb224783b0b3155d179a0342839621)

3. Adicione um nó **Code** para formatar os resultados da pesquisa:
   
   - Selecione “Run Once for All Items”
   - Cole este código:

```
const results = $input.all();
let message = "Últimas Notícias sobre IA:\n\n";

results.forEach((item) => {
  const webData = item.json.data.web;
  webData.forEach((article, index) => {
    message += `${index + 1}. ${article.title}\n`;
    message += `${article.description}\n`;
    message += `${article.url}\n\n`;
  });
});

return [{ json: { message } }];
```

![Adicionando o nó Code e colando o script de formatação](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-code-node-format-news-articles.gif?s=cafb96e0b7f2ef27a09ae2957390799b)

4. Atualize o nó **Telegram** (usando a credencial salva):
   
   - **Text**: Arraste o campo `message` do nó Code
   - **Chat ID**: Defina o Chat ID do destinatário

![Execução completa do fluxo com notícias de IA enviadas para o Telegram](https://mintlify.s3.us-west-1.amazonaws.com/firecrawl/images/guides/n8n/n8n-execute-workflow-telegram-delivery.gif)

### Exemplo 3: Resumo de notícias com IA

Este fluxo de trabalho adiciona IA ao Exemplo 2, usando a OpenAI para gerar resumos inteligentes das últimas notícias sobre IA antes de enviá-las ao Telegram. **Principais mudanças em relação ao Exemplo 2:**

- Adicionar a configuração de **credenciais da OpenAI**
- Adicionar o nó **AI Agent** entre Code e Telegram
- O AI Agent analisa e resume todos os artigos de forma inteligente
- O Telegram recebe o resumo gerado por IA em vez da lista bruta de notícias

**Modifique o fluxo de trabalho:**

1. **Obtenha sua chave de API da OpenAI**:
   
   - Acesse [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
   - Faça login ou crie uma conta
   - Clique em “**Create new secret key**”
   - Dê um nome (por exemplo, “n8n Integration”)
   - Copie a chave de API imediatamente (você não a verá novamente)

<!--THE END-->

![OpenAI dashboard showing API key creation](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/openai-api-key-creation-dashboard.gif?s=8222a339a403f85272102256fa91fc27)

2. **Adicione e conecte o nó AI Agent**:
   
   - Clique em ”**+**” após o nó Code
   - Pesquise por “**Basic LLM Chain**” ou “**AI Agent**”
   - Arraste o campo `message` do nó Code para o campo de prompt de entrada do AI Agent
   - Selecione **OpenAI** como provedor de LLM

<!--THE END-->

![Adding AI Agent node, dragging input from Code node, and connecting OpenAI as LLM](https://mintlify.s3.us-west-1.amazonaws.com/firecrawl/images/guides/n8n/n8n-ai-agent-openai-llm-setup.gif)

3. **Adicione suas credenciais da OpenAI**:
   
   - Clique em “**Create New Credential**” para OpenAI
   - Cole sua chave de API da OpenAI
   - Selecione o modelo: **gpt-5-mini** (mais econômico) ou **gpt-5** (mais capaz)
   - Clique em “**Save**”

<!--THE END-->

![Adding OpenAI credentials to the AI Agent node](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-openai-credentials-gpt-model.gif?s=c97249f572e8d530583918ebc3357d53)

4. **Adicione o system prompt ao AI Agent**:
   
   - No nó AI Agent, adicione este system prompt:

```
Você é um analista de notícias sobre IA. Analise os artigos de notícias sobre IA fornecidos e crie um resumo
conciso e esclarecedor destacando os principais desenvolvimentos e tendências.
Agrupe tópicos relacionados e forneça contexto sobre a importância desses desenvolvimentos.
Mantenha o resumo em tom conversacional e envolvente, com cerca de 3-4 parágrafos.
```

![Adicionando o prompt de sistema ao nó AI Agent](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-ai-agent-system-prompt-configuration.gif?s=45c34c7010aa6319f8d4dde84c6e5ab9)

5. **Atualize o nó do Telegram e teste**:
   
   - Atualize o nó do Telegram:
     
     - **Text**: Arraste a saída do AI Agent (o resumo gerado)
     - Remova o mapeamento antigo da mensagem do nó Code
   - Clique em “**Execute Workflow**” para testar
   - A IA analisará todas as matérias/notícias e criará um resumo
   - Confira no seu Telegram o resumo gerado pela IA

![Execução completa do workflow com resumo gerado pela IA enviado para o Telegram](https://mintlify.s3.us-west-1.amazonaws.com/firecrawl/images/guides/n8n/n8n-ai-summary-telegram-workflow-execution.gif)

## Entendendo as operações do Firecrawl

Agora que você criou alguns fluxos de trabalho, vamos explorar as diferentes operações do Firecrawl disponíveis no n8n. Cada operação foi projetada para casos de uso específicos de raspagem de dados na web.

### Fazer scrape de uma URL e obter seu conteúdo

Extrai o conteúdo de uma única página da web e o retorna em vários formatos. **O que faz:**

- Faz scrape de uma única URL
- Retorna Markdown limpo, HTML ou resumos gerados por IA
- Pode capturar capturas de tela e extrair links

**Melhor para:**

- Extração de artigos
- Monitoramento de páginas de produto
- Scrape de postagens de blog
- Geração de resumos de páginas

**Exemplo de caso de uso:** Resumos diários de blogs (como no Exemplo 1 acima)

### Pesquise e, opcionalmente, faça a coleta dos resultados

Realiza buscas na web e retorna resultados com opção de coleta de conteúdo. **O que faz:**

- Pesquisa na web, em notícias ou imagens
- Retorna títulos, descrições e URLs
- Opcionalmente coleta o conteúdo completo dos resultados

**Melhor para:**

- Automação de pesquisas
- Monitoramento de notícias
- Descoberta de tendências
- Encontrar conteúdo relevante

**Exemplo de caso de uso:** agregação de notícias por IA (como o Exemplo 2 acima)

### Rastrear um site

Descobre e extrai várias páginas de um site de forma recursiva. **O que faz:**

- Segue links automaticamente
- Extrai várias páginas em uma única operação
- Pode filtrar URLs por padrões

**Melhor para:**

- Extração completa de documentação
- Arquivamento de sites
- Coleta de dados em várias páginas

### Mapear um site e obter URLs

Retorna todas as URLs encontradas em um site sem extrair o conteúdo. **O que faz:**

- Descobre todos os links de um site
- Retorna uma lista limpa de URLs
- Rápido e leve

**Ideal para:**

- Descoberta de URLs
- Geração de sitemap
- Planejamento de crawls maiores

Usa IA para extrair informações estruturadas com base em prompts ou esquemas personalizados. **O que faz:**

- Extração de dados com IA
- Retorna dados no formato que você especificar
- Funciona em várias páginas

**Ideal para:**

- Extração de dados personalizada
- Criação de bancos de dados
- Coleta de informações estruturadas

### Coleta em Lote

Raspagem de várias URLs em paralelo com eficiência. **O que faz:**

- Processa várias URLs de uma vez
- Mais eficiente do que usar loops
- Retorna todos os resultados de uma só vez

**Ideal para:**

- Processar listas de URLs
- Coleta de dados em massa
- Projetos de raspagem em larga escala

### Agent

Usa um agente de IA para navegar e extrair dados de sites de forma autônoma com base em um prompt em linguagem natural. **O que ele faz:**

- Aceita um prompt descrevendo quais dados você precisa
- O agente de IA navega e extrai informações de forma autônoma
- Disponível nos modos **Sync** (aguarda os resultados) e **Async** (retorna um ID de job imediatamente)
- Use **Get Agent Status** para consultar os resultados ao usar o modo Async

**Melhor para:**

- Coleta de dados complexa em várias páginas, guiada por um prompt
- Extração de informações quando você não conhece a estrutura exata da página
- Tarefas de pesquisa que exigem navegação por múltiplas páginas

**Sync vs. Async:**

- **Agent (Sync)** inicia o job e aguarda o resultado em uma única etapa — mais simples para a maioria dos casos de uso. O parâmetro **Max Wait Time** controla por quanto tempo o nó consulta antes de expirar (padrão: 300 segundos, máximo: 600 segundos). Se o job do agente demorar mais do que isso, o nó retornará um status de timeout, mesmo que o job ainda possa ser concluído no lado do Firecrawl. Para jobs que possam exceder 10 minutos, use o modo async.
- **Agent (Async)** retorna um ID de job imediatamente. Adicione um segundo nó do Firecrawl com a operação **Get Agent Status** para recuperar os resultados quando o job for concluído.

Para detalhes sobre o recurso de agente, consulte a [documentação do Agent](https://docs.firecrawl.dev/pt-BR/features/agent).

## Modelos e exemplos de workflows

Em vez de começar do zero, você pode usar modelos prontos. A comunidade do n8n criou diversos workflows do Firecrawl que você pode copiar e personalizar.

### Modelos em destaque

### Como importar templates

Para usar um template da comunidade do n8n:

1. Clique em um link de template de workflow
2. Clique no botão “**Import template to localhost:5678 self-hosted instance**” na página do template
3. O workflow será aberto na sua instância do n8n
4. Configure as credenciais de cada nó
5. Personalize as configurações para o seu caso de uso
6. Ative o workflow

![Importando um template do n8n.io, mostrando o botão de importação e o workflow aparecendo no n8n](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-workflow-import.gif?s=5bd77d25fa2dc525e0032a483803fd00)

## Boas práticas

Siga estas diretrizes para criar fluxos de trabalho confiáveis e eficientes:

### Testes e Depuração

- Sempre teste os fluxos manualmente antes de ativar os agendamentos
- Use o botão “**Execute Workflow**” para testar todo o fluxo
- Verifique os dados de saída em cada nó para confirmar a precisão
- Use a aba “**Executions**” para revisar execuções anteriores e depurar problemas

![Aba Executions mostrando o histórico de execuções do fluxo com carimbos de data/hora e status](https://mintcdn.com/firecrawl/ATrkZnTEGYY5UO9D/images/guides/n8n/n8n-debugging.gif?s=2962335b6f72ea39cf6cb68cb6ed83c3)

### Tratamento de erros

- Adicione nós de gatilho de erro para capturar e lidar com falhas
- Configure notificações quando fluxos de trabalho falharem
- Use a opção “**Continue On Fail**” para nós não críticos
- Monitore regularmente as execuções do seu fluxo de trabalho

### Otimização de desempenho

- Use o Batch Scrape para várias URLs em vez de loops
- Defina limites de taxa adequados para evitar sobrecarregar os sites de destino
- Faça cache dos dados quando possível para reduzir requisições desnecessárias
- Agende fluxos de trabalho intensivos fora do horário de pico

### Segurança

- Nunca exponha chaves de API nas configurações de workflows
- Use o sistema de credenciais do n8n para armazenar autenticações com segurança
- Tenha cuidado ao compartilhar workflows publicamente
- Siga os termos de serviço e o arquivo robots.txt dos sites-alvo

## Próximos passos

Agora você tem os fundamentos para criar automações de web scraping com Firecrawl e n8n. Veja como continuar aprendendo:

### Explore recursos avançados

- Estude configurações de webhooks para processamento de dados em tempo real
- Experimente extração com IA usando prompts e esquemas
- Construa fluxos de trabalho complexos em múltiplas etapas com lógica ramificada

<!--THE END-->

- [Firecrawl Discord](https://discord.gg/firecrawl) - Tire dúvidas sobre o Firecrawl e discuta web scraping
- [n8n Community Forum](https://community.n8n.io/) - Faça perguntas sobre automação de workflows
- Compartilhe seus workflows e aprenda com outras pessoas

### Trilha de Aprendizado Recomendada

1. Conclua os fluxos de trabalho de exemplo deste guia
2. Adapte modelos da biblioteca da comunidade
3. Crie um fluxo de trabalho para resolver um problema real do seu dia a dia
4. Explore operações avançadas do Firecrawl
5. Contribua com seus próprios modelos para ajudar outras pessoas

## Recursos adicionais

- [Documentação da API Firecrawl](https://docs.firecrawl.dev/pt-BR/api-reference/v2-introduction)
- [Documentação do n8n](https://docs.n8n.io/)
- [Boas práticas de web scraping](https://www.firecrawl.dev/blog)