"""
Main module for the Todo CLI application.
Implements the interactive command-line interface for the todo app.
"""
import sys
from todolist import TodoList


class TodoCLI:
    """
    Command-line interface for the Todo application.
    """
    def __init__(self):
        """
        Initialize the CLI with a new TodoList.
        """
        self.todo_list = TodoList()
        self.running = True

    def run(self):
        """
        Run the main CLI loop, processing user commands until quit.
        """
        print("Welcome to the Todo CLI App!")
        print("Available commands: add, delete, update, list, complete, incomplete, help, quit")
        print("For help with a specific command, type 'help <command>'")
        
        while self.running:
            try:
                user_input = input("\n> ").strip()
                if not user_input:
                    continue
                
                self.process_command(user_input)
            except (EOFError, KeyboardInterrupt):
                print("\nGoodbye!")
                break

    def process_command(self, command):
        """
        Process a single command from the user.

        Args:
            command (str): The command string entered by the user
        """
        parts = command.split()
        cmd = parts[0].lower()
        
        if cmd == "add":
            self.handle_add(parts[1:])
        elif cmd == "delete":
            self.handle_delete(parts[1:])
        elif cmd == "update":
            self.handle_update(parts[1:])
        elif cmd in ["list", "view"]:
            self.handle_list(parts[1:])
        elif cmd == "complete":
            self.handle_complete(parts[1:])
        elif cmd == "incomplete":
            self.handle_incomplete(parts[1:])
        elif cmd == "quit":
            self.handle_quit()
        elif cmd == "help":
            self.handle_help(parts[1:])
        else:
            print(f"Unknown command: {cmd}. Type 'help' for available commands.")

    def handle_add(self, args):
        """
        Handle the 'add' command to add a new task.

        Args:
            args (list): Arguments following the 'add' command
        """
        if len(args) < 1:
            print("Usage: add <title> [description]")
            return
        
        title = args[0]
        description = " ".join(args[1:]) if len(args) > 1 else ""
        
        try:
            task = self.todo_list.add_task(title, description)
            print(f"Task added: ID={task.id} Title={task.title}")
        except ValueError as e:
            print(f"Error: {e}")

    def handle_delete(self, args):
        """
        Handle the 'delete' command to remove a task by ID.

        Args:
            args (list): Arguments following the 'delete' command
        """
        if len(args) != 1:
            print("Usage: delete <id>")
            return
        
        try:
            task_id = int(args[0])
            if self.todo_list.delete_task(task_id):
                print(f"Task {task_id} deleted")
            else:
                print(f"Task ID {task_id} not found")
        except ValueError:
            print("Error: ID must be a number")

    def handle_update(self, args):
        """
        Handle the 'update' command to modify a task by ID.

        Args:
            args (list): Arguments following the 'update' command
        """
        if len(args) < 2:
            print("Usage: update <id> [title=<new_title>] [desc=<new_desc>]")
            return
        
        try:
            task_id = int(args[0])
            
            # Parse the remaining arguments for title and description
            title = None
            description = None
            
            for arg in args[1:]:
                if arg.startswith("title="):
                    title = arg[6:]  # Remove "title=" prefix
                elif arg.startswith("desc="):
                    description = arg[5:]  # Remove "desc=" prefix
            
            if self.todo_list.update_task(task_id, title, description):
                print(f"Task {task_id} updated")
            else:
                print(f"Task ID {task_id} not found")
        except ValueError:
            print("Error: ID must be a number")

    def handle_list(self, args):
        """
        Handle the 'list' or 'view' command to display all tasks.

        Args:
            args (list): Arguments following the 'list' command
        """
        tasks = self.todo_list.list_tasks()
        
        if not tasks:
            print("No tasks")
            return
        
        for task in tasks:
            print(task.details())

    def handle_complete(self, args):
        """
        Handle the 'complete' command to mark a task as complete.

        Args:
            args (list): Arguments following the 'complete' command
        """
        if len(args) != 1:
            print("Usage: complete <id>")
            return
        
        try:
            task_id = int(args[0])
            if self.todo_list.mark_complete(task_id):
                print(f"Task {task_id} marked as complete")
            else:
                print(f"Task ID {task_id} not found")
        except ValueError:
            print("Error: ID must be a number")

    def handle_incomplete(self, args):
        """
        Handle the 'incomplete' command to mark a task as incomplete.

        Args:
            args (list): Arguments following the 'incomplete' command
        """
        if len(args) != 1:
            print("Usage: incomplete <id>")
            return
        
        try:
            task_id = int(args[0])
            if self.todo_list.mark_incomplete(task_id):
                print(f"Task {task_id} marked as incomplete")
            else:
                print(f"Task ID {task_id} not found")
        except ValueError:
            print("Error: ID must be a number")

    def handle_quit(self):
        """
        Handle the 'quit' command to exit the application.
        """
        print("Goodbye!")
        self.running = False

    def handle_help(self, args):
        """
        Handle the 'help' command to display usage information.

        Args:
            args (list): Arguments following the 'help' command
        """
        if not args:
            print("Available commands:")
            print("  add <title> [description]     - Add a new task")
            print("  delete <id>                   - Delete a task by ID")
            print("  update <id> [title=...] [desc=...] - Update task title or description")
            print("  list                          - List all tasks")
            print("  complete <id>                 - Mark task as complete")
            print("  incomplete <id>               - Mark task as incomplete")
            print("  help [command]                - Show help for a specific command")
            print("  quit                          - Exit the application")
        elif args[0] == "add":
            print("Usage: add <title> [description]")
            print("Add a new task with the given title and optional description.")
        elif args[0] == "delete":
            print("Usage: delete <id>")
            print("Delete the task with the given ID.")
        elif args[0] == "update":
            print("Usage: update <id> [title=<new_title>] [desc=<new_desc>]")
            print("Update the title or description of the task with the given ID.")
        elif args[0] in ["list", "view"]:
            print("Usage: list (or view)")
            print("Display all tasks with their ID, title, description, and completion status.")
        elif args[0] == "complete":
            print("Usage: complete <id>")
            print("Mark the task with the given ID as complete.")
        elif args[0] == "incomplete":
            print("Usage: incomplete <id>")
            print("Mark the task with the given ID as incomplete.")
        else:
            print(f"Unknown command: {args[0]}. Type 'help' for available commands.")


def main():
    """
    Main entry point for the Todo CLI application.
    """
    cli = TodoCLI()
    cli.run()


if __name__ == "__main__":
    main()