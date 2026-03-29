---
title: Episode 2
url: https://ampcode.com/podcast/episode-2
source: crawler
fetched_at: 2026-02-06T02:09:05.135792958-03:00
rendered_js: false
word_count: 5774
summary: This document explores the shift from traditional to agentic programming, emphasizing how architectural intuition is critical for guiding AI agents through complex, non-local code changes.
tags:
    - agentic-programming
    - software-architecture
    - developer-workflow
    - ai-coding-agents
    - engineering-mindset
category: concept
---

Thorsten and Quinn talk about how different agentic programming is from normal programming and how the mindset has to adapt to it. One thing they discuss is that having a higher-level architectural understanding is still very important, so that the agent can fill in the blanks. They also talk about how, surprisingly, the models are really, really good when they have inputs that a human would normally get. Most importantly, they share the realization that subscription-based pricing might make bad agentic products.

**Thorsten:** A lot of that stuff would break if you optimize for number of tokens. And...

**Quinn:** Yeah and I agree, If you're trying to satisfy a flat rate pricing business where you want to cater to a bunch of people building emoji games on the weekend and to people that are professional software developers who are some of those productive people on the planet, that's really hard. That's like if you're Apple and you want to also have the $19 Huawei phone.

**Thorsten:** Welcome to episode two of Raising an Agent. This is also week two in that we're recording this. There's already so much more to talk about than last week. With me again, Quinn, our CEO. Hi, Quinn.

**Quinn:** Hey, Thorsten. How's all the hacking been going?

**Thorsten:** It's going pretty well. I just sent somebody a DM saying it's addicting. I don't know what it is, whether it's this you can give into your distractions or something while this thing is running. But I think the main thing that makes it so addicting is, I don't know how it is for everybody else, but for me, I kind of have to get myself into some state of mind when I work on a feature. And it's this, I heard somebody say this a while back that senior engineers have to talk themselves into coding some things. And I like to think of it as that little shuffle that the break dancers do before they do the dance. Like you have to get into the move, the rhythm. And with like the prototype, as we call it, I skip all of this because I just start writing a wish list in the text box and send it off. And then it does stuff for me. And it feels like there's no barrier to entry because I personally would rather prefer it writing some wrong code that I then go in and fix versus me having a blank page that I have to draw something on. So that is addicting.

**Quinn:** And you know how when you're coding and someone comes and interrupts you, it fucks your flow? So when you message me and you're like, hey, Quinn, do you want to record the podcast? I was in flow.

**Thorsten:** Sorry about that.

**Quinn:** Yeah, no. Hey, it's worth it. But I have like a half typed out prompt, and I'm probably going to be able to pick it up a lot faster than if it was like all these code files and tabs and whatever. But we'll see. You got to wait till the next episode to find out.

**Thorsten:** Yeah.

**Quinn:** All right. That's all well and good. Where is it failing for you right now?

**Thorsten:** Where is it failing? That's yesterday what I tried. Okay, so sorry. Taking a step back. Where is it failing? I think, let me order my thoughts here. It's failing for me at certain things where you need some architectural sense of how the whole thing should work. Like it's fantastic when you use a Svelte component as we have, where you have a single file, where there's the CSS and there's like the TypeScript and there's the, I don't know if it's called JSX or something as well, but the HTML, if it's all one file and you have maybe a few other related components and all of the changes are local. And you pointed at this and you say, make this look nicer. And you put a screenshot in. And I did this yesterday a bunch of times. And it's addicting because suddenly I can do front end and I only have to put in screenshots with like an arrow that says this looks bad. And but then the other thing I tried was to create a command that would allow you to take the current selection of the editor and put it in the text prompt, in the prompt editor. And as you can imagine, for that, you kind of need, the prompt editor is not something that's exposed at a high level. It's an HTML element, I guess, right? You need to be able to talk to the extension from the editor or from the, I don't know, and basically say, what's the current active editor? And then add something to this.

**Quinn:** Yeah. It's like the VS Code API, the package.json file, the WebView API that we have. Yeah. It's so many different layers.

