"""
Tests for the Todo CLI Application
"""
import unittest
from src.todo_app import Task, TodoList, TodoCLI
from datetime import date


class TestTask(unittest.TestCase):
    """Test the Task class."""

    def test_task_creation(self):
        """Test creating a new task."""
        task = Task(1, "Test title", "Test description")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test title")
        self.assertEqual(task.description, "Test description")
        self.assertFalse(task.completed)
        self.assertIsNone(task.due_date)
        self.assertEqual(task.priority, "medium")
        self.assertEqual(task.tags, [])

    def test_task_str_representation(self):
        """Test string representation of a task."""
        task = Task(1, "Test title", "Test description")
        self.assertEqual(str(task), "[ ] 1. [M] Test title - Test description (Due: -, Tags: none)")

        task.completed = True
        self.assertEqual(str(task), "[x] 1. [M] Test title - Test description (Due: -, Tags: none)")

    def test_task_creation_with_new_fields(self):
        """Test creating a task with new fields."""
        due_date = date(2025, 12, 31)
        task = Task(1, "Test title", "Test description", due_date, "high", ["work", "urgent"])
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test title")
        self.assertEqual(task.description, "Test description")
        self.assertFalse(task.completed)
        self.assertEqual(task.due_date, due_date)
        self.assertEqual(task.priority, "high")
        self.assertEqual(task.tags, ["work", "urgent"])


