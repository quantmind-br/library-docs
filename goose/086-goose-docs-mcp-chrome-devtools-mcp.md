---
title: Chrome DevTools Extension | goose
url: https://block.github.io/goose/docs/mcp/chrome-devtools-mcp
source: github_pages
fetched_at: 2026-01-22T22:14:49.078107829-03:00
rendered_js: true
word_count: 398
summary: This tutorial explains how to integrate the Chrome DevTools MCP Server with goose to enable automated web performance testing and browser debugging.
tags:
    - chrome-devtools
    - mcp-server
    - goose
    - browser-automation
    - performance-testing
    - debugging
category: tutorial
---

This tutorial covers how to add the Chrome DevTools MCP Server as a goose extension to enable browser automation, web performance testing, and interactive web application debugging in a Chrome browser.

In this example, I'll show you how to use goose with the Chrome DevTools Extension to perform automated performance testing on a demo website.

```
Use the chrome dev tools extension to Navigate to https://www.saucedemo.com 
Then, login as performance_glitch_user and measure the site's performance
```

```

I'll help you navigate to the Sauce Demo site, login as the performance_glitch_user, and measure the performance impact. Let me start by checking what pages are currently open and then navigate to the site.

Perfect! I can see the login page for Swag Labs. I can see that `performance_glitch_user` is one of the accepted usernames, and the password for all users is `secret_sauce`. Let me log in with these credentials and then measure the performance.

I've successfully navigated to the Saucedemo website and logged in as the `performance_glitch_user` to measure the site's performance. Here's what I discovered:

## Performance Analysis Results for performance_glitch_user

### Initial Observations

1. **Login Performance**: The initial login with the performance_glitch_user took noticeably longer than normal - the click on the Login button actually timed out after 5 seconds, indicating significant delays.

2. **Page Load Metrics**: 
   - **Total Load Time**: ~5.03 seconds (5030ms)
   - **First Paint**: 5.08 seconds 
   - **First Contentful Paint**: 5.08 seconds
   - **Response Time**: 2.5ms (server response was actually fast)
   - **DOM Content Loaded**: 0.1ms

### Performance Issues Identified

The performance issues with the `performance_glitch_user` account appear to be **client-side rendering delays** rather than network or server issues:

- The server responds quickly (2.5ms response time)
- The major delay occurs in the rendering phase (5+ seconds to first paint)
- This suggests the performance glitch is intentionally built into the client-side JavaScript execution for this specific user

### Interactive Performance

- **Button Clicks**: Adding items to cart works, but with noticeable delays
- **DOM Queries**: Standard DOM operations perform normally (~0.1ms)
- **JavaScript Execution**: Basic computations run at normal speed (~2ms for 100k operations)

### Cart Functionality

I was able to successfully add multiple items to the cart (the cart counter increased from 1 to 3), showing that despite the performance issues, the core functionality remains intact.

### Conclusion

The `performance_glitch_user` account demonstrates **intentional performance degradation** primarily affecting:
- Initial page rendering (5+ second delays)
- Login process (timeouts)
- Visual feedback delays

This makes it an excellent test account for performance testing scenarios, as it simulates real-world performance issues that users might experience with slow devices or poor network conditions, while maintaining functional correctness.
```