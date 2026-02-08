"""Task model for the console todo application."""

from datetime import datetime


class Task:
    """Represents a single todo task."""

    def __init__(self, task_id, title, description="", completed=False):
        self.id = task_id
        self.title = title
        self.description = description
        self.completed = completed
        self.created_at = datetime.now()

    def __str__(self):
        status = "✓" if self.completed else "○"
        created_str = self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        return f"ID: {self.id} | {status} {self.title} | {self.description or '(no description)'} | Created: {created_str}"

    def to_dict(self):
        """Convert task to dictionary representation."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data):
        """Create Task instance from dictionary."""
        task = cls(
            task_id=data["id"],
            title=data["title"],
            description=data.get("description", ""),
            completed=data.get("completed", False)
        )
        # Restore the created_at timestamp if available
        if "created_at" in data:
            try:
                task.created_at = datetime.fromisoformat(data["created_at"])
            except ValueError:
                # If timestamp format is invalid, use current time
                task.created_at = datetime.now()
        return task