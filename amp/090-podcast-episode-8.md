---
title: Episode 8
url: https://ampcode.com/podcast/episode-8
source: crawler
fetched_at: 2026-02-06T02:09:00.308403585-03:00
rendered_js: false
word_count: 8908
summary: This document explores how the Amp team evaluates large language models for agentic coding, specifically focusing on the importance of tool calling, model alloying, and the ability of agents to self-correct during complex tasks.
tags:
    - llm-evaluation
    - agentic-coding
    - tool-calling
    - model-alloying
    - ai-development
    - software-engineering
    - self-correction
category: concept
---

In this episode, Beyang sits down with Camden to discuss how the Amp team evaluates new models: why tool calling is the key differentiator, how open models like K2 and Qwen stack up, what GPT-5 changes, and how qualitative "vibe checks" often matter more than benchmarks. They also dive into subagents, model alloys, and what the future of agentic coding looks like inside Amp.

**Camden:** I'm really interested in this because we've like kind of had a poor man's alloying with the Oracle.

**Beyang:** Yeah, that's true.

**Camden:** Like, uh, using the, the strengths of Sonnet to generate stuff quickly and like get something working and then using the, uh, reasoning power of o3 to kind of be a second opinion.

**Beyang:** All right so we're here uh with another edition of Raising an Agent this time we're going to be talking about how we evaluate different LLMs and models and so I got Camden from the Amp core team here uh to talk through how we've been doing that. Camden, how are things going?

**Camden:** Things are going great It's an exciting week for model developments and really, I guess, a few weeks of lots of interesting stuff going on.

**Beyang:** Yeah, definitely. Definitely. Yeah. So I guess to kick things off, you know, for people who don't know much about Amp, do you want to talk about like our philosophy related to what models we use and how we use them?

**Camden:** Yeah. Yeah. So Amp is a little bit different in that, uh, we build something that takes the best of models across the industry, not just from a single provider, um, and slot them in to build a product that is as a whole more effective at coding.

**Beyang:** Yeah. And so what, what current models do we have? Uh, like running inside Amp?

**Camden:** Yeah. Yeah. So our primary model right now is, uh, Sonnet 4. And this is the one that drives everything else. Um, and then the, the other models that we use are, um, we've been using o3 for our Oracle agent. Um, Oracle is a, the Oracle is, um, a, like a code review and, um, kind of planning agents meant to be kind of a, a smart, deep thinking agents to supplement Sonnet's, uh, faster iterative behavior. We also use Gemini Flash for summarization as a quick and cheap summarization model. We use Haiku for title generation. And let's see. And now we can enable GPT-5 as the primary agent for testing. Haven't enabled it by default, but we want users to be able to see how it works.

**Beyang:** Yeah. And this is a big milestone for us because up until now, like you mentioned, we use a variety of different models for different use cases. But up until now, we've basically just had the one model used as the main driver for the agent, right?

**Camden:** Yeah, yeah. We briefly had a similar toggle for Gemini Pro.

**Beyang:** Yeah.

**Camden:** But ended up removing it when we decided we wouldn't be able to get it to the level of quality that we were getting with Sonnet.

**Beyang:** Yeah. Do you want to talk a little bit about that? Because that was also an interesting moment. There are certain things that I think like Gemini Pro did really, really well, but it wasn't quite, at least for our use cases, it didn't quite get to the bar that we wanted to see.

**Camden:** Yeah, so I guess like to compare, Sonnet has two things that it's really good at that other foundation models have struggled to compete with. One is tool calling. Sonnet does that really well. It selects tools well. It generates arguments well. It, like knows how to explore a code base and iterate well. So it like really has this kind of agentic behavior built into its training. So with like in comparison, Gemini, it's really good at one-shotting. Like if you tell it like build me a website, it'll do it. And it'll do it fast and well. But when trying to use it in an existing code base or on complex tasks that require it to kind of explore the code base, find what it needs to do, I really kind of struggled with that. And ultimately, like Amp is built around this iterative self-correcting loop. So an agent that can't self-correct isn't that great yet.

**Beyang:** Yeah. It's like, it was really good at, you know, here's all the files, page them into context, and then like, you know, write a function that does X, Y, and Z. But I remember saying that sometimes even like the basic, like tool calling schema would kind of like confuse it or it would like get it wrong. And there'd be like a tool calling error that was completely unrelated to like anything reasoning related or, you know, high levels. It was almost just like the low-level mechanics of emitting tool calls in a structured form.

**Camden:** Yeah, exactly. The tool calling wrapper, I mean, the tool calling API is really just a schema that you ask the agent to generate things in and then pull the tool args out of the schema and send them back as tool calls. And this schema that was used for Gemini, like it would fail to generate correctly formatted. It was Python code that was generating to call these tools. And if you have a poorly escaped Python string, then that shows up as an error to our users.

**Beyang:** Yeah. And it's one of those things where it seems minor. It's like, oh, it gets it most of the time. But when you're in the middle of trying to write some code and you get this error and it disrupts the flow, it's actually quite annoying.

**Camden:** Yeah. Yeah, especially like when we're doing like tens of loops before the next user interaction. Like if it exits at the second iteration, then like you might have walked over, grabbed some coffee and come back and was not doing anything.

**Beyang:** Yeah, yeah. And we have someone on the team, Geoff Huntley, who loves doing it in that style. A Ralph Wiggum style, where it's like you fire and forget, go grab a beer at the pub and then, you know, you come back and hope that it's completed. I think if you prompt it well, I think we've seen really good results with the existing agent that have been doing reasonable stuff. But I feel like, you know, what we used to say with chained LLM calls, like each one is sort of a dice roll and so if you get like you know 98% fidelity on the first one that decays like 96% and then 92% and then um you know after a couple hops it quickly decays uh exponentially to something that is a lot more reliable um and that exponential decay even if it's like 98% percent uh you know fidelity on the first call it's still an exponential decay

**Camden:** yeah yeah and so the the interesting thing is like that decay was really visible in Gemini, um, where like if it started getting off track a little bit, like that compounded, um, and like Sonnet is interesting in that it kind of self-corrects. Like if it sees an error, like for example, if edit file failed for whatever reason, whether that's our fault or Sonnet's fault, um, like it would find a way to do that same thing. And like lots of times you'll see it like pull out said to the file or just like use the create file to override the whole thing. Find some creative way to get itself out of the ditch that it landed itself in and kind of move forward with its task.

**Beyang:** Yeah, it's got like multiple mechanisms for getting what it wants. I've seen a couple times, like if for whatever reason, like the read file tool fails, or actually it's like the write file, the edit file tool fails, it will like write a bash script to like, you know, cat the contents. It's like it knows enough about the tools at its disposal to find these sort of like creative workarounds.

**Camden:** yeah it is interesting and like I think earlier on like we spent a lot of time thinking about building an orthogonal tool set like tools that don't overlap at all um because it would confuse the model and like it wouldn't know how to proceed but now the model's kind of gotten good enough that this overlapping nature of the tool calls is almost an advantage um because when things go wrong and and they still do, there's different paths forward, and the models can discover those.

**Beyang:** Yeah, it's like a human. If for whatever reason your editor is acting up today, you have another editor, you fall back to editing files by hand. It's like you're trying to create a fork around. Cool. All right, so we tried it out with Gemini Pro. At that point, it didn't work very well. Are there any other models that we've tried along the way

**Camden:** as the main agentic driver yeah so uh every new model that pops up um I usually throw it in as the main agentic driver to test it out because like uh not because I think it's going to be useful there but because I think that's one of the best ways to kind of learn the personality of a model like being up there close and personal like using it for other things like summarizations all in the background and just like you don't get to know what its quirks are and things like that yeah Um, so I, uh, have like experimented with Opus. Um, we, uh, we don't use Opus in, uh, Amp mostly because it's more expensive than we think that the improvement is worth and

**Beyang:** it's almost slower.

**Camden:** Yeah. Yeah. And like, uh, Sonnet it's good and it's good enough. And, um, I don't think we can just buy the additional flow in cost. For the, the self-correcting loop.

**Beyang:** Totally.

**Camden:** Um, and then I've also experimented with, uh, quite a few of the, the new, um, like open models, um, a couple of weeks ago, Kimi K2 had its moment.

**Beyang:** Yep. Yep. Yep.

**Camden:** Um, and then Qwen3 coder is still really exciting.

**Beyang:** Yep. Um, how, how did those stack up? Cause there was like a ton of hype around those and you saw people tweeting about like oh my gosh it's like so blazingly fast yeah

**Camden:** yeah so they're they're quite good um like I I think these are some of the first uh open models that I've seen that can really do tool calling well um and so far that's kind of been the the limiting factor is if you can't do tool calling well yeah then we can't slot it in easily and we can't use it for semi-general use cases and So that was really exciting to me because especially when you have these open models that do this, now you have choice in provider as well. And along with the new open model stuff, there's been a lot of improvement on the hardware and provider sides as well. So companies like Groq or Cerebras, they're building custom hardware that makes serving these models super fast. Yeah. And fast is kind of a dimension that, uh, as like the AI coding industry hasn't been able to explore yet because really the, uh, the speed hasn't been there for models that are good enough to do particularly useful tasks.

**Beyang:** Today we're in like the 56k era of agents, I think, where it's like, you know, you still kind of like have to wait for it a little bit. This lag people are almost like orienting their workflows around like oh you know this one's working I'll let it do this thing I'm gonna fire up another thing or maybe I'll you know check my my messages or something yeah

