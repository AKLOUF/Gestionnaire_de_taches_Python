from models import Task
from datetime import datetime

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, priority, description=None):
        if title is "":
            raise ValueError("Task title cannot be empty.")

        task = Task(
            id=self.__generate_next_id(),
            title=title,
            creation_date=datetime.today().strftime("%d-%m-%Y"),
            priority=priority,
            description=description,
            status="not started"
        )
        self.tasks.append(task)

    def __generate_next_id(self):
        max([t.id for t in self.tasks], default=0) + 1

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def get_tasks(self):
        return self.tasks

    def get_task_by_id(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def finish_task(self, task_id):
        task = self.get_task_by_id(task_id)
        if task:
            task.mark_as_done()
            return True
        return False

    def modify_task(self, task_id, new_title):
        task = self.get_task_by_id(task_id)
        if task:
            task.modify_title(new_title)
            return True
        return False

    def filter_tasks_by_done_status(self, status):
        if status is None:
            return self.tasks
        return [task for task in self.tasks if task.status == status]

    def filter_tasks_by_priority(self, priority):
        return [task for task in self.tasks if task.priority == priority]

    def mark_task_as_done(self, task_id):
        task = self.get_task_by_id(task_id)
        if task:
            task.mark_as_done()
            return True
        return False

    def change_task_status(self, task_id, new_status):
        task = self.get_task_by_id(task_id)
        if task:
            task.status = new_status
            return True
        return False

    def change_task_priority(self, task_id, new_priority):
        task = self.get_task_by_id(task_id)
        if task:
            task.priority = new_priority
            return True
        return False

    def get_task_by_title(self, task_title):
        for task in self.tasks:
            if task.title == task_title:
                return task
        return None

    