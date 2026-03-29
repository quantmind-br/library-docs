---
title: ""
url: https://ampcode.com/news/AGENT.md
source: crawler
fetched_at: 2026-02-06T02:08:48.441345152-03:00
rendered_js: false
word_count: 504
summary: This document introduces AGENT.md and AGENTS.md files, which are used by the Amp tool to store project-specific guidance on structure, build steps, and coding conventions.
tags:
    - amp-code
    - agent-md
    - agents-md
    - project-configuration
    - ai-guidance
    - build-steps
category: configuration
---

<!doctype html>
<html lang="en">
	<head>
		<meta charset="utf-8" />
		<meta
			name="viewport"
			content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no"
		/>
		<link rel="manifest" href="/site.webmanifest" />
		<link rel="apple-touch-icon" href="/app-icon.png" />
		<meta name="apple-mobile-web-app-title" content="Amp" />
		<meta name="mobile-web-app-capable" content="yes" />
		<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
		<link rel="icon" href="/amp-mark-color.svg" />
		
		<link href="/_app/immutable/assets/Root.DcQjqUeO.css" rel="stylesheet">
		<link href="/_app/immutable/assets/0.BIQYclYx.css" rel="stylesheet">
		<link href="/_app/immutable/assets/app.5vIomWWs.css" rel="stylesheet">
		<link href="/_app/immutable/assets/marketing-header.NJHa1Q17.css" rel="stylesheet">
		<link href="/_app/immutable/assets/terminal-modal.BCQrSdgB.css" rel="stylesheet">
		<link href="/_app/immutable/assets/marketing-layout.BhL-4Tb6.css" rel="stylesheet">
		<link href="/_app/immutable/assets/recommended-reading.B5f5L6PV.css" rel="stylesheet">
		<link href="/_app/immutable/assets/161.BbVxmfuj.css" rel="stylesheet"><!--12qhfyh--><meta property="og:title" content="AGENT.md"/> <!--[--><meta property="og:description" content="Configure Amp with project guidance in `AGENTS.md` files"/><!--]--> <!--[--><meta property="og:image" content="https://ampcode.com/news/AGENT.md?og-image"/><meta name="twitter:image" content="https://ampcode.com/news/AGENT.md?og-image"/><!--]--> <meta name="twitter:site" content="@ampcode"/> <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="Amp"/> <link rel="alternate" type="application/rss+xml" title="Amp News RSS Feed" href="/news.rss"/> <link rel="alternate" type="application/rss+xml" title="Raising an Agent Podcast" href="/podcast.rss"/> <link rel="dns-prefetch" href="https://static.ampcode.com"/><!----><!--1bsnhax--><meta name="viewport" content="width=device-width, initial-scale=1.0"/><!----><!--1mqar8i--><meta property="og:type" content="article"/> <meta name="twitter:creator" content="@ampcode"/> <meta name="twitter:card" content="summary_large_image"/><!----><title>AGENT.md - Amp</title>
	</head>
	<body data-sveltekit-preload-data="hover">
		<div style="display: contents"><!--[--><!--[--><!----><!----><!--[--><!--[--><!----><!--[--><div class=" fixed top-1 right-3.5 z-50"><!----><!----><!--$s1--><!--[!--><button class="w-12 h-12 flex items-center justify-center touch-manipulation focus-visible:outline-none opacity-60 hover:opacity-100 mt-1 " aria-label="Toggle menu" id="bits-s1" aria-haspopup="dialog" aria-expanded="false" data-state="closed" data-popover-trigger="" type="button"><svg viewBox="0 0 24 24" width="24" height="24" class="h-6 w-6 transition-transform duration-150 opacity-80 "><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m6 9l6 6l6-6"></path></svg><!----></button><!--]--><!----><!----> <!----><!----><!--[!--><!--]--><!----><!----><!----><!----><!----><!----></div><!--]--> <div class="background-grid  svelte-vre9z4" aria-hidden="true"><svg class="background-grid-svg svelte-vre9z4" preserveAspectRatio="none"><line class="bg-grid-rail-line svelte-vre9z4" data-rail="margin-left"></line><line class="bg-grid-rail-line svelte-vre9z4" data-rail="1-2"></line><line class="bg-grid-rail-line svelte-vre9z4" data-rail="2-3"></line><line class="bg-grid-rail-line svelte-vre9z4" data-rail="3-4"></line><line class="bg-grid-rail-line svelte-vre9z4" data-rail="4-5"></line><line class="bg-grid-rail-line svelte-vre9z4" data-rail="margin-right"></line></svg></div><!----> <!--[!--><!--]--><!----> <div id="marketing-root" class="transition-opacity duration-150 relative min-h-screen flex flex-col svelte-1bsnhax"><!--[--><!--[--><nav class="grid-container items-center grid-section--dense"><a href="/" class="cell-pad justify-self-start self-center py-0 rail-tick-start"><!--[!--><svg class="h-[32px]" viewBox="0 0 281 144" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path d="M236.014 20C260.431 20.0001 280.602 37.4115 280.603 64.7432C280.602 93.5337 260.065 114.166 233.52 114.166C224.158 114.166 215.639 112.422 208.63 108.49C202.886 105.27 198.203 100.605 194.919 94.3379L188.115 141.822L187.946 143.016H174.214L174.448 141.423L191.772 22.4941H205.372L203.937 31.3369C212.143 23.8608 223.2 20.0002 236.014 20ZM47.082 20.1543C56.4435 20.1543 65.0012 21.8991 72.0488 25.8486C77.8222 29.0831 82.5323 33.7713 85.8271 40.085L88.1201 23.6924L88.2861 22.4932H101.863L89.1611 110.633L88.9873 111.826H75.4092L76.7227 102.855C68.5854 110.456 57.3981 114.323 44.5889 114.323C20.1709 114.323 0.000167223 96.9087 0 69.5771C0.000149745 40.7854 20.54 20.1549 47.082 20.1543ZM116.234 110.636L116.061 111.827H102.485L115.351 23.6855L115.521 22.4941H129.083L116.234 110.636ZM140.673 110.636L140.499 111.827H126.924L139.789 23.6855L139.96 22.4941H153.521L140.673 110.636ZM177.958 22.4941L165.108 110.636L164.935 111.827H151.36L164.225 23.6855L164.396 22.4941H177.958ZM48.4854 31.9844C27.8638 31.985 14.0133 48.3799 14.0127 68.9521C14.0127 77.7907 16.8094 86.1771 22.3145 92.334C27.7973 98.4657 36.0631 102.493 47.2402 102.493C67.8534 102.493 81.7122 85.9487 81.7129 65.3682C81.7129 55.4076 78.2493 47.0792 72.4131 41.2441C66.5794 35.4088 58.2871 31.9844 48.4854 31.9844ZM233.362 31.8291C212.749 31.8297 198.89 48.3716 198.89 68.9521C198.89 78.9123 202.356 87.2403 208.189 93.0742C214.023 98.9107 222.315 102.336 232.116 102.336C252.738 102.335 266.589 85.9407 266.59 65.3682C266.59 56.5296 263.795 48.1424 258.29 41.9863C252.807 35.8551 244.542 31.8291 233.362 31.8291Z"></path></svg><!--]--><!----></a> <div class="cell-pad col-span-full cell-pad--stroke-context lg:col-start-2 lg:col-span-3 flex items-center py-0 pb-2 sm:pb-0 overflow-x-auto whitespace-nowrap" style="mask-image: linear-gradient(to right, #000 95%, transparent 100%); -webkit-mask-image: linear-gradient(to right, #000 95%, transparent 100%);"><a href="/chronicle" class="font-mono rail-tick-start font-bold uppercase text-sm text-muted-foreground hover:text-foreground transition-colors tracking-wide shrink-0">Chronicle</a> <span class="font-sagittaire-text italic text-muted-foreground/50 normal-case mx-2 shrink-0">//</span> <span class="font-mono font-bold uppercase text-sm text-muted-foreground tracking-wide"><span class="opacity-30 font-normal">[</span>News<span class="font-normal opacity-30">]</span><!--[--> AGENT.md<!--]--></span></div></nav><!----><!--]--><!--]--> <div class="flex-1 min-h-0 flex flex-col"><!--[!--><!----><!--[!--><!--]--> <!--[!--><!--[!--><!--]--> <main class="flex-1 grid-container content-start"><header class="grid-section !pb-0 col-span-full grid grid-cols-subgrid pt-4 md:pt-6"><div class="cell-pad col-span-full lg:col-start-2 cell-pad--stroke-context lg:col-span-3 min-w-0"><time class="font-mono font-bold type-xs uppercase tracking-wider text-muted-foreground rail-tick-start">May 7, 2025</time> <div class="flex items-center gap-3 mt-2"><h1 class="font-sagittaire-display text-6xl md:text-6xl lg:text-8xl text-pretty tracking-tighter">AGENT.md</h1> <!--[!--><!--]--></div></div></header> <article class="grid-section col-span-full grid grid-cols-subgrid pb-16 md:pb-24"><div class="cell-pad hidden lg:block"></div> <div class="cell-pad col-span-full lg:col-start-2 overflow-x-clip min-w-0 lg:col-span-3"><!--[!--><!--]--> <!--[--><!--[!--><!--]--> <div class="prose dark:prose-invert news-content-body leading-[1.4]  svelte-1m63zip"><!--[!--><!----><p><em>Update: Amp now looks in files named <code>AGENTS.md</code> (with an <code>S</code>).</em></p>
<p>Amp now looks in the <code>AGENT.md</code> file at the root of your project for guidance on project structure, build &amp; test steps, conventions, and avoiding common mistakes. <a href="/manual#AGENTS.md">Manual&nbsp;&raquo;</a></p>
<p>Amp will offer to generate this file by reading your project and other agents&#39; files (<code>.cursorrules</code>, <code>.cursor/rules</code>, <code>.windsurfrules</code>, <code>.clinerules</code>, <code>CLAUDE.md</code>, and <code>.github/copilot-instructions.md</code>).</p>
<p>We chose <code>AGENT.md</code> as a naming standard to avoid the proliferation of agent-specific files in your repositories. We <a href="https://x.com/sqs/status/1920029114125201570">hope</a> other agents will follow this convention.</p>
<!----><!--]--></div><!--]--><!----></div> <!--[--><aside class="col-span-2 col-start-2 lg:col-start-5 lg:col-span-1 min-w-0 lg:mt-96"><div class="sticky top-20"><div><div class="translate-y-9 flex justify-end relative bleed-inline-end pointer-events-none z-10 !pr-0"><img src="/trumpeter/image.jpg" alt="" class="img-matte pointer-events-none w-1/2 lg:w-full svelte-1k18utt" aria-hidden="true" style="max-width: 400px"/></div> <a href="/news/multiple-AGENT.md-files" class="block group bleed-inline-end antialiased relative link-callout transition-colors svelte-1k18utt"><div class="flex flex-col items-start lg:gap-5 gap-4 py-8 pl-8 lg:py-10 lg:pl-10 2xl:pr-5 relative overflow-hidden"><div class="font-mono text-sm font-bold uppercase tracking-widest opacity-60">Also<span class="font-sagittaire-text italic normal-case mx-1">of</span>Interest</div> <div class="flex flex-col gap-3"><h4 class="type-base font-medium">Multiple AGENT.md Files</h4> <!--[--><p class="type-sm opacity-80">Use multiple `AGENT.md` files across directory trees</p><!--]--></div> <div class="inline-flex font-mono text-sm px-2 py-1 font-bold uppercase tracking-widest justify-start items-center gap-0.5 link-callout__cta svelte-1k18utt">Read <svg viewBox="0 0 24 24" width="24" height="24" class="size-3.5 transition-transform group-hover:translate-x-0.5"><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 12h14m-7-7l7 7l-7 7"></path></svg><!----></div></div></a></div></div></aside><!--]--></article></main><!--]--><!----><!--]--><!----><!----></div> <!--[--><footer class="grid-container border-t border-border grid-section" data-page-footer=""><div class="cell-pad section-header gap-[var(--lens-cell-padding)] svelte-1yl60m7"><a class="inline-block" href="/"><!--[!--><svg class="h-full w-20 md:w-30" viewBox="0 0 281 144" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path d="M236.014 20C260.431 20.0001 280.602 37.4115 280.603 64.7432C280.602 93.5337 260.065 114.166 233.52 114.166C224.158 114.166 215.639 112.422 208.63 108.49C202.886 105.27 198.203 100.605 194.919 94.3379L188.115 141.822L187.946 143.016H174.214L174.448 141.423L191.772 22.4941H205.372L203.937 31.3369C212.143 23.8608 223.2 20.0002 236.014 20ZM47.082 20.1543C56.4435 20.1543 65.0012 21.8991 72.0488 25.8486C77.8222 29.0831 82.5323 33.7713 85.8271 40.085L88.1201 23.6924L88.2861 22.4932H101.863L89.1611 110.633L88.9873 111.826H75.4092L76.7227 102.855C68.5854 110.456 57.3981 114.323 44.5889 114.323C20.1709 114.323 0.000167223 96.9087 0 69.5771C0.000149745 40.7854 20.54 20.1549 47.082 20.1543ZM116.234 110.636L116.061 111.827H102.485L115.351 23.6855L115.521 22.4941H129.083L116.234 110.636ZM140.673 110.636L140.499 111.827H126.924L139.789 23.6855L139.96 22.4941H153.521L140.673 110.636ZM177.958 22.4941L165.108 110.636L164.935 111.827H151.36L164.225 23.6855L164.396 22.4941H177.958ZM48.4854 31.9844C27.8638 31.985 14.0133 48.3799 14.0127 68.9521C14.0127 77.7907 16.8094 86.1771 22.3145 92.334C27.7973 98.4657 36.0631 102.493 47.2402 102.493C67.8534 102.493 81.7122 85.9487 81.7129 65.3682C81.7129 55.4076 78.2493 47.0792 72.4131 41.2441C66.5794 35.4088 58.2871 31.9844 48.4854 31.9844ZM233.362 31.8291C212.749 31.8297 198.89 48.3716 198.89 68.9521C198.89 78.9123 202.356 87.2403 208.189 93.0742C214.023 98.9107 222.315 102.336 232.116 102.336C252.738 102.335 266.589 85.9407 266.59 65.3682C266.59 56.5296 263.795 48.1424 258.29 41.9863C252.807 35.8551 244.542 31.8291 233.362 31.8291Z"></path></svg><!--]--><!----></a> <div class="footer-legal svelte-1yl60m7"><ul class="svelte-1yl60m7"><li class="svelte-1yl60m7"><a href="https://ampcodestatus.com" class="flex items-center gap-1.5 lg:gap-2"><span class="w-1.5 h-1.5 rounded-full operational order-2 md:order-1 svelte-17tm13q"></span> <span class="order-1 md:order-2">All Systems Operational</span></a><!----></li> <li class="svelte-1yl60m7"><a href="/security" class="svelte-1yl60m7">Security</a></li> <li class="svelte-1yl60m7"><a href="/terms" class="svelte-1yl60m7">Terms of Service</a></li></ul></div></div> <div class="cell-pad md:col-span-2 lg:col-start-3 lg:col-span-4 flex flex-col gap-8 lg:flex-row sm:grid sm:grid-cols-2 sm:gap-[var(--lens-cell-padding)] lg:flex lg:gap-0 lg:justify-between"><div class="footer-column svelte-1yl60m7"><h3 class="svelte-1yl60m7">Product</h3> <ul class="svelte-1yl60m7"><!--[!--><li class="svelte-1yl60m7"><a href="/auth/sign-up" class="svelte-1yl60m7">Get Started</a></li> <li class="svelte-1yl60m7"><a href="/auth/sign-in" class="svelte-1yl60m7">Sign In</a></li><!--]--> <li class="svelte-1yl60m7"><a href="/manual" class="svelte-1yl60m7">Owner's Manual</a></li> <li class="svelte-1yl60m7"><a href="/models" class="svelte-1yl60m7">Models</a></li> <li class="svelte-1yl60m7"><a href="/free" class="svelte-1yl60m7">Amp Free</a></li></ul></div> <div class="footer-column svelte-1yl60m7"><h3 class="svelte-1yl60m7">Resources</h3> <ul class="svelte-1yl60m7"><li class="svelte-1yl60m7"><a href="/chronicle" class="svelte-1yl60m7">Chronicle</a></li> <li class="svelte-1yl60m7"><a href="/pricing" class="svelte-1yl60m7">Pricing</a></li> <li class="svelte-1yl60m7"><a href="/podcast" class="svelte-1yl60m7">Podcast</a></li> <li class="svelte-1yl60m7"><a href="/press-kit" class="svelte-1yl60m7">Press Kit</a></li></ul></div> <div class="footer-column svelte-1yl60m7"><h3 class="svelte-1yl60m7">Guides</h3> <ul class="svelte-1yl60m7"><li class="svelte-1yl60m7"><a href="/how-to-build-an-agent" class="svelte-1yl60m7">How to Build an Agent</a></li> <li class="svelte-1yl60m7"><a href="/guides/context-management" class="svelte-1yl60m7">Context Management</a></li></ul></div> <div class="footer-column svelte-1yl60m7"><h3 class="svelte-1yl60m7">Community</h3> <ul class="svelte-1yl60m7"><li class="svelte-1yl60m7"><a href="https://x.com/ampcode" class="svelte-1yl60m7">𝕏 @ampcode</a></li> <li class="svelte-1yl60m7"><a href="https://buildcrew.team" class="svelte-1yl60m7">Build Crew</a></li> <li class="svelte-1yl60m7"><a href="https://www.youtube.com/@Sourcegraph/videos" class="svelte-1yl60m7">YouTube</a></li></ul></div></div></footer><!--]--></div> <!--[!--><!--]--><!----> <!--[--><!--[!--><!--]--> <!--[!--><!--]--><!--]--><!----><!--]--><!----><!--]--> <div class="sonner-container fixed bottom-4 left-4 z-50 flex flex-col gap-2 svelte-1c26wvq"><!--[--><!--]--></div><!----><!----><!----> <!--[!--><!--]--><!----> <!----><!----><!----><!--[!--><!--]--><!----><!----><!----><!----><!----><!----> <!--[!--><!--]--><!----><!--]--> <!--[!--><!--]--><!--]-->
			
			<script>
				{
					__sveltekit_yjq1ld = {
						base: "",
						env: {"PUBLIC_POSTHOG_API_KEY":"phc_3R88ilI9djOdvET3gRtwYKhlxAPmWON04kRIXeWjlQ3","PUBLIC_SLACK_APP_ID":"A09SJP9PVQU"}
					};

					const element = document.currentScript.parentElement;

					Promise.all([
						import("/_app/immutable/entry/start.DJCp_ipD.js"),
						import("/_app/immutable/entry/app.BQTbxdId.js")
					]).then(([kit, app]) => {
						kit.start(app, element, {
							node_ids: [0, 34, 161],
							data: [{type:"data",data:{user:void 0,userWorkspace:void 0,timezone:"UTC",mostRecentLeaderboard:null,viewerCanCreateAgentThread:false,posthogUserId:null,isNewUser:void 0,isAdvertiserManager:false,hasTaskListFeature:false,forcedTraceId:void 0,dtwConfig:{baseURL:"https://production.ampworkers.com",ampURL:"https://ampcode.com"}},uses:{}},null,{type:"data",data:{newsItem:{slug:"AGENT.md",date:"May 7, 2025",file:"20250507_AGENT.md.md",title:"AGENT.md",content:"_Update: Amp now looks in files named `AGENTS.md` (with an `S`)._\n\nAmp now looks in the `AGENT.md` file at the root of your project for guidance on project structure, build & test steps, conventions, and avoiding common mistakes. [Manual&nbsp;&raquo;](/manual#AGENTS.md)\n\nAmp will offer to generate this file by reading your project and other agents' files (`.cursorrules`, `.cursor/rules`, `.windsurfrules`, `.clinerules`, `CLAUDE.md`, and `.github/copilot-instructions.md`).\n\nWe chose `AGENT.md` as a naming standard to avoid the proliferation of agent-specific files in your repositories. We [hope](https://x.com/sqs/status/1920029114125201570) other agents will follow this convention.",excerpt:void 0,indexOnlyContent:void 0,url:"/news/AGENT.md",preview:false,previewFlagName:void 0,ogImage:void 0,tagline:"Configure Amp with project guidance in `AGENTS.md` files",showTagline:false,screenshot:void 0,backgroundImage:void 0,footnotes:void 0,recommendedReading:{href:"/news/multiple-AGENT.md-files",title:"Multiple AGENT.md Files",subtitle:"Use multiple `AGENT.md` files across directory trees"}},title:"AGENT.md",openGraphTitle:"AGENT.md",openGraphDescription:"Configure Amp with project guidance in `AGENTS.md` files",openGraphImage:"https://ampcode.com/news/AGENT.md?og-image"},uses:{search_params:["og-image"],params:["slug"],url:1}}],
							form: null,
							error: null
						});
					});
				}
			</script>
		</div>
		<!-- prettier-ignore -->
		<script>
			/*
			 * ⚠️ 🚨 CRITICAL GDPR COMPLIANCE WARNING 🚨 ⚠️
			 *
			 * DO NOT MODIFY THE POSTHOG CONFIGURATION BELOW WITHOUT LEGAL REVIEW!
			 *
			 * This PostHog configuration is specifically designed for GDPR compliance:
			 *
			 * 🔒 persistence: 'memory' - Uses memory storage instead of cookies
			 * 🔒 mask_all_text: true - Masks all text content to prevent PII collection
			 * 🔒 mask_all_element_attributes: true - Masks element attributes that may contain PII
			 * 🔒 disable_session_recording: true - Prevents recording of user sessions
			 * 🔒 before_send function - Sanitizes URLs to remove sensitive team names and data
			 *
			 * If changes are needed, consult legal team first!
			 */
			// PostHog snippet https://posthog.com/docs/libraries/js
			// biome-ignore lint/complexity/noCommaOperator: copied from snippet
			// biome-ignore lint/complexity/noArguments: copied from snippet
			!((t,e)=> {var o,n,p,r;e.__SV||(window.posthog=e,e._i=[],e.init=(i,s,a)=> {function g(t,e){var o=e.split(".");2==o.length&&(t=t[o[0]],e=o[1]),t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}}(p=t.createElement("script")).type="text/javascript",p.crossOrigin="anonymous",p.async=!0,p.src=s.api_host.replace(".i.posthog.com","-assets.i.posthog.com")+"/static/array.js",(r=t.getElementsByTagName("script")[0]).parentNode.insertBefore(p,r);var u=e;for(void 0!==a?u=e[a]=[]:a="posthog",u.people=u.people||[],u.toString=(t)=> {var e="posthog";return"posthog"!==a&&(e+="."+a),t||(e+=" (stub)"),e},u.people.toString=()=> u.toString(1)+".people (stub)",o="init capture register register_once register_for_session unregister unregister_for_session getFeatureFlag getFeatureFlagPayload isFeatureEnabled reloadFeatureFlags updateEarlyAccessFeatureEnrollment getEarlyAccessFeatures on onFeatureFlags onSessionId getSurveys getActiveMatchingSurveys renderSurvey canRenderSurvey getNextSurveyStep identify setPersonProperties group resetGroups setPersonPropertiesForFlags resetPersonPropertiesForFlags setGroupPropertiesForFlags resetGroupPropertiesForFlags reset get_distinct_id getGroups get_session_id get_session_replay_url alias set_config startSessionRecording stopSessionRecording sessionRecordingStarted captureException loadToolbar get_property getSessionProperty createPersonProfile opt_in_capturing opt_out_capturing has_opted_in_capturing has_opted_out_capturing clear_opt_in_out_capturing debug".split(" "),n=0;n<o.length;n++)g(u,o[n]);e._i.push([i,s,a])},e.__SV=1)})(document,window.posthog||[]);
			var posthogKey = 'phc_3R88ilI9djOdvET3gRtwYKhlxAPmWON04kRIXeWjlQ3';
			if (posthogKey) {
				posthog.init(posthogKey, {
					persistence: 'memory',
					bootstrap: (() => {
						var phAnonId = new URLSearchParams(window.location.search).get('ph_did')
						return phAnonId ? { distinctID: phAnonId, isIdentifiedID: false } : undefined
					})(),
					api_host: 'https://us.i.posthog.com',
					defaults: '2025-05-24',
					mask_all_text: true,
					mask_all_element_attributes: true,
					disable_session_recording: true,
					capture_exceptions: false,
					session_recording: {
						maskTextSelector: '*', // Masks all text elements (not including inputs)
					},
					before_send: (event, data) => {
						// Pre-compiled regexes for sensitive data patterns
						var teamRegex = /\/teams\/[^/]+/g
						var userRegex = /\/profile\/user_[^/]+/g
						var authorRegex = /author=user_[^&]*/g
						var userIdRegex = /user_[A-Z0-9]+/g
						var teamIdRegex = /team_[A-Z0-9]+/g

						function sanitizeUrl(url) {
							return (
								url &&
								url
									.replace(teamRegex, '/teams/[REDACTED]')
									.replace(userRegex, '/profile/[REDACTED]')
									.replace(authorRegex, 'author=[REDACTED]')
							)
						}

						function sanitizeIds(str) {
							return (
								str &&
								str
									.replace(userIdRegex, '[REDACTED]')
									.replace(teamIdRegex, '[REDACTED]')
									.replace(teamRegex, '/teams/[REDACTED]')
									.replace(userRegex, '/profile/[REDACTED]')
									.replace(authorRegex, 'author=[REDACTED]')
							)
						}

						// Only sanitize if properties exist
						var props = event.properties
						if (props) {
							// Sanitize URLs
							if (props.$current_url) props.$current_url = sanitizeUrl(props.$current_url)
							if (props.$pathname) props.$pathname = sanitizeUrl(props.$pathname)
							if (props.$referrer) props.$referrer = sanitizeUrl(props.$referrer)

							// Sanitize element chains
							if (props.$elements_chain)
								props.$elements_chain = sanitizeIds(props.$elements_chain)
						}
						return event
						},
				})
			}
	</script>
	</body>
</html>