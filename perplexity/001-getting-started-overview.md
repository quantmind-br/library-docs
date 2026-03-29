---
title: "null"
url: https://docs.perplexity.ai/docs/getting-started/overview.md
source: llms
fetched_at: 2026-02-04T07:23:04.622735848-03:00
rendered_js: false
word_count: 820
summary: This document serves as the primary landing page and index for Perplexity AI's developer documentation, providing navigation to available pages and a quickstart guide for making API calls.
tags:
    - perplexity-ai
    - api-documentation
    - quickstart
    - developer-tools
    - search-api
    - code-examples
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# null

export const PerplexityLogo = () => {
  return <div className="relative w-[120px] h-[80px]">
      <img src="/logo/PerplexityWordmark.svg" alt="Perplexity" className="block dark:hidden w-[120px] h-[80px] object-contain" />
      <img src="/logo/PerplexityWordmark_Light.svg" alt="Perplexity" className="hidden dark:block w-[120px] h-[80px] object-contain" />
    </div>;
};

export const SonarLogo = () => {
  return <svg xmlns="http://www.w3.org/2000/svg" width="80" height="30" viewBox="0 0 219 47" fill="none" className="text-foreground">
  <path d="M194.057 1.28212H201.77V7.26314C201.77 7.66217 201.968 7.86059 202.367 7.86059C202.766 7.86059 203.052 7.63382 203.224 7.17592C204.194 5.01072 205.535 3.47349 207.251 2.56205C208.965 1.59392 211.338 1.10986 214.364 1.10986H218.049V8.80037H213.165C209.338 8.80037 206.482 9.71181 204.598 11.5347C202.712 13.3576 201.77 16.3492 201.77 20.5073V45.7157H194.057V1.28212Z" fill="currentColor" />
  <path d="M145.653 32.4715C145.653 28.5402 146.996 25.4635 149.68 23.2416C152.421 20.963 156.505 19.7659 161.933 19.6526L178.212 19.3102V17.5157C178.212 14.1556 177.242 11.5347 175.299 9.65511C173.356 7.77555 170.329 6.83577 166.217 6.83577C162.563 6.83577 159.791 7.63382 157.907 9.22774C156.023 10.8238 155.079 12.8735 155.079 15.381H146.94C147.112 12.4766 147.969 9.85572 149.51 7.52044C151.052 5.18515 153.252 3.36228 156.106 2.05182C158.963 0.684667 162.332 0 166.217 0C172.728 0 177.641 1.56776 180.953 4.69891C184.265 7.83224 185.922 12.2477 185.922 17.9431V45.7157H178.212V41.1018C178.212 40.7595 178.04 40.5894 177.697 40.5894C177.412 40.5894 177.126 40.7595 176.84 41.1018C173.755 45.0332 169.215 46.9978 163.217 46.9978C157.733 46.9978 153.422 45.659 150.28 42.9814C147.195 40.3038 145.653 36.7998 145.653 32.4715ZM153.365 32.4715C153.365 34.8635 154.307 36.7431 156.194 38.1102C158.077 39.4774 160.705 40.1621 164.076 40.1621C168.474 40.1621 171.93 38.965 174.442 36.573C176.956 34.181 178.212 30.677 178.212 26.0631V25.7208L161.933 26.0631C159.019 26.1198 156.85 26.7173 155.422 27.8577C154.05 28.9392 153.365 30.4786 153.365 32.4715Z" fill="currentColor" />
  <path d="M105.794 1.28212V6.15328C105.794 6.55231 105.995 6.75073 106.394 6.75073C106.566 6.75073 106.708 6.69404 106.821 6.58065C106.993 6.41058 107.163 6.23832 107.336 6.06824C110.362 2.02347 114.989 0.00218047 121.214 0.00218047C126.812 0.00218047 131.21 1.56994 134.408 4.70109C137.607 7.83442 139.205 12.2499 139.205 17.9453V45.7179H131.495V19.2274C131.495 15.1826 130.466 12.106 128.41 9.99745C126.354 7.88894 123.384 6.83577 119.501 6.83577C115.103 6.83577 111.703 8.17458 109.305 10.8522C106.963 13.4731 105.792 17.4023 105.792 22.6442V45.7157H98.0818V1.28212H105.794Z" fill="currentColor" />
  <path d="M68.9421 0C73.2834 0 77.1951 0.911436 80.6795 2.73431C84.2206 4.55718 86.992 7.23479 88.9893 10.7672C91.0455 14.2995 92.0746 18.5427 92.0746 23.4989C92.0746 28.4551 91.0455 32.6983 88.9893 36.2307C86.9898 39.763 84.2206 42.4406 80.6795 44.2635C77.1951 46.0864 73.2834 46.9978 68.9421 46.9978C64.6007 46.9978 60.6606 46.0864 57.1196 44.2635C53.6352 42.4406 50.866 39.763 48.8098 36.2307C46.8103 32.6983 45.8116 28.4551 45.8116 23.4989C45.8116 18.5427 46.8103 14.2995 48.8098 10.7672C50.866 7.23479 53.6373 4.55718 57.1196 2.73431C60.6606 0.911436 64.6029 0 68.9421 0ZM68.9421 6.83577C64.3151 6.83577 60.5734 8.31631 57.7192 11.2796C54.9195 14.1839 53.5218 18.2571 53.5218 23.4989C53.5218 28.7408 54.9216 32.8422 57.7192 35.8033C60.5756 38.7077 64.3151 40.1621 68.9421 40.1621C73.569 40.1621 77.2823 38.7099 80.0799 35.8033C82.9363 32.84 84.3645 28.7386 84.3645 23.4989C84.3645 18.2592 82.9363 14.1839 80.0799 11.2796C77.2802 8.31631 73.569 6.83577 68.9421 6.83577Z" fill="currentColor" />
  <path d="M22.2757 0C25.989 0 29.3011 0.625794 32.2142 1.87956C35.184 3.13333 37.5259 4.92786 39.2397 7.26314C40.9536 9.59842 41.8672 12.3044 41.9806 15.381H33.8409C33.383 9.68346 29.3862 6.83577 21.8461 6.83577C18.5907 6.83577 16.0482 7.46156 14.221 8.71533C12.4505 9.9691 11.5652 11.563 11.5652 13.5015C11.5652 15.1543 12.1648 16.3492 13.3641 17.0905C14.62 17.8319 16.7351 18.5144 19.7049 19.1423L27.8446 20.8518C32.2426 21.7633 35.6136 23.0737 37.9554 24.7832C40.3539 26.4927 41.5532 29.1987 41.5532 32.9011C41.5532 35.6354 40.753 38.0841 39.1547 40.2493C37.5564 42.3578 35.2996 44.0084 32.3865 45.2055C29.5301 46.4026 26.218 47 22.4479 47C15.6514 47 10.3965 45.4911 6.68314 42.4712C2.9698 39.3945 0.74354 35.3498 0 30.3347H8.13969C9.22556 36.8848 13.9942 40.1621 22.4479 40.1621C26.1613 40.1621 28.9872 39.5079 30.9299 38.1974C32.8727 36.8303 33.8431 35.2058 33.8431 33.3263C33.8431 32.0725 33.5007 31.1327 32.8139 30.5069C32.1859 29.8223 31.3006 29.3099 30.1581 28.9697C29.0155 28.6274 27.1032 28.1717 24.4169 27.6026L16.2772 25.8931C12.3371 25.095 9.28007 23.7562 7.11051 21.8766C4.94094 19.9971 3.85507 17.2628 3.85507 13.6737C3.85507 9.45887 5.56892 6.12494 8.99661 3.67627C12.4221 1.22542 16.8507 0 22.2757 0Z" fill="currentColor" />
</svg>;
};

