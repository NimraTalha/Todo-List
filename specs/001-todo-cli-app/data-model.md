# Data Model: Todo CLI Application

**Feature**: Todo CLI Application
**Date**: 2025-12-27
**Branch**: `001-todo-cli-app`

## Overview

This document defines the data model for the Todo CLI application, including entities, attributes, relationships, and validation rules based on the feature specification.

## Entities

### Task

The Task entity represents a single todo item in the application.

#### Attributes

| Attribute | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| id | Integer | Yes | Auto-generated | Unique identifier, auto-incrementing starting from 1 |
| title | String | Yes | N/A | Title of the task |
| description | String | No | Empty string | Detailed description of the task |
| completed | Boolean | Yes | False | Completion status of the task |

#### Validation Rules

- `id`: Must be a positive integer, unique within the TodoList
- `title`: Must not be empty or contain only whitespace
- `description`: Can be empty, no length limit (within memory constraints)
- `completed`: Must be a boolean value (True/False)

#### State Transitions

- `incomplete` → `complete`: When user marks task as complete
- `complete` → `incomplete`: When user marks task as incomplete

### TodoList

The TodoList entity manages a collection of Task objects in memory.

#### Attributes

| Attribute | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| tasks | List of Task objects | Yes | Empty list | Collection of all tasks |
| next_id | Integer | Yes | 1 | Counter for generating next task ID |

#### Methods

- `add_task(title, description)`: Creates a new Task with auto-generated ID and adds to the list
- `delete_task(task_id)`: Removes a task by its ID
- `update_task(task_id, title=None, description=None)`: Updates title or description of a task by ID
- `get_task(task_id)`: Retrieves a task by its ID
- `list_tasks()`: Returns all tasks in the list
- `mark_complete(task_id)`: Sets completed status to True for a task by ID
- `mark_incomplete(task_id)`: Sets completed status to False for a task by ID

#### Validation Rules

- `tasks`: All items must be valid Task objects
- `next_id`: Must be incremented after each new task creation

## Relationships

### TodoList → Task (One-to-Many)

- One TodoList contains many Task objects
- Tasks are stored in the `tasks` list attribute of TodoList
- Each Task has a reference to its TodoList through the list structure

## Data Flow

### Creation Flow

1. User inputs "add" command with title and optional description
2. CLI parses the command and calls TodoList.add_task()
3. TodoList creates a new Task with:
   - `id` = current `next_id` value
   - `title` = provided title
   - `description` = provided description (or empty string)
   - `completed` = False
4. Task is added to the `tasks` list
5. `next_id` is incremented by 1

### Update Flow

1. User inputs "update" command with task ID and new values
2. CLI parses the command and calls TodoList.update_task()
3. TodoList finds the Task with matching ID
4. Updates specified attributes (title and/or description)
5. Task remains in the same position in the list

### Status Change Flow

1. User inputs "complete" or "incomplete" command with task ID
2. CLI parses the command and calls appropriate TodoList method
3. TodoList finds the Task with matching ID
4. Updates the `completed` attribute to True or False
5. Task remains in the same position in the list

## Constraints

### Memory Constraints

- All data stored in memory only (Phase I requirement)
- No persistence to files or databases
- Data lost when application exits

### Identity Constraints

- Task IDs are unique within a single TodoList
- Task IDs are sequential starting from 1
- Deleted task IDs are not reused

### Data Integrity

- Task titles cannot be empty
- Task objects must maintain valid state (all required attributes present)
- Completed status can only be True or False