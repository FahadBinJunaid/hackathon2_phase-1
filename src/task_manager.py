"""Task manager for the console todo application."""

from .task import Task


class TaskManager:
    """Manages in-memory storage and operations for tasks."""

    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title, description=""):
        """Add a new task with auto-incrementing ID."""
        if not title.strip():
            raise ValueError("Task title cannot be empty")

        task = Task(self.next_id, title.strip(), description.strip())
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_all_tasks(self):
        """Get all tasks."""
        return self.tasks

    def get_task_by_id(self, task_id):
        """Get a specific task by ID."""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id, title=None, description=None):
        """Update a task's details."""
        task = self.get_task_by_id(task_id)
        if not task:
            return None

        if title is not None:
            task.title = title.strip() if title.strip() else task.title
        if description is not None:
            task.description = description.strip()

        return task

    def delete_task(self, task_id):
        """Delete a task by ID."""
        task = self.get_task_by_id(task_id)
        if not task:
            return False

        self.tasks.remove(task)
        return True

    def mark_task_complete(self, task_id):
        """Mark a task as complete."""
        task = self.get_task_by_id(task_id)
        if not task:
            return None

        task.completed = True
        return task

    def get_next_id(self):
        """Get the next available ID without incrementing the counter."""
        return self.next_id

    def task_exists(self, task_id):
        """Check if a task with the given ID exists."""
        return self.get_task_by_id(task_id) is not None