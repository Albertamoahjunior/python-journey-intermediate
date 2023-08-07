class Task:
    def __init__(self, name, due_time=None, due_date=None, description=None):
        self.name = name
        self.time = due_time
        self.date = due_date
        self.description = description
        self.subtasks = {}

    def __del__(self):
        pass

    def add_time(self, time):
        self.time = time

    def set_date(self, date):
        self.date = date

    def add_category(self, category):
        self.category = category

    def add_description(self, description):
        self.description = description

    def add_subtask(self, subtask):
        self.subtasks[subtask.get_task()] = subtask

    def get_task(self):
        return self.name

    def get_time(self):
        return self.time

    def get_date(self):
        return self.date

    def get_description(self):
        return self.description

    def get_subtask(self):
        return self.subtasks

    def delete(self):
        self.destroy()
