---
title: Improving the developer and user experience for third-party apps
url: https://developer.spotify.com/blog/2021-05-27-improving-the-developer-and-user-experience-for-third-party-apps
source: crawler
fetched_at: 2026-02-27T23:40:13.875332-03:00
rendered_js: true
word_count: 1115
summary: This document introduces new operational modes for Spotify apps, specifically Development Mode and Extended Quota Mode, alongside updated developer policies and review processes.
tags:
    - spotify-api
    - developer-policy
    - app-review
    - rate-limits
    - oauth-scopes
    - developer-platform
category: guide
---

Improving the developer and user experience for third-party apps

Posted May 27, 2021

![](https://developer.spotify.com/images/avatars/ole-hejlskov.png)

Ole Hejlskov

Third-party apps are an essential part of the Spotify experience. From playlist management software to social listening experiences, thousands of important apps connect to the Web API every day. Since we launched the Spotify Developer Platform, we have seen developers worldwide use our APIs to create apps, integrations or use it as a learning platform to learn new skills. We love seeing all the different apps, projects and integrations, and we want to continue supporting and encouraging this. At Spotify, we continue to focus on improving the user experience, quality, and safety of the third-party apps that our users install.

To support these efforts, we are launching three changes to our platform to help developers build better apps for the Spotify community. These changes include two new modes for apps, **Development Mode** and **Extended Quota Mode**, where Spotify will review apps to ensure they meet our rules and guidelines. We're also launching the new **Spotify Developer Policy**, which makes it easier to understand the nuances of our Developer Terms.

## Development Mode for new apps

Starting today, all new third-party apps begin in what we're calling Development Mode. Development Mode is designed to help you explore our APIs, and caters for apps that are under development, personal use, or are intended for a small number of users. You can invite up to 25 Spotify users to install your Development Mode app, each identified by you in the [Developer Dashboard](https://developer.spotify.com/dashboard).

![-](https://developer-assets.spotifycdn.com/images/blog/2021-05-20-users.png)

As before, all apps in this mode can access the full breadth of Web API functionality with no additional approvals needed. We designed the development mode to fit the majority of use cases for single-user apps. If you're exploring the APIs, building home automation, Magic Mirrors or similar use cases, this mode will fit perfectly. If you wish to onboard more than 25 users you will need to submit a quota extension request.

## Extended Quota Mode

Extended Quota Mode may be granted once the app has been reviewed and tested by Spotify to ensure it meets with our rules and guidelines.

Apps in this mode will have higher API rate limits and no limits on the amount of Spotify users that can connect. However, to ensure ongoing quality and safety for our users OAuth scopes will be locked to those requested at time of Spotify review.

Submitting a quota extension request can be done via the [Developer Dashboard](https://developer.spotify.com/dashboard), where you will have to provide information about the app, usage, monetisation considerations and required OAuth scopes, along with motivations for the use of the scopes and date. We encourage you to provide as much information as possible and instructions on how to best test your app.

*Please note that you can't submit a quota extension without having at least a working demo for your app.*

![-](https://developer-assets.spotifycdn.com/images/blog/2021-05-20-modes.png)

Once you have submitted the request, a dedicated team at Spotify will review all the provided information and test out your app as soon as they can. If we’re unable to grant your app an Extended Quota, we’ll try and give you actionable feedback where possible so you can adjust accordingly and re-submit the request.

## Introducing the Spotify Developer Policy

Today, we published a set of updates to our developer platform rules, which are divided into three documents: [Spotify Developer Terms](https://developer.spotify.com/terms), [Spotify Developer Policy](https://developer.spotify.com/policy) and [Complying with Spotify’s Developer Policy](https://developer.spotify.com/compliance-tips).

The new Spotify Developer Policy is where you’ll find most of the key product rules that developers are expected to follow when creating software that uses our Web API and other platform tools. The guidance in our Developer Policy is designed to help you easily find the information you need to successfully develop apps that protect users’ privacy, respect the intellectual property of our creator community, and meet Spotify’s design and user experience standards. The Developer Terms are still an important legal document, so if you’re building apps on our Developer Platform, you’ll want to be familiar with the Developer Terms and the Developer Policy.

To further elaborate on the rules in the Spotify Developer Policy, we have published a third document, entitled "Complying with Spotify’s Developer Policy”. This guide is a good place to find examples of how our policies apply in practice and tips you can use to ensure your app is in line with the rules.

## Summary

With the introduction of Development Mode, Extended Quota Mode, and the Spotify Developer Policy, we aim to improve the developer experience by making it easier to meet our rules and guidelines, ultimately enhancing the user experience. We always value feedback, so be sure to post your questions in our [Developer Forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer) and check out the Q&A section below.

### Questions and Answers

**Q: I already have an app today. What do these changes mean for me?**  
A: All existing apps will not be affected by these changes in the short term. Your app will be placed in the “Extended Quota” mode and will continue to work the same, but we will eventually reach out to review existing apps. There are no actions for existing apps at this stage.

**Q: My existing app is now in the Extended Quota mode but I want to trigger the review process**  
A: As of the release today, our system does not offer a way to trigger existing apps’ review process. We are working hard to provide this feature as soon as possible.

**Q: I submitted a commercial request, and I'm currently waiting for a reply**  
A: The process to review apps for extended quota mode will also look at commercial interest and monetisation considerations. Note that we have a strict policy on the types of monetisation we can support. Please consult the [Complying with Spotify’s Developer Policy](https://developer.spotify.com/compliance-tips), [Developer Terms](https://developer.spotify.com/terms), [Developer Policy](https://developer.spotify.com/policy), and [Design Guidelines](https://developer.spotify.com/documentation/design) to ensure your app is compliant and submit an extended quota request via the [Developer Dashboard](https://developer.spotify.com/dashboard).

**Q: Will OAuth scopes be locked in once my app is approved for extended quota mode?**  
A: Yes, when submitting your app for review, there is a section about the required OAuth scopes and the motivations for using the scopes. Once the review is completed, the scopes are locked in, and your app is limited to those scopes. Should you need additional scopes you can request a scope change via the [Developer Dashboard](https://developer.spotify.com/dashboard).

**Q: How can I see the status of my extended quota request?**  
A: You can see the status of your request via the [Developer Dashboard](https://developer.spotify.com/dashboard). Requests will be processed as they come in, and we will respond in a timely manner.

**Q: I still have questions!**  
A: Please post your questions, comments and feedback on the [developer forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer).