# CLI API Contract: Todo CLI Application

**Feature**: Todo CLI Application
**Date**: 2025-12-27
**Version**: 1.0

## Overview

This document specifies the command-line interface (CLI) contract for the Todo CLI application. It defines the commands, parameters, expected inputs, and outputs.

## Command Structure

The application follows the pattern: `[command] [arguments]`

## Commands

### 1. Add Task

**Command**: `add`

**Description**: Adds a new task to the todo list.

**Syntax**: `add <title> [description]`

**Parameters**:
- `title` (required): The title of the task (string)
- `description` (optional): The description of the task (string)

**Success Response**:
```
Task added: ID=<id> Title=<title>
```

**Error Responses**:
- If title is missing:
```
Usage: add <title> [description]
```

**Example**:
```
> add Buy groceries
Task added: ID=1 Title=Buy groceries

> add Clean house Weekly cleaning routine
Task added: ID=2 Title=Clean house
```

### 2. List Tasks

**Command**: `list` or `view`

**Description**: Displays all tasks in the todo list.

**Syntax**: `list` or `view`

**Success Response**:
```
ID: <id> [ ] Title: <title>
   Description: <description>
ID: <id> [x] Title: <title>
   Description: <description>
```

For completed tasks, show `[x]`, for incomplete tasks show `[ ]`.

If no tasks exist:
```
No tasks
```

**Example**:
```
> list
ID: 1 [x] Title: Buy groceries
   Description: 
ID: 2 [ ] Title: Clean house
   Description: Weekly cleaning routine
```

### 3. Update Task

**Command**: `update`

**Description**: Updates the title or description of an existing task.

**Syntax**: `update <id> [title=<new_title>] [desc=<new_desc>]`

**Parameters**:
- `id` (required): The ID of the task to update (integer)
- `title` (optional): New title for the task
- `desc` (optional): New description for the task

**Success Response**:
```
Task <id> updated
```

**Error Responses**:
- If ID doesn't exist:
```
Task ID <id> not found
```
- If ID is not a number:
```
Error: ID must be a number
```

**Example**:
```
> update 1 title=Buy groceries and cook desc=Get ingredients for dinner
Task 1 updated
```

### 4. Delete Task

**Command**: `delete`

**Description**: Removes a task from the todo list.

**Syntax**: `delete <id>`

**Parameters**:
- `id` (required): The ID of the task to delete (integer)

**Success Response**:
```
Task <id> deleted
```

**Error Responses**:
- If ID doesn't exist:
```
Task ID <id> not found
```
- If ID is not a number:
```
Error: ID must be a number
```

**Example**:
```
> delete 1
Task 1 deleted
```

### 5. Mark Complete

**Command**: `complete`

**Description**: Marks a task as complete.

**Syntax**: `complete <id>`

**Parameters**:
- `id` (required): The ID of the task to mark complete (integer)

**Success Response**:
```
Task <id> marked as complete
```

**Error Responses**:
- If ID doesn't exist:
```
Task ID <id> not found
```
- If ID is not a number:
```
Error: ID must be a number
```

**Example**:
```
> complete 2
Task 2 marked as complete
```

### 6. Mark Incomplete

**Command**: `incomplete`

**Description**: Marks a task as incomplete.

**Syntax**: `incomplete <id>`

**Parameters**:
- `id` (required): The ID of the task to mark incomplete (integer)

**Success Response**:
```
Task <id> marked as incomplete
```

**Error Responses**:
- If ID doesn't exist:
```
Task ID <id> not found
```
- If ID is not a number:
```
Error: ID must be a number
```

**Example**:
```
> incomplete 2
Task 2 marked as incomplete
```

### 7. Help

**Command**: `help`

**Description**: Displays help information.

**Syntax**: `help [command]`

**Parameters**:
- `command` (optional): Specific command to get help for

**Success Response**:
```
Available commands:
  add <title> [description]     - Add a new task
  delete <id>                   - Delete a task by ID
  update <id> [title=...] [desc=...] - Update task title or description
  list                          - List all tasks
  complete <id>                 - Mark task as complete
  incomplete <id>               - Mark task as incomplete
  help [command]                - Show help for a specific command
  quit                          - Exit the application
```

**Example**:
```
> help
Available commands: ...

> help add
Usage: add <title> [description]
Add a new task with the given title and optional description.
```

### 8. Quit

**Command**: `quit`

**Description**: Exits the application.

**Syntax**: `quit`

**Success Response**:
```
Goodbye!
```

**Example**:
```
> quit
Goodbye!
```

## Common Error Patterns

### Invalid Command
```
Unknown command: <command>. Type 'help' for available commands.
```

### Invalid ID
```
Error: ID must be a number
```

### Non-existent ID
```
Task ID <id> not found
```

## Status Indicators

- `[ ]` - Incomplete task
- `[x]` - Complete task

## Data Types

- `id`: Integer (positive)
- `title`: String (non-empty)
- `description`: String (can be empty)
- `status`: Boolean (represented as [ ] or [x])

## Validation Rules

1. Task titles cannot be empty
2. IDs must be positive integers
3. IDs must exist in the current task list
4. Commands must be valid as defined above