**Thorsten:** It's yeah and I'm not there to guide it. Like, I'm not a big VS Code extension developer yet so I'm like, "how would I do this?" so this was exploration and a lot of other things and I told it to do this and it went and did stuff and then I saw in the diff I saw it you know do document query selector stuff to find the editor I'm like, "no no no no that's probably not how you should do it." So what I did was I then, you know, pulled the eject handle and I said, "okay, everything you learned so far, everything that I told you to do, everything you did, and you would now do differently, put this in a single markdown file, put this in a task.md file." And, you know, name is whatever, debatable. "Put all of this in." And then it wrote all of the information it had, all of the things it learned in the conversation in this. And then it summarized correctly after, you know, after editing the file, it summarized correctly and it said, "we should probably find a better way to find the active editor. Like we should have a proper API to, you know, find out which one is active." And then I said, "please also put this in." So then I started a new agent and I said, "somebody else worked on a problem and they wrote up everything they did in task.md. Please look at task.md and also run git diff main", because I was on a branch, "and look at the code they wrote and tell me what you would do differently." And it came back with seven points and it said, "I would simplify this. I would create an API for this. I would do this. I would do this. I would do that." And at that point, the old version didn't even work. So I was like, "yeah, go ahead. Implement all of these seven things." So I basically restarted whole thing. And the new agent implemented all seven and now it works. And I haven't checked the code yet, but apparently it's simplified stuff. But that to me was this moment of, okay, you need to have some architectural instinct to kind of guide it. And if you cannot guide it of what's good architecture or whatnot, it's easy for it to go off the rails. So if you know how to make a change, or if you think the change is, say, locally contained or whatever you want to call it, then it's really good if it's something hairy and you need to invent say new APIs or new primitives then it can get off the rails and one last thought on this is that yesterday while looking at it go off the rails I wondered is this you know that famous curve that we've been seeing where oh the junior engineers love AI tooling super senior you know senior engineers love it but the people in the middle, they're not so enthused about it. And I wondered whether that is because if you're a junior engineer, you're mostly concerned about local changes, like small local changes, and you might not have that gut instinct for architectural changes yet. When you're a senior engineer, you do have that gut instinct for architectural changes. And you kind of know when something starts to smell funny, and you don't really care about the line by line stuff. You're more like, "we should probably not do this in this file and do this over here." And I wonder whether if you're, say, an engineer with three years experience and you haven't seen a lot of things fail or succeed yet and you haven't built up that instinct yet, whether then you're in this uncanny valley of it does stuff, but you don't know why it doesn't work and you don't know why it's bad or something like this.

**Quinn:** Yeah.

**Thorsten:** Yeah. I don't know. That's my thought to start this.

**Quinn:** Yeah. And so where my mind goes is how do you take the approach that you took or something else and have it know that it's failing and then get it on the right path? And what you did, it worked in that case, but maybe it would be worse in another case. So how do you systematize this? And that's tough. I mean, it does feel like a lot of the times I've seen it go off the rails. Another even like super dumb LLM would have been able to identify it. Like I had a case where it was writing a Vitest test and it mocked the exact thing that it was testing at the top of the file and then it tested it and it was the dumbest thing ever. I was shocked that it was so dumb. That was so obvious to catch.

**Thorsten:** But yeah, it tests. It wrote some tests for me a couple of days ago. And then I said, you know, what code do I have to comment out to test whether the test actually tests, you know, what it's supposed to test? Because that's I write tests and then I want to see them fail and only then do I commit them so it wrote his test and I said exactly it's like what comment should I comment out what code should I comment out then he came back with some code I commented out and the test didn't fail and then it was I got to change the whole testing approach and it simplified all of the tests but it took took the attention and the nudging to to kind of trigger this behavior and again like maybe if you're this is your first year of coding you don't think I should test that the tests actually test what they're supposed to test

**Quinn:** Yeah

**Thorsten:** You skip over it but

