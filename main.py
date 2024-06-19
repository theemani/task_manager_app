"""
main.py
A script to demonstrate how to use the TaskManager class.
"""

from task_manager.task_manager import TaskManager


def main():
    task_manager = TaskManager()

    # Create a new task
    task_manager.create_task(1, "New Task", "Description of the new task")

    # Retrieve and print task details
    task = task_manager.tasks[0]
    print(f"Task Created: {task.get_task_name()
                           } - {task.get_task_description()}")

    # Update the task
    task_manager.update_task(1, task_status="completed")

    # Retrieve and print updated task details
    updated_task = task_manager.tasks[0]
    print(f"Task Updated: {updated_task.get_task_name(
    )} - {updated_task.get_task_description()} - Status: {updated_task.get_task_status()}")

    # Notify user with a specific message
    task_manager.notify_user("Task has been updated!")


if __name__ == "__main__":
    main()
