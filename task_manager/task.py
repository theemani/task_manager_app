"""
task.py
Defines the Task class for the task manager application.
"""


class Task:
    def __init__(
            self,
            task_id,
            task_name,
            task_description,
            task_status="pending"):
        """
        Initializes a new task with the given attributes.

        :param task_id: int, the ID of the task
        :param task_name: str, the name of the task
        :param task_description: str, the description of the task
        :param task_status: str, the status of the task (default is "pending")
        """
        self.task_id = task_id
        self.task_name = task_name
        self.task_description = task_description
        self.task_status = task_status

    def get_task_id(self):
        return self.task_id

    def set_task_id(self, task_id):
        self.task_id = task_id

    def get_task_name(self):
        return self.task_name

    def set_task_name(self, task_name):
        self.task_name = task_name

    def get_task_description(self):
        return self.task_description

    def set_task_description(self, task_description):
        self.task_description = task_description

    def get_task_status(self):
        return self.task_status

    def set_task_status(self, task_status):
        self.task_status = task_status