export const QuickstartBanner = () => <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between bg-[#114F56] border border-border rounded-xl p-4 md:p-6 w-full mt-4 mb-8 gap-4">
    <div className="flex items-center gap-3 sm:gap-4 flex-1">
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 40 35" fill="none" className="flex-shrink-0">
        <path d="M7.3187 33C4.77908 30.4604 3.04959 27.2246 2.34892 23.7021C1.64825 20.1795 2.00788 16.5283 3.38233 13.2101C4.75678 9.89188 7.08432 7.05577 10.0706 5.0604C13.0569 3.06503 16.5678 2 20.1594 2C23.751 2 27.2619 3.06503 30.2482 5.0604C33.2345 7.05577 35.5621 9.89188 36.9365 13.2101C38.311 16.5283 38.6706 20.1795 37.9699 23.7021C37.2693 27.2246 35.5398 30.4604 33.0002 33M28.2303 12.0886L20.1594 20.1594" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round" className="text-[#F7F7F8]" />
      </svg>
      <div className="flex flex-col min-w-0">
        <span className="font-semibold text-base md:text-lg text-[#F7F7F8]">Quickstart Guide</span>
        <span className="text-sm md:text-base text-[#F7F7F8] opacity-80 mt-0.5">Getting started is simple and fast—make your first API call within minutes.</span>
      </div>
    </div>
    <div className="flex flex-col sm:flex-row gap-2 sm:ml-4">
      <a href="/docs/getting-started/quickstart" className="px-6 py-3 bg-[#20808D] hover:bg-[#114F56] dark:bg-[#35BDC8] dark:hover:bg-[#92DCE2] text-[#F7F7F8] dark:text-[#121516] rounded-full font-medium text-base shadow transition-all duration-200 whitespace-nowrap text-center">
        Get Started
      </a>
    </div>
  </div>;

export const UseCaseTabs = () => {
  const [selected, setSelected] = useState(0);
  const [copied, setCopied] = useState(false);
  const copyToClipboard = async text => {
    try {
      await navigator.clipboard.writeText(text);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch (err) {
      console.error('Failed to copy text: ', err);
    }
  };
  const useCases = [{
    label: 'Find Results',
    codeExamples: [{
      language: 'bash',
      code: `curl https://api.perplexity.ai/search \\
  -H "Authorization: Bearer YOUR_API_KEY" \\
  -H "Content-Type: application/json" \\
  -d '{
    "query": [
      "What is Comet Browser?",
      "Perplexity AI",
      "Perplexity Changelog"
    ]
  }' | jq`
    }, {
      language: 'python',
      code: `from perplexity import Perplexity

client = Perplexity()

search = client.search.create(
    query=[
      "What is Comet Browser?",
      "Perplexity AI",
      "Perplexity Changelog"
    ]
)

for result in search.results:
    print(f"{result.title}: {result.url}")`
    }, {
      language: 'typescript',
      code: `import Perplexity from '@perplexity-ai/perplexity_ai';

const client = new Perplexity();

const search = await client.search.create({
  query: [
    "What is Comet Browser?",
    "Perplexity AI",
    "Perplexity Changelog"
  ]
});

search.results.forEach(result => {
  console.log(\`\${result.title}: \${result.url}\`);
});`
    }]
  }, {
    label: 'Agentic Research',
    codeExamples: [{
      language: 'bash',
      code: `curl https://api.perplexity.ai/v1/responses \\
  -H "Authorization: Bearer YOUR_API_KEY" \\
  -H "Content-Type: application/json" \\
  -d '{
    "preset": "pro-search",
    "input": "What are the major AI developments and announcements from today across the tech industry?"
  }' | jq`
    }, {
      language: 'python',
      code: `from perplexity import Perplexity

client = Perplexity()

response = client.responses.create(
    preset="pro-search",
    input="What are the major AI developments and announcements from today across the tech industry?"
)

print(response.output_text)`
    }, {
      language: 'javascript',
      code: `import Perplexity from '@perplexity-ai/perplexity_ai';

const client = new Perplexity();

const response = await client.responses.create({
  preset: 'pro-search',
  input: 'What are the major AI developments and announcements from today across the tech industry?'
});

console.log(response.output_text);`
    }]
  }, {
    label: 'Filter your sources',
    codeExamples: [{
      language: 'bash',
      code: `curl https://api.perplexity.ai/chat/completions \\
  -H "Authorization: Bearer YOUR_API_KEY" \\
  -H "Content-Type: application/json" \\
  -d '{
    "model": "sonar",
    "messages": [
      {
        "role": "user", 
        "content": "What are the most promising machine learning breakthroughs in computer vision and multimodal AI from recent arXiv publications?"
      }
    ],
    "web_search_options": {
      "search_domain_filter": ["arxiv.org"],
      "search_recency_filter": "month"
    }
  }' | jq`
    }, {
      language: 'python',
      code: `from perplexity import Perplexity

client = Perplexity()

completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "What are the most promising machine learning breakthroughs in computer vision and multimodal AI from recent arXiv publications?"
        }
    ],
    model="sonar",
    web_search_options={
        "search_domain_filter": ["arxiv.org"],
        "search_recency_filter": "month"
    }
)

print(completion.choices[0].message.content)`
    }, {
      language: 'javascript',
      code: `import Perplexity from '@perplexity-ai/perplexity_ai';

const client = new Perplexity();

const completion = await client.chat.completions.create({
  messages: [
    {
      role: 'user',
      content: 'What are the most promising machine learning breakthroughs in computer vision and multimodal AI from recent arXiv publications?'
    }
  ],
  model: 'sonar',
  web_search_options: {
    search_domain_filter: ['arxiv.org'],
    search_recency_filter: 'month'
  }
});

console.log(completion.choices[0].message.content);`
    }]
  }, {
    label: 'Structured Outputs',
    codeExamples: [{
      language: 'bash',
      code: `curl https://api.perplexity.ai/v1/responses \\
  -H "Authorization: Bearer YOUR_API_KEY" \\
  -H "Content-Type: application/json" \\
  -d '{
    "preset": "pro-search",
    "input": "Find the top 3 trending AI startups with recent funding. Include company name, funding amount, and focus area.",
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "schema": {
          "type": "object",
          "properties": {
            "startups": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "company_name": {"type": "string"},
                  "funding_amount": {"type": "string"},
                  "focus_area": {"type": "string"}
                },
                "required": ["company_name", "funding_amount", "focus_area"]
              }
            }
          },
          "required": ["startups"]
        }
      }
    }
  }' | jq`
    }, {
      language: 'python',
      code: `from perplexity import Perplexity

client = Perplexity()

response = client.responses.create(
    preset="pro-search",
    input="Find the top 3 trending AI startups with recent funding. Include company name, funding amount, and focus area.",
    response_format={
        "type": "json_schema",
        "json_schema": {
            "schema": {
                "type": "object",
                "properties": {
                    "startups": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "company_name": {"type": "string"},
                                "funding_amount": {"type": "string"},
                                "focus_area": {"type": "string"}
                            },
                            "required": ["company_name", "funding_amount", "focus_area"]
                        }
                    }
                },
                "required": ["startups"]
            }
        }
    }
)


for item in response.output:
    if hasattr(item, 'content'):
        print(item.content[0].text)
        break`
    }, {
      language: 'javascript',
      code: `import Perplexity from '@perplexity-ai/perplexity_ai';

const client = new Perplexity();

const response = await client.responses.create({
  preset: 'pro-search',
  input: 'Find the top 3 trending AI startups with recent funding. Include company name, funding amount, and focus area.',
  response_format: {
    type: 'json_schema',
    json_schema: {
      schema: {
        type: 'object',
        properties: {
          startups: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                company_name: { type: 'string' },
                funding_amount: { type: 'string' },
                focus_area: { type: 'string' }
              },
              required: ['company_name', 'funding_amount', 'focus_area']
            }
          }
        },
        required: ['startups']
      }
    }
  }
});

console.log(response.output_text);`
    }]
  }];
  const selectedUseCase = useCases[selected];
  return <section className="mx-auto w-full p-4 sm:p-6 lg:p-8 rounded-2xl border border-[rgba(222,247,249,0.30)] bg-[#081F22] dark:bg-[#B2D4D7] flex flex-col lg:flex-row gap-4 sm:gap-6 lg:gap-8 not-prose" aria-label="Sonar use case examples" style={{
    boxSizing: 'border-box',
    backgroundColor: 'var(--color-ecru)'
  }}>
      <nav className="flex flex-col lg:w-1/4 lg:min-w-[240px]" aria-label="Use case tabs">
        <h2 className="text-xl mt-2 font-semibold mb-4 text-[#121516]">Try Our APIs</h2>
        <div className="flex flex-row lg:flex-col gap-1 flex-1 overflow-x-auto lg:overflow-x-visible pb-2 lg:pb-0">
          {useCases.map((uc, idx) => <button key={uc.label} type="button" aria-current={selected === idx} aria-controls={`usecase-panel-${idx}`} className={`py-2 px-3 lg:px-2 flex items-center justify-center lg:justify-start text-[#121516] rounded-lg hover:bg-[#92DCE2] whitespace-nowrap lg:whitespace-normal text-sm lg:text-base ${selected === idx ? 'bg-[#92DCE2]' : ''}`} onClick={() => setSelected(idx)}>
              {uc.label}
            </button>)}
        </div>
        <a href="https://www.perplexity.ai/account/api/group" className="mt-4 lg:mt-auto text-sm underline px-2 text-[#121516] opacity-80 text-center lg:text-left">Get Started</a>
      </nav>

      <div className="flex-1 relative dark:bg-[#0D0E10] self-start rounded-2xl overflow-hidden" id={`usecase-panel-${selected}`} role="tabpanel" aria-live="polite">
        <CodeGroup>
            <pre className="language-python" filename="Python">
              <code>{selectedUseCase.codeExamples[1].code}</code>
            </pre>
            <pre className="language-typescript" filename="TypeScript">
              <code>{selectedUseCase.codeExamples[2].code}</code>
            </pre>
            <pre className="language-bash" filename="cURL">
              <code>{selectedUseCase.codeExamples[0].code}</code>
            </pre>
          </CodeGroup>
      </div>
    </section>;
};

<div className="w-full max-w-6xl mx-auto px-4 sm:px-6 md:px-8 lg:px-12 py-6 sm:py-8">
  <div className="flex flex-col lg:flex-row justify-between items-start lg:items-center mt-6 sm:mt-8 mb-8 sm:mb-12 gap-4">
    <div className="flex items-center gap-2">
      <PerplexityLogo />

      <h1 className="text-xl sm:text-2xl font-bold text-foreground"><span className="font-thin">API Platform</span></h1>
    </div>

    <div className="lg:ml-8 max-w-full lg:max-w-md lg:text-right">
      <span className="text-xs sm:text-sm text-muted-foreground font-mono leading-relaxed">
        Power your products with unparalleled real-time, web-wide research and Q\&A capabilities.
      </span>
    </div>
  </div>

  <QuickstartBanner />

  <UseCaseTabs />

  <div className="mt-12">
    <div className="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-4xl mx-auto">
      <div className="flex flex-col items-center">
        <h3 className="text-xl font-semibold text-foreground mb-2">Search</h3>
        <p className="text-sm text-muted-foreground text-center mb-4">Get ranked web search results with advanced filtering and real-time data.</p>

        <a href="/docs/search/quickstart" className="block rounded-xl overflow-hidden shadow-md hover:shadow-lg hover:scale-105 transform transition-all duration-300 cursor-pointer w-full">
          <img src="https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/overview/Search.png?fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=f6d833e8b6f9c372e99bfc54c0edf7af" alt="Search API" className="w-full h-48 object-cover" data-og-width="1216" width="1216" data-og-height="720" height="720" data-path="docs/assets/images/overview/Search.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/overview/Search.png?w=280&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=10ded69a2a4f0c74f2903efb1e12b3ef 280w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/overview/Search.png?w=560&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=e3bed31866f2c2fd9f96fb8b16bb3285 560w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/overview/Search.png?w=840&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=f418876152a867fda6df2f1c0525b781 840w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/overview/Search.png?w=1100&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=2e6e8278206cfa89a90d92d08c2b3651 1100w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/overview/Search.png?w=1650&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=bdb2d0de5c74447fed7a79f7c5205f8b 1650w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/overview/Search.png?w=2500&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=e5274e310929668a838552e4d0d18fac 2500w" />
        </a>
      </div>

      <div className="flex flex-col items-center">
        <h3 className="text-xl font-semibold text-foreground mb-2">Grounded LLM</h3>
        <p className="text-sm text-muted-foreground text-center mb-4">Build AI applications with web-grounded chat completions and reasoning models.</p>

        <a href="/docs/getting-started/quickstart" className="block rounded-xl overflow-hidden shadow-md hover:shadow-lg hover:scale-105 transform transition-all duration-300 cursor-pointer w-full">
          <img src="https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/overview/Grounded.png?fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=3b6f32ee4a8af2570b3a73f39ab365c3" alt="Grounded LLM" className="w-full h-48 object-cover" data-og-width="1216" width="1216" data-og-height="720" height="720" data-path="docs/assets/images/overview/Grounded.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/overview/Grounded.png?w=280&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=1a8301d7ac84d31ca3e6284b03a40450 280w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/overview/Grounded.png?w=560&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=31422ebf57504a9cc46fe07584052a5b 560w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/overview/Grounded.png?w=840&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=b097a383931d8dd29850d1a0bd6ca654 840w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/overview/Grounded.png?w=1100&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=1e235da6e820aa1b108d4b2d2b9a1da0 1100w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/overview/Grounded.png?w=1650&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=21bd31b0ea9cd9d9a83c5596bf971a08 1650w, https://mintcdn.com/perplexity/qLnd99sJyTqU60Ni/docs/assets/images/overview/Grounded.png?w=2500&fit=max&auto=format&n=qLnd99sJyTqU60Ni&q=85&s=b1efe78d69f111ef29042c98c5150e45 2500w" />
        </a>
      </div>
    </div>
  </div>
</div>