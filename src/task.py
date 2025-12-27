"""
Module defining the Task class for the Todo CLI application.
"""
class Task:
    """
    Represents a single todo task with id, title, description, and completion status.
    """
    def __init__(self, task_id, title, description=""):
        """
        Initialize a new Task instance.
        
        Args:
            task_id (int): Unique identifier for the task
            title (str): Title of the task
            description (str, optional): Description of the task. Defaults to "".
        """
        self.id = task_id
        self.title = title
        self.description = description
        self.completed = False

    def __str__(self):
        """
        String representation of the task for display purposes.
        
        Returns:
            str: Formatted string showing task status, ID, and title
        """
        status = "[x]" if self.completed else "[ ]"
        return f"ID: {self.id} {status} Title: {self.title}"

    def details(self):
        """
        Detailed string representation of the task including description.
        
        Returns:
            str: Formatted string with full task details
        """
        status = "[x]" if self.completed else "[ ]"
        return f"ID: {self.id} {status} Title: {self.title}\n   Description: {self.description}"