**Camden:** I I'm excited for a couple reasons they're like speed because it's so unexplored the DX of it is also unexplored like the experience of how you would even interact with these could change so drastically like right now it's like the kind of fire and forget, you let it do its thing, you come back. If you're really bored, you can watch it. Um, but like in a world where you're generating 2,000 tokens per second, um, that is a world where we could maybe spin up 10 of them at the same time. And if five of them fail, who cares? You know, because it's now cheap. Uh, and if like you come back and one of them has the right thing and we can analyze results, 10 times faster, then like the self correction has more opportunities to, to pick up on like the paths that are promising.

**Beyang:** Yeah, totally.

**Camden:** Yeah. So that part is like a, a really fast, but slightly dumber model. And I think that's kind of interesting for a lot of the more specialized use cases, like specifically we have, we've got this code search agent. Um, and it doesn't need to really understand the code well. Uh, it just needs to be able to sift through large amounts of files, pick out the ones that are actually relevant to the query that you're asking them out and, uh, spit that back to the primary model that does the real thinking. Um, so this is a scenario where the speed smarts trade off is very clearly in the direction of speed. Um, and we can take advantage of these new models to plug it into that spot and, um, provide a better user experience out of the box.

**Beyang:** Yep. So I think like a lot of people will want to know, like, you know, if, if Qwen and K2 were like almost there and they're like, so blazingly fast, um, you know, why didn't we turn these on as the main agent, a driver? Like, what was your kind of like qualitative assessment of how they performed in all things considered for the overall like user experience

**Camden:** yeah so like I I think it's exciting progress but I think it's still very obviously not at the level that we're getting with Sonnet

**Beyang:** yeah it's like 80% of the way there?

**Camden:** yeah I think that's fair

**Beyang:** what does 80% mean is like 80% is good on each thing and that kind of degrades over time or like it it would work well four out of five times or

**Camden:** For me it was it would work well on four out of five like mini tasks none on so like the problem is that like a a larger task that I give it a composed of tens of mini tasks so like if you were to like say um edit this file that comments or like modify this function to do x then like eight four out of five times that would work well um but if you're saying design, build, test this feature, then that's a handful of tasks and it gets into this exponential, the multiplicative decay.

**Beyang:** It's really interesting because I think it's like, it really depends on like how many hops is your ideal use case. Because I feel like right now there's this gap that I see in the world of people using AI dev tools where like some people are still very much in like the AI IDE modality, which is like human in the loop at every single turn. And then other people have made the leap to like full agent mode, which is like, hey, I'm going to have this write, you know, 95% of my code. I'm just going to instruct what to do. And it's almost like if you're coming from the, like, I approve every single file change and tool use, I'm like in the loop with the model. It's like the open source models are probably like, you know, they compare very favorably to what you've been using. But the people who are in like full agent land where we are, it's like a little bit of degradation means that I can't fire and forget. It almost like pulls you back into the, you know, old school. I say old school, it's like, you know, 12 months old.

**Camden:** Yeah. I mean, it's kind of this self-correcting loop. Like if you have the right feedback, then these open models can be great. But like right now, the human is kind of the fallback feedback. So if you don't build out the tests or the type-packing or the linting or whatever, then the human has to be the one that gives the agent the input to fix itself.

**Beyang:** Yeah.

**Camden:** So at that point, having an agent that gets that last 20% is really important.

**Beyang:** Yeah. It's like that last X percent to make the exponential decay across, I don't know, like 100 iterated tool calls. There's like some threshold at which it flips.

**Camden:** Yeah.

**Beyang:** Okay, cool. So like our assessment then is like K2 and the new Qwen model. See potential there to power like the narrowly scoped sub agents for like search and retrieval, but they're not quite there yet as the main agentic driver. But now today GPT-5 is out. What do you make of GPT-5?

**Camden:** Yeah, yeah. I'm excited about GPT-5. I think it's like a, um, a good general model. Uh, to like, that's what it's supposed to be. So I'm glad. But I think the thing that excites me is like, uh, we talked about tool calling earlier and historically OpenAI has, uh, really kind of been behind there. Um, and GPT-5 seems to have really raised that bar. So now a lot of the use cases that we would use a smarter, more heavy reasoning model that we couldn't really before because the tool calling wasn't there, those now open up for us. So I think that's where I'm really excited is kind of pushing the boundaries of how we can use a strong reasoning agent that can also call tools well.

**Beyang:** yeah and and this is like the first model that we've tested for which it's it's like an actually a contender for that main agentic driver

**Camden:** yeah yeah it is and you know there's there's going to be it's going to take time to really tune it and to like figure out what it's good at and like figure out whether this is something that can provide the same quality of experience that Sonnet does yeah but early signs are promising like early signs are exciting and like exciting enough that we decided to put it in front of users and get their takes as well

**Beyang:** yeah and the thing that you mentioned about it taking some amount of time I think that's especially salient because I think it's almost dangerous to say like okay we have this existing model harness uh that's been kind of like tuned for one class of models you know mainly like Sonnet and Opus uh uh mostly Sonnet um and to say like okay like here's a brand new model uh let's drop it in and expect it to just you know just work as well much better it's it's dangerous I feel like if you do that it can maybe give you a false impression of the model's actual underlying capabilities.

