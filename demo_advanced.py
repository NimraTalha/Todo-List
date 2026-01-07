"""
Comprehensive Demo Script for Advanced Todo CLI Application
This script demonstrates all features of the application including the Advanced Level features.
"""
from src.todo_app import TodoList
from datetime import date, datetime
import time


def demo():
    print("=== Advanced Todo App Demo ===\n")
    
    # Create a new todo list
    todo_list = TodoList()
    
    # Demo: Add tasks with various advanced features
    print("1. Adding tasks with advanced features...")
    
    # Add a recurring daily task
    task1 = todo_list.add_task(
        "Water plants", 
        "Water the garden", 
        due_date=date(2025, 1, 1),
        priority="high", 
        tags=["home", "daily"],
        recurrence="daily"
    )
    print(f"   Added recurring task: {task1}")
    
    # Add a recurring weekly task
    task2 = todo_list.add_task(
        "Weekly team meeting", 
        "Attend the weekly team sync", 
        due_date=date(2025, 1, 5),
        due_datetime=datetime(2025, 1, 5, 10, 0),
        priority="medium", 
        tags=["work", "meeting"],
        recurrence="weekly"
    )
    print(f"   Added recurring task: {task2}")
    
    # Add a task with full datetime
    task3 = todo_list.add_task(
        "Doctor appointment", 
        "Annual checkup with Dr. Smith", 
        due_datetime=datetime(2025, 1, 10, 14, 30),
        priority="high", 
        tags=["health", "appointment"]
    )
    print(f"   Added task with datetime: {task3}")
    
    # Add a regular task
    task4 = todo_list.add_task(
        "Finish report", 
        "Complete the quarterly report", 
        due_date=date(2025, 1, 15),
        priority="high", 
        tags=["work", "urgent"]
    )
    print(f"   Added regular task: {task4}\n")
    
    # Demo: View all tasks
    print("2. Viewing all tasks...")
    for task in todo_list.get_all_tasks():
        print(f"   {task}")
    print()
    
    # Demo: Mark a recurring task as complete (this should auto-generate a new instance)
    print("3. Marking recurring task as complete (auto-respawn)...")
    print(f"   Before marking complete: {len(todo_list.get_all_tasks())} tasks")
    todo_list.mark_task_complete(task1.id, True)
    print(f"   After marking complete: {len(todo_list.get_all_tasks())} tasks")
    
    # Show the newly generated task
    for task in todo_list.get_all_tasks():
        if task.recurrence and task.id > task1.id:  # New recurring task
            print(f"   Auto-generated task: {task}")
    print()
    
    # Demo: Update a task with advanced fields
    print("4. Updating a task with advanced fields...")
    result = todo_list.update_task(
        task4.id, 
        title="Finish annual report", 
        priority="low",
        recurrence="monthly"
    )
    if result:
        updated_task = todo_list.get_task(task4.id)
        print(f"   Updated task: {updated_task}")
    print()
    
    # Demo: Search functionality
    print("5. Searching for tasks...")
    from src.todo_app import keyword_search
    search_results = keyword_search(todo_list.get_all_tasks(), "report")
    print(f"   Search results for 'report':")
    for task in search_results:
        print(f"     {task}")
    print()
    
    # Demo: Filter by status
    print("6. Filtering tasks by status...")
    from src.todo_app import filter_by_status
    completed_tasks = filter_by_status(todo_list.get_all_tasks(), "complete")
    print(f"   Completed tasks:")
    for task in completed_tasks:
        print(f"     {task}")
    print()
    
    # Demo: Filter by recurrence
    print("7. Filtering tasks by recurrence...")
    from src.todo_app import get_overdue_tasks
    recurring_tasks = [task for task in todo_list.get_all_tasks() if task.recurrence]
    print(f"   Recurring tasks:")
    for task in recurring_tasks:
        print(f"     {task}")
    print()
    
    # Demo: Sort by priority
    print("8. Sorting tasks by priority...")
    from src.todo_app import sort_by_priority
    sorted_tasks = sort_by_priority(todo_list.get_all_tasks())
    print(f"   Tasks sorted by priority (High -> Medium -> Low):")
    for task in sorted_tasks:
        print(f"     {task}")
    print()
    
    # Demo: Check overdue functionality
    print("9. Checking overdue tasks...")
    from src.todo_app import is_overdue
    for task in todo_list.get_all_tasks():
        if is_overdue(task):
            print(f"     OVERDUE: {task}")
    if not any(is_overdue(task) for task in todo_list.get_all_tasks()):
        print("     No overdue tasks")
    print()
    
    # Demo: Final task list
    print("10. Final task list...")
    for task in todo_list.get_all_tasks():
        overdue_indicator = " [OVERDUE]" if is_overdue(task) else ""
        print(f"   {task}{overdue_indicator}")
    print()
    
    print("=== Advanced Demo completed ===")


if __name__ == "__main__":
    demo()