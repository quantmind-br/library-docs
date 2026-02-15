---
title: Quiz Submission Questions | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/quiz_submission_questions
source: sitemap
fetched_at: 2026-02-15T09:08:42.868336-03:00
rendered_js: false
word_count: 898
summary: This document specifies the API for managing questions within a quiz submission, covering endpoints for retrieving question lists, submitting answers, and flagging items for review. It also details the specific data formats required for different quiz question types like essay, matching, and multiple blanks.
tags:
    - canvas-lms
    - quiz-submissions
    - rest-api
    - educational-technology
    - question-answering
    - api-reference
category: api
---

## Quiz Submission Questions API

API for answering and flagging questions in a quiz-taking session.

**A QuizSubmissionQuestion object looks like:**

```
{
  // The ID of the QuizQuestion this answer is for.
"id": 1,
  // Whether this question is flagged.
"flagged": true,
  // The provided answer (if any) for this question. The format of this parameter
  // depends on the type of the question, see the Appendix for more information.
"answer": null,
  // The possible answers for this question when those possible answers are
  // necessary.  The presence of this parameter is dependent on permissions.
"answers": null
}
```

[Quizzes::QuizSubmissionQuestionsController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_submission_questions_controller.rb)

`GET /api/v1/quiz_submissions/:quiz_submission_id/questions`

**Scope:** `url:GET|/api/v1/quiz_submissions/:quiz_submission_id/questions`

Get a list of all the question records for this quiz submission.

**200 OK** response code is returned if the request was successful.

**Request Parameters:**

Associations to include with the quiz submission question.

Allowed values: `quiz_question`

**Example Response:**

```
{
  "quiz_submission_questions": [QuizSubmissionQuestion]
}
```