**Camden:** oh yeah yeah absolutely I as I'm doing that's like the thing that I have to constantly keep in my mind is like trying to not evaluate models for a specific use case, but rather like try and use the eval as a way to pull out what models are good at. Um, because we're changing so quickly. So like the, the scope of problems and the types of problems that these models can solve is also changing quickly. So being open to a model not performing as well, our benchmarks that we kind of arbitrarily decided on. Yeah. Finding the things that it's it really shines at I think that's where there's a lot of opportunity to kind of build alloys of models that says okay uh that lead to a better overall experience

**Beyang:** I like that term alloy too

**Camden:** yes yeah did you read that paper?

**Beyang:** I did I did there was there was a paper and then there was also like the Expo uh blog post I don't know if you saw that as well um but that was, yeah, like alloys are this idea that you can combine multiple models in sort of like the same inference chain. And almost like counterintuitively, this yields better results than using like one model or the other. And I say counterintuitive, because it's like, it's like you're switching brains midstream, right? And you would think that a completely separate model would have more trouble, you know, reasoning over tokens generated by a different model, because in theory, you know, the perplexity is, is higher. And, you know, that's typically correlated with like lower quality output. But there's been some research that shows it's exactly the opposite. And, you know, you can speculate as to why, you know, there's like more diversity of tokens or maybe it's like closer simulation of like human output or something but like there's something about that that um I don't know it's an area of active research and it's something that I think we're excited to explore

**Camden:** I'm really interested in this because we've like kind of had a poor man's alloying with the oracle like yeah that's true like uh using the the strengths of Sonnet to generate stuff quickly and like get there get something working and then using the reasoning power of o3 to kind of be a second opinion. That side of the intuitively makes sense to me, but mixing the tokens together is just feels dirty.

**Beyang:** Even we haven't gone that far, but, you know, everything's changing, as they say. Cool. I want to talk a little bit about how our own impressions of GPT-5 have evolved, because I think this speaks to the model evaluation process. So, like, I have my own thoughts, my own, like, first impressions of GPT-5, but, like, what were your, when you first got access to the model, what was the initial...

**Camden:** I mean, yeah, so the first thing I did was just plug it in, right? And it was kind of awful. I think it worked.

**Beyang:** Right. In what ways?

**Camden:** So, like, our system prompt is very tightly tuned to Sonnet, right? It corrects for a lot of Sonnet-isms that either don't exist in GPT-5 or like really push GPT-5 into kind of dangerous and weird, not dangerous, that's a bad word, but weird territory. So like our talk about like our prompting around succinctness, right?

**Beyang:** Yes.

**Camden:** GPT-5 took that very literal.

**Beyang:** Yes, I remember that. It was like emitting like 4 word responses. Yeah, yeah. Not even like grammatical, right? Like, it's like,

**Camden:** "why use more words when few do fine?"

**Beyang:** It's very instructable, right? Like, which is a big delta from, I think, like our experiences with Sonnet, especially like, you know, like Sonnet 4 is much better, but like Sonnet 3.7, I think the common complaint was that it disregards instructions because it wants to do its own like agentic.

**Camden:** Yeah. Strong personality.

**Beyang:** Strong personality. Yes. Yes. Yeah. Strong constitutional personality, I think that folks from Anthropic would say.

**Camden:** Yeah, absolutely. Other things like, I mean, another example of this is we instruct Sonnet to link its responses to the relevant pieces of code. And when it works great, it's really nice. But Sonnet does that very consistently. And when I toss that same prompt chunk into GPT-5, it responded great. And so this is something I'm excited about is less, uh, more pliable, um, prompting, um, just kind of being able to get it to do things that it. Isn't doing out of the box more easily.

**Beyang:** Yeah. It's, it does seem more steerable and definitely like follows instructions. Uh, like you said, almost to, to a fault. But again, this is, this is coming from like an indexing on Sonnet world where if you want to steer it, um, there's certain instructions really doesn't like to follow and that requires much more like intentional prompting doesn't seem to be the case of the GPT-5

**Camden:** yeah yeah I mean another example on Sonnet is like emojis, like, "oh get rid of emojis"

**Beyang:** yeah Thorsten hates emojis

**Camden:** yeah yeah I don't think I've seen a single emoji in GPT-5 so Thorsten'll be happy

**Beyang:** yeah and no and no, "you're absolutely right!" yeah yeah it's much more like personality wise Sonnet feels um Sonnet presents almost like a uh patina of high agreeability high agreeability right like you're absolutely right whatever you say you know that's that's great underneath the hood it doesn't actually want to obey as many instructions whereas GPT-5 feels more like you know it's less nice uh on the surface but it will actually do more of what you tell it to do. At least that's my, my general impression.

