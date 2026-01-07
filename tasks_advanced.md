# Tasks: Todo App - Advanced Level Features

## Feature Overview
Extending the existing Basic + Intermediate Level CLI Todo app to include Advanced Level features: Recurring Tasks and Due Date & Time Reminders. Maintaining 100% backward compatibility with existing functionality.

## Implementation Strategy
- MVP: Implement Due Date & Time Reminders feature first
- Incremental delivery: Add features one by one while maintaining functionality
- Backward compatibility: Preserve all existing Basic + Intermediate Level functionality
- Standard library only: No external dependencies

## Dependencies
- User Story 2 (Recurring Tasks) depends on foundational datetime updates from User Story 1
- User Story 2 also depends on recurrence field addition to Task model

## Parallel Execution Examples
- CLI command parsing for recurrence can be developed in parallel with datetime parsing
- Display formatting for recurrence indicators can be developed in parallel with overdue warnings

---

## Phase 1: Setup

- [ ] T001 Create project structure documentation in README.md
- [ ] T002 Set up development environment with Python 3.13+ requirements
- [ ] T003 Verify existing Basic + Intermediate Level functionality works before changes

---

## Phase 2: Foundational Updates

- [x] T004 Update Task model with due_datetime and recurrence fields in src/todo_app.py
- [x] T005 Update TodoList methods to handle new Task fields in src/todo_app.py
- [x] T006 Update Task string representation to include new fields in src/todo_app.py
- [x] T007 Update tests to verify new Task fields work correctly in test_todo_app.py

---

## Phase 3: [US1] Due Dates & Time Reminders Feature

- [x] T008 [US1] Implement datetime parsing function in src/todo_app.py
- [x] T009 [US1] Update CLI to parse datetime from add command in src/todo_app.py
- [x] T010 [US1] Update CLI to parse datetime from update command in src/todo_app.py
- [x] T011 [US1] Update display formatting to show full datetime in src/todo_app.py
- [x] T012 [US1] Add datetime validation to add_task method in src/todo_app.py
- [x] T013 [US1] Add datetime validation to update_task method in src/todo_app.py
- [x] T014 [US1] Create tests for datetime functionality in test_todo_app.py
- [x] T015 [US1] Implement overdue detection function in src/todo_app.py
- [x] T016 [US1] Implement remind command in CLI in src/todo_app.py
- [x] T017 [US1] Add overdue indicators to display formatting in src/todo_app.py
- [x] T018 [US1] Create tests for reminder functionality in test_todo_app.py
- [x] T019 [US1] Verify backward compatibility with existing commands

**Story Goal**: Enhance due dates to full datetime support and add browser notifications for reminders, evolving the CLI toward intelligent features while keeping backward compatibility.

**Independent Test Criteria**: 
- Add/Update commands support full datetime: 'add <title> <description> [due:YYYY-MM-DD HH:MM]' (back-compatible with date-only)
- Parse and validate datetime format; fallback to date-only if no time provided
- View/List shows full datetime: e.g., "Due: 2025-12-31 14:00" with overdue indicator if past current time (e.g., "[Overdue]")
- Enable reminders: new command 'remind <id>' to simulate/setup browser notification
- Task model extended with due_datetime: datetime | None = None (replace or enhance prior due_date)
- Overdue filtering in search/filter: 'filter due:overdue'

---

## Phase 4: [US2] Recurring Tasks Feature

- [x] T020 [US2] Implement recurrence validation function in src/todo_app.py
- [x] T021 [US2] Update CLI to parse recurrence from add command in src/todo_app.py
- [x] T022 [US2] Update CLI to parse recurrence from update command in src/todo_app.py
- [x] T023 [US2] Update display formatting to show recurrence indicators in src/todo_app.py
- [x] T024 [US2] Add recurrence validation to add_task method in src/todo_app.py
- [x] T025 [US2] Add recurrence validation to update_task method in src/todo_app.py
- [x] T026 [US2] Implement auto-respawn logic in mark_task_complete method in src/todo_app.py
- [x] T027 [US2] Create tests for recurrence functionality in test_todo_app.py
- [x] T028 [US2] Create tests for auto-respawn behavior in test_todo_app.py
- [x] T029 [US2] Verify backward compatibility with existing commands

**Story Goal**: Extend the existing Todo app to support recurring tasks that auto-reschedule based on intervals like daily, weekly, or monthly, maintaining full compatibility with Basic and Intermediate levels.

**Independent Test Criteria**:
- Add command supports recurrence: 'add <title> <description> [rec:daily|weekly|monthly]' (integrates with due date for initial scheduling)
- When marking a recurring task complete, automatically create a new task with same title, desc, priority, tags – but due date advanced by interval (e.g., +1 day for daily, +7 for weekly)
- View/List shows recurrence indicator: e.g., "[R:weekly]" next to task
- Update command allows changing or removing recurrence: 'update <id> [rec:monthly]' or 'rec:none'
- Existing non-recurring tasks unaffected; old tasks default to no recurrence
- Handles edge cases like completing before due date or no initial due date (use creation date as base)
- Task model extended with recurrence: str | None = None (values: "daily", "weekly", "monthly")

---

## Phase 5: Polish & Cross-Cutting Concerns

- [x] T030 Update README.md with new command documentation
- [x] T031 Create comprehensive demo script showcasing all new features
- [x] T032 Run full regression test suite to ensure all Basic + Intermediate Level functionality still works
- [x] T033 Perform integration testing of combined features
- [x] T034 Update error handling and user-friendly messages
- [x] T035 Final code review and cleanup
- [x] T036 Document any architectural decisions made during implementation

---

## MVP Scope
The MVP will include:
- T001-T007: Foundational updates
- T008-T019: Due Dates & Time Reminders feature (US1)

This provides a complete, independently testable increment that adds value while maintaining all existing functionality.