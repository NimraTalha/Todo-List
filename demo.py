#!/usr/bin/env python3
"""
Demo script to showcase the Todo CLI application functionality.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from task import Task
from todolist import TodoList

def demo():
    print("Todo CLI Application Demo")
    print("=" * 30)
    
    # Create a new todo list
    todo_list = TodoList()
    
    print("\n1. Adding tasks:")
    task1 = todo_list.add_task("Buy groceries", "Milk, bread, eggs")
    print(f"   {task1}")
    
    task2 = todo_list.add_task("Clean house", "Weekly cleaning routine")
    print(f"   {task2}")
    
    print(f"\n2. Current tasks ({len(todo_list.list_tasks())} total):")
    for task in todo_list.list_tasks():
        print(f"   {task.details()}")
    
    print("\n3. Updating a task:")
    todo_list.update_task(1, title="Buy groceries and cook", description="Get ingredients for dinner")
    updated_task = todo_list.get_task(1)
    print(f"   Updated: {updated_task}")
    
    print("\n4. Marking a task as complete:")
    todo_list.mark_complete(1)
    completed_task = todo_list.get_task(1)
    print(f"   {completed_task}")
    
    print("\n5. Deleting a task:")
    todo_list.delete_task(2)
    remaining_tasks = todo_list.list_tasks()
    print(f"   Remaining tasks: {len(remaining_tasks)}")
    for task in remaining_tasks:
        print(f"   {task}")
    
    print("\nDemo completed successfully!")

if __name__ == "__main__":
    demo()