"""
task_manager.py
Defines the TaskManager class for managing tasks.
"""

from task_manager.task import Task
from task_manager.file_manager import FileManager


class TaskManager:
    def __init__(self):
        """
        Initializes the TaskManager with an empty list of tasks.
        """
        self.tasks = []
        self.file_manager = FileManager("tasks.json")
        self.load_tasks()

    def create_task(self, task_id, task_name, task_description):
        """
        Creates a new task and adds it to the list.

        :param task_id: int, the ID of the task
        :param task_name: str, the name of the task
        :param task_description: str, the description of the task
        """
        task = Task(task_id, task_name, task_description)
        self.tasks.append(task)
        self.save_tasks()
        self.notify_user("A new task has been created!")

    def update_task(
            self,
            task_id,
            task_name=None,
            task_description=None,
            task_status=None):
        """
        Updates an existing task.

        :param task_id: int, the ID of the task
        :param task_name: str, the new name of the task (optional)
        :param task_description: str, the new description of the task (optional)
        :param task_status: str, the new status of the task (optional)
        """
        for task in self.tasks:
            if task.get_task_id() == task_id:
                if task_name is not None:
                    task.set_task_name(task_name)
                if task_description is not None:
                    task.set_task_description(task_description)
                if task_status is not None:
                    task.set_task_status(task_status)
                self.save_tasks()
                return

    def notify_user(self, message):
        """
        Notifies the user about a specific event.

        :param message: str, the notification message
        """
        print(f"Notification: {message}")

    def save_tasks(self):
        """
        Saves the tasks to a file.
        """
        tasks_data = [
            {
                "task_id": task.get_task_id(),
                "task_name": task.get_task_name(),
                "task_description": task.get_task_description(),
                "task_status": task.get_task_status(),
            }
            for task in self.tasks
        ]
        self.file_manager.save_data(tasks_data)

    def load_tasks(self):
        """
        Loads tasks from a file.
        """
        tasks_data = self.file_manager.load_data()
        self.tasks = [Task(**task_data) for task_data in tasks_data]
