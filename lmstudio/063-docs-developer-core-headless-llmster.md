---
title: Setup llmster as a Startup Task on Linux
url: https://lmstudio.ai/docs/developer/core/headless_llmster
source: sitemap
fetched_at: 2026-04-07T21:29:57.210688253-03:00
rendered_js: false
word_count: 241
summary: This guide details the process of setting up lmstudio's headless daemon, `llmster`, to run automatically on Linux systems using systemd for service management. It covers installation, model downloading, manual testing, and creating the necessary systemd service file.
tags:
    - linux-service
    - systemctl
    - headless-daemon
    - llmster
    - model-loading
    - api-server
category: guide
---

`llmster`, LM Studio's headless daemon, can be configured to run on startup. This guide covers setting up `llmster` to launch, load a model, and start an HTTP server automatically using `systemctl` on Linux.

This guide is for Linux systems without a graphical interface. For machines with a GUI, you can configure LM Studio to [run as a service on login](https://lmstudio.ai/docs/developer/core/headless) instead.

## Install the Daemon[](#install-the-daemon "Link to 'Install the Daemon'")

Run the following command to install `llmster`:

```

curl -fsSL https://lmstudio.ai/install.sh | bash
```

Verify the installation:


## Download a Model[](#download-a-model "Link to 'Download a Model'")

Download a model to use with the server:

```

lms get openai/gpt-oss-20b
```

The output will show the model path. You'll need this for the systemd configuration.

## Manual Test[](#manual-test "Link to 'Manual Test'")

Before configuring systemd, verify everything works manually.

Load the model:

```

lms load openai/gpt-oss-20b
```

Start the server:


Verify the API is responding:

```

curl http://localhost:1234/v1/models
```

Stop the server when done testing:


## Create Systemd Service[](#create-systemd-service "Link to 'Create Systemd Service'")

Create `/etc/systemd/system/lmstudio.service`. Replace `YOUR_USERNAME` with your username.

```

[Unit]
Description=LM Studio Server

[Service]
Type=oneshot
RemainAfterExit=yes
User=YOUR_USERNAME
Environment="HOME=/home/YOUR_USERNAME"
ExecStartPre=/home/YOUR_USERNAME/.lmstudio/bin/lms daemon up
ExecStartPre=/home/YOUR_USERNAME/.lmstudio/bin/lms load openai/gpt-oss-20b --yes
ExecStart=/home/YOUR_USERNAME/.lmstudio/bin/lms server start
ExecStop=/home/YOUR_USERNAME/.lmstudio/bin/lms daemon down

[Install]
WantedBy=multi-user.target
```

This unit automatically loads the `openai/gpt-oss-20b` model on startup. Alternatively, you can avoid loading a specific model on startup and instead rely on [Just-In-Time (JIT) loading and Eviction](https://lmstudio.ai/docs/developer/core/ttl-and-auto-evict) in the server.

## Enable and Start the Service[](#enable-and-start-the-service "Link to 'Enable and Start the Service'")

```

sudo systemctl daemon-reload
sudo systemctl enable lmstudio.service
sudo systemctl start lmstudio.service
```

## Verify[](#verify "Link to 'Verify'")

Check the service status:

```

systemctl status lmstudio
```

Test the API:

```

curl http://localhost:1234/v1/models
```

## Service Management[](#service-management "Link to 'Service Management'")

```

# Stop the service
sudo systemctl stop lmstudio

# Restart the service
sudo systemctl restart lmstudio

# Disable auto-start
sudo systemctl disable lmstudio
```

Chat with other LM Studio developers, discuss LLMs, hardware, and more on the [LM Studio Discord server](https://discord.gg/aPQfnNkxGC).

Please report bugs and issues in the [lmstudio-bug-tracker](https://github.com/lmstudio-ai/lmstudio-bug-tracker/issues) GitHub repository.