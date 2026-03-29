---
title: Docker Install
url: https://epi052.github.io/feroxbuster-docs/installation/docker
source: github_pages
fetched_at: 2026-02-06T10:56:45.51604181-03:00
rendered_js: true
word_count: 153
summary: This document explains how to use the feroxbuster web discovery tool within a Docker container, including instructions for configuration, piping input, and using proxies.
tags:
    - feroxbuster
    - docker
    - container-usage
    - network-security
    - web-fuzzing
    - cli-tool
category: tutorial
---

> The following steps assume you have docker installed / setup

Thanks to github user **@EONRaider**, we have an official docker image pushed to the docker hub with each new release.

You can simply jump right into usage with `sudo docker run epi052/feroxbuster ...`!

```

sudodockerrun--init-itepi052/feroxbuster-uhttp://example.com-xjs,html
```

## Piping from stdin and proxying all requests through socks5 proxy

[Section titled “Piping from stdin and proxying all requests through socks5 proxy”](#piping-from-stdin-and-proxying-all-requests-through-socks5-proxy)

```

cattargets.txt|sudodockerrun--net=host--init-iepi052/feroxbuster--stdin-xjs,html--proxysocks5://127.0.0.1:9050
```

## Mount a volume to pass in ferox-config.toml

[Section titled “Mount a volume to pass in ferox-config.toml”](#mount-a-volume-to-pass-in-ferox-configtoml)

You’ve got some options available if you want to pass in a config file. [ferox-config.toml](https://epi052.github.io/feroxbuster-docs/configuration/ferox-config-toml/) can live in multiple locations and still be valid, so it’s up to you how you’d like to pass it in. Below are a few valid examples:

```

sudodockerrun--init-v $(pwd)/ferox-config.toml:/etc/feroxbuster/ferox-config.toml-itepi052/feroxbuster-uhttp://example.com
```

```

sudodockerrun--init-v~/.config/feroxbuster:/root/.config/feroxbuster-itepi052/feroxbuster-uhttp://example.com
```

Note: If you are on a SELinux enforced system, you will need to pass the `:Z` attribute also.

```

dockerrun--init-v (pwd)/ferox-config.toml:/etc/feroxbuster/ferox-config.toml:Z -it epi052/feroxbuster -u http://example.com
```

## Define an alias for simplicity

[Section titled “Define an alias for simplicity”](#define-an-alias-for-simplicity)

```

aliasferoxbuster="sudo docker run --init -v ~/.config/feroxbuster:/root/.config/feroxbuster -i epi052/feroxbuster"
```