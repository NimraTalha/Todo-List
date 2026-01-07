---
id: 4
title: todo-intermediate-tasks
stage: tasks
date: 2025-12-27
surface: agent
model: Qwen
feature: extend-todo-app
branch: main
user: jc
command: /sp.tasks
labels: ["todo", "intermediate", "tasks", "planning"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - C:\Users\jc\Desktop\hackathone2\tasks.md

tests:
 - C:\Users\jc\Desktop\hackathone2\test_todo_app.py

---

## Prompt

Extend Task Model for Intermediate Level Features Objective: Safely extend the existing Task model and TodoList to support Intermediate Level fields while preserving 100% backward compatibility with the current working Basic Level app. Target audience: Qwen/Spec-Kit Plus generating code on top of an already functional Basic Todo CLI app. Focus: Add new optional fields (due_date, priority, tags) to Task, ensure old tasks automatically get defaults, and prepare the foundation for upcoming Intermediate features. Success criteria: - Existing Task class extended with three new attributes: - due_date: date | None = None - priority: str = "medium" (values: "high", "medium", "low") - tags: list[str] = [] (empty list by default) - All existing tasks (already in memory or created before this update) automatically treated as: - due_date=None, priority="medium", tags=[] - No breaking changes: current add, delete, update (title/desc only), view, mark commands continue to work exactly as before - TodoList class handles the new fields transparently - Type hints updated everywhere needed - Docstrings updated to mention new fields - No changes to task IDs, title, description, or completed behavior - Code remains clean, PEP8 compliant, standard library only Constraints: - You are extending an EXISTING working Basic Level codebase - DO NOT rewrite or refactor any Basic functionality - DO NOT change existing method signatures that would break current CLI commands - Use standard library only: from datetime import date; from typing import List, Optional - Prefer dataclasses if already used, otherwise normal class with __init__ updates - Default values must be applied automatically for old tasks - No new dependencies introduced Not building: - New CLI commands or parsing changes yet (those come in separate specs) - Display changes in View/List (separate spec) - Search, filter, sort logic (separate specs) - Validation of new fields (will be added when enhancing Add/Update) Additional Instruction for Qwen: Carefully modify only the Task class definition and any necessary TodoList initialization/loading logic. Preserve all existing methods and attributes exactly. If using a list of dicts instead of Task objects, migrate to proper Task dataclass/object with defaults.Type

## Response snapshot

Successfully created a comprehensive tasks.md file for extending the Todo CLI app to include Intermediate Level features. The tasks are organized in phases:

1. Phase 1: Setup tasks
2. Phase 2: Foundational updates to the Task model
3. Phase 3: Due Dates feature (US1)
4. Phase 4: Priorities & Tags feature (US2)
5. Phase 5: Search & Filter feature (US3)
6. Phase 6: Sort Tasks feature (US4)
7. Phase 7: Polish & Cross-Cutting Concerns

Each task follows the required checklist format with proper IDs, story labels, and file paths. The implementation strategy focuses on MVP delivery with incremental features while maintaining backward compatibility. Dependencies between user stories are clearly identified, and parallel execution opportunities are noted.

## Outcome

- ✅ Impact: Comprehensive task breakdown for intermediate level features
- 🧪 Tests: All existing tests continue to pass, new tests planned for each feature
- 📁 Files: Created tasks.md with 45 specific, actionable tasks
- 🔁 Next prompts: Ready for implementation of individual tasks
- 🧠 Reflection: Tasks are well-organized by user story for independent implementation and testing

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): All tests PASS
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin implementation of foundational updates (T004-T007)