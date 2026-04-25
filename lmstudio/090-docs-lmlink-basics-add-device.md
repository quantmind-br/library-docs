---
title: Add a Device
url: https://lmstudio.ai/docs/lmlink/basics/add-device
source: sitemap
fetched_at: 2026-04-07T21:27:42.04815788-03:00
rendered_js: false
word_count: 303
summary: This document explains how to connect and manage multiple AI devices using LM Link, detailing steps for both GUI-equipped and headless machines. It also covers loading models from remote devices via the model loader or API/SDK.
tags:
    - lmlink
    - device-setup
    - remote-model-loading
    - headless-machine
    - llmster
    - multi-device
category: guide
---

## Add a new device[](#add-a-new-device "Link to 'Add a new device'")

![undefined](https://lmstudio.ai/assets/docs/lmlink-adddevice.png)

Add Device modal in LM Link

### Machines with GUI[](#machines-with-gui)

To begin using LM Link, add an additional device to the link:

- Download and install LM Studio on the device, at [https://lmstudio.ai/download](https://lmstudio.ai/download)
- Click on LM Link in the sidebar and follow the steps to enable LM Link.

Once LM Link is enabled, your devices will connect to each other automatically.

### Machines without GUI[](#machines-without-gui)

To add a headless machine, connect remotely by using llmster in the terminal:

- Install `llmster` on the headless machine

```

curl -fsSL https://lmstudio.ai/install.sh | bash
```

- Log in from the terminal

<!--THE END-->


- Follow the instructions in your terminal output to complete login.
- Once logged in, run the following command:


Your devices will automatically discover each other over the link, and your headless machine will immediately appear on the LM Link page for your other device. Once connected, models from remote machines will appear locally for loading and inference.

## Load models on remote machines[](#load-models-on-remote-machines "Link to 'Load models on remote machines'")

![undefined](https://lmstudio.ai/assets/docs/lmlink-useremotemodels.png)

Load models on remote devices with LM Link

When using LM Link, the model loader shows both local models and remote models on linked devices.

You can filter the model loader to display only local or remote models, or to display all available models at once. Remote models can be loaded and configured with the same familiar controls, either in the GUI or by using lms in the terminal.

If you have the same model on multiple devices, they will show up as separate entries, with the associated device name identified. If you are loading models via API/SDK, you can [set a preferred device](https://lmstudio.ai/docs/lmlink/basics/preferred-device) to specify which device to load the model from when multiple options are available.

Using LM Studio’s parallel requests, you can also serve multiple clients simultaneously across your LM Link network.