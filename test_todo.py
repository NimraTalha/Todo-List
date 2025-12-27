#!/usr/bin/env python3
"""
Simple test script to verify the Todo CLI application functionality.
"""
import sys
import os
# Add the src directory to the path so we can import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from task import Task
from todolist import TodoList

def test_task_creation():
    """Test basic task creation"""
    print("Testing Task creation...")
    task = Task(1, "Test task", "This is a test task")
    
    assert task.id == 1
    assert task.title == "Test task"
    assert task.description == "This is a test task"
    assert task.completed == False
    
    print("PASS: Task creation works correctly")
    print(f"  Task string: {str(task)}")
    print(f"  Task details: {task.details()}")
    
def test_todolist_operations():
    """Test basic TodoList operations"""
    print("\nTesting TodoList operations...")
    todo_list = TodoList()
    
    # Test adding a task
    task = todo_list.add_task("Buy milk", "Get whole milk from the store")
    assert task.id == 1
    assert task.title == "Buy milk"
    assert task.description == "Get whole milk from the store"
    assert len(todo_list.list_tasks()) == 1
    
    print("PASS: Add task works correctly")

    # Test listing tasks
    tasks = todo_list.list_tasks()
    assert len(tasks) == 1
    assert tasks[0].id == 1

    print("PASS: List tasks works correctly")

    # Test updating a task
    success = todo_list.update_task(1, title="Buy whole milk", description="Get 2% milk from the store")
    assert success == True
    task = todo_list.get_task(1)
    assert task.title == "Buy whole milk"
    assert task.description == "Get 2% milk from the store"

    print("PASS: Update task works correctly")

    # Test marking complete/incomplete
    success = todo_list.mark_complete(1)
    assert success == True
    task = todo_list.get_task(1)
    assert task.completed == True

    print("PASS: Mark complete works correctly")

    success = todo_list.mark_incomplete(1)
    assert success == True
    task = todo_list.get_task(1)
    assert task.completed == False

    print("PASS: Mark incomplete works correctly")

    # Test deleting a task
    success = todo_list.delete_task(1)
    assert success == True
    assert len(todo_list.list_tasks()) == 0
    assert todo_list.get_task(1) is None

    print("PASS: Delete task works correctly")
    
def test_error_conditions():
    """Test error conditions"""
    print("\nTesting error conditions...")
    todo_list = TodoList()
    
    # Test adding task without title
    try:
        todo_list.add_task("")
        assert False, "Should have raised ValueError"
    except ValueError:
        print("PASS: Correctly rejects empty title")

    # Test updating non-existent task
    success = todo_list.update_task(999, title="Non-existent")
    assert success == False
    print("PASS: Correctly handles update for non-existent task")

    # Test deleting non-existent task
    success = todo_list.delete_task(999)
    assert success == False
    print("PASS: Correctly handles deletion of non-existent task")

    # Test marking complete for non-existent task
    success = todo_list.mark_complete(999)
    assert success == False
    print("PASS: Correctly handles marking complete for non-existent task")

if __name__ == "__main__":
    print("Running tests for Todo CLI application modules...\n")

    test_task_creation()
    test_todolist_operations()
    test_error_conditions()

    print("\nPASS: All tests passed! The core functionality is working correctly.")