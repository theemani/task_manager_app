"""
test_task.py
Unit tests for the Task class.
"""

import unittest
from task_manager.task import Task


class TestTask(unittest.TestCase):
    def test_task_initialization(self):
        task = Task(1, "Test Task", "This is a test task")
        self.assertEqual(task.get_task_id(), 1)
        self.assertEqual(task.get_task_name(), "Test Task")
        self.assertEqual(task.get_task_description(), "This is a test task")
        self.assertEqual(task.get_task_status(), "pending")

    def test_task_update(self):
        task = Task(1, "Test Task", "This is a test task")
        task.set_task_name("Updated Task")
        task.set_task_description("Updated description")
        task.set_task_status("completed")
        self.assertEqual(task.get_task_name(), "Updated Task")
        self.assertEqual(task.get_task_description(), "Updated description")
        self.assertEqual(task.get_task_status(), "completed")


if __name__ == "__main__":
    unittest.main()