**Camden:** Yeah. The, the interesting thing there is like one thing, one behavior in GPT-5 that I've struggled to prompt out so far is, uh, kind of asking the user for permission or input to proceed. Um, like,

**Beyang:** yeah

**Camden:** it wants the human to check its work in, in a lot of cases. Yeah. Yeah. So I, I'm sure there's probably a way to prompt us out. I haven't figured it out yet. Um, I, I think that's another characteristic that's interesting that theme

**Beyang:** yeah that's interesting so so my first impression of the model I did basically what you did um is you know drop it in and there wasn't really any customization and the first thing I noticed was you know I I had to run on some simple task and then like I alt tabbed away to do something else and I came back later and it was still running it was still running like the first uh search query I was like why is this so slow uh and it turns out that like I think the the model with the kind of like Sonnet scaffolding um it just had a greater propensity to issue queries that were like full natural language uh questions to our uh search subagent um whereas Sonnet uh it typically it does it does more keyword searches or its natural language queries are more succinct and so with the like longer natural language queries our our search subagent um would just take that and run with it and so it would kind of like spin and spin and spin wanting to kind of like cover all the possible paths of what the user might be looking for and the upshot was it just ended up taking uh much longer and so like that's that's another thing that we had to tune.

**Camden:** yeah yeah it's like uh the the verbosity is it took a little bit of work um but it I I talked to some people at OpenAI and they like have this new verbosity arg in the API which we're not actually using because we can just prompt it and be more specific about how verbose we want it to be but it's something that like GPT now responds well to um so it took a little work but

**Beyang:** yeah and I think we're still you know we've we've had access to it for um you know a couple weeks now and so we've we made a lot of of progress from those initial uh days and I think it works really really well now like I'm really excited uh I'm gonna I'm just I'm gonna use it as like my main driver for a week and and see see how it goes um but I think we're still at like the very tip of the iceberg because going back to the you made much earlier it's like we're no longer the days where you just like drop a model into uh application scaffolding and be like okay it's now it's in the model selector and and have at it I think um at least our takeaway is that you have to be much more intentional about uh making sure that there is the right kind of like scaffolding around the model otherwise um I don't know like, all... Everything comes down to the user experience at the end of the day and like as tool builders like that's our contract with the end user it's like a good user experience something that you can use day to day and it's not frustrating and it does take a fair amount of of tweaking.

**Camden:** Yeah. And I mean, I expect to be doing a ton of tweaking still like over the next week or two, like there are still plenty of things that I, I want to fix. Um, but the, the nice thing is like, uh, it's good enough now that I can use it for my day-to-day tasks, which means that the, the behaviors are more discovery. Yes. So there was definitely like a, a threshold below, which it was just frustrating like I felt like I was getting such poor results that I wasn't even able to um push it to do what I wanted better, because I didn't even know why it was working so poorly

**Beyang:** yes yes as as you're right like the threshold is like as soon as I can get this point like maybe it takes a little bit longer maybe it takes a couple of like behavior shifts on my end but as long as I can get it to the point where I can like have it do stuff and then push it uh that's night and day from like oh it didn't work and I can't get it to work and so ergo I have to like fall back uh to not using it because like part of I feel like part of making this work is also it's like this human reinforcement learning right and so until it gets good enough to be like used in the everyday like reinforcement learning process as a human you're going to get like a limited amount of feedback or it's going to be much tougher to iterate on on the the prompting and the tool descriptions and all that scaffolding

**Camden:** I'll be really interested to see like how our users react to it because um even with all the tuning like it's not going to feel the same with Sonnet it still has its own personality

**Beyang:** yeah

**Camden:** but like I, I found I was initially really frustrated even after I got it working reasonably well because I was so used to Sonnet-isms that like those have ingrained themselves into my workflow yeah so like when GPT doesn't react the same way like, "what are you doing?"

**Beyang:** this feels like the positive reinforcement

**Camden:** yeah yeah

**Beyang:** I totally get that um I I part of me wonders so like one of the things that's really exciting is the the high degree of instructability which we've already touched upon a little bit and I think like that has implications for use as like the main agent driver which is like that's that's an experiment that'll effectively play itself out in only the next couple weeks as we see how users react to it but the instructability aspect of it is also exciting because that potentially opens it up to being uh much or versatile in the use of sub-agents uh because it's more instructable and so I wonder if if now we'll see a proliferation of sub-agents that are targeted at different sub-tasks, like search and retrieval or explanation, explanation at different verbosity levels or in different personas. Because GPT-5 does seem to obey instructions pretty well in terms of what you want it to do, how you want it to behave, the style in which it answers.

**Camden:** Have you had the chance to kick the tires on the smaller models that were released today?

**Beyang:** No. Have you?

**Camden:** No. I ran the tests against them. But I'm curious if they have the same properties of GPT-5. Like a little less stupid or a little more stupid and a little faster.

