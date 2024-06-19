"""
test_task_manager.py
Unit tests for the TaskManager class.
"""

import unittest
from task_manager.task_manager import TaskManager


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.task_manager = TaskManager()
        self.task_manager.file_manager.filename = "test_tasks.json"  # Use a test file

    def tearDown(self):
        import os
        if os.path.exists("test_tasks.json"):
            os.remove("test_tasks.json")

    def test_create_task(self):
        self.task_manager.create_task(1, "Test Task", "This is a test task")
        self.assertEqual(len(self.task_manager.tasks), 1)
        task = self.task_manager.tasks[0]
        self.assertEqual(task.get_task_id(), 1)
        self.assertEqual(task.get_task_name(), "Test Task")
        self.assertEqual(task.get_task_description(), "This is a test task")

    def test_update_task(self):
        self.task_manager.create_task(1, "Test Task", "This is a test task")
        self.task_manager.update_task(
            1, "Updated Task", "Updated description", "completed")
        task = self.task_manager.tasks[0]
        self.assertEqual(task.get_task_name(), "Updated Task")
        self.assertEqual(task.get_task_description(), "Updated description")
        self.assertEqual(task.get_task_status(), "completed")

    def test_notify_user(self):
        self.task_manager.notify_user()
        # Check the output manually or mock the print function


if __name__ == "__main__":
    unittest.main()
