class Category:
    def __init__(self, name,description=None,scale=None):
        self.scale = scale
        self.name = name
        self.description = description
        self.tasks = {}

    def delete_category(self):
        pass

    def get_category_name(self):
        return self.name

    def get_category_desc(self):
        return self.description

    def set_scale(self, scale):
        self.scale = scale

    def get_scale(self):
        return self.scale

    def set_tasks(self, tasks):
        self.tasks[tasks.get_task()] = tasks

    def get_tasks(self):
        return self.tasks

    def set_description(self, description):
        self.description = description
