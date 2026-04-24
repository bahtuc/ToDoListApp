from storage import load_tasks, save_tasks


class TaskManager:
    def __init__(self):
        self.tasks = load_tasks()

    def get_tasks(self):
        return self.tasks

    def add_task(self, task):
        if task and task not in self.tasks:
            self.tasks.append(task)
            self._sync()

    def delete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            self._sync()

    def clear_tasks(self):
        self.tasks = []
        self._sync()

    def _sync(self):
        save_tasks(self.tasks)