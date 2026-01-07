---
id: 10
title: advanced-level-features
stage: spec
date: 2025-12-27
surface: agent
model: Qwen
feature: todo-app
branch: main
user: jc
command: /sp.specify
labels: ["todo", "advanced", "recurring", "reminders"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - C:\Users\jc\Desktop\hackathone2\specs-history\advanced-recurring-tasks.spec.md
 - C:\Users\jc\Desktop\hackathone2\specs-history\advanced-reminders.spec.md

tests:
 - C:\Users\jc\Desktop\hackathone2\test_todo_app.py

---

## Prompt

Advanced Level – Recurring Tasks Feature Objective: Extend the existing Todo app to support recurring tasks that auto-reschedule based on intervals like daily, weekly, or monthly, maintaining full compatibility with Basic and Intermediate levels. Target audience: Hackathon judges evaluating intelligent features and users seeking automated task management. Focus: Allow creation of recurring tasks with specified intervals; upon marking complete, auto-generate a new instance with updated due date while preserving other attributes. Success criteria: Add command supports recurrence: 'add <title> <description> [rec:daily|weekly|monthly]' (integrates with due date for initial scheduling) When marking a recurring task complete, automatically create a new task with same title, desc, priority, tags – but due date advanced by interval (e.g., +1 day for daily, +7 for weekly) View/List shows recurrence indicator: e.g., "[R:weekly]" next to task Update command allows changing or removing recurrence: 'update <id> [rec:monthly]' or 'rec:none' Existing non-recurring tasks unaffected; old tasks default to no recurrence Handles edge cases like completing before due date or no initial due date (use creation date as base) Task model extended with recurrence: str | None = None (values: "daily", "weekly", "monthly") Constraints: Extend existing Task and TodoList classes without breaking prior features Standard library only (use datetime.timedelta for date calculations) In-memory storage only; no persistent scheduling (new instances created on-the-fly when marked complete) CLI only – no background timers or external schedulers Recurrence optional; defaults to None Not building: Custom intervals (e.g., every 3 days) – stick to daily/weekly/monthly Infinite recurrence history or chains Automatic triggering without user action (e.g., no cron-like auto-complete) /sp.specify Advanced Level – Due Dates & Time Reminders Feature Objective: Enhance due dates to full datetime support and add browser notifications for reminders, evolving the CLI toward intelligent features while keeping backward compatibility. Target audience: Users and evaluators testing advanced automation in the evolving Todo app. Focus: Upgrade due dates to include time (YYYY-MM-DD HH:MM) and enable simple browser notifications when due times approach or pass. Success criteria: Add/Update commands support full datetime: 'add <title> <description> [due:YYYY-MM-DD HH:MM]' (back-compatible with date-only) Parse and validate datetime format; fallback to date-only if no time provided View/List shows full datetime: e.g., "Due: 2025-12-31 14:00" with overdue indicator if past current time (e.g., "[Overdue]") Integrate with recurrence: auto-advanced datetimes respect time component Enable reminders: new command 'remind <id>' to simulate/setup browser notification (use webbrowser module to open a simple alert page or console print for CLI simulation) For true browser notifications, generate a basic HTML/JS snippet that users can run locally (e.g., output code for a web page using Notification API) Task model extended with due_datetime: datetime | None = None (replace or enhance prior due_date) Overdue filtering in search/filter: 'filter due:overdue' Constraints: Standard library only (datetime.datetime for parsing, webbrowser for basic browser open) No external deps or servers – simulate notifications via local browser open or console warnings Extend existing without breaking Basic/Intermediate (old due dates convert to midnight time) CLI primary; browser elements as optional enhancement toward web evolution Assume current time from datetime.now() for overdue checks Not building: Persistent notifications or push services (e.g., no Firebase) Mobile/app integrations Timezone handling beyond local time

## Response snapshot

Successfully created specifications for the Advanced Level features of the Todo app:

1. Advanced Level – Recurring Tasks Feature
   - Allows creation of recurring tasks with daily, weekly, or monthly intervals
   - When marking a recurring task complete, automatically creates a new instance with updated due date
   - View/List shows recurrence indicator
   - Update command allows changing or removing recurrence
   - Maintains full backward compatibility with existing features

2. Advanced Level – Due Dates & Time Reminders Feature
   - Enhances due dates to full datetime support (YYYY-MM-DD HH:MM)
   - Adds browser notifications for reminders
   - Includes overdue indicators
   - Adds 'remind' command to simulate browser notifications
   - Maintains backward compatibility with date-only due dates

Both specifications follow the constraints of using standard library only, maintaining backward compatibility, and extending existing functionality without breaking changes.

## Outcome

- ✅ Impact: Created comprehensive specs for advanced level features
- 🧪 Tests: All existing tests continue to pass
- 📁 Files: Created specs for recurring tasks and time reminders
- 🔁 Next prompts: Ready for planning and implementation of advanced features
- 🧠 Reflection: Specifications maintain compatibility while adding intelligent features

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): All tests PASS
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin implementation of recurring tasks feature