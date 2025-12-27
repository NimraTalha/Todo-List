---

description: "Task list for Todo CLI Application feature"
---

# Tasks: Todo CLI Application

**Input**: Design documents from `/specs/001-todo-cli-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

<!--
  ============================================================================
  IMPORTANT: The tasks below are SAMPLE TASKS for illustration purposes only.

  The /sp.tasks command MUST replace these with actual tasks based on:
  - User stories from spec.md (with their priorities P1, P2, P3...)
  - Feature requirements from plan.md
  - Entities from data-model.md
  - Endpoints from contracts/

  Tasks MUST be organized by user story so each story can be:
  - Implemented independently
  - Tested independently
  - Delivered as an MVP increment

  DO NOT keep these sample tasks in the generated tasks.md file.
  ============================================================================
-->

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure per implementation plan
- [x] T002 Initialize Python 3.13 project with core dependencies
- [x] T003 [P] Configure linting and formatting tools

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [x] T004 Create base Task model in src/task.py
- [x] T005 [P] Create TodoList model in src/todolist.py
- [x] T006 [P] Setup CLI routing structure in src/cli.py
- [x] T007 Create main application entry point in src/main.py
- [x] T008 Configure error handling and validation infrastructure
- [x] T009 Setup environment configuration management

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Todo (Priority: P1) 🎯 MVP

**Goal**: Allow users to add new todo items to their list so that they can track tasks they need to complete.

**Independent Test**: The application allows users to add a new todo with an ID, title, and description. The todo appears in the list when viewed.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T010 [P] [US1] Contract test for add command in tests/contract/test_add.py
- [ ] T011 [P] [US1] Integration test for add user journey in tests/integration/test_add_journey.py

### Implementation for User Story 1

- [x] T012 [P] [US1] Create Task model in src/task.py
- [x] T013 [P] [US1] Create TodoList model in src/todolist.py
- [x] T014 [US1] Implement add_task method in src/todolist.py (depends on T012, T013)
- [x] T015 [US1] Implement add command in src/cli.py
- [x] T016 [US1] Add validation for title requirement in src/todolist.py
- [x] T017 [US1] Add logging for add operations in src/todolist.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View All Todos (Priority: P1)

**Goal**: Allow users to view all their todos so that they can see what tasks they need to complete.

**Independent Test**: The application displays all todos with their ID, title, description, and completion status in a clear, readable format.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [ ] T018 [P] [US2] Contract test for list command in tests/contract/test_list.py
- [ ] T019 [P] [US2] Integration test for list user journey in tests/integration/test_list_journey.py

### Implementation for User Story 2

- [x] T020 [P] [US2] Implement list_tasks method in src/todolist.py
- [x] T021 [US2] Implement list command in src/cli.py
- [x] T022 [US2] Add display formatting for tasks with status indicators in src/task.py
- [x] T023 [US2] Integrate with User Story 1 components (if needed)

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Update Todo (Priority: P2)

**Goal**: Allow users to update the title or description of an existing todo so that they can keep their task information current.

**Independent Test**: The application allows users to update the title or description of a specific todo by ID.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [ ] T024 [P] [US3] Contract test for update command in tests/contract/test_update.py
- [ ] T025 [P] [US3] Integration test for update user journey in tests/integration/test_update_journey.py

### Implementation for User Story 3

- [x] T026 [P] [US3] Implement update_task method in src/todolist.py
- [x] T027 [US3] Implement update command in src/cli.py
- [x] T028 [US3] Add validation for ID existence in src/todolist.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: User Story 4 - Delete Todo (Priority: P2)

**Goal**: Allow users to delete a todo so that they can remove tasks that are no longer relevant.

**Independent Test**: The application allows users to delete a specific todo by ID.

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [ ] T029 [P] [US4] Contract test for delete command in tests/contract/test_delete.py
- [ ] T030 [P] [US4] Integration test for delete user journey in tests/integration/test_delete_journey.py

### Implementation for User Story 4

- [x] T031 [P] [US4] Implement delete_task method in src/todolist.py
- [x] T032 [US4] Implement delete command in src/cli.py
- [x] T033 [US4] Add validation for ID existence in src/todolist.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 7: User Story 5 - Mark Todo Complete (Priority: P2)

**Goal**: Allow users to mark a todo as complete so that they can track which tasks they have finished.

**Independent Test**: The application allows users to mark a specific todo as complete by ID.

### Tests for User Story 5 (OPTIONAL - only if tests requested) ⚠️

- [ ] T034 [P] [US5] Contract test for complete/incomplete commands in tests/contract/test_complete.py
- [ ] T035 [P] [US5] Integration test for complete user journey in tests/integration/test_complete_journey.py

### Implementation for User Story 5

- [x] T036 [P] [US5] Implement mark_complete and mark_incomplete methods in src/todolist.py
- [x] T037 [US5] Implement complete and incomplete commands in src/cli.py
- [x] T038 [US5] Add validation for ID existence in src/todolist.py

**Checkpoint**: All user stories should now be independently functional

---

[Add more user story phases as needed, following the same pattern]

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] TXXX [P] Documentation updates in docs/
- [x] TXXX Code cleanup and refactoring
- [x] TXXX Performance optimization across all stories
- [x] TXXX [P] Additional unit tests (if requested) in tests/unit/
- [x] TXXX Security hardening
- [x] TXXX Run quickstart.md validation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3/US4 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

### Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Contract test for add command in tests/contract/test_add.py"
Task: "Integration test for add user journey in tests/integration/test_add_journey.py"

# Launch all models for User Story 1 together:
Task: "Create Task model in src/task.py"
Task: "Create TodoList model in src/todolist.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence