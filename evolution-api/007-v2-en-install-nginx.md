---
title: Nginx and SSL - Evolution API Documentation
url: https://doc.evolution-api.com/v2/en/install/nginx
source: sitemap
fetched_at: 2026-04-12T18:46:43.932587719-03:00
rendered_js: false
word_count: 118
summary: This document provides a step-by-step guide on how to install and configure Nginx as a reverse proxy to securely expose an API, including setting up virtual hosts and securing the service with SSL using Certbot.
tags:
    - nginx
    - reverse-proxy
    - api-configuration
    - ssl-setup
    - linux-guide
    - webserver
category: guide
---

## Nginx Configuration

To securely expose the Evolution API on the web, you can configure Nginx as a reverse proxy.

### Installing Nginx

Install, start, and enable Nginx:

```
apt-get install -y nginx
systemctl start nginx
systemctl enable nginx
systemctl status nginx
```

If the message “Active: active (running)” appears, Nginx is working correctly.

### Nginx Configuration

Remove the default Nginx configuration:

```
rm /etc/nginx/sites-enabled/default
```

Create a new configuration file:

```
nano /etc/nginx/conf.d/default.conf
```

Add the following configuration:

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

Reload Nginx to apply the changes:

If necessary, make the `nginx` user the owner of the web directory:

```
chown www-data:www-data /usr/share/nginx/html -R
```

To configure a Virtual Host, create a configuration file:

```
nano /etc/nginx/sites-available/api
```

Add the following configuration:

```
server {
  server_name replace-this-with-your-cool-domain.com;

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

Create a symbolic link to enable the configuration:

```
ln -s /etc/nginx/sites-available/api /etc/nginx/sites-enabled
nginx -t
```

Reload Nginx:

## Install Certbot for SSL Certificate

To secure your Evolution API with SSL, install Certbot:

```
snap install --classic certbot
```

### Configure SSL with Certbot

To configure SSL, use the command:

```
certbot --nginx -d replace-this-with-your-cool-domain.com
```