**Quinn:** Yeah and so one thing we've talked about is when we have these tools like edit file should we have higher level tools like should edit file actually do what a human would do go look at the file see what diagnostics there are go and make the edit make sure there's no new diagnostics added format it should that all be encapsulated in edit file or should that be a bunch of other tools that it sometimes calls, sometimes doesn't. Or if we can tell that it's writing a test and there's an even higher level of us thinking we're smarter than the model, should we have it go and run test coverage, check mutations, have some obvious passes like that? And these are the things we got to answer.

**Thorsten:** Yeah. I think that stuff, I mean, we can talk about cost in a second, but I think...

**Quinn:** With costs? I don't know, man. You know what's expensive as hell? Software developers

**Thorsten:** I mean so what I wrote down in my notes here is right it's when you run say Aider or Claude Code or something they prominently display the cost of a session right and basically the first time I tried Aider over Christmas and I built like this dumb emoji game and then it basically sent me a bill and said like you just spent $15 today to code this useless game you know at first you have the um what do you call it sticker shock and you see the number and you go this PR costs two dollars or five dollars or whatever but I think every engineer who sees that number then has this other step where they go yeah but what's my hourly rate like if I if I calculate how much I am paid for working on a PR for an hour like it's maybe not that expensive But yeah, I think that the software...

**Quinn:** There's a lot of software developers who work at big groups of people where someone else pays the bills in a corporation. And I'm telling you, as someone who hires a lot of software engineers, and all of our customers do too, anything that can make them more productive is valuable. And it's this classic thing like devs who would buy a cup of coffee for $5 who would never pay for something. Devs could be so cheap. Everyone could be so cheap. But yeah, if you put the price so front and center, you're not going to want to do it.

**Thorsten:** Yeah.

**Quinn:** Like that's the difference between like an Uber and a taxi. And so I don't know, in the enterprise, you don't need to put that price front and center. And there's a lot of people where there's a big business to be built and someone is willing to pay for that.

**Thorsten:** Yeah, but we're seeing the world is changing, right? Like think bold prediction. I think this whole $10 a month, $20 a month, whatever, this subscription flat rate model, it seems a little bit outdated now when you have these tools. And I think usage-based pricing or some other form of pricing, that's what we're going to see a lot in the future. The big reason for that is we we talked about this last week not on this podcast but we talked about and it was somebody was asking why does Claude Code feel so different than the other tools and I I would say Claude Code feels like our prototype and I think our prototype is even better in some regard but why does it feel different and somebody else was saying that's because it's not optimized to save costs, to save tokens. And I put this in my notes as the magic of the no token limit, because if you optimize for requests or say a low number of requests or say low number of tokens, you will end up with a completely different product. And if you say, let it rip and you take out all of the limits and you put, you give the tools to the model and then you put it in a loop. That's where all the magic comes from. The magic is not like a lot of the magic is in the tools and a lot of the magic is in how it's integrated. A large part is instead of, you know, concrete example, the model tries to edit a file and it fails and we send back the error message. Okay, now you got to fix it if we're optimizing for cost and request, right? But since we're not right now, we just sent the error message back up to the model and guess what? The model then goes, oh, let me try it. It's a different way. And it's this autonomy comes from, or the agentness comes from it having no limits and you not restricting it to one turn or two turns or something.

**Quinn:** Yeah. We even prompt cache everything so that the next turn is going to be fast. So I was worried that'd be slow.

**Thorsten:** Yeah, but it's actually fast. Yeah. But yeah, I think a lot of that stuff would break if you optimize for number of tokens. And yeah.

**Quinn:** And I agree if you're trying to satisfy a flat rate pricing business where you want to cater to a bunch of people building emoji games on the weekend and to people that are professional software developers who are some of those productive people on the planet. That's really hard. That's like if you're Apple and you want to also have the $19 Huawei phone, something like that. Do you remember what the name of the environment variable in our prototype is?

**Thorsten:** Yeah, it had a bunch of curse words in there. To show the price.