class TestTodoList(unittest.TestCase):
    """Test the TodoList class."""

    def setUp(self):
        """Set up a fresh TodoList for each test."""
        self.todo_list = TodoList()

    def test_add_task(self):
        """Test adding a new task."""
        task = self.todo_list.add_task("Test title", "Test description")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test title")
        self.assertEqual(task.description, "Test description")
        self.assertFalse(task.completed)
        self.assertIsNone(task.due_date)
        self.assertEqual(task.priority, "medium")
        self.assertEqual(task.tags, [])
        self.assertEqual(len(self.todo_list.get_all_tasks()), 1)

    def test_add_task_without_description(self):
        """Test adding a task without description."""
        task = self.todo_list.add_task("Test title")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test title")
        self.assertEqual(task.description, "")
        self.assertFalse(task.completed)
        self.assertIsNone(task.due_date)
        self.assertEqual(task.priority, "medium")
        self.assertEqual(task.tags, [])
        
    def test_delete_task(self):
        """Test deleting a task."""
        task = self.todo_list.add_task("Test title", "Test description")
        self.assertEqual(len(self.todo_list.get_all_tasks()), 1)
        
        result = self.todo_list.delete_task(task.id)
        self.assertTrue(result)
        self.assertEqual(len(self.todo_list.get_all_tasks()), 0)
        
    def test_delete_nonexistent_task(self):
        """Test deleting a task that doesn't exist."""
        result = self.todo_list.delete_task(999)
        self.assertFalse(result)
        
    def test_update_task(self):
        """Test updating a task."""
        task = self.todo_list.add_task("Original title", "Original description")

        result = self.todo_list.update_task(task.id, "New title", "New description")
        self.assertTrue(result)

        updated_task = self.todo_list.get_task(task.id)
        self.assertEqual(updated_task.title, "New title")
        self.assertEqual(updated_task.description, "New description")

    def test_update_task_partial(self):
        """Test updating only title or description."""
        task = self.todo_list.add_task("Original title", "Original description")

        # Update only title
        result = self.todo_list.update_task(task.id, title="New title")
        self.assertTrue(result)

        updated_task = self.todo_list.get_task(task.id)
        self.assertEqual(updated_task.title, "New title")
        self.assertEqual(updated_task.description, "Original description")

        # Update only description
        result = self.todo_list.update_task(task.id, description="Newer description")
        self.assertTrue(result)

        updated_task = self.todo_list.get_task(task.id)
        self.assertEqual(updated_task.title, "New title")
        self.assertEqual(updated_task.description, "Newer description")

    def test_update_task_with_new_fields(self):
        """Test updating a task with new fields (due_date, priority, tags)."""
        task = self.todo_list.add_task("Original title", "Original description")

        # Verify initial values
        self.assertIsNone(task.due_date)
        self.assertEqual(task.priority, "medium")
        self.assertEqual(task.tags, [])

        # Update with new fields
        from datetime import date
        new_due_date = date(2025, 12, 31)
        result = self.todo_list.update_task(
            task.id,
            due_date=new_due_date,
            priority="high",
            tags=["work", "urgent"]
        )
        self.assertTrue(result)

        updated_task = self.todo_list.get_task(task.id)
        self.assertEqual(updated_task.due_date, new_due_date)
        self.assertEqual(updated_task.priority, "high")
        self.assertEqual(updated_task.tags, ["work", "urgent"])

    def test_update_task_mixed_fields(self):
        """Test updating a mix of old and new fields."""
        task = self.todo_list.add_task("Original title", "Original description")

        # Update with mix of old and new fields
        from datetime import date
        new_due_date = date(2025, 12, 31)
        result = self.todo_list.update_task(
            task.id,
            title="New title",
            due_date=new_due_date,
            priority="low"
        )
        self.assertTrue(result)

        updated_task = self.todo_list.get_task(task.id)
        self.assertEqual(updated_task.title, "New title")
        self.assertEqual(updated_task.due_date, new_due_date)
        self.assertEqual(updated_task.priority, "low")
        self.assertEqual(updated_task.tags, [])  # Should remain unchanged
        
    def test_update_nonexistent_task(self):
        """Test updating a task that doesn't exist."""
        result = self.todo_list.update_task(999, "New title")
        self.assertFalse(result)
        
    def test_get_task(self):
        """Test getting a specific task."""
        task = self.todo_list.add_task("Test title", "Test description")
        
        retrieved = self.todo_list.get_task(task.id)
        self.assertEqual(retrieved.id, task.id)
        self.assertEqual(retrieved.title, task.title)
        self.assertEqual(retrieved.description, task.description)
        self.assertEqual(retrieved.completed, task.completed)
        
    def test_get_nonexistent_task(self):
        """Test getting a task that doesn't exist."""
        retrieved = self.todo_list.get_task(999)
        self.assertIsNone(retrieved)
        
    def test_get_all_tasks(self):
        """Test getting all tasks."""
        task1 = self.todo_list.add_task("Title 1", "Description 1")
        task2 = self.todo_list.add_task("Title 2", "Description 2")
        
        all_tasks = self.todo_list.get_all_tasks()
        self.assertEqual(len(all_tasks), 2)
        self.assertIn(task1, all_tasks)
        self.assertIn(task2, all_tasks)
        
    def test_mark_task_complete(self):
        """Test marking a task as complete."""
        task = self.todo_list.add_task("Test title", "Test description")
        self.assertFalse(task.completed)
        
        result = self.todo_list.mark_task_complete(task.id, True)
        self.assertTrue(result)
        
        updated_task = self.todo_list.get_task(task.id)
        self.assertTrue(updated_task.completed)
        
    def test_mark_task_incomplete(self):
        """Test marking a task as incomplete."""
        task = self.todo_list.add_task("Test title", "Test description")
        task.completed = True
        self.assertTrue(task.completed)
        
        result = self.todo_list.mark_task_complete(task.id, False)
        self.assertTrue(result)
        
        updated_task = self.todo_list.get_task(task.id)
        self.assertFalse(updated_task.completed)
        
    def test_mark_nonexistent_task(self):
        """Test marking a task that doesn't exist."""
        result = self.todo_list.mark_task_complete(999, True)
        self.assertFalse(result)


class TestTodoCLI(unittest.TestCase):
    """Test the TodoCLI class."""
    
    def setUp(self):
        """Set up a fresh TodoCLI for each test."""
        self.cli = TodoCLI()
    
    def test_initial_state(self):
        """Test the initial state of the CLI."""
        self.assertIsNotNone(self.cli.todo_list)
        self.assertEqual(len(self.cli.todo_list.get_all_tasks()), 0)


    def test_validate_date_format(self):
        """Test the validate_date_format function."""
        from src.todo_app import validate_date_format

        # Valid dates
        self.assertTrue(validate_date_format("2025-12-31"))
        self.assertTrue(validate_date_format("2023-02-28"))  # Valid date
        self.assertTrue(validate_date_format("2024-02-29"))  # Leap year

        # Invalid dates
        self.assertFalse(validate_date_format("2023-02-29"))  # Invalid date
        self.assertFalse(validate_date_format("2023-04-31"))  # Invalid date
        self.assertFalse(validate_date_format("2023-13-01"))  # Invalid month

        # Invalid formats
        self.assertFalse(validate_date_format("2025/12/31"))
        self.assertFalse(validate_date_format("31-12-2025"))
        self.assertFalse(validate_date_format("2025-1-1"))
        self.assertFalse(validate_date_format("25-12-31"))
        self.assertFalse(validate_date_format("invalid"))
        self.assertFalse(validate_date_format(""))


