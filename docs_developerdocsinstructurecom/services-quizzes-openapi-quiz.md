---
title: Quiz API | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/quizzes/openapi_quiz
source: sitemap
fetched_at: 2026-02-15T09:15:26.159848-03:00
rendered_js: false
word_count: 366
summary: This document specifies API endpoints, required parameters, and response behaviors for managing courses, quiz sessions, and cloning operations within a learning management platform.
tags:
    - api-reference
    - canvas-lms
    - quiz-management
    - request-parameters
    - error-handling
    - rest-api
category: api
---

idsstring\[]OptionalExample: `["160","161"]`

404

returns nothing when none of the banks belong to authorized user

404

returns nothing when none of the banks belong to authorized user

404

populates the export\_settings field with the given export\_settings param

404

populates the export\_settings field with the given export\_settings param

404

example at ./spec/requests/api/v1/courses\_controller\_spec.rb:208

404

example at ./spec/requests/api/v1/courses\_controller\_spec.rb:208

canvas\_idintegerRequiredExample: `9999`

404

is expected to be not found

404

is expected to be not found

canvas\_idintegerRequiredExample: `201`

404

is expected to be not found

404

is expected to be not found

canvas\_idintegerRequiredExample: `196`

404

associates courses which have previously been archived

/api/courses/{canvas\_id}/associate\_courses

404

associates courses which have previously been archived

canvas\_idintegerRequiredExample: `550000000000154`

404

replaces the local canvas\_id with the global canavs\_id

/api/courses/{canvas\_id}/associate\_quizzes

404

replaces the local canvas\_id with the global canavs\_id

404

is expected to be bad request

/api/items/check\_shareability

404

is expected to be bad request

404

is expected to be unprocessable

/api/quiz\_clone\_jobs/create\_batch

404

is expected to be unprocessable

idsstring\[]OptionalExample: `["1674","1675","1676","1677","1678","1679","1680","1681","1682","1683","1684","1685","1686","1687","1688","1689","1690","1691","1692","1693","1694","1695","1696","1697","1698","1699","1700","1701","1702","1703","1704","1705","1706","1707","1708","1709","1710","1711","1712","1713","1714","1715","1716","1717","1718","1719","1720","1721","1722","1723","1724"]`

quiz\_idintegerOptionalExample: `3499`

404

returns all the quiz sessions without paginating

404

returns all the quiz sessions without paginating

idintegerRequiredExample: `1764`

disable\_ac\_invalidationstringOptionalExample: `true`

idintegerOptionalExample: `1764`

quiz\_idintegerOptionalExample: `3533`

quiz\_session\_idintegerOptionalExample: `1436`

404

does not invalidate the student access code

404

does not invalidate the student access code

idintegerRequiredExample: `145`

200

then the elapsed time should be the sum of the previous and current attempt

/api/quiz\_sessions/{id}/time

200

then the elapsed time should be the sum of the previous and current attempt

quiz\_session\_idintegerRequiredExample: `146`

formatstringOptionalExample: `json`

200

then the assignment will autosubmit and cannot be resumed

/api/quiz\_sessions/{quiz\_session\_id}/quiz\_session\_response\_events

200

then the assignment will autosubmit and cannot be resumed

quiz\_session\_idintegerRequiredExample: `160`

200

should not modify the session response data

/api/quiz\_sessions/{quiz\_session\_id}/session\_item\_responses

200

should not modify the session response data

/api/quiz\_sync\_jobs/create\_batch

context\_idintegerOptionalExample: `2462`

formatstringOptionalExample: `json`

quiz\_idsstring\[]OptionalExample: `["2762","2764"]`

versionintegerOptionalExample: `1`

401

uses v1 endpoints by default

404

fails with not\_found if any one quiz is missing

quiz\_idintegerRequiredExample: `1461`

404

does not create a bank share job

/api/quizzes/{quiz\_id}/quiz\_clone\_jobs

404

does not create a bank share job

404

indicates the content is shareable

/api/stimuli/check\_shareability

404

indicates the content is shareable

filterstringOptionalExample: `a`

pageintegerOptionalExample: `1`

per\_pageintegerOptionalExample: `1`

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).