**Quinn:** yeah "vite underscore I'm a fucking idiot who cares more about cost than building something awesome so show me..."

**Thorsten:** Yeah it's something low ambition yeah I think it's that would have killed it from the start and I mean again I don't know how the world is going to change but I think if anything one trend over the last two years was that this stuff has become cheaper like the token prices have come down and I'm not sure we're going to see an end to that so yeah it's I think it's not bad to bank on this

**Quinn:** Yeah totally

**Thorsten:** And again like one other thing just on because I talked with somebody else and they were asking oh I want to see how you do this and I think often the answer to how exactly does this work is the answer often is just let the model do it You can tell the model, going back to the thing we talked about in the last recording, checkpoints, restore points. If you want to optimize for cost, you build restore points, right? And because then you don't have to do anything. It's cheap. It's free. But if you don't have to optimize for cost, you can tell the model, undo the things that you did. And it does it pretty well. Like its recall of its own actions is pretty good. So that to me is this. Yes, if you want to optimize for low cost, then you have to build a solution to this. But if you don't want to do it, the model can do a lot of stuff on its own. And yeah, it's kind of reminiscent of, oh, you hire a freelancer. So if you don't have to worry about cost, you can let them do everything. But if you have to worry about cost, it's this, what's the most effective thing this person can do? And don't give them this task because that's a waste of money and time.

**Quinn:** Yeah.

**Thorsten:** Yeah, don't have to do it.

**Quinn:** There's another interesting trade-off that is probably going to be harder for us, which is speed. Because it is sometimes kind of slow. And that's kind of annoying. Sometimes I would like it to be faster. I would also like it to be doing more things in the background, more feedback loops, running tests and so on, which in theory is going to make it even slower.

**Thorsten:** Yeah. Yeah. Let's talk about this. So this is recent, I think, I don't know, Friday, I don't know where we started talking about We need to have multiple agents running. And I think that was kind of the theme of the last few days, right? That you added something that you can now have multiple agents running at the same time. And, you know, that's relatively straightforward. It's not as fancy as it might sound like, but it's you have multiple things running at the same time. I think that, again, was a big unlock in how to think about this, right? In that you start to think, okay, how can I behave? I don't know. Box them into different parts of the code base. How can I have one agent running on the front end stuff and one agent running on the back end? But I want to hear you talk about it because you built this and you have thoughts on it.

**Quinn:** Yeah. Well, partly because it was slow and partly because I wanted the UI to feel more minimal, more about the work that you're doing, not about the tabs and history and all that. Now you just have multiple tabs and each one is an agent and you can switch between them. And I found that for exactly the problem that you faced when doing that VS Code across multiple layers change, that I was telling it to, hey, make this change, but you only work in this directory, like web slash or server slash or something like that. And that worked. And again, there's a case where I just relied on the model. You could imagine a UI thing that says, here's a selector of the file paths and I'm going to scope it and all that, blah, blah, blah. No, I just free natural language. And that was really easy and that worked. And then given that you have one going here, well, I don't want to do them in serial. So I paralyzed them and I had two running. And then the interesting thing is how might they communicate? Cause right now they don't see each other's changes. I mean, if they ask for a tool call, they'll see it, but that is interesting. Another idea is some notion of a supervisor agent, which might be something that is a top level agent by itself. It might be one that's somehow, I don't know. We got to think through all of this.

**Thorsten:** Yeah.

**Quinn:** But it's possible. And it feels like we can kind of prototype some of these primitives and then we can build first class features later on top. And that's what comes from this really tight feedback loop with us chatting and building it and using it all the damn time. I'm using it all the damn time. I just wanted to share a quick screenshot.

**Thorsten:** Yes, let's do it. I think that's possible here.

**Quinn:** Yeah. Here we go. Yeah, this is my Linux machine, but I think it's in the preview.app. And you can see over here on the right all the threads that I had. And I find that as our prototype gets more and more useful, the sidebar width of it, you know, starts taking up more. And I don't always keep it open. But you can see some of the examples of things I tried it on. And just, you know, how many we're talking about. I don't know how many this is, like, you know, maybe 35 or 40.

