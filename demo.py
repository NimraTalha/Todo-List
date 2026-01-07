"""
Demo script for the Todo CLI Application
This script demonstrates all the main features of the application.
"""
from src.todo_app import TodoList


def demo():
    print("=== Todo App Demo ===\n")
    
    # Create a new todo list
    todo_list = TodoList()
    
    # Demo: Add tasks
    print("1. Adding tasks...")
    task1 = todo_list.add_task("Buy groceries", "Get milk, bread, and eggs")
    task2 = todo_list.add_task("Walk the dog", "Take Fido to the park")
    task3 = todo_list.add_task("Finish report", "Complete the quarterly report")
    print(f"   Added: {task1}")
    print(f"   Added: {task2}")
    print(f"   Added: {task3}\n")
    
    # Demo: View all tasks
    print("2. Viewing all tasks...")
    for task in todo_list.get_all_tasks():
        print(f"   {task}")
    print()
    
    # Demo: Mark a task as complete
    print("3. Marking a task as complete...")
    todo_list.mark_task_complete(task1.id, True)
    print(f"   Marked task {task1.id} as complete: {task1}\n")
    
    # Demo: Update a task
    print("4. Updating a task...")
    todo_list.update_task(task2.id, "Walk the dog", "Take Fido to the park for 30 minutes")
    updated_task = todo_list.get_task(task2.id)
    print(f"   Updated task {task2.id}: {updated_task}\n")
    
    # Demo: View all tasks again to see changes
    print("5. Viewing all tasks after updates...")
    for task in todo_list.get_all_tasks():
        print(f"   {task}")
    print()
    
    # Demo: Delete a task
    print("6. Deleting a task...")
    success = todo_list.delete_task(task3.id)
    if success:
        print(f"   Deleted task with ID {task3.id}")
    else:
        print(f"   Failed to delete task with ID {task3.id}")
    
    # View final list
    print("\n7. Final task list...")
    for task in todo_list.get_all_tasks():
        print(f"   {task}")
    if not todo_list.get_all_tasks():
        print("   No tasks remaining.")
    
    print("\n=== Demo completed ===")


if __name__ == "__main__":
    demo()