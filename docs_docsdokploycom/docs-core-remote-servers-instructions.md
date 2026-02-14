---
title: Deploy Server | Dokploy
url: https://docs.dokploy.com/docs/core/remote-servers/instructions
source: crawler
fetched_at: 2026-02-14T14:12:47.938402-03:00
rendered_js: true
word_count: 411
summary: This guide provides step-by-step instructions for configuring remote servers and deploying applications using Dokploy on a VPS.
tags:
    - dokploy
    - remote-server
    - vps-deployment
    - ssh-keys
    - server-setup
    - multi-server
category: guide
---

Step-by-step guide to setup a remote server and deploy applications on a VPS.

Remote servers allows you to deploy your apps remotely to different servers without needing to build and run them where the Dokploy UI is installed.

1. To install Dokploy UI, follow the [installation guide](https://docs.dokploy.com/docs/core/remote-servers/en/docs/core/get-started/installation).

If your remote server is configured with a different shell (other than bash), you must configure bash as the default shell, as Dokploy has been developed and tested with bash.

2. Create an SSH key by going to `/dashboard/settings/ssh-keys` and add a new key. Be sure to copy the public key.
   
   ![Architecture Diagram](https://docs.dokploy.com/_next/image?url=%2Fassets%2Fssh-keys.png&w=3840&q=75)
3. Decide which remote server to deploy your apps on. We recommend these reliable providers:

<!--THE END-->

- [Hostinger](https://www.hostinger.com/vps-hosting?ref=dokploy) Get 20% off with this [referral link](https://www.hostinger.com/vps-hosting?REFERRALCODE=1SIUMAURICI97).
- [DigitalOcean](https://www.digitalocean.com/pricing/droplets#basic-droplets) Get $200 credits for free with this [referral link](https://m.do.co/c/db24efd43f35).
- [Hetzner](https://www.hetzner.com/cloud/) Get €20 credits with this [referral link](https://hetzner.cloud/?ref=vou4fhxJ1W2D).
- [Vultr](https://www.vultr.com/pricing/#cloud-compute) Referral Link: [Referral Link](https://www.vultr.com/?ref=9679828)
- [Linode](https://www.linode.com/es/pricing/#compute-shared).
- [Scaleway](https://www.scaleway.com/en/pricing/?tags=baremetal%2Cavailable).
- [Google Cloud](https://cloud.google.com/).
- [AWS](https://aws.amazon.com/ec2/pricing/).

<!--THE END-->

4. When creating the server, it should ask for SSH keys. Ideally, use your computer's public key and the key you generated in the previous step. Here's how to add the public key in Hostinger:
   
   ![Adding SSH key](https://docs.dokploy.com/_next/image?url=%2Fassets%2Fhostinger-add-sshkey.png&w=3840&q=75)

The steps are similar across other providers.

5. Copy the server’s IP address and ensure you know the username (often `root`). Fill in all fields and click `Create`.
   
   ![Add server](https://docs.dokploy.com/_next/image?url=%2Fassets%2Fmulti-server-add-server.png&w=3840&q=75)
6. To test connectivity, open the server dropdown and click `Enter Terminal`. If everything is correct, you should be able to interact with the remote server.
7. Click `Setup Server` to proceed. There are two tabs: SSH Keys and Deployments. This guide explains the easy way, but you can follow the manual process via the Dokploy UI if you prefer.
   
   ![Setup process](https://docs.dokploy.com/_next/image?url=%2Fassets%2Fmulti-server-setup-2.png&w=3840&q=75)
8. Click `Deployments`, then `Setup Server`. If everything is correct, you should see output similar to this:
   
   ![Server setup output](https://docs.dokploy.com/_next/image?url=%2Fassets%2Fmulti-server-setup-3.png&w=3840&q=75)

You only need to run this setup once. If Dokploy updates later, check the release notes to see if rerunning this command is required.

09. You're ready to deploy your apps! Let's test it out:
    
    ![Add app](https://docs.dokploy.com/_next/image?url=%2Fassets%2Fmulti-server-add-app.png&w=3840&q=75)
10. To check which server an app belongs to, you’ll see the server name at the top. If no server is selected, it defaults to `Dokploy Server`. Click `Deploy` to start building your app on the remote server. You can check the `Logs` tab to see the build process. For this example, we’ll use a test repo:  
    Repo: `https://github.com/Dokploy/examples.git`  
    Branch: `main`  
    Build Path: `/astro`
    
    ![App setup](https://docs.dokploy.com/_next/image?url=%2Fassets%2Fmulti-server-setup-app.png&w=3840&q=75)
11. Once the build is done, go to `Domains` and create a free domain. Just click `Create` and you’re good to go! 🎊

![Finished setup](https://docs.dokploy.com/_next/image?url=%2Fassets%2Fmulti-server-finish.png&w=3840&q=75)