**Beyang:** Yeah, yeah, yeah. The thread is also interesting. You tried it with GPT-OSS, right? Someone did.

**Camden:** Yeah, I think Nico maybe, but I haven't played around with the OSS models much. I've been very focused on GPT-5. Yeah, yeah, yeah.

**Beyang:** Yeah, that's the big moment this week. Cool. Well, like, where do you think the path goes from here? Like, now we have, like, two top-level models within Amp. There's a lot more exploration to do. There's also these, like, open-source models that are quickly closing the gap. You know, what's next on your plate in terms of like evaluating models? What are you most excited about?

**Camden:** Yeah, so right now I'm excited about kind of productionizing the bits that we've got in the pipeline. So like finishing tuning GPT-5 as much as that's ever a finished job, running it through more rigorous evals and getting user feedback across a more diverse set of tasks. But then the other big thing that I'm excited about is like exploring the speed dimension. And like I said, that's one of those that could really change the UX of these tools. And I would love to see how far we can push that. And like, I mean, Amp's usage-based model makes this easier to experiment with because we don't have to worry about this being profitable.

**Beyang:** Yes. We don't have a cost constraint that would force us, that would close off like some areas of exploration.

**Camden:** Exactly. So like adding that 2000 tokens per second, you can burn through a lot of cash. And it's super fast. So if you're only doing 200 tokens, that's fine. But like, I mean, for me, I'd be happy to burn through a bunch of cash to get my job done more quickly.

**Beyang:** Yeah. It's like, if you could get sort of like real time. Feedback, but at the level of quality and robustness that we currently see with like Sonnet and GPT-5, I feel like that would change the game, uh, again, like that would be like a step function. It would be like qualitatively different. Um, because of, I mean, there's the whole, what are they? They call it like the different thresholds of like latency at which human brain like perceives it. If you get it to within the range, like couple second latency for like most tasks. It almost, it almost addresses one of the key pain points in agentic coding that I see now in field personally, which is the distraction effect.

**Camden:** Yes.

**Beyang:** It's kind of like, like you're waiting for it to do.

**Camden:** Do I have tab over to Slack?

**Beyang:** Yeah. Yeah. Yeah. It's like you tab over to Slack and then you get sucked into the slack thing and then and then you're like oh crap it was doing something let me go back and then you have to like paging a bunch of context again

**Camden:** yeah the uh the threshold that I care about is like, "do I switch to another window?" like if I can if it can keep me engaged enough that I don't leave and like I'm following along with what it's doing because it's doing it fast enough that I uh don't care even following along like that's going to be a UX thing to solve yeah we're generating this fast

**Beyang:** yeah

**Camden:** like I can't keep track of tens of tool calls being called totally in five seconds then

**Beyang:** and then it's just like okay let me just see the diff it it generated and we'll see if it it was right or wrong or on the right right track

**Camden:** so I think we're going to need like new UI abstractions even

**Beyang:** yeah yeah um or there's there's just like certain elements of the UI that don't have to like take up user attention and or and make it seem like they're not waiting like the whole streaming text thing let's be honest it's just the way to show progress uh and holding attention so that you don't get bored because if they're like if if rather than streaming text if it just like had a spinner and you had to wait for the whole thing to appear at once I think people would the the lived experience of AI would be a lot less like magical yes um and and I think it's it's also kind of like I'm optimistic here because like you said before it's like the the open source models are super fast they're not quite there yet for you know the full agent stuff and you know who knows how long it'll take to get there maybe like next month we'll be there maybe it'll be like you know six months from now um or longer but but I think I'm very optimistic that her like um these specific tasks like search uh will be able to get them to a point where they can work just as well but be be a lot faster and I feel like um I don't have hard tests to back this up but I feel like a lot of times I'm waiting it is for like a particular like uh um like search sub agent run to complete because it's doing its thing right it's finding the context and and oh and

**Camden:** also goes back to the like you're not showing streaming progress because it's all collapsed yeah

**Beyang:** yeah that's true it's like yeah yeah yeah like you have less patience for uh the sub agents in Amp because um we try to make interface less noisy yeah interesting um okay one last thing that we haven't discussed yet the the whole like evaluation process you know like quantitative evals qualitative evals uh vibe checking um what is what is kind of like your process and philosophy for evaluating models

**Camden:** yeah so I'm I'm really heavy into qualitative evals um like basically every time I've looked at a quantitative eval and tried to get any useful information out of it I fail um because like the the number of dimensions that we're trying to measure in order to like come to the best user experience it's it's too many to condense into any single number or even like a set of numbers that captures the "how this actually feels?" So like to the extent that I care about quantitative evals, it's like the is this good enough even to like land in our in our radar? And like there's enough out there that I'm comfortable depending on those to kind of do the initial weed through of...

**Beyang:** this is like the phone screen right it's like you kick the tires and...