**Thorsten:** 35, yeah. That's a lot.

**Quinn:** And that's all just in the last 24 hours.

**Thorsten:** Yeah. I mean, I think mine looks similar. I think I also bumped into one thing that you mentioned. I had the same thought yesterday, and then I basically woke up and I read your message saying the same thing. And that is, and again, I'm not stealing your credit with all of this.

**Quinn:** I don't care about credit.

**Thorsten:** No, no, no. I know, but it's just uncanny how often this happens where we come up with this or bump into the same thing. And the thing is, yesterday I had to then work on this command thing and it took a while, right? And it ran builds and, you know, just keeps going. And while it was doing this, I noticed, I think, one or two other bugs. I knew, for example, you know how when you mention the file in the text, we auto add it to the context. And I noticed that in the UI, we don't like, it's not unique. Like we showed the same file name twice, even though it's only attached once. And while it was working, I thought, oh, I could start another agent to fix this. Like it can one shot this. But then I bumped into the problem of, oh, the other thing is currently modifying the file system. It's going to run into build errors and whatnot. So what I want is something like git work tree so I can have a different checkout. And the thing should work over here and run the tools on its own. And then you start to think, what are we doing here? Like, this is crazy because it's suddenly, you want to have long-running tasks on the same code base. You want to have multiple workspaces. You want to run the same tools at the same time. And I don't know. It's mind-blowing. Like, it's this, we're entering a different stage in some sense. And you can say, you know, the skeptics, they will say, yeah, but it goes off the rail or does the wrong thing or does this other thing and blah, blah, blah. Again, like last week, somebody sent me an email and they said, hey, on your website, it still says you're employed at Zed, but you're back at Sourcegraph. Please change this. And I basically took that email this person sent me and gave it to the agent and say, fix this on my website and didn't mention any files. And it did it. And it changed it correctly. And then I sent it back to this person. And this person was not impressed. They were saying, you could have done this in five seconds or you could have done this faster. But my point with this anecdote is just take a step back and look at where we are, man. Like I take it.

**Quinn:** The next time someone does that, what you should do is have one of your kids do it.

**Thorsten:** Yeah, maybe.

**Quinn:** And then videotape them. And when they say, oh, you could have done it, then send them that video.

**Thorsten:** Yeah. But that's the point, right? It's just take a step back and look at where we are. Like I can, you know how often people call up their agency today, their marketing agency, and say, can you change this on our website? And then somebody goes and does it and there's like all of this over it. With this close to being able to send an email to an agent that opens a PR and then sends you a screenshot and says, is this okay? And if you say, yes, it's okay. In these words, it will go and merge the PR. And now we're talking about, I have a thing running on my machine and it takes 20 minutes to fix a PR that another machine created. And now I want another machine to run. So I need a different workspace. Like this is insane. If you take a step, like, where are we? Like, I don't know. It's mind-blowing.

**Quinn:** It's mind-blowing.

**Thorsten:** And what I keep saying is you need to see the trajectory. Don't look at the snapshot. Don't look at the current state. See this as the start of a trajectory or whatever, the middle of the trajectory. And maybe, yes, this will maybe plateau. But look, man, I can build you an email to website changes bot. Like I can do this today. And it would take me a day maybe to build this. And then you can change your WordPress page via email or via WhatsApp. You can even send annotated screenshots and do a circle around stuff and say, fix this. And it will do it. And that's wild.

**Quinn:** There seems to be some people, some personality types who are able to exploit that and get a ton of value from it. And then others who just don't. And I don't know what it is. I do know of some people who were very against it and very skeptical, and now they've come around. But even if you made an email bot, you can make it, and it would be really good in the hands of a lot of people, but it would be very far from perfect. And if you put me in a room with someone who didn't like it, and I tried to explain, oh, well, if it said that in this case, then here's what you could have done. And I think a lot of people would know to do that anyway. It would actually be hard for me to explain those things. And I mean, look, I'm really trying, but I think I can have a little bit of empathy for those people. And I don't know what it is about their personality or approach to things.

