---
title: Calendar Events | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/calendar_events
source: sitemap
fetched_at: 2026-02-15T09:05:30.354295-03:00
rendered_js: false
word_count: 1599
summary: This document defines the data structures and API endpoint for managing and retrieving calendar and assignment events. It provides details on object schemas and request parameters for filtering events by date, type, and context.
tags:
    - calendar-api
    - canvas-lms
    - restful-api
    - event-management
    - assignment-events
    - api-documentation
category: api
---

API for creating, accessing and updating calendar events.

**A CalendarEvent object looks like:**

```
{
  // The ID of the calendar event
"id": 234,
  // The title of the calendar event
"title": "Paintball Fight!",
  // The start timestamp of the event
"start_at": "2012-07-19T15:00:00-06:00",
  // The end timestamp of the event
"end_at": "2012-07-19T16:00:00-06:00",
  // The HTML description of the event
"description": "<b>It's that time again!</b>",
  // The location name of the event
"location_name": "Greendale Community College",
  // The address where the event is taking place
"location_address": "Greendale, Colorado",
  // the context code of the calendar this event belongs to (course, group, user,
  // or account)
"context_code": "course_123",
  // if specified, it indicates which calendar this event should be displayed on.
  // for example, a section-level event would have the course's context code here,
  // while the section's context code would be returned above)
"effective_context_code": null,
  // the context name of the calendar this event belongs to (course, user or
  // group)
"context_name": "Chemistry 101",
  // a comma-separated list of all calendar contexts this event is part of
"all_context_codes": "course_123,course_456",
  // Current state of the event ('active', 'locked' or 'deleted') 'locked'
  // indicates that start_at/end_at cannot be changed (though the event could be
  // deleted). Normally only reservations or time slots with reservations are
  // locked (see the Appointment Groups API)
"workflow_state": "active",
  // Whether this event should be displayed on the calendar. Only true for
  // course-level events with section-level child events.
"hidden": false,
  // Normally null. If this is a reservation (see the Appointment Groups API), the
  // id will indicate the time slot it is for. If this is a section-level event,
  // this will be the course-level parent event.
"parent_event_id": null,
  // The number of child_events. See child_events (and parent_event_id)
"child_events_count": 0,
  // Included by default, but may be excluded (see include[] option). If this is a
  // time slot (see the Appointment Groups API) this will be a list of any
  // reservations. If this is a course-level event, this will be a list of
  // section-level events (if any)
"child_events": null,
  // URL for this calendar event (to update, delete, etc.)
"url": "https://example.com/api/v1/calendar_events/234",
  // URL for a user to view this event
"html_url": "https://example.com/calendar?event_id=234&include_contexts=course_123",
  // The date of this event
"all_day_date": "2012-07-19",
  // Boolean indicating whether this is an all-day event (midnight to midnight)
"all_day": false,
  // When the calendar event was created
"created_at": "2012-07-12T10:55:20-06:00",
  // When the calendar event was last updated
"updated_at": "2012-07-12T10:55:20-06:00",
  // Various Appointment-Group-related fields.These fields are only pertinent to
  // time slots (appointments) and reservations of those time slots. See the
  // Appointment Groups API. The id of the appointment group
"appointment_group_id": null,
  // The API URL of the appointment group
"appointment_group_url": null,
  // If the event is a reservation, this a boolean indicating whether it is the
  // current user's reservation, or someone else's
"own_reservation": false,
  // If the event is a time slot, the API URL for reserving it
"reserve_url": null,
  // If the event is a time slot, a boolean indicating whether the user has
  // already made a reservation for it
"reserved": false,
  // The type of participant to sign up for a slot: 'User' or 'Group'
"participant_type": "User",
  // If the event is a time slot, this is the participant limit
"participants_per_appointment": null,
  // If the event is a time slot and it has a participant limit, an integer
  // indicating how many slots are available
"available_slots": null,
  // If the event is a user-level reservation, this will contain the user
  // participant JSON (refer to the Users API).
"user": null,
  // If the event is a group-level reservation, this will contain the group
  // participant JSON (refer to the Groups API).
"group": null,
  // Boolean indicating whether this has important dates.
"important_dates": true,
  // Identifies the recurring event series this event may belong to.
"series_uuid": null,
  // An iCalendar RRULE for defining how events in a recurring event series
  // repeat.
"rrule": null,
  // Boolean indicating if is the first event in the series of recurring events.
"series_head": null,
  // A natural language expression of how events occur in the series.
"series_natural_language": "Daily 5 times",
  // Boolean indicating whether this has blackout date.
"blackout_date": true
}
```

