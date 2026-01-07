"""
Demo script for the Todo CLI Application - Intermediate Level Features
This script demonstrates all the main features of the application including the new Intermediate Level features.
"""
from src.todo_app import TodoList
from datetime import date


def demo():
    print("=== Todo App Demo - Intermediate Level Features ===\n")
    
    # Create a new todo list
    todo_list = TodoList()
    
    # Demo: Add tasks with various features
    print("1. Adding tasks with new features (due dates, priorities, tags)...")
    task1 = todo_list.add_task("Buy groceries", "Get milk, bread, and eggs", 
                               due_date=date(2025, 1, 15), priority="medium", tags=["home", "shopping"])
    task2 = todo_list.add_task("Walk the dog", "Take Fido to the park", 
                               due_date=date(2025, 1, 10), priority="high", tags=["personal", "pet"])
    task3 = todo_list.add_task("Finish report", "Complete the quarterly report", 
                               due_date=date(2025, 1, 20), priority="high", tags=["work", "urgent"])
    task4 = todo_list.add_task("Call mom", "Wish her happy birthday", 
                               due_date=date(2025, 1, 5), priority="low", tags=["family"])
    print(f"   Added: {task1}")
    print(f"   Added: {task2}")
    print(f"   Added: {task3}")
    print(f"   Added: {task4}\n")
    
    # Demo: View all tasks
    print("2. Viewing all tasks...")
    for task in todo_list.get_all_tasks():
        print(f"   {task}")
    print()
    
    # Demo: Mark a task as complete
    print("3. Marking a task as complete...")
    todo_list.mark_task_complete(task1.id, True)
    print(f"   Marked task {task1.id} as complete: {task1}\n")
    
    # Demo: Update a task with new features
    print("4. Updating a task with new features...")
    todo_list.update_task(task2.id, description="Take Fido to the park for 30 minutes", 
                         priority="medium", tags=["personal", "pet", "exercise"])
    updated_task = todo_list.get_task(task2.id)
    print(f"   Updated task {task2.id}: {updated_task}\n")
    
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
    
    # Demo: Filter by priority
    print("7. Filtering tasks by priority...")
    from src.todo_app import filter_by_priority
    high_priority_tasks = filter_by_priority(todo_list.get_all_tasks(), "high")
    print(f"   High priority tasks:")
    for task in high_priority_tasks:
        print(f"     {task}")
    print()
    
    # Demo: Filter by due date
    print("8. Filtering tasks by due date...")
    from src.todo_app import filter_by_due_date
    due_before = filter_by_due_date(todo_list.get_all_tasks(), f"before:{date(2025, 1, 12).strftime('%Y-%m-%d')}")
    print(f"   Tasks due before {date(2025, 1, 12).strftime('%Y-%m-%d')}:")
    for task in due_before:
        print(f"     {task}")
    print()
    
    # Demo: Sort by priority
    print("9. Sorting tasks by priority...")
    from src.todo_app import sort_by_priority
    sorted_by_priority = sort_by_priority(todo_list.get_all_tasks())
    print(f"   Tasks sorted by priority (High -> Medium -> Low):")
    for task in sorted_by_priority:
        print(f"     {task}")
    print()
    
    # Demo: Sort by due date
    print("10. Sorting tasks by due date...")
    from src.todo_app import sort_by_due_date
    sorted_by_due_date = sort_by_due_date(todo_list.get_all_tasks())
    print(f"   Tasks sorted by due date (earliest first):")
    for task in sorted_by_due_date:
        print(f"     {task}")
    print()
    
    # Demo: Sort by title
    print("11. Sorting tasks by title...")
    from src.todo_app import sort_by_title
    sorted_by_title = sort_by_title(todo_list.get_all_tasks())
    print(f"   Tasks sorted alphabetically by title:")
    for task in sorted_by_title:
        print(f"     {task}")
    print()
    
    # Demo: Complex filtering and sorting combined
    print("12. Combining filters and sorts...")
    # First filter by priority, then sort by due date
    high_priority_tasks = filter_by_priority(todo_list.get_all_tasks(), "high")
    sorted_high_priority = sort_by_due_date(high_priority_tasks)
    print(f"   High priority tasks sorted by due date:")
    for task in sorted_high_priority:
        print(f"     {task}")
    print()
    
    print("=== Demo completed ===")


if __name__ == "__main__":
    demo()