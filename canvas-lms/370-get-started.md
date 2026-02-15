---
title: Get Started | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/get_started
source: sitemap
fetched_at: 2026-02-15T09:11:44.647722-03:00
rendered_js: false
word_count: 475
summary: This document introduces the Instructure Developer Documentation portal, providing an overview of API integration capabilities, authentication procedures, and instructions for handling API requests and responses.
tags:
    - instructure-api
    - canvas-lms
    - authentication
    - api-integration
    - error-handling
    - pagination
    - developer-portal
category: guide
---

Hello! Welcome to Instructure's Developer Documentation portal.

This portal contains API documentation for all Instructure products.

Below are some examples of things you can do using Instructure product APIs:

### Integrate Canvas LMS into Your Applications

- Integrate Canvas LMS into your applications.
- For example, automate course creation
- Synchronize student data between Canvas and your SIS or CRM
- Retrieve [grades](https://developerdocs.instructure.com/services/canvas/resources/grade_change_log) and assessment results with API

### Access Rich Educational Data with Data Access Platform (DAP)

- Access rich educational data with Data Access Platform (DAP)
- For example, get detailed analytics about your student performance
- Create institutional reports
- Or integrate Canvas data into your business intelligence tools

### Improve Your Assessments with Quizzes

- Improve your assessments with [quizzes](https://developerdocs.instructure.com/services/quizzes/openapi_quiz)
- You can quickly create and share quizzes
- You can get quiz results for analysis

<!--THE END-->

- With personalized course information for the students
- Give instant feedback on assignments and quizzes

<!--THE END-->

To access API endpoints for most of our services you need to get an Access Key. The way of getting these Access keys may be different for each service. Go into the subsection of the service you would like to use and look for a subpage called Authentication, OAuth, Developer Keys.

**Examples:**

### 2. Make Your First Request!

1. Take your authentication key or secret you got in the previous step.
2. Find an API you would like to try.
3. If there is a "Test it" button, you can click on it and test it on the spot.
4. Otherwise, use Postman or Terminal with curl for testing it.

### 3. Understand the Responses

When you make an API call, you'll typically get a response in JSON format. Here's how to quickly understand and use these responses:

#### ✅ Successful Response (with status 200 or 201):

A successful response usually looks something like this (this is just an example):

```
{
"id":123,
"name":"Introduction to Biology",
"course_code":"BIO101"
}
```

Each response includes data fields (like `id`, `name`, and `course_code`) clearly describing what you've requested. You can use these fields directly in your applications.

#### ⚠️ Error Response (status 4xx):

If something goes wrong, you'll get an error response, for example:

```
{
"errors":[
{
"message":"Invalid access token."
}
]
}
```

Errors come with clear messages indicating the problem. Common issues include authentication errors, incorrect parameters, or permission issues.

#### 📑 Pagination and Large Data:

Some services, for example Canvas LMS, split API calls into multiple pages when you request a lot of data (like a long list of courses or users):

- Check for a Link header in the response, which provides URLs for the next or previous page of results.

```
Link:<https://canvas.instructure.com/api/v1/courses?page=2>;rel="next"
```

You can follow these links to fetch all the data. Find more info about [Canvas pagination here](https://developerdocs.instructure.com/services/canvas/basics/file.pagination).

- Use tools like [Postmanarrow-up-right](https://www.postman.com/) or browser extensions (like JSONView) to visualize responses clearly.
- Always refer to the specific API's documentation page for detailed descriptions of each data field.

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).