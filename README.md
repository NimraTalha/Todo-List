# Todo CLI App

This is a simple command-line todo application that stores tasks in memory. It's part of the "Evolution of Todo" hackathon project, demonstrating the progression from CLI to distributed cloud-native AI systems.

## Setup Instructions

### Prerequisites
- Python 3.13+
- UV package manager (optional, for virtual environment management)

### Windows Users
Windows users must use WSL 2 (Windows Subsystem for Linux) for development:
```bash
# Install WSL 2
wsl --install

# Set WSL 2 as default
wsl --set-default-version 2

# Install Ubuntu
wsl --install -d Ubuntu-22.04
```

### Installation
1. Clone the repository
2. Navigate to the project directory
3. (Optional) Create a virtual environment using UV:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows WSL: source .venv/Scripts/activate
   ```

### Running the Application
To run the application:
```bash
cd src
python main.py
```

## Features

The application supports the following commands:

- `add <title> [description]` - Add a new task
- `delete <id>` - Delete a task by ID
- `update <id> [title=...] [desc=...]` - Update task title or description
- `list` (or `view`) - List all tasks
- `complete <id>` - Mark task as complete
- `incomplete <id>` - Mark task as incomplete
- `help` - Show available commands
- `quit` - Exit the application

## Example Usage

```
> add Buy groceries
Task added: ID=1 Title=Buy groceries

> add Clean house Weekly cleaning routine
Task added: ID=2 Title=Clean house

> list
ID: 1 [ ] Title: Buy groceries
   Description: 
ID: 2 [ ] Title: Clean house
   Description: Weekly cleaning routine

> complete 1
Task 1 marked as complete

> list
ID: 1 [x] Title: Buy groceries
   Description: 
ID: 2 [ ] Title: Clean house
   Description: Weekly cleaning routine

> quit
Goodbye!
```

## Project Structure

- `src/` - Contains all Python source code
  - `main.py` - Entry point of the application
  - `cli.py` - Command-line interface implementation
  - `todolist.py` - Todo list management
  - `task.py` - Task model definition
- `specs/` - Contains specification files
- `requirements.txt` - Project dependencies (none beyond standard library)
- `README.md` - This file