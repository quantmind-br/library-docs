---
title: Code blocks
url: https://docs.docker.com/contribute/components/code-blocks/
source: llms
fetched_at: 2026-01-24T14:01:52.446031837-03:00
rendered_js: false
word_count: 212
summary: This document provides instructions on using Rouge syntax highlighting hints and formatting features for code blocks, including variable placeholders and language-specific identifiers.
tags:
    - syntax-highlighting
    - rouge-formatter
    - code-blocks
    - technical-documentation
    - markdown-formatting
category: guide
---

Rouge provides lots of different code block "hints". If you leave off the hint, it tries to guess and sometimes gets it wrong. These are just a few hints that we use often.

## [Variables](#variables)

If your example contains a placeholder value that's subject to change, use the format `<[A-Z_]+>` for the placeholder value: `<MY_VARIABLE>`

This syntax is reserved for variable names, and will cause the variable to be rendered in a special color and font style.

## [Highlight lines](#highlight-lines)

```
incoming := map[string]interface{}{
    "asdf": 1,
    "qwer": []interface{}{},
    "zxcv": []interface{}{
        map[string]interface{}{},
        true,
        int(1e9),
        "tyui",
    },
}    
```

````
```go {hl_lines=[7,8]}
incoming := map[string]interface{}{
    "asdf": 1,
    "qwer": []interface{}{},
    "zxcv": []interface{}{
        map[string]interface{}{},
        true,
        int(1e9),
        "tyui",
    },
}   
```
````

## [Collapsible code blocks](#collapsible-code-blocks)

```
# syntax=docker/dockerfile:1ARG GO_VERSION="1.21"FROMgolang:${GO_VERSION}-alpineASbaseENV CGO_ENABLED=0
ENV GOPRIVATE="github.com/foo/*"RUN apk add --no-cache file git rsync openssh-clientRUN mkdir -p -m 0700 ~/.ssh && ssh-keyscan github.com >> ~/.ssh/known_hostsWORKDIR/srcFROMbaseASvendor# this step configure git and checks the ssh key is loadedRUN --mount=type=ssh <<EOT  set -e  echo "Setting Git SSH protocol"  git config --global url."git@github.com:".insteadOf "https://github.com/"  (    set +e    ssh -T git@github.com    if [ ! "$?" = "1" ]; then      echo "No GitHub SSH key loaded exiting..."      exit 1    fi  )EOT# this one download go modulesRUN --mount=type=bind,target=. \
    --mount=type=cache,target=/go/pkg/mod \
    --mount=type=ssh \
    go mod download -xFROMvendorASbuildRUN --mount=type=bind,target=. \
    --mount=type=cache,target=/go/pkg/mod \
    --mount=type=cache,target=/root/.cache \
    go build ...
```

## [Bash](#bash)

Use the `bash` language code block when you want to show a Bash script:

```
#!/usr/bin/bash
echo "deb https://download.docker.com/linux/ubuntu noble stable" | sudo tee /etc/apt/sources.list.d/docker.list
```

If you want to show an interactive shell, use `console` instead. In cases where you use `console`, make sure to add a dollar character for the user sign:

```
$ echo "deb https://download.docker.com/linux/ubuntu noble stable" | sudo tee /etc/apt/sources.list.d/docker.list
```

## [Go](#go)

```
incoming:=map[string]interface{}{"asdf":1,"qwer":[]interface{}{},"zxcv":[]interface{}{map[string]interface{}{},true,int(1e9),"tyui",},}
```

## [PowerShell](#powershell)

```
Install-Module DockerMsftProvider -Force
Install-Package Docker -ProviderName DockerMsftProvider -Force
[System.Environment]::SetEnvironmentVariable("DOCKER_FIPS", "1", "Machine")
Expand-Archive docker-18.09.1.zip -DestinationPath $Env:ProgramFiles -Force
```

## [Python](#python)

```
return html.format(name=os.getenv('NAME', "world"), hostname=socket.gethostname(), visits=visits)
```

## [Ruby](#ruby)

```
docker_service 'default' do
  action [:create, :start]
end
```

## [JSON](#json)

```
"server": {
  "http_addr": ":4443",
  "tls_key_file": "./fixtures/notary-server.key",
  "tls_cert_file": "./fixtures/notary-server.crt"
}
```

#### [HTML](#html)

```
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
</head>
</html>
```

## [Markdown](#markdown)

If you want to include a triple-fenced code block inside your code block, you can wrap your block in a quadruple-fenced code block:

`````
````markdown
# Hello
```go
log.Println("did something")
```
````
`````

## [ini](#ini)

```
[supervisord]
nodaemon=true
[program:sshd]
command=/usr/sbin/sshd -D
```

## [Dockerfile](#dockerfile)

```
# syntax=docker/dockerfile:1FROMubuntuRUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" > /etc/apt/sources.list.d/pgdg.listRUN apt-get update && apt-get install -y python-software-properties software-properties-common postgresql-9.3 postgresql-client-9.3 postgresql-contrib-9.3# Note: The official Debian and Ubuntu images automatically ``apt-get clean``# after each ``apt-get``USERpostgresRUN    /etc/init.d/postgresql start &&\
    psql --command "CREATE USER docker WITH SUPERUSER PASSWORD 'docker';" &&\
    createdb -O docker dockerRUN echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/9.3/main/pg_hba.confRUN echo "listen_addresses='*'" >> /etc/postgresql/9.3/main/postgresql.confEXPOSE5432VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]CMD ["/usr/lib/postgresql/9.3/bin/postgres", "-D", "/var/lib/postgresql/9.3/main", "-c", "config_file=/etc/postgresql/9.3/main/postgresql.conf"]
```

## [YAML](#yaml)

```
authorizedkeys:image:dockercloud/authorizedkeysdeployment_strategy:every_nodeautodestroy:alwaysenvironment:- AUTHORIZED_KEYS=ssh-rsa AAAAB3Nsomelongsshkeystringhereu9UzQbVKy9o00NqXa5jkmZ9Yd0BJBjFmb3WwUR8sJWZVTPFLvolumes:/root:/user:rw
```