**Thorsten:** Yeah, I don't understand it anymore. At one point, I think I understood it because you think about, oh, yeah, it might not be efficient yet. It might not do this. But for me, like if you would have told me, like when I was a teenager, I remember thinking about, you know, or if we would have a tool to do this and then I can SSH into a server and then it could do, and it would, all of the pieces in these dreams of what one day we could do where all this, once we figure out this part and once this, you know, gets easier to parse language and stuff like this. And now we have this universal thing that you can plug in and basically can build a thing that you call via voice message and say, can you check how many processes they're running on my machine, you know, on my Linux machine? And it will do it. And that to me is magical. And I don't know how people cannot see the implications of that. Maybe it's, you know, as people say, it's, it's, somebody said yesterday, the quote of, if your job is dependent on you not understanding something, then you will not understand it. And maybe they're scared of, oh, it will make software engineers obsolete. But I think.

**Quinn:** Yeah. The problem is their job is dependent on them understanding

**Thorsten:** Yeah.

**Quinn:** How to use these things. So.

**Thorsten:** Exactly. Yes. Yes.

**Quinn:** I think these people genuinely do not know how to use these things or they have not used these things. But when I say they don't know how to use these things, that's tough because it feels like a blame the users thing. And I get it. It's hard. These are nuanced. But there's just some people where if it doesn't work, then they try something else and they've evolved to figure out this intuition for how to get it right. And they actually view that as fun. And other people don't see that as fun.

**Thorsten:** Yeah. But I don't know. I think everybody needs to really try to steelman this and find their own moment where they get a glimpse of what it's capable of. I tried it a bunch over the last two years and it hasn't happened. And it took me basically in the last three months building our autocomplete and working with models and then using Cursor and Agents and Claude and whatnot. It took me a lot of head against the wall to break through it. And then you start to see that then everything else looks like a black and white movie. And then it feels hard to explain to people what you saw. But I think everybody needs to do this on their own. But I would urge everybody to don't treat this as like the oracle of code coming on earth and now helping you write code. Treat this as tools that you have to kind of use a correct way or a certain way. And then you will see something that will make you understand, okay, if this gets fixed better, this will change a lot of stuff.

**Quinn:** But you know the reality is right now, for anyone to get in that kind of loop, they got to go -- I mean, this prototype, it's not even available to them yet. There's Claude Code, which is pretty damn good. Okay, they get Claude Code, and they got to make sure it works on their repo, that it can run tests. They got to get some MCPs, like the puppeteer one is really valuable. They got to do all this setup. It's like, yeah, it is a big learning curve right now. So one of the things I'm really excited about is we can make it so that it works in the editor that you have. And it is set up in your code base because someone else at your company already did that. This is not like, you know, v0, but someone else has already set it up. It's got all the right feedback loops with tests and browser and visual and all that stuff. It's going to work so much better than if it didn't have those things. And ultimately, I do believe that even these people who don't see it when it doesn't work and other people are talking about it, when it actually works in front of their own damn eyes, I think that is going to win them over. And every single day, probably 10, 50,000 people out there are won over. So it's going pretty damn fast. And I hope we can accelerate it.

**Thorsten:** I agree. I think what we need to end with this picture, I think the goal is not that we end up with a tool where everybody has to train their own intern, you know, in large companies. But it's this, no, like the company trains the intern, the AI intern, and then everybody gets a clone of that intern. But the intern knows how to navigate the code base and how to do stuff. So that will be a big, big, big, big, big, big help.

**Quinn:** And then a code review agent is a safety net on the other end.

**Thorsten:** There you go.

**Quinn:** Yeah.

**Thorsten:** Boom. Yeah. All right. I think we have time. Let's wrap this up and let's get back to coding.

**Quinn:** Happy hacking.

**Thorsten:** Bye-bye.

**Quinn:** Bye.