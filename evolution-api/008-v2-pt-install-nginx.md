---
title: Nginx e SSL - Evolution API Documentation
url: https://doc.evolution-api.com/v2/pt/install/nginx
source: sitemap
fetched_at: 2026-04-12T18:45:54.047346484-03:00
rendered_js: false
word_count: 136
summary: This document provides a comprehensive guide on setting up Nginx as a reverse proxy to securely expose an Evolution API on the web, including detailed steps for initial setup, virtual host configuration, and securing the service with SSL using Certbot.
tags:
    - nginx-configuration
    - reverse-proxy
    - ssl-setup
    - api-exposure
    - linux-guide
    - webserver
category: guide
---

## Configuração do Nginx

Para expor a Evolution API na web de forma segura, você pode configurar o Nginx como um proxy reverso.

### Instalação do Nginx

Instale, inicie e habilite o Nginx:

```
apt-get install -y nginx
systemctl start nginx
systemctl enable nginx
systemctl status nginx
```

Se a informação “Ativo: ativo (em execução)” aparecer, o Nginx está funcionando corretamente.

### Configuração do Nginx

Remova a configuração padrão do Nginx:

```
rm /etc/nginx/sites-enabled/default
```

Crie um novo arquivo de configuração:

```
nano /etc/nginx/conf.d/default.conf
```

Adicione a seguinte configuração:

```
server {
  listen 80;
  listen [::]:80;
  server_name _;

  location / {
    proxy_pass http://127.0.0.1:8080;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection 'upgrade';
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_cache_bypass $http_upgrade;
  }

  location ~* \.(jpg|jpeg|gif|png|webp|svg|woff|woff2|ttf|css|js|ico|xml)$ {
    expires 360d;
  }

  location ~ /\.ht {
    deny all;
  }
}
```

Recarregue o Nginx para aplicar as alterações:

Se necessário, faça o usuário `nginx` ser o proprietário do diretório da web:

```
chown www-data:www-data /usr/share/nginx/html -R
```

Para configurar um Virtual Host, crie um arquivo de configuração:

```
nano /etc/nginx/sites-available/api
```

Adicione a seguinte configuração:

```
server {
  server_name substitua-isso-pelo-seu-domínio-legal.com;

  location / {
    proxy_pass http://127.0.0.1:8080;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection 'upgrade';
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_cache_bypass $http_upgrade;
  }
}
```

Crie um link simbólico para habilitar a configuração:

```
ln -s /etc/nginx/sites-available/api /etc/nginx/sites-enabled
nginx -t
```

Recarregue o Nginx:

## Instalar o Certbot para o Certificado SSL

Para proteger sua Evolution API com SSL, instale o Certbot:

```
snap install --classic certbot
```

### Configurar SSL com Certbot

Para configurar o SSL, use o comando:

```
certbot --nginx -d substitua-isso-pelo-seu-domínio-legal.com
```