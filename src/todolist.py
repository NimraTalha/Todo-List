"""
Module defining the TodoList class for managing multiple tasks in the Todo CLI application.
"""
from task import Task


class TodoList:
    """
    Manages a collection of Task objects in memory.
    """
    def __init__(self):
        """
        Initialize an empty todo list.
        """
        self.tasks = []
        self.next_id = 1

    def add_task(self, title, description=""):
        """
        Add a new task to the list.
        
        Args:
            title (str): Title of the task
            description (str, optional): Description of the task. Defaults to "".
        
        Returns:
            Task: The newly created task
        """
        if not title:
            raise ValueError("Title is required")
        
        task = Task(self.next_id, title, description)
        self.tasks.append(task)
        self.next_id += 1
        return task

    def delete_task(self, task_id):
        """
        Delete a task by its ID.
        
        Args:
            task_id (int): ID of the task to delete
        
        Returns:
            bool: True if task was deleted, False if task was not found
        """
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                del self.tasks[i]
                return True
        return False

    def update_task(self, task_id, title=None, description=None):
        """
        Update a task's title or description by its ID.
        
        Args:
            task_id (int): ID of the task to update
            title (str, optional): New title for the task
            description (str, optional): New description for the task
        
        Returns:
            bool: True if task was updated, False if task was not found
        """
        for task in self.tasks:
            if task.id == task_id:
                if title is not None:
                    task.title = title
                if description is not None:
                    task.description = description
                return True
        return False

    def get_task(self, task_id):
        """
        Get a task by its ID.
        
        Args:
            task_id (int): ID of the task to retrieve
        
        Returns:
            Task or None: The task if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def list_tasks(self):
        """
        Get all tasks in the list.
        
        Returns:
            list: List of all Task objects
        """
        return self.tasks

    def mark_complete(self, task_id):
        """
        Mark a task as complete by its ID.
        
        Args:
            task_id (int): ID of the task to mark complete
        
        Returns:
            bool: True if task was marked complete, False if task was not found
        """
        task = self.get_task(task_id)
        if task:
            task.completed = True
            return True
        return False

    def mark_incomplete(self, task_id):
        """
        Mark a task as incomplete by its ID.
        
        Args:
            task_id (int): ID of the task to mark incomplete
        
        Returns:
            bool: True if task was marked incomplete, False if task was not found
        """
        task = self.get_task(task_id)
        if task:
            task.completed = False
            return True
        return False