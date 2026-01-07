---
id: 14
title: recurring-tasks-feature
stage: green
date: 2025-12-27
surface: agent
model: Qwen
feature: todo-app
branch: main
user: jc
command: /sp.implement
labels: ["todo", "advanced", "recurring", "implementation"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - C:\Users\jc\Desktop\hackathone2\src\todo_app.py
 - C:\Users\jc\Desktop\hackathone2\test_todo_app.py
 - C:\Users\jc\Desktop\hackathone2\tasks_advanced.md

tests:
 - C:\Users\jc\Desktop\hackathone2\test_todo_app.py

---

## Prompt

Advanced Level – Recurring Tasks Feature Objective: Extend the existing Todo app to support recurring tasks that auto-reschedule based on intervals like daily, weekly, or monthly, maintaining full compatibility with Basic and Intermediate levels. Target audience: Hackathon judges evaluating intelligent features and users seeking automated task management. Focus: Allow creation of recurring tasks with specified intervals; upon marking complete, auto-generate a new instance with updated due date while preserving other attributes. Success criteria: Add command supports recurrence: 'add <title> <description> [rec:daily|weekly|monthly]' (integrates with due date for initial scheduling) When marking a recurring task complete, automatically create a new task with same title, desc, priority, tags – but due date advanced by interval (e.g., +1 day for daily, +7 for weekly) View/List shows recurrence indicator: e.g., "[R:weekly]" next to task Update command allows changing or removing recurrence: 'update <id> [rec:monthly]' or 'rec:none' Existing non-recurring tasks unaffected; old tasks default to no recurrence Handles edge cases like completing before due date or no initial due date (use creation date as base) Task model extended with recurrence: str | None = None (values: "daily", "weekly", "monthly") Constraints: Extend existing Task and TodoList classes without breaking prior features Standard library only (use datetime.timedelta for date calculations) In-memory storage only; no persistent scheduling (new instances created on-the-fly when marked complete) CLI only – no background timers or external schedulers Recurrence optional; defaults to None Not building: Custom intervals (e.g., every 3 days) – stick to daily/weekly/monthly Infinite recurrence history or chains Automatic triggering without user action (e.g., no cron-like auto-complete) /sp.specify Advanced Level – Due Dates & Time Reminders Feature Objective: Enhance due dates to full datetime support and add browser notifications for reminders, evolving the CLI toward intelligent features while keeping backward compatibility. Target audience: Users and evaluators testing advanced automation in the evolving Todo app. Focus: Upgrade due dates to include time (YYYY-MM-DD HH:MM) and enable simple browser notifications when due times approach or pass. Success criteria: Add/Update commands support full datetime: 'add <title> <description> [due:YYYY-MM-DD HH:MM]' (back-compatible with date-only) Parse and validate datetime format; fallback to date-only if no time provided View/List shows full datetime: e.g., "Due: 2025-12-31 14:00" with overdue indicator if past current time (e.g., "[Overdue]") Integrate with recurrence: auto-advanced datetimes respect time component Enable reminders: new command 'remind <id>' to simulate/setup browser notification (use webbrowser module to open a simple alert page or console print for CLI simulation) For true browser notifications, generate a basic HTML/JS snippet that users can run locally (e.g., output code for a web page using Notification API) Task model extended with due_datetime: datetime | None = None (replace or enhance prior due_date) Overdue filtering in search/filter: 'filter due:overdue' Constraints: Standard library only (datetime.datetime for parsing, webbrowser for basic browser open) No external deps or servers – simulate notifications via local browser open or console warnings Extend existing without breaking Basic/Intermediate (old due dates convert to midnight time) CLI primary; browser elements as optional enhancement toward web evolution Assume current time from datetime.now() for overdue checks Not building: Persistent notifications or push services (e.g., no Firebase) Mobile/app integrations Timezone handling beyond local time

## Response snapshot

Successfully implemented the Recurring Tasks feature for the Todo CLI app. Completed tasks:

1. Implemented recurrence validation function
2. Updated CLI to parse recurrence from add and update commands
3. Updated display formatting to show recurrence indicators
4. Added recurrence validation to add_task and update_task methods
5. Implemented auto-respawn logic in mark_task_complete method
6. Created comprehensive tests for recurrence functionality
7. Created tests for auto-respawn behavior
8. Verified backward compatibility with existing commands

The auto-respawn logic creates a new task with the same properties when a recurring task is marked as complete, advancing the due date by the recurrence interval (daily, weekly, or monthly). All functionality maintains 100% backward compatibility with the existing Basic and Intermediate Level app. The implementation uses only standard library components and follows all specified constraints.

## Outcome

- ✅ Impact: Successfully implemented Recurring Tasks feature while maintaining backward compatibility
- 🧪 Tests: All 43 unit tests pass successfully, including new recurrence and auto-respawn functionality tests
- 📁 Files: Updated todo_app.py, test_todo_app.py, and tasks_advanced.md
- 🔁 Next prompts: Ready for final polish and cross-cutting concerns
- 🧠 Reflection: Implementation successfully extends existing functionality without breaking changes

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): All tests PASS
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin final polish and cross-cutting concerns