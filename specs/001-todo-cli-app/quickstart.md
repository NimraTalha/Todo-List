# Quickstart Guide: Todo CLI Application

**Feature**: Todo CLI Application
**Date**: 2025-12-27
**Branch**: `001-todo-cli-app`

## Overview

This guide provides quick instructions for setting up and running the Todo CLI application. The application is a command-line tool that allows users to manage todo tasks in memory.

## Prerequisites

- Python 3.13 or higher
- UV package manager (optional, for virtual environment management)
- Windows users: WSL 2 with Ubuntu 22.04 (as per project constitution)

## Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Set up Virtual Environment (Optional but Recommended)

```bash
uv venv  # or python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Navigate to Source Directory

```bash
cd src
```

## Running the Application

### Direct Execution

```bash
python main.py
```

### Expected Output

```
Welcome to the Todo CLI App!
Available commands: add, delete, update, list, complete, incomplete, help, quit
For help with a specific command, type 'help <command>'
```

## Basic Usage

### Adding a Task

```
> add Buy groceries
Task added: ID=1 Title=Buy groceries
```

### Adding a Task with Description

```
> add Clean house Weekly cleaning routine
Task added: ID=2 Title=Clean house
```

### Listing All Tasks

```
> list
ID: 1 [ ] Title: Buy groceries
   Description: 
ID: 2 [ ] Title: Clean house
   Description: Weekly cleaning routine
```

### Marking a Task as Complete

```
> complete 1
Task 1 marked as complete
```

### Updating a Task

```
> update 1 title=Buy groceries and cook desc=Get ingredients for dinner
Task 1 updated
```

### Deleting a Task

```
> delete 2
Task 2 deleted
```

### Getting Help

```
> help
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

### Exiting the Application

```
> quit
Goodbye!
```

## Common Commands Reference

| Command | Description | Example |
|---------|-------------|---------|
| `add <title> [description]` | Add a new task | `add Buy milk` |
| `list` | List all tasks | `list` |
| `update <id> [title=...] [desc=...]` | Update task details | `update 1 title=Buy whole milk` |
| `delete <id>` | Delete a task | `delete 1` |
| `complete <id>` | Mark task as complete | `complete 1` |
| `incomplete <id>` | Mark task as incomplete | `incomplete 1` |
| `help` | Show help | `help` |
| `quit` | Exit application | `quit` |

## Troubleshooting

### Common Issues

1. **Command not recognized**
   - Check spelling of the command
   - Use `help` to see available commands

2. **Invalid ID error**
   - Verify the task ID exists using `list`
   - IDs are integers assigned sequentially starting from 1

3. **Empty title error**
   - When using `add`, a title is required
   - Example: `add My task title` (not just `add`)

### Error Messages

- `"Usage: add <title> [description]"` - Need to provide at least a title when adding
- `"Task ID <id> not found"` - The specified ID doesn't exist
- `"Error: ID must be a number"` - The ID provided wasn't a valid number

## Development

### File Structure

```
src/
├── main.py          # Entry point
├── cli.py           # Command-line interface
├── todolist.py      # Todo list management
├── task.py          # Task model
└── __init__.py      # Package initialization
```

### Running Tests

If tests exist in the project:
```bash
# From the project root
python -m pytest tests/
```

## Next Steps

1. Explore all available commands using `help`
2. Add your first task with `add <title>`
3. Practice the core workflow: add → list → update → complete → delete
4. Review the full specification in `specs/001-todo-cli-app/spec.md`