[Quizzes::QuizSubmissionQuestionsController#answerarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_submission_questions_controller.rb)

`POST /api/v1/quiz_submissions/:quiz_submission_id/questions`

**Scope:** `url:POST|/api/v1/quiz_submissions/:quiz_submission_id/questions`

Provide or update an answer to one or more QuizQuestions.

**Request Parameters:**

The attempt number of the quiz submission being taken. Note that this must be the latest attempt index, as questions for earlier attempts can not be modified.

The unique validation token you received when the Quiz Submission was created.

Access code for the Quiz, if any.

**Example Request:**

```
{
  "attempt": 1,
  "validation_token": "YOUR_VALIDATION_TOKEN",
  "access_code": null,
  "quiz_questions": [{
    "id": "1",
    "answer": "Hello World!"
  }, {
    "id": "2",
    "answer": 42.0
  }]
}
```

Returns a list of [QuizSubmissionQuestion](https://developerdocs.instructure.com/services/canvas/resources/quiz_submission_questions#quizsubmissionquestion) objects.

[Quizzes::QuizSubmissionQuestionsController#formatted\_answerarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_submission_questions_controller.rb)

`GET /api/v1/quiz_submissions/:quiz_submission_id/questions/:id/formatted_answer`

**Scope:** `url:GET|/api/v1/quiz_submissions/:quiz_submission_id/questions/:id/formatted_answer`

Matches the intended behavior of the UI when a numerical answer is entered and returns the resulting formatted number

**Request Parameters:**

**Example Response:**

```
{
  "formatted_answer": 12.1234
}
```

[Quizzes::QuizSubmissionQuestionsController#flagarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_submission_questions_controller.rb)

`PUT /api/v1/quiz_submissions/:quiz_submission_id/questions/:id/flag`

**Scope:** `url:PUT|/api/v1/quiz_submissions/:quiz_submission_id/questions/:id/flag`

Set a flag on a quiz question to indicate that you want to return to it later.

**Request Parameters:**

The attempt number of the quiz submission being taken. Note that this must be the latest attempt index, as questions for earlier attempts can not be modified.

The unique validation token you received when the Quiz Submission was created.

Access code for the Quiz, if any.

**Example Request:**

```
{
  "attempt": 1,
  "validation_token": "YOUR_VALIDATION_TOKEN",
  "access_code": null
}
```

[Quizzes::QuizSubmissionQuestionsController#unflagarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_submission_questions_controller.rb)

`PUT /api/v1/quiz_submissions/:quiz_submission_id/questions/:id/unflag`

**Scope:** `url:PUT|/api/v1/quiz_submissions/:quiz_submission_id/questions/:id/unflag`

Remove the flag that you previously set on a quiz question after you’ve returned to it.

**Request Parameters:**

The attempt number of the quiz submission being taken. Note that this must be the latest attempt index, as questions for earlier attempts can not be modified.

The unique validation token you received when the Quiz Submission was created.

Access code for the Quiz, if any.

**Example Request:**

```
{
  "attempt": 1,
  "validation_token": "YOUR_VALIDATION_TOKEN",
  "access_code": null
}
```

#### Appendix: Question Answer Formats

.appendix\_entry div.syntaxhighlighter table { width: 100%; }

.appendix\_entry h4 { color: green; }

**Essay Questions**

- Question parametric type: `essay_question`
- Parameter synopsis: `{ "answer": "Answer text." }`

**Example request**

```
{
  "answer": "<h2>My essay</h2>\n\n<p>This is a long article.</p>"
}
```

**Possible errors**

The answer text is larger than the allowed limit of 16 kilobytes.

**Fill In Multiple Blanks Questions**

- Question parametric type: `fill_in_multiple_blanks_question`
- Parameter type: `Hash{String => String}`
- Parameter synopsis: `{ "answer": { "variable": "Answer string." } }`

**Example request**

Given that the question accepts answers to two variables, `color1` and `color2`:

```
{
  "answer": {
    "color1": "red",
    "color2": "green"
  }
}
```

**Possible errors**

The answer map contains a variable that is not accepted by the question.

The answer text is larger than the allowed limit of 16 kilobytes.

**Fill In The Blank Questions**

- Question parametric type: `short_answer_question`
- Parameter synopsis: `{ "answer": "Some sentence." }`

**Example request**

```
{
  "answer": "Hello World!"
}
```

**Possible errors**

Similar to the errors produced by [Essay Questions](https://developerdocs.instructure.com/services/canvas/resources/quiz_submission_questions#essay-questions).

**Formula Questions**

- Question parametric type: `calculated_question`
- Parameter synopsis: `{ "answer": decimal }` where `decimal` is either a rational number, or a literal version of it (String)

**Example request**

With an exponent:

With a string for a number:

**Possible errors**

`Parameter must be a valid decimal.`

The specified value could not be processed as a decimal.

**Matching Questions**

- Question parametric type: `matching_question`
- Parameter type: `Array<Hash>`
- Parameter synopsis: `{ "answer": [{ "answer_id": id, "match_id": id }] }` where the IDs must identify answers and matches accepted by the question.

**Example request**

Given that the question accepts 3 answers with IDs `[ 3, 6, 9 ]` and 6 matches with IDs: `[ 10, 11, 12, 13, 14, 15 ]`:

```
{
  "answer": [{
    "answer_id": 6,
    "match_id": 10
  }, {
    "answer_id": 3,
    "match_id": 14
  }]
}
```

The above request:

- pairs `answer#6` with `match#10`
- pairs `answer#3` with `match#14`
- leaves `answer#9` *un-matched*

**Possible errors**

```
<tr>
  <td>400 Bad Request</td>
  <td><code>Answer entry must be of type Hash, got '...'.</code></td>
  <td>One of the entries of the match-pairings set is not a valid hash.</td>
</tr>
<tr>
  <td>400 Bad Request</td>
  <td><code>Missing parameter 'answer_id'.</code></td>
  <td>One of the entries of the match-pairings does not specify an <code>answer_id</code>.</td>
</tr>
<tr>
  <td>400 Bad Request</td>
  <td><code>Missing parameter 'match_id'.</code></td>
  <td>One of the entries of the match-pairings does not specify an <code>match_id</code>.</td>
</tr>
<tr>
  <td>400 Bad Request</td>
  <td><code>Parameter must be of type Integer.</code></td>
  <td>
    One of the specified <code>answer_id</code> or <code>match_id</code>
    is not an integer.
  </td>
</tr>
<tr>
  <td>400 Bad Request</td>
  <td><code>Unknown answer '123'.</code></td>
  <td>An <code>answer_id</code> you supplied does not identify a valid answer
  for that question.</td>
</tr>
<tr>
  <td>400 Bad Request</td>
  <td><code>Unknown match '123'.</code></td>
  <td>A <code>match_id</code> you supplied does not identify a valid match
  for that question.</td>
</tr>
```

`Answer must be of type Array.`

The match-pairings set you supplied is not an array.

**Multiple Choice Questions**

- Question parametric type: `multiple_choice_question`
- Parameter synopsis: `{ "answer": answer_id }` where `answer_id` is an ID of one of the question's answers.

**Example request**

Given an answer with an ID of 5:

**Possible errors**

`Parameter must be of type Integer.`

The specified \`answer\_id\` is not an integer.

The specified \`answer\_id\` is not a valid answer.

**Multiple Dropdowns Questions**

- Question parametric type: `multiple_dropdowns_question`
- Parameter type: `Hash{String => Integer}`
- Parameter synopsis: `{ "answer": { "variable": answer_id } }` where the keys are variables accepted by the question, and their values are IDs of answers provided by the question.

**Example request**

Given that the question accepts 3 answers to a variable named `color` with the ids `[ 3, 6, 9 ]`:

```
{
  "answer": {
    "color": 6
  }
}
```

**Possible errors**

The answer map you supplied contains a variable that is not accepted by the question.

An `answer_id` you supplied does not identify a valid answer for that question.

**Multiple Answers Questions**

- Question parametric type: `multiple_answers_question`
- Parameter type: `Array<Integer>`
- Parameter synopsis: `{ "answer": [ answer_id ] }` where the array items are IDs of answers accepted by the question.

**Example request**

Given that the question accepts 3 answers with the ids `[ 3, 6, 9 ]` and we want to select the answers `3` and `6`:

**Possible errors**

```
<tr>
  <td>400 Bad Request</td>
  <td><code>Unknown answer '123'.</code></td>
  <td>An answer ID you supplied in the selection set does not identify a
    valid answer for that question.</td>
</tr>
```

`Selection must be of type Array.`

The selection set you supplied is not an array.

`Parameter must be of type Integer.`

One of the answer IDs you supplied is not a valid ID.

**Numerical Questions**

- Question parametric type: `numerical_question`

This is similar to [Formula Questions](https://developerdocs.instructure.com/services/canvas/resources/quiz_submission_questions#formula-questions).

**True/False Questions**

- Question parametric type: `true_false_question`

The rest is similar to [Multiple Choice questions](https://developerdocs.instructure.com/services/canvas/resources/quiz_submission_questions#multiple-choice-questions).

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).