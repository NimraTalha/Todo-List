"""
Todo CLI Application
A simple in-memory todo application with basic CRUD operations.
"""
from typing import List, Optional
from datetime import datetime, date, timedelta
import re


def validate_date_format(date_str: str) -> bool:
    """
    Validate that a date string is in YYYY-MM-DD format and represents a valid date.

    Args:
        date_str: Date string to validate

    Returns:
        True if the date string is valid, False otherwise
    """
    # Check if the format matches YYYY-MM-DD
    if not re.match(r'^\d{4}-\d{2}-\d{2}$', date_str):
        return False

    try:
        # Try to parse the date to ensure it's a valid date
        year, month, day = map(int, date_str.split('-'))
        date(year, month, day)
        return True
    except ValueError:
        return False


def validate_datetime_format(datetime_str: str) -> bool:
    """
    Validate that a datetime string is in YYYY-MM-DD HH:MM format and represents a valid datetime.

    Args:
        datetime_str: Datetime string to validate

    Returns:
        True if the datetime string is valid, False otherwise
    """
    # Check if the format matches YYYY-MM-DD HH:MM
    if not re.match(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$', datetime_str):
        return False

    try:
        # Try to parse the datetime to ensure it's a valid datetime
        datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')
        return True
    except ValueError:
        return False


def validate_priority(priority: str) -> bool:
    """
    Validate that a priority string is one of the allowed values: 'high', 'medium', 'low'.
    The validation is case-insensitive.

    Args:
        priority: Priority string to validate

    Returns:
        True if the priority is valid, False otherwise
    """
    valid_priorities = {'high', 'medium', 'low'}
    return priority.lower() in valid_priorities


def validate_recurrence(recurrence: str) -> bool:
    """
    Validate that a recurrence string is one of the allowed values: 'daily', 'weekly', 'monthly'.
    The validation is case-insensitive.

    Args:
        recurrence: Recurrence string to validate

    Returns:
        True if the recurrence is valid, False otherwise
    """
    valid_recurrences = {'daily', 'weekly', 'monthly'}
    return recurrence.lower() in valid_recurrences


def parse_datetime_from_string(datetime_str: str) -> Optional[datetime]:
    """
    Parse a datetime string in 'YYYY-MM-DD HH:MM' format into a datetime object.
    If the string is in 'YYYY-MM-DD' format only, it will be converted to a datetime
    at midnight (00:00).

    Args:
        datetime_str: Datetime string to parse

    Returns:
        datetime object if parsing is successful, None otherwise
    """
    if not datetime_str:
        return None

    # Check if it's in full datetime format (YYYY-MM-DD HH:MM)
    if re.match(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$', datetime_str):
        try:
            return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')
        except ValueError:
            return None

    # Check if it's in date-only format (YYYY-MM-DD)
    elif re.match(r'^\d{4}-\d{2}-\d{2}$', datetime_str):
        try:
            date_obj = datetime.strptime(datetime_str, '%Y-%m-%d').date()
            # Convert to datetime at midnight
            return datetime.combine(date_obj, datetime.min.time())
        except ValueError:
            return None

    # Invalid format
    return None


def advance_date_by_recurrence_interval(original_date: date, recurrence: str) -> date:
    """
    Advance a date by the recurrence interval (daily, weekly, monthly).

    Args:
        original_date: Original date to advance
        recurrence: Recurrence interval ('daily', 'weekly', 'monthly')

    Returns:
        New date advanced by the recurrence interval
    """
    recurrence = recurrence.lower()

    if recurrence == 'daily':
        return original_date + timedelta(days=1)
    elif recurrence == 'weekly':
        return original_date + timedelta(weeks=1)
    elif recurrence == 'monthly':
        # For monthly, we'll add approximately one month by adding 30 days
        # A more sophisticated implementation would handle months with different lengths
        try:
            # Try to add one month by adjusting the year/month
            if original_date.month == 12:
                new_month = 1
                new_year = original_date.year + 1
            else:
                new_month = original_date.month + 1
                new_year = original_date.year

            # Handle case where the day doesn't exist in the next month (e.g., Jan 31 -> Feb 31 doesn't exist)
            max_day_in_new_month = date(new_year, new_month, 1).replace(month=new_month+1, day=1) - timedelta(days=1)
            new_day = min(original_date.day, max_day_in_new_month.day)

            return date(new_year, new_month, new_day)
        except ValueError:
            # Fallback to adding 30 days if the above calculation fails
            return original_date + timedelta(days=30)
    else:
        # If invalid recurrence, return the original date
        return original_date


def parse_tags_from_string(tags_str: str) -> List[str]:
    """
    Parse a comma-separated string of tags into a list of individual tags.
    Trims whitespace and converts tags to lowercase for consistency.

    Args:
        tags_str: Comma-separated string of tags

    Returns:
        List of individual tags
    """
    if not tags_str:
        return []

    # Split by comma, trim whitespace, and convert to lowercase
    tags = [tag.strip().lower() for tag in tags_str.split(',') if tag.strip()]
    return tags


def keyword_search(tasks: List[Task], keyword: str) -> List[Task]:
    """
    Search for tasks that contain the keyword in their title or description.
    The search is case-insensitive.

    Args:
        tasks: List of tasks to search through
        keyword: Keyword to search for

    Returns:
        List of tasks that match the keyword
    """
    if not keyword:
        return []

    keyword_lower = keyword.lower()
    matching_tasks = []

    for task in tasks:
        # Check if keyword is in title or description (case-insensitive)
        if (keyword_lower in task.title.lower() or
            keyword_lower in task.description.lower()):
            matching_tasks.append(task)

    return matching_tasks


def filter_by_status(tasks: List[Task], status: str) -> List[Task]:
    """
    Filter tasks by their completion status.

    Args:
        tasks: List of tasks to filter
        status: Status to filter by ('complete' or 'incomplete')

    Returns:
        List of tasks that match the status
    """
    if status.lower() == 'complete':
        return [task for task in tasks if task.completed]
    elif status.lower() == 'incomplete':
        return [task for task in tasks if not task.completed]
    else:
        # If invalid status, return empty list or all tasks based on requirement
        # For now, return empty list to indicate no matches
        return []


def filter_by_priority(tasks: List[Task], priority: str) -> List[Task]:
    """
    Filter tasks by their priority level.

    Args:
        tasks: List of tasks to filter
        priority: Priority to filter by ('high', 'medium', 'low')

    Returns:
        List of tasks that match the priority
    """
    if validate_priority(priority):
        return [task for task in tasks if task.priority.lower() == priority.lower()]
    else:
        # If invalid priority, return empty list
        return []


def filter_by_due_date(tasks: List[Task], date_filter: str) -> List[Task]:
    """
    Filter tasks by their due date.

    Args:
        tasks: List of tasks to filter
        date_filter: Date filter in format 'before:YYYY-MM-DD', 'after:YYYY-MM-DD', or 'on:YYYY-MM-DD'

    Returns:
        List of tasks that match the date filter
    """
    if not date_filter or ':' not in date_filter:
        return []

    filter_type, date_str = date_filter.split(':', 1)
    filter_type = filter_type.lower()
    date_str = date_str.strip()

    if not validate_date_format(date_str):
        return []

    # Parse the date
    year, month, day = map(int, date_str.split('-'))
    filter_date = date(year, month, day)

    result_tasks = []

    for task in tasks:
        if task.due_date is None:
            # Skip tasks without due dates unless filtering for tasks without due dates
            # For now, we'll only include tasks that have due dates
            continue

        if filter_type == 'on':
            if task.due_date == filter_date:
                result_tasks.append(task)
        elif filter_type == 'before':
            if task.due_date < filter_date:
                result_tasks.append(task)
        elif filter_type == 'after':
            if task.due_date > filter_date:
                result_tasks.append(task)

    return result_tasks


def sort_by_priority(tasks: List[Task], reverse: bool = False) -> List[Task]:
    """
    Sort tasks by priority level (High → Medium → Low).

    Args:
        tasks: List of tasks to sort
        reverse: If True, sort in descending order (Low → Medium → High)

    Returns:
        List of tasks sorted by priority
    """
    # Define priority order: High (1), Medium (2), Low (3)
    priority_order = {"high": 1, "medium": 2, "low": 3}

    # Sort by priority order, then by creation time as a secondary sort
    return sorted(tasks,
                 key=lambda task: (priority_order.get(task.priority.lower(), 4), task.created_at),
                 reverse=reverse)


def sort_by_due_date(tasks: List[Task], reverse: bool = False) -> List[Task]:
    """
    Sort tasks by due date. Tasks without due dates are placed at the end.

    Args:
        tasks: List of tasks to sort
        reverse: If True, sort in descending order (latest first)

    Returns:
        List of tasks sorted by due date
    """
    def sort_key(task):
        # If task has no due date, place it at the end (or beginning if reverse)
        if task.due_date is None:
            # Use a far future date if sorting normally, far past if reverse
            return date.max if not reverse else date.min
        return task.due_date

    return sorted(tasks, key=sort_key, reverse=reverse)


def sort_by_creation_time(tasks: List[Task], reverse: bool = False) -> List[Task]:
    """
    Sort tasks by creation time.

    Args:
        tasks: List of tasks to sort
        reverse: If True, sort in descending order (newest first)

    Returns:
        List of tasks sorted by creation time
    """
    return sorted(tasks, key=lambda task: task.created_at, reverse=reverse)


def sort_by_title(tasks: List[Task], reverse: bool = False) -> List[Task]:
    """
    Sort tasks by title (alphabetically).

    Args:
        tasks: List of tasks to sort
        reverse: If True, sort in descending order (Z → A)

    Returns:
        List of tasks sorted by title
    """
    return sorted(tasks, key=lambda task: task.title.lower(), reverse=reverse)


def is_overdue(task: Task) -> bool:
    """
    Check if a task is overdue based on its due date or due datetime.

    Args:
        task: Task to check for overdue status

    Returns:
        True if the task is overdue, False otherwise
    """
    if task.completed:
        return False  # Completed tasks are not considered overdue

    # Check due_datetime first if available
    if task.due_datetime:
        return task.due_datetime < datetime.now()

    # If no due_datetime, check due_date
    if task.due_date:
        # Compare with today's date at midnight
        today = datetime.now().date()
        return task.due_date < today

    # If no due date/time, task is not overdue
    return False


def get_overdue_tasks(tasks: List[Task]) -> List[Task]:
    """
    Get all overdue tasks from a list of tasks.

    Args:
        tasks: List of tasks to check

    Returns:
        List of overdue tasks
    """
    return [task for task in tasks if is_overdue(task)]


class Task:
    """
    Represents a single task in the todo list.
    """
    def __init__(self, task_id: int, title: str, description: str = "",
                 due_date: Optional[date] = None, priority: str = "medium", tags: Optional[List[str]] = None,
                 due_datetime: Optional[datetime] = None, recurrence: Optional[str] = None):
        self.id = task_id
        self.title = title
        self.description = description
        self.completed = False
        self.created_at = datetime.now()
        self.due_date = due_date  # New field: due date (optional)
        self.priority = priority  # New field: priority level (high, medium, low)
        self.tags = tags if tags is not None else []  # New field: list of tags
        self.due_datetime = due_datetime  # New field: due datetime (optional)
        self.recurrence = recurrence  # New field: recurrence pattern (daily, weekly, monthly)

    def __str__(self) -> str:
        status = "[x]" if self.completed else "[ ]"
        # Use due_datetime if available, otherwise use due_date
        if self.due_datetime:
            due_str = self.due_datetime.strftime("%Y-%m-%d %H:%M")
        elif self.due_date:
            due_str = self.due_date.strftime("%Y-%m-%d")
        else:
            due_str = "-"
        priority_char = {"high": "H", "medium": "M", "low": "L"}.get(self.priority, "M")
        tags_str = ", ".join(self.tags) if self.tags else "none"
        recurrence_str = f" [R:{self.recurrence}]" if self.recurrence else ""
        return f"{status} {self.id}. [{priority_char}]{recurrence_str} {self.title} - {self.description} (Due: {due_str}, Tags: {tags_str})"


class TodoList:
    """
    Manages a collection of tasks in memory.
    """
    def __init__(self):
        self.tasks: List[Task] = []
        self.next_id = 1

    def add_task(self, title: str, description: str = "", due_date=None, priority: str = "medium",
                 tags: Optional[List[str]] = None, due_datetime: Optional[datetime] = None,
                 recurrence: Optional[str] = None) -> Task:
        """Add a new task to the list."""
        # Validate due date if provided
        if due_date is not None and not isinstance(due_date, date):
            raise ValueError("Due date must be a date object or None")

        # Validate priority
        if not validate_priority(priority):
            raise ValueError(f"Priority must be one of 'high', 'medium', or 'low'. Got: {priority}")

        # Validate recurrence if provided
        if recurrence is not None and not validate_recurrence(recurrence):
            raise ValueError(f"Recurrence must be one of 'daily', 'weekly', or 'monthly'. Got: {recurrence}")

        # Use empty list if tags is None
        if tags is None:
            tags = []

        task = Task(self.next_id, title, description, due_date, priority, tags, due_datetime, recurrence)
        self.tasks.append(task)
        self.next_id += 1
        return task

    def delete_task(self, task_id: int) -> bool:
        """Delete a task by ID."""
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                del self.tasks[i]
                return True
        return False

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None,
                    due_date: Optional[date] = None, priority: Optional[str] = None, tags: Optional[List[str]] = None,
                    due_datetime: Optional[datetime] = None, recurrence: Optional[str] = None) -> bool:
        """Update a task's title, description, due_date, priority, tags, due_datetime, and/or recurrence by ID."""
        for task in self.tasks:
            if task.id == task_id:
                if title is not None:
                    task.title = title
                if description is not None:
                    task.description = description
                if due_date is not None:
                    # Validate due date if provided
                    if not isinstance(due_date, date) and due_date is not None:
                        raise ValueError("Due date must be a date object or None")
                    task.due_date = due_date
                if priority is not None:
                    # Validate priority if provided
                    if not validate_priority(priority):
                        raise ValueError(f"Priority must be one of 'high', 'medium', or 'low'. Got: {priority}")
                    task.priority = priority
                if tags is not None:
                    task.tags = tags
                if due_datetime is not None:
                    # Validate due datetime if provided
                    if not isinstance(due_datetime, datetime) and due_datetime is not None:
                        raise ValueError("Due datetime must be a datetime object or None")
                    task.due_datetime = due_datetime
                if recurrence is not None:
                    # Validate recurrence if provided
                    if not validate_recurrence(recurrence):
                        raise ValueError(f"Recurrence must be one of 'daily', 'weekly', or 'monthly'. Got: {recurrence}")
                    task.recurrence = recurrence
                return True
        return False

    def get_task(self, task_id: int) -> Optional[Task]:
        """Get a task by ID."""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def get_all_tasks(self) -> List[Task]:
        """Get all tasks."""
        return self.tasks

    def mark_task_complete(self, task_id: int, completed: bool = True) -> bool:
        """Mark a task as complete or incomplete."""
        for task in self.tasks:
            if task.id == task_id:
                task.completed = completed

                # If marking as complete and task has recurrence, create a new instance
                if completed and task.recurrence:
                    # Create a new task with the same properties but advanced due date
                    new_due_date = None
                    if task.due_date:
                        new_due_date = advance_date_by_recurrence_interval(task.due_date, task.recurrence)

                    # If the original task had a due_datetime, advance that too
                    new_due_datetime = None
                    if task.due_datetime:
                        # Advance the date part while keeping the same time
                        advanced_date = advance_date_by_recurrence_interval(task.due_datetime.date(), task.recurrence)
                        new_due_datetime = datetime.combine(advanced_date, task.due_datetime.time())

                    # Create new task with incremented ID
                    new_task = Task(
                        task_id=self.next_id,
                        title=task.title,
                        description=task.description,
                        due_date=new_due_date,
                        priority=task.priority,
                        tags=task.tags.copy(),
                        due_datetime=new_due_datetime,
                        recurrence=task.recurrence
                    )

                    self.tasks.append(new_task)
                    self.next_id += 1
                    print(f"Auto-generated recurring task: {new_task}")

                return True
        return False


class TodoCLI:
    """
    Command-line interface for the todo application.
    """
    def __init__(self):
        self.todo_list = TodoList()

    def run(self):
        """Run the main CLI loop."""
        print("Welcome to the Todo App!")
        print("Commands: add, delete, update, list, complete, incomplete, search, remind, quit")

        while True:
            try:
                command = input("\nEnter command: ").strip().lower()

                if command == "quit" or command == "exit":
                    print("Goodbye!")
                    break
                elif command == "add":
                    self.handle_add()
                elif command == "delete":
                    self.handle_delete()
                elif command == "update":
                    self.handle_update()
                elif command == "list" or command == "ls":
                    self.handle_list()
                elif command == "complete":
                    self.handle_complete()
                elif command == "incomplete":
                    self.handle_incomplete()
                elif command == "search":
                    self.handle_search()
                elif command == "remind":
                    self.handle_remind()
                else:
                    print(f"Unknown command: {command}")
                    print("Available commands: add, delete, update, list, complete, incomplete, search, remind, quit")
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except Exception as e:
                print(f"An error occurred: {e}")

    def handle_add(self):
        """Handle the add command."""
        title = input("Enter task title: ").strip()
        if not title:
            print("Title cannot be empty.")
            return

        description = input("Enter task description (optional): ").strip()

        # Ask for due date/datetime if desired
        due_datetime_str = input("Enter due date/time (YYYY-MM-DD HH:MM format, optional): ").strip()
        due_datetime = None
        due_date = None

        if due_datetime_str:
            # Try to parse as full datetime first
            due_datetime = parse_datetime_from_string(due_datetime_str)
            if due_datetime is None:
                print(f"Invalid datetime format: {due_datetime_str}. Expected YYYY-MM-DD HH:MM. Task will be created without due date/time.")
            else:
                print(f"Due date/time set to: {due_datetime_str}")
        else:
            # If no datetime provided, ask for date only
            due_date_str = input("Enter due date (YYYY-MM-DD format, optional): ").strip()
            if due_date_str:
                if validate_date_format(due_date_str):
                    year, month, day = map(int, due_date_str.split('-'))
                    due_date = date(year, month, day)
                    print(f"Due date set to: {due_date_str}")
                else:
                    print(f"Invalid date format: {due_date_str}. Expected YYYY-MM-DD. Task will be created without due date.")

        # Ask for priority
        priority = input("Enter priority (high/medium/low, default: medium): ").strip().lower()
        if priority and not validate_priority(priority):
            print(f"Invalid priority: {priority}. Using default 'medium'.")
            priority = "medium"
        elif not priority:
            priority = "medium"  # Default priority

        # Ask for recurrence
        recurrence = input("Enter recurrence (daily/weekly/monthly, optional): ").strip().lower()
        if recurrence and not validate_recurrence(recurrence):
            print(f"Invalid recurrence: {recurrence}. Valid options are daily, weekly, or monthly. Task will be created without recurrence.")
            recurrence = None

        # Ask for tags
        tags_str = input("Enter tags (comma-separated, optional): ").strip()
        tags = parse_tags_from_string(tags_str)

        # Add the task with all provided information
        task = self.todo_list.add_task(title, description, due_date, priority, tags, due_datetime, recurrence)
        print(f"Added task: {task}")

    def handle_delete(self):
        """Handle the delete command."""
        try:
            task_id = int(input("Enter task ID to delete: "))
        except ValueError:
            print("Invalid task ID. Please enter a number.")
            return
            
        if self.todo_list.delete_task(task_id):
            print(f"Deleted task with ID {task_id}")
        else:
            print(f"Task with ID {task_id} not found.")

    def handle_update(self):
        """Handle the update command."""
        try:
            task_id = int(input("Enter task ID to update: "))
        except ValueError:
            print("Invalid task ID. Please enter a number.")
            return

        task = self.todo_list.get_task(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        title = input(f"Enter new title (current: '{task.title}'): ").strip()
        description = input(f"Enter new description (current: '{task.description}'): ").strip()

        # Ask for due datetime update
        due_datetime_str = input(f"Enter new due date/time (YYYY-MM-DD HH:MM format, current: '{task.due_datetime.strftime('%Y-%m-%d %H:%M') if task.due_datetime else 'None'}', leave blank to keep current): ").strip()
        due_datetime = None
        due_datetime_updated = False
        if due_datetime_str:
            parsed_dt = parse_datetime_from_string(due_datetime_str)
            if parsed_dt:
                due_datetime = parsed_dt
                due_datetime_updated = True
                print(f"Due date/time updated to: {due_datetime_str}")
            else:
                print(f"Invalid datetime format: {due_datetime_str}. Expected YYYY-MM-DD HH:MM. Due date/time will not be changed.")
        elif due_datetime_str == "":  # User wants to clear the due datetime
            due_datetime = None
            due_datetime_updated = True
            print("Due date/time cleared.")

        # If due datetime wasn't updated, ask for due date update
        due_date = None
        due_date_updated = False
        if not due_datetime_updated and due_datetime_str == "":
            due_date_str = input(f"Enter new due date (YYYY-MM-DD format, current: '{task.due_date.strftime('%Y-%m-%d') if task.due_date else 'None'}', leave blank to keep current): ").strip()
            if due_date_str:
                if validate_date_format(due_date_str):
                    year, month, day = map(int, due_date_str.split('-'))
                    due_date = date(year, month, day)
                    due_date_updated = True
                    print(f"Due date updated to: {due_date_str}")
                else:
                    print(f"Invalid date format: {due_date_str}. Expected YYYY-MM-DD. Due date will not be changed.")
            elif due_date_str == "":  # User wants to clear the due date
                due_date = None
                due_date_updated = True
                print("Due date cleared.")

        # Ask for priority update
        priority = input(f"Enter new priority (high/medium/low, current: '{task.priority}', leave blank to keep current): ").strip().lower()
        priority_updated = False
        if priority:
            if validate_priority(priority):
                priority_updated = True
                print(f"Priority updated to: {priority}")
            else:
                print(f"Invalid priority: {priority}. Priority will not be changed.")
                priority = None  # Reset to indicate no change
        else:
            priority = None  # No change requested

        # Ask for recurrence update
        recurrence = input(f"Enter new recurrence (daily/weekly/monthly, current: '{task.recurrence if task.recurrence else 'None'}', leave blank to keep current): ").strip().lower()
        recurrence_updated = False
        if recurrence:
            if validate_recurrence(recurrence):
                recurrence_updated = True
                print(f"Recurrence updated to: {recurrence}")
            else:
                print(f"Invalid recurrence: {recurrence}. Valid options are daily, weekly, or monthly. Recurrence will not be changed.")
                recurrence = None  # Reset to indicate no change
        elif recurrence == "":  # User wants to clear the recurrence
            recurrence = None
            recurrence_updated = True
            print("Recurrence cleared.")

        # Ask for tags update
        tags_str = input(f"Enter new tags (comma-separated, current: '{', '.join(task.tags) if task.tags else 'None'}', leave blank to keep current): ").strip()
        tags = None
        tags_updated = False
        if tags_str:
            tags = parse_tags_from_string(tags_str)
            tags_updated = True
            print(f"Tags updated to: {', '.join(tags)}")
        elif tags_str == "":  # User wants to clear tags
            tags = []
            tags_updated = True
            print("Tags cleared.")

        # Use current values if new values are empty
        new_title = title if title else None
        new_description = description if description else None
        new_due_datetime = due_datetime if due_datetime_updated else None
        new_due_date = due_date if due_date_updated else None
        new_priority = priority if priority_updated else None
        new_recurrence = recurrence if recurrence_updated else None
        new_tags = tags if tags_updated else None

        if self.todo_list.update_task(task_id, new_title, new_description, new_due_date, new_priority, new_tags, new_due_datetime, new_recurrence):
            updated_task = self.todo_list.get_task(task_id)
            print(f"Updated task: {updated_task}")
        else:
            print("Failed to update task.")

    def handle_remind(self):
        """Handle the remind command to simulate browser notifications."""
        try:
            task_id = int(input("Enter task ID to remind about: "))
        except ValueError:
            print("Invalid task ID. Please enter a number.")
            return

        task = self.todo_list.get_task(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return

        # Check if task is overdue
        if is_overdue(task):
            print(f"⚠️  REMINDER: Task '{task.title}' is OVERDUE!")
        else:
            print(f"🔔 REMINDER: Task '{task.title}'")

        print(f"   Description: {task.description}")
        if task.due_datetime:
            print(f"   Due: {task.due_datetime.strftime('%Y-%m-%d %H:%M')}")
        elif task.due_date:
            print(f"   Due: {task.due_date.strftime('%Y-%m-%d')}")

        # Simulate opening a simple browser notification
        print("\nOpening simulated notification in browser...")
        print("If this were a real application, a browser notification would appear.")

        # Optionally, we could generate HTML for a local notification page
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Task Reminder</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    max-width: 500px;
                    margin: 50px auto;
                    padding: 20px;
                    border: 1px solid #ccc;
                    border-radius: 8px;
                    background-color: #f9f9f9;
                }}
                .overdue {{
                    border-left: 5px solid #ff0000;
                    background-color: #ffe6e6;
                }}
                .normal {{
                    border-left: 5px solid #007bff;
                }}
                h1 {{
                    color: #333;
                    margin-top: 0;
                }}
                .due {{
                    font-weight: bold;
                    color: #666;
                }}
            </style>
        </head>
        <body class="{'overdue' if is_overdue(task) else 'normal'}">
            <h1>Task Reminder</h1>
            <h2>{task.title}</h2>
            <p><strong>Description:</strong> {task.description}</p>
            <p class="due"><strong>Due:</strong> {task.due_datetime.strftime('%Y-%m-%d %H:%M') if task.due_datetime else (task.due_date.strftime('%Y-%m-%d') if task.due_date else 'Not set')}</p>
            {(f'<p style="color: red; font-weight: bold;">⚠️ This task is OVERDUE!</p>' if is_overdue(task) else '')}
        </body>
        </html>
        """

        import tempfile
        import os
        import webbrowser

        # Create a temporary HTML file with the notification
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.html') as f:
            f.write(html_content)
            temp_path = f.name

        # Open the file in the default browser
        webbrowser.open('file://' + os.path.abspath(temp_path))

        print(f"Notification page opened in your browser: {os.path.basename(temp_path)}")
        print("(The temporary file will remain until you close the application)")

    def handle_search(self):
        """Handle the search command."""
        keyword = input("Enter keyword to search for: ").strip()
        if not keyword:
            print("Keyword cannot be empty.")
            return

        # Perform the search
        matching_tasks = keyword_search(self.todo_list.get_all_tasks(), keyword)

        if not matching_tasks:
            print("No tasks match your search.")
        else:
            print(f"\nSearch results for '{keyword}':")
            for task in matching_tasks:
                print(task)

    def handle_list(self):
        """Handle the list command with optional filtering and sorting."""
        # For now, implement basic filtering and sorting based on user input
        # In a more advanced implementation, we would parse command arguments

        print("You can filter the list by:")
        print("  - status: 'complete' or 'incomplete'")
        print("  - priority: 'high', 'medium', or 'low'")
        print("  - due date: 'before:YYYY-MM-DD', 'after:YYYY-MM-DD', or 'on:YYYY-MM-DD'")
        print("  - due: 'overdue' for overdue tasks")
        print("  - Leave blank for no filter")

        # Get filter options from user
        status_filter = input("Filter by status (complete/incomplete, optional): ").strip()
        priority_filter = input("Filter by priority (high/medium/low, optional): ").strip()
        due_date_filter = input("Filter by due date (before:YYYY-MM-DD, after:YYYY-MM-DD, on:YYYY-MM-DD, overdue, optional): ").strip()

        # Get sort option from user
        print("\nYou can sort the list by:")
        print("  - priority: 'priority' (High → Medium → Low)")
        print("  - due date: 'due' (earliest first, None at end)")
        print("  - creation time: 'created' (newest first)")
        print("  - title: 'title' (alphabetical)")
        print("  - Leave blank for no sorting")

        sort_option = input("Sort by (priority/due/created/title, optional): ").strip().lower()
        sort_reverse = False
        if sort_option:
            sort_reverse_input = input("Reverse order? (yes/no, default: no): ").strip().lower()
            if sort_reverse_input in ['yes', 'y', 'true']:
                sort_reverse = True

        # Get all tasks
        tasks = self.todo_list.get_all_tasks()

        # Apply filters
        if status_filter:
            tasks = filter_by_status(tasks, status_filter)

        if priority_filter:
            tasks = filter_by_priority(tasks, priority_filter)

        if due_date_filter:
            if due_date_filter.lower() == 'overdue':
                tasks = get_overdue_tasks(tasks)
            else:
                tasks = filter_by_due_date(tasks, due_date_filter)

        # Apply sorting
        if sort_option == 'priority':
            tasks = sort_by_priority(tasks, sort_reverse)
        elif sort_option == 'due':
            tasks = sort_by_due_date(tasks, sort_reverse)
        elif sort_option == 'created':
            tasks = sort_by_creation_time(tasks, sort_reverse)
        elif sort_option == 'title':
            tasks = sort_by_title(tasks, sort_reverse)

        # Display results
        if not tasks:
            print("\nNo tasks match your filters.")
        else:
            print("\nFiltered and Sorted Todo List:")
            for task in tasks:
                # Add overdue indicator if applicable
                task_str = str(task)
                if is_overdue(task):
                    task_str += " [OVERDUE]"
                print(task_str)

    def handle_complete(self):
        """Handle the complete command."""
        try:
            task_id = int(input("Enter task ID to mark as complete: "))
        except ValueError:
            print("Invalid task ID. Please enter a number.")
            return
            
        if self.todo_list.mark_task_complete(task_id, True):
            task = self.todo_list.get_task(task_id)
            print(f"Marked task as complete: {task}")
        else:
            print(f"Task with ID {task_id} not found.")

    def handle_incomplete(self):
        """Handle the incomplete command."""
        try:
            task_id = int(input("Enter task ID to mark as incomplete: "))
        except ValueError:
            print("Invalid task ID. Please enter a number.")
            return
            
        if self.todo_list.mark_task_complete(task_id, False):
            task = self.todo_list.get_task(task_id)
            print(f"Marked task as incomplete: {task}")
        else:
            print(f"Task with ID {task_id} not found.")


def main():
    """Main entry point for the application."""
    app = TodoCLI()
    app.run()


if __name__ == "__main__":
    main()