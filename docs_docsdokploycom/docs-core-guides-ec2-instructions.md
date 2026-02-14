---
title: EC2 Instructions | Dokploy
url: https://docs.dokploy.com/docs/core/guides/ec2-instructions
source: crawler
fetched_at: 2026-02-14T14:12:50.721855-03:00
rendered_js: true
word_count: 361
summary: This document provides a step-by-step guide for setting up an AWS EC2 remote server and connecting it to Dokploy using SSH keys for application deployment.
tags:
    - aws-ec2
    - dokploy
    - ssh-keys
    - server-setup
    - cloud-deployment
    - remote-server
category: guide
---

Instructions for setting up a remote server on EC2

In this guide we will show you how to setup a remote server on AWS EC2 and add an SSH Key on dokploy to connect to the server and start deploying your applications.

1. An AWS account
2. A domain that is managed by AWS Route53

If you already have an SSH Key you can skip this step and simply go to settings -&gt; SSH Keys and add the SSH Key you have stored on your machine

Navigate to Dokploy Settings -&gt; SSH Keys and add a new key

You will receive a public key and a private key. Copy the public key and save it.

![SSH Keys](https://docs.dokploy.com/_next/image?url=%2Fassets%2Fssh-keys.png&w=3840&q=75)

Login to your AWS account, navigate to EC2 and click on Launch Instance.

We will then be prompted to select an AMI (Amazon Machine Image) and we will select the Ubuntu Server 22.04 LTS AMI.

It should like this:

![EC2 AMI](https://docs.dokploy.com/_next/image?url=%2Fassets%2Fimages%2Fdeployment%2Foracle%2Foracle-shape.png&w=3840&q=75)

Select the instance type you want to use. For this guide we will use the `t2.micro` instance type which is free tier eligible.

Now we need to add the SSH Key we created in step 1 to the EC2 instance.

Click on Security Group and then add a new key pair.

Add the name of your SSH Key and paste the public key you copied in step 1.

![Add SSH Key](https://docs.dokploy.com/_next/image?url=%2Fassets%2Fhostinger-add-sshkey.png&w=3840&q=75)

You will have to create a security group that allows SSH (port 22) access from your IP address. and open all HTTP and HTTPS ports for ingress and egress traffic (Port 80 and 443).

Opening port 22 to the internet is a security risk. It is recommended to use a bastion host or a VPN to access your EC2 instance securely.

Now click on Launch Instance and wait for the instance to be created.

Now that we have the EC2 instance running, we can add it to Dokploy.

Navigate to Dokploy -&gt; Settings -&gt; Servers and click on Add Server and copy the server IP Address.

Navigate to Dokploy -&gt; Settings -&gt; Servers -&gt; Setup Server and follow the instructions.

Now that the server is setup, you can deploy your application to the server.