**Camden:** that's a great great way to um yeah so like and then the other side of this is um to give models the best chance you really have to work with them right like you have to do the tuning ahead of time in order to even see how they could perform on the types of tasks that we're throwing at it in Amp. Um, so we have built out like a standard set of tasks that we manually run it through and like run it through many times and tune the prompts as we go and kind of take notes about like features of the models that we see, because like we talked about earlier, the not only do we want to pick the best models for specific tasks, but we also want to find what models are good at so that we slot them into the more specific things. Um, and if we're just measuring for the specific things that we care about, then we'll fail to discover the, the bonuses.

**Beyang:** Yeah. It's like, if you try to reduce the dimensionality of your evaluation criteria too much, you basically setting yourself up to like miss any sort of like new capabilities or possibilities.

**Camden:** Yeah.

**Beyang:** which is very dangerous in AI land because new things are emerging like every month.

**Camden:** Yes, absolutely. Yeah. And we have to basically change our eval set every time a new model drops.

**Beyang:** Yeah.

**Camden:** Which kind of defeats the purpose of an eval set.

**Beyang:** Yeah. Yeah, totally. It's like, um, oh, it didn't pass on this, but the vibes feel good. So let's make it pass. And then it's like, what are we even doing at that point? Yeah.

**Camden:** Um, yeah, I think that's right.

**Beyang:** So what is like a qualitative eval then? Is it just like a workflow that, you know, you did at some point and now you just wanted to do it again?

**Camden:** Yeah. I mean, I start, I always start with like a vibe check, just throwing it in and using it for my, my daily tasks. Um, and, but then I like, it's kind of a set of scripts. Like I maintain a couple open source repos. I nab a GitHub issue from there, throw it at Amp and say like, "all right, fix this."

**Beyang:** Yep.

**Camden:** And then sometime like another dimension is heavily prompted, like go through this checklist.

**Beyang:** Yep.

**Camden:** Other dimensions are like how well it uses sub agents to split up large tasks or how well it selects the most useful tool for a job.

**Beyang:** Yep.

**Camden:** Which those are things that like, I don't necessarily want to force it in any one direction because they can choose different paths and that's okay. Like GPT-5, for example, doesn't seem to like running our code-based search agent as much. But it can run a bunch of parallel searches at the same time. So it ends up being okay.

**Beyang:** Yeah. It's almost like, I feel like listening to you describe this, it's like the role or the job to be done here is like you're a model taster. You know, you throw it all in.

**Camden:** Model sommelier.

**Beyang:** Yeah, exactly. It's like, ah, you know, it's no subagent use, but more from this region. It's funny, too, because I feel like, you know, like developers were very technical people. We always like to be very scientific and data driven but it a lot of it does come down to art more than science even if you talk to like uh like ML researchers now like model researchers talk about like you know how do you know at what point in the training process do you know if it's ready I feel like you hear like similar echoes there it's like you know you halt training, you try the model with existing weights, and then either you keep going or you make adjustments along the way. There is no scientific method where you just turn the crank and

**Camden:** it's kind of interesting.

**Beyang:** It is.

**Camden:** It's frustrating. Trying to do this and not be able to build a graph of my results. Frustrating.

**Beyang:** I think that's And we've discussed this before. That's one area where quantitative evals do seem useful. It's basically like unit tests or like regression tests where like you're trying to explore some new area and get it to work for that, but you don't want to get into this like whack-a-mole state where there are these other existing use cases that are really important. You want those to remain robust.

**Camden:** Yeah, absolutely. And that's kind of what the setup scripts that I'm talking about acts as. Yeah. Because even if they're human-driven, I still act as like a, um, a set of regression tests. The things that I really do like quantitative, uh, evals for though, are like more observational analysis. Um, so like, even if it's not a number goes up and being able to look at trends across like many runs is really useful. So like if even a tool call counts or like, I mean, latencies are one of the really hard measurable things that we still have.

**Beyang:** Yeah.

**Camden:** Um, and then like, uh, things like number of lines generated, even like how wordy the models are, um, the, those are interesting and like, what aren't something that you'd necessarily be able to just pick up on if you're not, uh, looking at it across the broad set of samples.

**Beyang:** Totally. Sometimes those point you in the direction of like, oh, um, you know, it's going to behave like this or or maybe it reinforces some kind of like vague impression that you have like oh it seems more verbose is the data bear that out or is am I like hallucinating something here

**Camden:** yeah absolutely kind of hints you in the direction of uh what might be worth pursuing

