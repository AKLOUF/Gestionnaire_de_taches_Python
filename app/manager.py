class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

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

    def finish_task(self, task_title):
        task = self.get_task_by_title(task_title)
        if task:
            task.mark_as_done()
            return True
        return False

    def modify_task(self, task_title, new_title):
        task = self.get_task_by_title(task_title)
        if task:
            task.modify_title(new_title)
            return True
        return False

    def filter_tasks_by_done_status(self, done=None):
        if done is None:
            return self.tasks
        return [task for task in self.tasks if task.done.lower() == done.lower()]

    def filter_tasks_by_priority(self, priority):
        return [task for task in self.tasks if task.priority == priority]

    def mark_task_as_done(self, task_title):
        task = self.get_task_by_title(task_title)
        if task:
            task.mark_as_done()
            return True
        return False

    def get_task_by_title(self, task_title):
        for task in self.tasks:
            if task.title == task_title:
                return task
        return None