**An AssignmentEvent object looks like:**

```
{
  // A synthetic ID for the assignment
  "id": "assignment_987",
  // The title of the assignment
  "title": "Essay",
  // The due_at timestamp of the assignment
  "start_at": "2012-07-19T23:59:00-06:00",
  // The due_at timestamp of the assignment
  "end_at": "2012-07-19T23:59:00-06:00",
  // The HTML description of the assignment
  "description": "<b>Write an essay. Whatever you want.</b>",
  // the context code of the (course) calendar this assignment belongs to
  "context_code": "course_123",
  // Current state of the assignment ('published' or 'deleted')
  "workflow_state": "published",
  // URL for this assignment (note that updating/deleting should be done via the
  // Assignments API)
  "url": "https://example.com/api/v1/calendar_events/assignment_987",
  // URL for a user to view this assignment
  "html_url": "http://example.com/courses/123/assignments/987",
  // The due date of this assignment
  "all_day_date": "2012-07-19",
  // Boolean indicating whether this is an all-day event (e.g. assignment due at
  // midnight)
  "all_day": true,
  // When the assignment was created
  "created_at": "2012-07-12T10:55:20-06:00",
  // When the assignment was last updated
  "updated_at": "2012-07-12T10:55:20-06:00",
  // The full assignment JSON data (See the Assignments API)
  "assignment": null,
  // The list of AssignmentOverrides that apply to this event (See the Assignments
  // API). This information is useful for determining which students or sections
  // this assignment-due event applies to.
  "assignment_overrides": null,
  // Boolean indicating whether this has important dates.
  "important_dates": true,
  // An iCalendar RRULE for defining how events in a recurring event series
  // repeat.
  "rrule": "FREQ=DAILY;INTERVAL=1;COUNT=5",
  // Trueif this is the first event in the series of recurring events.
  "series_head": null,
  // A natural language expression of how events occur in the series.
  "series_natural_language": "Daily 5 times"
}
```

[CalendarEventsApiController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/calendar_events_api_controller.rb)

`GET /api/v1/calendar_events`

**Scope:** `url:GET|/api/v1/calendar_events`

Retrieve the paginated list of calendar events or assignments for the current user

**Request Parameters:**

Defaults to “event”

Allowed values: `event`, `assignment`, `sub_assignment`

Only return events since the start\_date (inclusive). Defaults to today. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ.

Only return events before the end\_date (inclusive). Defaults to start\_date. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. If end\_date is the same as start\_date, then only events on that day are returned.

Defaults to false (dated events only). If true, only return undated events and ignore start\_date and end\_date.

Defaults to false (uses start\_date, end\_date, and undated criteria). If true, all events are returned, ignoring start\_date, end\_date, and undated criteria.

List of context codes of courses, groups, users, or accounts whose events you want to see. If not specified, defaults to the current user (i.e personal calendar, no course/group events). Limited to 10 context codes, additional ones are ignored. The format of this field is the context type, followed by an underscore, followed by the context id. For example: course\_42

Array of attributes to exclude. Possible values are “description”, “child\_events” and “assignment”

Array of optional attributes to include. Possible values are “web\_conference” and “series\_natural\_language”

Defaults to false. If true, only events with important dates set to true will be returned.

Defaults to false. If true, only events with blackout date set to true will be returned.