**Beyang:** yeah yeah totally. Um I also think it's it's interesting because I think one of the things that over indexing on quantitative evals does is it makes it seem like it's it's like a horse race uh or like any sort of race right like where there's like one winner you know first place gets the gold medal and then everything else is just useless and I feel like with agents especially we might be heading into a world where you know each model has its own set of characteristics and and strengths um and so it's maybe it's no longer going to be the case where it's like you know the the main model that you use that gets like 90% of your day-to-day usage is just one model you know we don't necessarily have to uh you know like when we're when we're evaluating GPT-5 in the next couple weeks it's not like the decision in front of us isn't like you know Sonnet or GPT, it's more like let's actually understand the strengths of each model and let's see how human users react to it, how they change their behavior to unlock its capabilities. And then, and then we just have to figure out how to expose these things in the application in a way that like steers people toward the sweet spot of each model, I guess.

**Camden:** That steering is a really tough problem too. Yeah like the these tools are so wide open and the types of problems that they can solve that like I mean everyone on the Amp team uses Amp extremely differently

**Beyang:** you'd notice that just scrolling through the thread feed it's like who's who's got the like 100 message chain versus who's doing the kind of like short sweet like sniper sniper shot uh

**Camden:** yeah and I mean I'd call us all expert Amp users But like trying to then even give recommendations for how to use Amp is difficult because we don't all agree.

**Beyang:** Yeah. And it's one of those things where like, I think philosophically too, we want to make, we want, we want to make a power tool, right? You know, a power tool that's easy to use, but it's got a tool. It's got to be a tool that, I don't know, like different people are going to use it very differently. Um and I don't know do you have thoughts on like how to do this properly I I mean I I don't so far but

**Camden:** no it it has and like I mean the thing I always try and keep in mind is that like you can have a pit of success that users aren't forced to fall into

**Beyang:** yes

**Camden:** like a golden path but you're allowed to stray like

**Beyang:** yeah

**Camden:** so I I mean we've kind of gone down this direction with our public blog posts, right?

**Beyang:** Yeah.

**Camden:** This is how I use Amp. It's not prescriptive. It's descriptive.

**Beyang:** Yeah.

**Camden:** Which I think works well and gives people ideas.

**Beyang:** Yeah.

**Camden:** Without kind of baking it too far into the product.

**Beyang:** Yeah. And almost like recipes where like, you know, if you're first starting out, try this and then you can kind of evolve things. The phrase that comes to mind, like, you know, I think it was like, it was Kiefer Borson originally, which is like, you want to cut with the grain, cut with the grain of the model. Um so it's like each model has a sort of like natural behavior that that like it wants to do things in a certain way because it was trained to do it in that way

**Camden:** yeah

**Beyang:** and you really don't want to go against that because then you're just you're kind of like fighting against this nature um and but like the set of things it can do is potentially vast I mean there's like billions and billions of parameters um it's yeah I don't know like I I I hate to over like anthropomorphize but in some ways it does feel like working with a human being right like every human is going to be different and when you start to work closely with someone it's more about understanding their unique talents their strengths their weaknesses and how to like communicate with them

**Camden:** yeah I mean I mean And that's why I used the word personality earlier. It's like, you can, you get to know the Sonnet-isms and grow to depend on them. But there will be GPT-5 isms, there'll be Gemini-isms.

**Beyang:** Do you have any inkling for how to make these choices salient to the user at a top level? I think we're, you know, we've been very like public about like, you know, no model selector, at least not in the way that it's been implemented for like chat based LLMs.

**Camden:** Yes. I mean, I think that's still the right choice just because of how sensitive these are to the system prompts. I don't know. Like we just can't build something that works for every model well with its own unique set of system prompts um but like I really like our sub-agent model

**Beyang:** yeah

**Camden:** I mean where I mean it kind of it keeps the the agent isolated in its own little box and it's clear to the user that this is something different and behaves differently and it had the name. Uh, it's like the Oracle is a name describing what it's meant to do.

**Beyang:** Yup. And it's distinct from the model name, which today it's o3, but you know, we were just discussing like, you know, maybe it's time to change. Um, especially cause there's certain behaviors in GPT-5 that seem, uh, especially on like high reasoning, uh, mode, right. Which seem like it could be competitive or, or better than o3 in some cases.

**Camden:** Oh yeah, I don't think it'll be a hard switch.

**Beyang:** Yeah, and then it's like, you know, you've changed the implementation to make it more or less like strictly better. And at that point, it's like an implementation detail. You don't need to surface the underlying model identifier to the end user. Because like, honestly, it's not just the model you're changing. It's also like the tool descriptions and the construction of the event and the code that surrounds it too. So yeah anyways there's a lot of work to do we should probably get back to it there's a lot of stuff to explore especially today um I don't know any any final kind of like parting thoughts

**Camden:** yeah I'm just I'm excited to see how Anthropic responds.

**Beyang:** yeah and you know I think there's a lot of great people there insanely smart and I just feel very fortunate to be in this position I mean living at this time, you know, sometimes you get like pinch yourself, like what time to be alive. And it's great to have so many like intelligent people advancing the frontier of the models. Yeah. Everything's changing and everything is going to continue to change. I don't think there's like an end in sight yet.

**Camden:** Nah, here for the ride.

**Beyang:** Cool. All right.