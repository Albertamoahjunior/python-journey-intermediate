class Node:
    def __init__(self,task):
        self.descendants = []
        self.task = task

    def set_task(self, task):
        self.task = task

    def set_descendants(self, descendants):
        self.descendants.append(descendants)

    def get_descendants(self):
        return self.descendants