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

    def filter_tasks(self, done=None):
        if done is None:
            return self.tasks
        return [task for task in self.tasks if task.done == done]