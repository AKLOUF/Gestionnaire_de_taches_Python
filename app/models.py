from enum import Enum

class TaskPriority(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

    @staticmethod
    def _priority_transform(choice):
        if choice == "1":
            return TaskPriority.HIGH
        elif choice == "2":
            return TaskPriority.MEDIUM
        elif choice == "3":
            return TaskPriority.LOW
        else:
            raise ValueError("Invalid priority choice. Please choose 1, 2, or 3.")

class TaskStatus(Enum):
    NOT_STARTED = "not started"
    IN_PROGRESS = "in progress"
    DONE = "done"

    @staticmethod
    def _status_transform(choice):
        if choice == "1":
            return TaskStatus.NOT_STARTED
        elif choice == "2":
            return TaskStatus.IN_PROGRESS
        elif choice == "3":
            return TaskStatus.DONE
        else:
            raise ValueError("Invalid status choice. Please choose 1, 2, or 3.")


class Task:
    def __init__(self, id, title, creation_date, priority, description, status):
        self.id = id
        self.title = title
        self.creation_date = creation_date
        self.priority = priority
        self.description = description
        self.status = status

    def mark_as_done(self):
        self.status = "done"

    def modify_title(self, new_title):
        self.title = new_title

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'creation_date': self.creation_date,
            'priority': self.priority,
            'description': self.description,
            'status': self.status
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get('id'),
            title=data.get('title'),
            creation_date=data.get('creation_date'),
            priority=data.get('priority'),
            description=data.get('description'),
            status=data.get('status')
        )