Returns a list of [CalendarEvent](https://developerdocs.instructure.com/services/canvas/resources/calendar_events#calendarevent) objects.

[CalendarEventsApiController#user\_indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/calendar_events_api_controller.rb)

`GET /api/v1/users/:user_id/calendar_events`

**Scope:** `url:GET|/api/v1/users/:user_id/calendar_events`

Retrieve the paginated list of calendar events or assignments for the specified user. To view calendar events for a user other than yourself, you must either be an observer of that user or an administrator.

**Request Parameters:**

Defaults to “event”

Allowed values: `event`, `assignment`

Only return events since the start\_date (inclusive). Defaults to today. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ.

Only return events before the end\_date (inclusive). Defaults to start\_date. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. If end\_date is the same as start\_date, then only events on that day are returned.

Defaults to false (dated events only). If true, only return undated events and ignore start\_date and end\_date.

Defaults to false (uses start\_date, end\_date, and undated criteria). If true, all events are returned, ignoring start\_date, end\_date, and undated criteria.

List of context codes of courses, groups, users, or accounts whose events you want to see. If not specified, defaults to the current user (i.e personal calendar, no course/group events). Limited to 10 context codes, additional ones are ignored. The format of this field is the context type, followed by an underscore, followed by the context id. For example: course\_42

Array of attributes to exclude. Possible values are “description”, “child\_events” and “assignment”

When type is “assignment”, specifies the allowable submission types for returned assignments. Ignored if type is not “assignment” or if exclude\_submission\_types is provided.

`exclude_submission_types[]`

When type is “assignment”, specifies the submission types to be excluded from the returned assignments. Ignored if type is not “assignment”.

Array of optional attributes to include. Possible values are “web\_conference” and “series\_natural\_language”

Defaults to false If true, only events with important dates set to true will be returned.

Defaults to false If true, only events with blackout date set to true will be returned.

Returns a list of [CalendarEvent](https://developerdocs.instructure.com/services/canvas/resources/calendar_events#calendarevent) objects.

[CalendarEventsApiController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/calendar_events_api_controller.rb)

`POST /api/v1/calendar_events`

**Scope:** `url:POST|/api/v1/calendar_events`

Create and return a new calendar event

**Request Parameters:**

`calendar_event[context_code]`

Context code of the course, group, user, or account whose calendar this event should be added to.

Short title for the calendar event.

`calendar_event[description]`

Longer HTML description of the event.

Start date/time of the event.

End date/time of the event.

`calendar_event[location_name]`

Location name of the event.

`calendar_event[location_address]`

`calendar_event[time_zone_edited]`

When true event is considered to span the whole day and times are ignored.

`calendar_event[child_event_data][X][start_at]`

Section-level start time(s) if this is a course event. X can be any identifier, provided that it is consistent across the start\_at, end\_at and context\_code

`calendar_event[child_event_data][X][end_at]`

Section-level end time(s) if this is a course event.

`calendar_event[child_event_data][X][context_code]`

Context code(s) corresponding to the section-level start and end time(s).

`calendar_event[duplicate][count]`

Number of times to copy/duplicate the event. Count cannot exceed 200.

`calendar_event[duplicate][interval]`

Defaults to 1 if duplicate ‘count\` is set. The interval between the duplicated events.

`calendar_event[duplicate][frequency]`

Defaults to “weekly”. The frequency at which to duplicate the event

Allowed values: `daily`, `weekly`, `monthly`

`calendar_event[duplicate][append_iterator]`

Defaults to false. If set to ‘true\`, an increasing counter number will be appended to the event title when the event is duplicated. (e.g. Event 1, Event 2, Event 3, etc)

The recurrence rule to create a series of recurring events. Its value is the [iCalendar RRULEarrow-up-right](https://icalendar.org/iCalendar-RFC-5545/3-8-5-3-recurrence-rule.html) defining how the event repeats. Unending series not supported.

`calendar_event[blackout_date]`

If the blackout\_date is true, this event represents a holiday or some other special day that does not count in course pacing.

**Example Request:**

```
curl 'https://<canvas>/api/v1/calendar_events.json' \
     -X POST \
     -F 'calendar_event[context_code]=course_123' \
     -F 'calendar_event[title]=Paintball Fight!' \
     -F 'calendar_event[start_at]=2012-07-19T21:00:00Z' \
     -F 'calendar_event[end_at]=2012-07-19T22:00:00Z' \
     -H "Authorization: Bearer <token>"
```

[CalendarEventsApiController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/calendar_events_api_controller.rb)

`GET /api/v1/calendar_events/:id`

**Scope:** `url:GET|/api/v1/calendar_events/:id`

Returns detailed information about a specific calendar event or assignment.

Returns a [CalendarEvent](https://developerdocs.instructure.com/services/canvas/resources/calendar_events#calendarevent) object.

[CalendarEventsApiController#reservearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/calendar_events_api_controller.rb)

`POST /api/v1/calendar_events/:id/reservations`

**Scope:** `url:POST|/api/v1/calendar_events/:id/reservations`

`POST /api/v1/calendar_events/:id/reservations/:participant_id`

**Scope:** `url:POST|/api/v1/calendar_events/:id/reservations/:participant_id`

Reserves a particular time slot and return the new reservation

**Request Parameters:**

User or group id for whom you are making the reservation (depends on the participant type). Defaults to the current user (or user’s candidate group).

Comments to associate with this reservation

Defaults to false. If true, cancel any previous reservation(s) for this participant and appointment group.

**Example Request:**

```
curl 'https://<canvas>/api/v1/calendar_events/345/reservations.json' \
     -X POST \
     -F 'cancel_existing=true' \
     -H "Authorization: Bearer <token>"
```

[CalendarEventsApiController#updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/calendar_events_api_controller.rb)

`PUT /api/v1/calendar_events/:id`

**Scope:** `url:PUT|/api/v1/calendar_events/:id`

Update and return a calendar event

**Request Parameters:**

`calendar_event[context_code]`

Context code of the course, group, user, or account to move this event to. Scheduler appointments and events with section-specific times cannot be moved between calendars.

Short title for the calendar event.

`calendar_event[description]`

Longer HTML description of the event.

Start date/time of the event.

End date/time of the event.

`calendar_event[location_name]`

Location name of the event.

`calendar_event[location_address]`

`calendar_event[time_zone_edited]`

When true event is considered to span the whole day and times are ignored.

`calendar_event[child_event_data][X][start_at]`

Section-level start time(s) if this is a course event. X can be any identifier, provided that it is consistent across the start\_at, end\_at and context\_code

`calendar_event[child_event_data][X][end_at]`

Section-level end time(s) if this is a course event.

`calendar_event[child_event_data][X][context_code]`

Context code(s) corresponding to the section-level start and end time(s).

Valid if the event whose ID is in the URL is part of a series. This defines the shape of the recurring event series after it’s updated. Its value is the iCalendar RRULE. Unending series are not supported.

Valid if the event whose ID is in the URL is part of a series. Update just the event whose ID is in in the URL, all events in the series, or the given event and all those following. Some updates may create a new series. For example, changing the start time of this and all following events from the middle of a series.

Allowed values: `one`, `all`, `following`

`calendar_event[blackout_date]`

If the blackout\_date is true, this event represents a holiday or some other special day that does not count in course pacing.

**Example Request:**

```
curl 'https://<canvas>/api/v1/calendar_events/234' \
     -X PUT \
     -F 'calendar_event[title]=Epic Paintball Fight!' \
     -H "Authorization: Bearer <token>"
```

[CalendarEventsApiController#destroyarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/calendar_events_api_controller.rb)

`DELETE /api/v1/calendar_events/:id`

**Scope:** `url:DELETE|/api/v1/calendar_events/:id`

Delete an event from the calendar and return the deleted event

**Request Parameters:**

Reason for deleting/canceling the event.

Valid if the event whose ID is in the URL is part of a series. Delete just the event whose ID is in in the URL, all events in the series, or the given event and all those following.

Allowed values: `one`, `all`, `following`

**Example Request:**

```
curl 'https://<canvas>/api/v1/calendar_events/234' \
     -X DELETE \
     -F 'cancel_reason=Greendale layed off the janitorial staff :(' \
     -F 'which=following'
     -H "Authorization: Bearer <token>"
```

[CalendarEventsApiController#save\_enabled\_account\_calendarsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/calendar_events_api_controller.rb)

`POST /api/v1/calendar_events/save_enabled_account_calendars`

**Scope:** `url:POST|/api/v1/calendar_events/save_enabled_account_calendars`

Creates and updates the enabled\_account\_calendars and mark\_feature\_as\_seen user preferences

**Request Parameters:**

Flag to mark account calendars feature as seen

`enabled_account_calendars[]`

An array of account Ids to remember in the calendars list of the user

**Example Request:**

```
curl 'https://<canvas>/api/v1/calendar_events/save_enabled_account_calendars' \
     -X POST \
     -F 'mark_feature_as_seen=true' \
     -F 'enabled_account_calendars[]=1' \
     -F 'enabled_account_calendars[]=2' \
     -H "Authorization: Bearer <token>"
```

[CalendarEventsApiController#set\_course\_timetablearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/calendar_events_api_controller.rb)

`POST /api/v1/courses/:course_id/calendar_events/timetable`

**Scope:** `url:POST|/api/v1/courses/:course_id/calendar_events/timetable`

Creates and updates “timetable” events for a course. Can automaticaly generate a series of calendar events based on simple schedules (e.g. “Monday and Wednesday at 2:00pm” )

Existing timetable events for the course and course sections will be updated if they still are part of the timetable. Otherwise, they will be deleted.

**Request Parameters:**

`timetables[course_section_id][]`

An array of timetable objects for the course section specified by course\_section\_id. If course\_section\_id is set to “all”, events will be created for the entire course.

`timetables[course_section_id][][weekdays]`

A comma-separated list of abbreviated weekdays (Mon-Monday, Tue-Tuesday, Wed-Wednesday, Thu-Thursday, Fri-Friday, Sat-Saturday, Sun-Sunday)

`timetables[course_section_id][][start_time]`

Time to start each event at (e.g. “9:00 am”)

`timetables[course_section_id][][end_time]`

Time to end each event at (e.g. “9:00 am”)

`timetables[course_section_id][][location_name]`

A location name to set for each event

**Example Request:**

```
curl 'https://<canvas>/api/v1/calendar_events/timetable' \
     -X POST \
     -F 'timetables[all][][weekdays]=Mon,Wed,Fri' \
     -F 'timetables[all][][start_time]=11:00 am' \
     -F 'timetables[all][][end_time]=11:50 am' \
     -F 'timetables[all][][location_name]=Room 237' \
     -H "Authorization: Bearer <token>"
```

[CalendarEventsApiController#get\_course\_timetablearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/calendar_events_api_controller.rb)

`GET /api/v1/courses/:course_id/calendar_events/timetable`

**Scope:** `url:GET|/api/v1/courses/:course_id/calendar_events/timetable`

Returns the last timetable set by the [Set a course timetable](https://developerdocs.instructure.com/services/canvas/resources/calendar_events#method.calendar_events_api.set_course_timetable) endpoint

[CalendarEventsApiController#set\_course\_timetable\_eventsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/calendar_events_api_controller.rb)

`POST /api/v1/courses/:course_id/calendar_events/timetable_events`

**Scope:** `url:POST|/api/v1/courses/:course_id/calendar_events/timetable_events`

Creates and updates “timetable” events for a course or course section. Similar to [setting a course timetable](https://developerdocs.instructure.com/services/canvas/resources/calendar_events#method.calendar_events_api.set_course_timetable), but instead of generating a list of events based on a timetable schedule, this endpoint expects a complete list of events.

**Request Parameters:**

Events will be created for the course section specified by course\_section\_id. If not present, events will be created for the entire course.

An array of event objects to use.

Location name for the event

A unique identifier that can be used to update the event at a later time If one is not specified, an identifier will be generated based on the start and end times

Title for the meeting. If not present, will default to the associated course’s name

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).