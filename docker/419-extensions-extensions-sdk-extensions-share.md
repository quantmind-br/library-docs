---
title: Share your extension
url: https://docs.docker.com/extensions/extensions-sdk/extensions/share/
source: llms
fetched_at: 2026-01-24T14:27:58.733497554-03:00
rendered_js: false
word_count: 147
summary: This document explains how to share and install Docker extensions using command-line instructions or shareable URLs that provide a visual preview in Docker Desktop.
tags:
    - docker-extension
    - extension-sharing
    - installation
    - docker-desktop
    - cli
    - preview-link
category: guide
---

Table of contents

* * *

Once your extension image is accessible on Docker Hub, anyone with access to the image can install the extension.

People can install your extension by typing `docker extension install my/awesome-extension:latest` in to the terminal.

However, this option doesn't provide a preview of the extension before it's installed.

Docker lets you share your extensions using a URL.

When people navigate to this URL, it opens Docker Desktop and displays a preview of your extension in the same way as an extension in the Marketplace. From the preview, users can then select **Install**.

![Navigate to extension link](https://docs.docker.com/extensions/extensions-sdk/extensions/images/open-share.png)

![Navigate to extension link](https://docs.docker.com/extensions/extensions-sdk/extensions/images/open-share.png)

To generate this link you can either:

- Run the following command:
  
  ```
  $ docker extension share my/awesome-extension:0.0.1
  ```
- Once you have installed your extension locally, navigate to the **Manage** tab and select **Share**.
  
  ![Share button](https://docs.docker.com/extensions/extensions-sdk/extensions/images/list-preview.png)
  
  ![Share button](https://docs.docker.com/extensions/extensions-sdk/extensions/images/list-preview.png)

> Note
> 
> Previews of the extension description or screenshots, for example, are created using [extension labels](https://docs.docker.com/extensions/extensions-sdk/extensions/labels/).