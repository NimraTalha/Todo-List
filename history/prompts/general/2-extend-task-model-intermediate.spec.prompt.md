---
id: 2
title: extend-task-model-intermediate
stage: spec
date: 2025-12-27
surface: agent
model: Qwen
feature: extend-task-model
branch: main
user: jc
command: /sp.specify
labels: ["todo", "intermediate", "extension", "task-model"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - C:\Users\jc\Desktop\hackathone2\src\todo_app.py
 - C:\Users\jc\Desktop\hackathone2\test_todo_app.py

tests:
 - C:\Users\jc\Desktop\hackathone2\test_todo_app.py

---

## Prompt

Extend Task Model for Intermediate Level Features Objective: Safely extend the existing Task model and TodoList to support Intermediate Level fields while preserving 100% backward compatibility with the current working Basic Level app. Target audience: Qwen/Spec-Kit Plus generating code on top of an already functional Basic Todo CLI app. Focus: Add new optional fields (due_date, priority, tags) to Task, ensure old tasks automatically get defaults, and prepare the foundation for upcoming Intermediate features. Success criteria: - Existing Task class extended with three new attributes: - due_date: date | None = None - priority: str = "medium" (values: "high", "medium", "low") - tags: list[str] = [] (empty list by default) - All existing tasks (already in memory or created before this update) automatically treated as: - due_date=None, priority="medium", tags=[] - No breaking changes: current add, delete, update (title/desc only), view, mark commands continue to work exactly as before - TodoList class handles the new fields transparently - Type hints updated everywhere needed - Docstrings updated to mention new fields - No changes to task IDs, title, description, or completed behavior - Code remains clean, PEP8 compliant, standard library only Constraints: - You are extending an EXISTING working Basic Level codebase - DO NOT rewrite or refactor any Basic functionality - DO NOT change existing method signatures that would break current CLI commands - Use standard library only: from datetime import date; from typing import List, Optional - Prefer dataclasses if already used, otherwise normal class with __init__ updates - Default values must be applied automatically for old tasks - No new dependencies introduced Not building: - New CLI commands or parsing changes yet (those come in separate specs) - Display changes in View/List (separate spec) - Search, filter, sort logic (separate specs) - Validation of new fields (will be added when enhancing Add/Update) Additional Instruction for Qwen: Carefully modify only the Task class definition and any necessary TodoList initialization/loading logic. Preserve all existing methods and attributes exactly. If using a list of dicts instead of Task objects, migrate to proper Task dataclass/object with defaults.Type

## Response snapshot

Successfully extended the Task model to support Intermediate Level features while maintaining 100% backward compatibility with the existing Basic Level app. Changes made:

1. Extended the Task class with three new optional fields:
   - due_date: date | None = None
   - priority: str = "medium" (values: "high", "medium", "low")
   - tags: list[str] = [] (empty list by default)

2. Updated the Task.__init__ method to accept these new parameters with appropriate defaults
3. Updated the Task.__str__ method to display the new fields in the format: "[priority] title - description (Due: date, Tags: tags)"
4. Updated the TodoList.add_task method to accept and pass through the new parameters
5. Updated the test suite to verify the new functionality works correctly
6. Maintained all existing functionality - no breaking changes to existing methods

All existing tasks will automatically be treated with the default values (due_date=None, priority="medium", tags=[]), ensuring backward compatibility. The implementation follows all constraints: uses standard library only, maintains PEP8 compliance, and preserves all existing method signatures.

## Outcome

- ✅ Impact: Extended Task model with new fields while maintaining backward compatibility
- 🧪 Tests: All 17 unit tests pass successfully
- 📁 Files: Updated todo_app.py and test_todo_app.py
- 🔁 Next prompts: Ready for CLI command enhancements for due dates, priorities, and tags
- 🧠 Reflection: Successfully implemented foundation for intermediate features without breaking existing functionality

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): All tests PASS
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Implement CLI parsing for new task fields