class TestTodoCLI(unittest.TestCase):
    """Test the TodoCLI class."""

    def setUp(self):
        """Set up a fresh TodoCLI for each test."""
        self.cli = TodoCLI()

    def test_initial_state(self):
        """Test the initial state of the CLI."""
        self.assertIsNotNone(self.cli.todo_list)
        self.assertEqual(len(self.cli.todo_list.get_all_tasks()), 0)


class TestTodoListExtended(unittest.TestCase):
    """Extended tests for the TodoList class."""

    def setUp(self):
        """Set up a fresh TodoList for each test."""
        self.todo_list = TodoList()

    def test_add_task_with_invalid_due_date_type(self):
        """Test adding a task with an invalid due date type raises an error."""
        # This test verifies that the add_task method validates due date type properly
        with self.assertRaises(ValueError):
            self.todo_list.add_task("Test title", "Test description", due_date="not_a_date_object")  # Invalid type

    def test_validate_priority(self):
        """Test the validate_priority function."""
        from src.todo_app import validate_priority

        # Valid priorities (case insensitive)
        self.assertTrue(validate_priority("high"))
        self.assertTrue(validate_priority("medium"))
        self.assertTrue(validate_priority("low"))
        self.assertTrue(validate_priority("HIGH"))
        self.assertTrue(validate_priority("Medium"))
        self.assertTrue(validate_priority("lOw"))

        # Invalid priorities
        self.assertFalse(validate_priority("urgent"))
        self.assertFalse(validate_priority("critical"))
        self.assertFalse(validate_priority(""))
        self.assertFalse(validate_priority("HIGH1"))
        self.assertFalse(validate_priority("HIGH MEDIUM"))

    def test_parse_tags_from_string(self):
        """Test the parse_tags_from_string function."""
        from src.todo_app import parse_tags_from_string

        # Normal case
        self.assertEqual(parse_tags_from_string("work,home,urgent"), ["work", "home", "urgent"])

        # With spaces
        self.assertEqual(parse_tags_from_string(" work , home , urgent "), ["work", "home", "urgent"])

        # Single tag
        self.assertEqual(parse_tags_from_string("work"), ["work"])

        # Empty string
        self.assertEqual(parse_tags_from_string(""), [])

        # With mixed case (should convert to lowercase)
        self.assertEqual(parse_tags_from_string("Work,HoMe,Urgent"), ["work", "home", "urgent"])

        # Empty tags in between
        self.assertEqual(parse_tags_from_string("work,,urgent"), ["work", "urgent"])

        # Only commas and spaces
        self.assertEqual(parse_tags_from_string(" , , "), [])

    def test_add_task_with_priority_and_tags(self):
        """Test adding a task with priority and tags."""
        task = self.todo_list.add_task("Test title", "Test description", priority="high", tags=["work", "urgent"])

        self.assertEqual(task.priority, "high")
        self.assertEqual(task.tags, ["work", "urgent"])

    def test_add_task_invalid_priority(self):
        """Test adding a task with invalid priority raises an error."""
        with self.assertRaises(ValueError):
            self.todo_list.add_task("Test title", "Test description", priority="invalid_priority")

    def test_update_task_with_priority_and_tags(self):
        """Test updating a task with priority and tags."""
        task = self.todo_list.add_task("Test title", "Test description")

        # Verify initial values
        self.assertEqual(task.priority, "medium")
        self.assertEqual(task.tags, [])

        # Update with new priority and tags
        result = self.todo_list.update_task(task.id, priority="high", tags=["work", "important"])
        self.assertTrue(result)

        updated_task = self.todo_list.get_task(task.id)
        self.assertEqual(updated_task.priority, "high")
        self.assertEqual(updated_task.tags, ["work", "important"])

    def test_update_task_invalid_priority(self):
        """Test updating a task with invalid priority raises an error."""
        task = self.todo_list.add_task("Test title", "Test description")

        with self.assertRaises(ValueError):
            self.todo_list.update_task(task.id, priority="invalid_priority")

    def test_keyword_search(self):
        """Test the keyword_search function."""
        from src.todo_app import keyword_search
        from datetime import date

        # Add some tasks
        task1 = self.todo_list.add_task("Buy groceries", "Get milk and bread", priority="high")
        task2 = self.todo_list.add_task("Walk the dog", "Take Fido to the park", priority="medium")
        task3 = self.todo_list.add_task("Finish report", "Complete quarterly report", priority="low",
                                        tags=["work", "urgent"])

        # Test searching in title
        results = keyword_search(self.todo_list.get_all_tasks(), "groceries")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].id, task1.id)

        # Test searching in description
        results = keyword_search(self.todo_list.get_all_tasks(), "park")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].id, task2.id)

        # Test case-insensitive search
        results = keyword_search(self.todo_list.get_all_tasks(), "GROCERIES")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].id, task1.id)

        # Test search with no matches
        results = keyword_search(self.todo_list.get_all_tasks(), "nonexistent")
        self.assertEqual(len(results), 0)

        # Test empty keyword
        results = keyword_search(self.todo_list.get_all_tasks(), "")
        self.assertEqual(len(results), 0)

    def test_filter_by_status(self):
        """Test the filter_by_status function."""
        from src.todo_app import filter_by_status

        # Add some tasks
        task1 = self.todo_list.add_task("Task 1", "Description 1")
        task2 = self.todo_list.add_task("Task 2", "Description 2")

        # Mark one task as complete
        self.todo_list.mark_task_complete(task1.id)

        # Test filtering for complete tasks
        results = filter_by_status(self.todo_list.get_all_tasks(), "complete")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].id, task1.id)

        # Test filtering for incomplete tasks
        results = filter_by_status(self.todo_list.get_all_tasks(), "incomplete")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].id, task2.id)

        # Test case-insensitive filtering
        results = filter_by_status(self.todo_list.get_all_tasks(), "COMPLETE")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].id, task1.id)

        # Test invalid status
        results = filter_by_status(self.todo_list.get_all_tasks(), "invalid")
        self.assertEqual(len(results), 0)

    def test_filter_by_priority(self):
        """Test the filter_by_priority function."""
        from src.todo_app import filter_by_priority

        # Add some tasks with different priorities
        task1 = self.todo_list.add_task("Task 1", "Description 1", priority="high")
        task2 = self.todo_list.add_task("Task 2", "Description 2", priority="medium")
        task3 = self.todo_list.add_task("Task 3", "Description 3", priority="low")

        # Test filtering for high priority
        results = filter_by_priority(self.todo_list.get_all_tasks(), "high")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].id, task1.id)

        # Test filtering for medium priority
        results = filter_by_priority(self.todo_list.get_all_tasks(), "medium")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].id, task2.id)

        # Test case-insensitive filtering
        results = filter_by_priority(self.todo_list.get_all_tasks(), "HIGH")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].id, task1.id)

        # Test invalid priority
        results = filter_by_priority(self.todo_list.get_all_tasks(), "invalid")
        self.assertEqual(len(results), 0)

    def test_filter_by_due_date(self):
        """Test the filter_by_due_date function."""
        from src.todo_app import filter_by_due_date
        from datetime import date, timedelta

        # Add some tasks with different due dates
        today = date.today()
        tomorrow = today + timedelta(days=1)
        next_week = today + timedelta(days=7)
        last_week = today - timedelta(days=7)

        task1 = self.todo_list.add_task("Task 1", "Description 1", due_date=today)
        task2 = self.todo_list.add_task("Task 2", "Description 2", due_date=tomorrow)
        task3 = self.todo_list.add_task("Task 3", "Description 3", due_date=last_week)
        task4 = self.todo_list.add_task("Task 4", "Description 4")  # No due date

        # Test filtering for tasks due 'on' a specific date
        results = filter_by_due_date(self.todo_list.get_all_tasks(), f"on:{today.strftime('%Y-%m-%d')}")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].id, task1.id)

        # Test filtering for tasks due 'after' a specific date
        results = filter_by_due_date(self.todo_list.get_all_tasks(), f"after:{last_week.strftime('%Y-%m-%d')}")
        self.assertEqual(len(results), 2)  # task1 (today) and task2 (tomorrow)

        # Test filtering for tasks due 'before' a specific date
        results = filter_by_due_date(self.todo_list.get_all_tasks(), f"before:{next_week.strftime('%Y-%m-%d')}")
        # This should include task3 (last week), task1 (today), and task2 (tomorrow)
        self.assertEqual(len(results), 3)

        # Test invalid date format
        results = filter_by_due_date(self.todo_list.get_all_tasks(), "on:invalid-date")
        self.assertEqual(len(results), 0)

        # Test invalid filter type
        results = filter_by_due_date(self.todo_list.get_all_tasks(), f"invalid:{today.strftime('%Y-%m-%d')}")
        self.assertEqual(len(results), 0)


    def test_sort_by_priority(self):
        """Test the sort_by_priority function."""
        from src.todo_app import sort_by_priority
        from datetime import datetime

        # Add tasks with different priorities
        task1 = self.todo_list.add_task("Task 1", "Description 1", priority="low")
        task2 = self.todo_list.add_task("Task 2", "Description 2", priority="high")
        task3 = self.todo_list.add_task("Task 3", "Description 3", priority="medium")

        # Sort by priority (default: high to low)
        sorted_tasks = sort_by_priority(self.todo_list.get_all_tasks())

        # Check that high priority comes first
        self.assertEqual(sorted_tasks[0].id, task2.id)  # high priority
        self.assertEqual(sorted_tasks[1].id, task3.id)  # medium priority
        self.assertEqual(sorted_tasks[2].id, task1.id)  # low priority)

        # Test reverse sorting (low to high)
        sorted_tasks_reverse = sort_by_priority(self.todo_list.get_all_tasks(), reverse=True)
        self.assertEqual(sorted_tasks_reverse[0].id, task1.id)  # low priority
        self.assertEqual(sorted_tasks_reverse[1].id, task3.id)  # medium priority
        self.assertEqual(sorted_tasks_reverse[2].id, task2.id)  # high priority

    def test_sort_by_due_date(self):
        """Test the sort_by_due_date function."""
        from src.todo_app import sort_by_due_date
        from datetime import date, timedelta

        # Add tasks with different due dates
        today = date.today()
        tomorrow = today + timedelta(days=1)
        next_week = today + timedelta(days=7)

        task1 = self.todo_list.add_task("Task 1", "Description 1", due_date=tomorrow)
        task2 = self.todo_list.add_task("Task 2", "Description 2", due_date=next_week)  # Later date
        task3 = self.todo_list.add_task("Task 3", "Description 3", due_date=today)     # Earlier date
        task4 = self.todo_list.add_task("Task 4", "Description 4")  # No due date

        # Sort by due date (earliest first)
        sorted_tasks = sort_by_due_date(self.todo_list.get_all_tasks())

        # Check that tasks are sorted by due date, with no-due-date task at the end
        self.assertEqual(sorted_tasks[0].id, task3.id)  # today (earliest)
        self.assertEqual(sorted_tasks[1].id, task1.id)  # tomorrow
        self.assertEqual(sorted_tasks[2].id, task2.id)  # next week
        self.assertEqual(sorted_tasks[3].id, task4.id)  # no due date (last)

        # Test reverse sorting (latest first)
        sorted_tasks_reverse = sort_by_due_date(self.todo_list.get_all_tasks(), reverse=True)
        self.assertEqual(sorted_tasks_reverse[0].id, task2.id)  # next week (latest)
        self.assertEqual(sorted_tasks_reverse[1].id, task1.id)  # tomorrow
        self.assertEqual(sorted_tasks_reverse[2].id, task3.id)  # today
        self.assertEqual(sorted_tasks_reverse[3].id, task4.id)  # no due date (last)

    def test_sort_by_creation_time(self):
        """Test the sort_by_creation_time function."""
        from src.todo_app import sort_by_creation_time
        from datetime import datetime, timedelta

        # Add tasks (they will have different creation times)
        task1 = self.todo_list.add_task("Task 1", "Description 1")
        task2 = self.todo_list.add_task("Task 2", "Description 2")
        task3 = self.todo_list.add_task("Task 3", "Description 3")

        # Sort by creation time (newest first)
        sorted_tasks = sort_by_creation_time(self.todo_list.get_all_tasks(), reverse=True)

        # Check that the most recently created task comes first
        self.assertEqual(sorted_tasks[0].id, task3.id)  # Most recent
        self.assertEqual(sorted_tasks[1].id, task2.id)  # Middle
        self.assertEqual(sorted_tasks[2].id, task1.id)  # Oldest

        # Test reverse sorting (oldest first)
        sorted_tasks_reverse = sort_by_creation_time(self.todo_list.get_all_tasks(), reverse=False)
        self.assertEqual(sorted_tasks_reverse[0].id, task1.id)  # Oldest
        self.assertEqual(sorted_tasks_reverse[1].id, task2.id)  # Middle
        self.assertEqual(sorted_tasks_reverse[2].id, task3.id)  # Most recent

    def test_sort_by_title(self):
        """Test the sort_by_title function."""
        from src.todo_app import sort_by_title

        # Add tasks with titles that will sort alphabetically
        task1 = self.todo_list.add_task("Zebra Task", "Description 1")
        task2 = self.todo_list.add_task("Apple Task", "Description 2")
        task3 = self.todo_list.add_task("Mango Task", "Description 3")

        # Sort by title (alphabetical)
        sorted_tasks = sort_by_title(self.todo_list.get_all_tasks())

        # Check that tasks are sorted alphabetically by title
        self.assertEqual(sorted_tasks[0].id, task2.id)  # "Apple Task" (first alphabetically)
        self.assertEqual(sorted_tasks[1].id, task3.id)  # "Mango Task" (middle)
        self.assertEqual(sorted_tasks[2].id, task1.id)  # "Zebra Task" (last alphabetically)

        # Test reverse sorting (Z to A)
        sorted_tasks_reverse = sort_by_title(self.todo_list.get_all_tasks(), reverse=True)
        self.assertEqual(sorted_tasks_reverse[0].id, task1.id)  # "Zebra Task" (last alphabetically)
        self.assertEqual(sorted_tasks_reverse[1].id, task3.id)  # "Mango Task" (middle)
        self.assertEqual(sorted_tasks_reverse[2].id, task2.id)  # "Apple Task" (first alphabetically)

    def test_task_creation_with_new_advanced_fields(self):
        """Test creating a task with new advanced fields (due_datetime, recurrence)."""
        from datetime import datetime
        from src.todo_app import validate_recurrence

        # Test creating a task with due_datetime and recurrence
        due_dt = datetime(2025, 12, 31, 14, 30)
        task = self.todo_list.add_task(
            "Test task",
            "Test description",
            due_datetime=due_dt,
            recurrence="weekly"
        )

        self.assertEqual(task.title, "Test task")
        self.assertEqual(task.description, "Test description")
        self.assertEqual(task.due_datetime, due_dt)
        self.assertEqual(task.recurrence, "weekly")

        # Verify recurrence validation
        self.assertTrue(validate_recurrence("daily"))
        self.assertTrue(validate_recurrence("weekly"))
        self.assertTrue(validate_recurrence("monthly"))
        self.assertFalse(validate_recurrence("yearly"))

    def test_task_str_representation_with_new_fields(self):
        """Test string representation of a task with new fields."""
        from datetime import date, datetime
        from src.todo_app import Task

        # Test with due_datetime
        due_dt = datetime(2025, 12, 31, 14, 30)
        task = Task(1, "Test title", "Test description", due_date=date(2025, 12, 31),
                   due_datetime=due_dt, recurrence="weekly")
        expected_str = "[ ] 1. [M] [R:weekly] Test title - Test description (Due: 2025-12-31 14:30, Tags: none)"
        self.assertEqual(str(task), expected_str)

        # Test with recurrence but no due_datetime
        task2 = Task(2, "Test title 2", "Test description 2", due_date=date(2025, 12, 31),
                    recurrence="daily")
        expected_str2 = "[ ] 2. [M] [R:daily] Test title 2 - Test description 2 (Due: 2025-12-31, Tags: none)"
        self.assertEqual(str(task2), expected_str2)

        # Test with no recurrence
        task3 = Task(3, "Test title 3", "Test description 3", due_date=date(2025, 12, 31))
        expected_str3 = "[ ] 3. [M] Test title 3 - Test description 3 (Due: 2025-12-31, Tags: none)"
        self.assertEqual(str(task3), expected_str3)

    def test_add_task_with_advanced_fields(self):
        """Test adding a task with advanced fields."""
        from datetime import datetime
        from src.todo_app import validate_recurrence

        due_dt = datetime(2025, 12, 31, 14, 30)
        task = self.todo_list.add_task(
            "Advanced task",
            "Advanced description",
            due_date=date(2025, 12, 31),
            due_datetime=due_dt,
            recurrence="monthly"
        )

        self.assertEqual(task.title, "Advanced task")
        self.assertEqual(task.description, "Advanced description")
        self.assertEqual(task.due_date, date(2025, 12, 31))
        self.assertEqual(task.due_datetime, due_dt)
        self.assertEqual(task.recurrence, "monthly")

    def test_update_task_with_advanced_fields(self):
        """Test updating a task with advanced fields."""
        from datetime import datetime
        from src.todo_app import validate_recurrence

        # Add a basic task
        task = self.todo_list.add_task("Basic task", "Basic description")

        # Update with advanced fields
        due_dt = datetime(2025, 12, 31, 14, 30)
        result = self.todo_list.update_task(
            task.id,
            due_datetime=due_dt,
            recurrence="weekly"
        )

        self.assertTrue(result)
        updated_task = self.todo_list.get_task(task.id)
        self.assertEqual(updated_task.due_datetime, due_dt)
        self.assertEqual(updated_task.recurrence, "weekly")

    def test_validate_datetime_format(self):
        """Test the validate_datetime_format function."""
        from src.todo_app import validate_datetime_format

        # Valid datetime formats
        self.assertTrue(validate_datetime_format("2025-12-31 14:30"))
        self.assertTrue(validate_datetime_format("2023-02-28 09:15"))

        # Invalid datetime formats
        self.assertFalse(validate_datetime_format("2025/12/31 14:30"))
        self.assertFalse(validate_datetime_format("31-12-2025 14:30"))
        self.assertFalse(validate_datetime_format("2025-1-1 14:30"))
        self.assertFalse(validate_datetime_format("2025-12-31 4:30"))
        self.assertFalse(validate_datetime_format("2025-12-31 14:3"))
        self.assertFalse(validate_datetime_format("2025-13-01 14:30"))  # Invalid month
        self.assertFalse(validate_datetime_format("2025-12-32 14:30"))  # Invalid day
        self.assertFalse(validate_datetime_format("2025-12-31"))  # Missing time
        self.assertFalse(validate_datetime_format("2025-12-31 25:00"))  # Invalid hour
        self.assertFalse(validate_datetime_format("2025-12-31 14:60"))  # Invalid minute
        self.assertFalse(validate_datetime_format(""))

    def test_validate_recurrence(self):
        """Test the validate_recurrence function."""
        from src.todo_app import validate_recurrence

        # Valid recurrence values (case insensitive)
        self.assertTrue(validate_recurrence("daily"))
        self.assertTrue(validate_recurrence("weekly"))
        self.assertTrue(validate_recurrence("monthly"))
        self.assertTrue(validate_recurrence("DAILY"))
        self.assertTrue(validate_recurrence("Weekly"))
        self.assertTrue(validate_recurrence("mOnThLy"))

        # Invalid recurrence values
        self.assertFalse(validate_recurrence("yearly"))
        self.assertFalse(validate_recurrence("fortnightly"))
        self.assertFalse(validate_recurrence(""))
        self.assertFalse(validate_recurrence("daily1"))
        self.assertFalse(validate_recurrence("daily weekly"))

    def test_advance_date_by_recurrence_interval(self):
        """Test the advance_date_by_recurrence_interval function."""
        from src.todo_app import advance_date_by_recurrence_interval
        from datetime import date

        # Test daily recurrence
        original_date = date(2025, 1, 1)
        advanced_daily = advance_date_by_recurrence_interval(original_date, "daily")
        expected_daily = date(2025, 1, 2)
        self.assertEqual(advanced_daily, expected_daily)

        # Test weekly recurrence
        advanced_weekly = advance_date_by_recurrence_interval(original_date, "weekly")
        expected_weekly = date(2025, 1, 8)
        self.assertEqual(advanced_weekly, expected_weekly)

        # Test monthly recurrence
        advanced_monthly = advance_date_by_recurrence_interval(original_date, "monthly")
        expected_monthly = date(2025, 2, 1)  # Should advance to February 1st
        self.assertEqual(advanced_monthly, expected_monthly)

        # Test monthly recurrence with month-end date (edge case)
        month_end_date = date(2025, 1, 31)
        advanced_monthly_end = advance_date_by_recurrence_interval(month_end_date, "monthly")
        # Since February doesn't have 31 days, it should go to the last day of February
        expected_monthly_end = date(2025, 2, 28)  # February 28th (not leap year)
        self.assertEqual(advanced_monthly_end, expected_monthly_end)

        # Test invalid recurrence
        same_date = advance_date_by_recurrence_interval(original_date, "invalid")
        self.assertEqual(same_date, original_date)

    def test_recurring_task_auto_respawn(self):
        """Test that marking a recurring task complete creates a new instance."""
        from datetime import date
        from src.todo_app import advance_date_by_recurrence_interval

        # Add a recurring task
        original_task = self.todo_list.add_task(
            "Water plants",
            "Water the garden",
            due_date=date(2025, 1, 1),
            recurrence="daily",
            priority="medium",
            tags=["home", "daily"]
        )

        # Verify initial state
        all_tasks = self.todo_list.get_all_tasks()
        self.assertEqual(len(all_tasks), 1)
        self.assertEqual(all_tasks[0].recurrence, "daily")

        # Mark the task as complete
        result = self.todo_list.mark_task_complete(original_task.id, True)
        self.assertTrue(result)

        # Verify that a new task was created
        all_tasks_after = self.todo_list.get_all_tasks()
        self.assertEqual(len(all_tasks_after), 2)

        # Find the new task (should have a different ID)
        new_task = None
        for task in all_tasks_after:
            if task.id != original_task.id:
                new_task = task
                break

        self.assertIsNotNone(new_task)
        self.assertEqual(new_task.title, original_task.title)
        self.assertEqual(new_task.description, original_task.description)
        self.assertEqual(new_task.priority, original_task.priority)
        self.assertEqual(new_task.tags, original_task.tags)
        self.assertEqual(new_task.recurrence, original_task.recurrence)

        # Check that the due date was advanced correctly
        expected_new_due_date = advance_date_by_recurrence_interval(original_task.due_date, "daily")
        self.assertEqual(new_task.due_date, expected_new_due_date)

        # Verify the original task is marked as complete
        original_task_after = self.todo_list.get_task(original_task.id)
        self.assertTrue(original_task_after.completed)

    def test_non_recurring_task_no_respawn(self):
        """Test that marking a non-recurring task complete does not create a new instance."""
        from datetime import date

        # Add a non-recurring task
        original_task = self.todo_list.add_task(
            "Buy groceries",
            "Get milk and bread",
            due_date=date(2025, 1, 1),
            recurrence=None,
            priority="high"
        )

        # Verify initial state
        all_tasks = self.todo_list.get_all_tasks()
        self.assertEqual(len(all_tasks), 1)

        # Mark the task as complete
        result = self.todo_list.mark_task_complete(original_task.id, True)
        self.assertTrue(result)

        # Verify that no new task was created
        all_tasks_after = self.todo_list.get_all_tasks()
        self.assertEqual(len(all_tasks_after), 1)

        # Verify the original task is marked as complete
        original_task_after = self.todo_list.get_task(original_task.id)
        self.assertTrue(original_task_after.completed)


if __name__ == '__main__':
    unittest.main()