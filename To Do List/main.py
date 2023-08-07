from interface import *
import time
from category import Category
from task import Task
from kronos import Kairos

'''variables that keep track of the items been stored'''
tasks = []
cat_scale = 0
task_row = 1
checked = NORMAL
tasks_subtasks_page = ""
category_details = {
    "title": "",
    "description": "",
    "scale": 0
}
tasks_details = {
    "title": "",
    "description": "",
    "due_date": "",
    "due_time": "",
}

'''function to go through all tasks'''
def search_time_up():
    global tasks
    while True:
        current_date = Kairos().date
        current_time = Kairos().time
        due_task_name = " "
        for cat in tasks:
            available_tasks = cat.get_tasks()
            for task_name, task_obj in available_tasks.items():
                task_date = task_obj.get_date()
                task_time = task_obj.get_time()
                if current_date == task_date and current_time == task_time:
                    print("wow")
                else:
                    subtasks = task_obj.get_subtask()
                    for subtask_name, subtasks_obj in subtasks.items():
                        subtask_date = subtasks_obj.get_date()
                        subtask_time = subtasks_obj.get_time()
                        if current_date == subtask_date and current_time == subtask_time:
                            print("Okay")
        time.sleep(30)


'''Function that adds category to memory'''
def save_category():
    category = Category(name=category_details["title"])
    category.set_description(description=category_details["description"])
    category.set_scale(scale=category_details["scale"])
    position = int(category_details["scale"])
    tasks.insert(position, category)


'''Function that adds a task to memory'''
def save_task():
    global tasks, tasks_details
    task = Task(name=tasks_details["title"])
    task.add_description(description=tasks_details["description"])
    task.set_date(date=tasks_details["date"])
    task.add_time(time=tasks_details["time"])

    tasks[int(cat_scale)].set_tasks(tasks=task)


'''Function to edit task'''
def edit_task(name, new_desc, new_time, new_date):
    task_content = " "
    print(tasks[0].get_tasks()[f"{name}"].get_description())
    for cat in tasks:
        available_tasks = cat.get_tasks().items()
        for task, obj in available_tasks:
            if name == task:
                tasks[tasks.index(cat)].get_tasks()[f"{name}"].add_description(new_desc)
                tasks[tasks.index(cat)].get_tasks()[f"{name}"].add_time(new_time)
                tasks[tasks.index(cat)].get_tasks()[f"{name}"].set_date(new_date)
                break
    print(tasks[0].get_tasks()[f"{name}"].get_description())


'''Function that  adds a subtask to task'''
def save_subtask(cat, task):
    global tasks, tasks_details
    subtask = Task(name=tasks_details["title"])
    subtask.add_description(description=tasks_details["description"])
    subtask.set_date(date=tasks_details["due_date"])
    subtask.add_time(time=tasks_details["due_time"])
    parent_task = tasks[int(cat)].get_tasks()[f"{task}"]
    parent_task.add_subtask(subtask)


'''Function that deletes category'''
def delete_category(cat):
    global tasks
    pass


'''Function that adds category in the memory'''
def add_category():
    global category_details, cat_scale, task_row
    category_pane = Tab(page=task_panel)

    '''Function delete tasks'''
    def delete_subtasks(parent_name, child_name):
        global task_subtasks_page
        for cat in tasks:
            available_tasks = cat.get_tasks().items()
            for task, obj in available_tasks:
                if parent_name == task:
                    task_subtasks = tasks[tasks.index(cat)].get_tasks()[f"{parent_name}"].get_subtask()
                    for subtask, sub_obj in task_subtasks.items():
                        if subtask == child_name:
                            task_subtasks.pop(f"{child_name}")
                            break

    '''Function to show the subtasks for a particular task'''
    def view_subtasks(name):
        global task_subtasks_page
        for cat in tasks:
            available_tasks = cat.get_tasks().items()
            for task, obj in available_tasks:
                if name == task:
                    task_subtasks = tasks[tasks.index(cat)].get_tasks()[f"{name}"].get_subtask()
                    task_subtasks_obj = task_subtasks.values()

        task_subtasks_page = SubtaskPage(subtasks=task_subtasks_obj, add_task=lambda: add_subtask(name), name=name,
                                         delete=delete_subtasks)

    def view_subtask(name):
        subtask_content = " "
        for cat in tasks:
            available_tasks = cat.get_tasks()
            for task, obj in available_tasks.items():
                available_subtasks = obj.get_subtask()
                for subtask, sub_obj in available_subtasks.items():
                    if subtask == name:
                        subtask_content = sub_obj.get_description()
        view_subtask_page = TaskPage(add_task=add_subtask, task_description=subtask_content,
                                     subtasks=lambda: view_subtasks(name))

    '''Function to post subtasks'''
    def post_subtask(title, desc, due_time, due_date, subtask_parent):
        global checked, tasks_subtasks_page
        subtask_panes = Tab(page=tasks_subtasks_page)
        subtask_panes.grid(column=0, row=5)
        task = NewButton(page=subtask_panes)
        task.config(width=20, text=title, command=lambda: view_subtask(title))
        task.grid(column=0, row=0, sticky="w")

        def check_task():
            if task["state"] == "disabled":
                task["state"] = "active"
            else:
                task["state"] = "disabled"

        task_check = CheckStuff(page=subtask_panes)
        task_check.config(height=2)
        task_check.grid(column=1, row=0, sticky="w")

        tasks_details["title"] = title
        tasks_details["description"] = desc
        tasks_details["time"] = due_time
        tasks_details["date"] = due_date

        '''finding category and task_obj using task_name'''
        for cat in tasks:
            category_for_sub = 0
            task = subtask_parent
            for cat in tasks:
                available_tasks = cat.get_tasks().items()
                for task, obj in available_tasks:
                    if task == subtask_parent:
                        category_for_sub = cat.get_scale()

        save_subtask(cat=category_for_sub, task=task)


    '''Function that calls the editing page for adding a task'''
    def add_subtask(name):
        new_subtask = EditPage(name="Add Subtask", due_time=Kairos().time,
                               due_date=Kairos().date, execution=post_subtask,
                               subtask_parent_name=name)

    '''Deleting tasks'''
    def delete_task(name, task_pane, task_checking, self_button, execute_pane):
        global task_row
        task_content = " "
        for cat in tasks:
            available_tasks = cat.get_tasks().items()
            for task, obj in available_tasks:
                if name == task:
                    cat_tasks = tasks[tasks.index(cat)].get_tasks()
                    cat_tasks.pop(f"{name}")
                    break
        task_pane.destroy()
        task_checking.destroy()
        self_button.destroy()
        execute_pane.destroy()
        task_row -= 1

    '''Function to view contents of a task'''
    def view_task(name):
        task_content = " "
        for cat in tasks:
            available_tasks = cat.get_tasks().items()
            for task, obj in available_tasks:
                if name == task:
                    task_content = tasks[tasks.index(cat)].get_tasks()[f"{name}"].get_description()
                    task_name = tasks[tasks.index(cat)].get_tasks()[f"{name}"].get_task()
                    task_time = tasks[tasks.index(cat)].get_tasks()[f"{name}"].get_time()
                    task_date = tasks[tasks.index(cat)].get_tasks()[f"{name}"].get_date()
                    task_properties = [task_name, task_content, task_date, task_time]
        task_view = TaskPage(add_task=add_subtask, task_description=task_content, subtasks=lambda: view_subtasks(name),
                             task_properties=task_properties, edit=edit_task)

    '''Function to post tasks on the front panel'''
    def post_task(title, desc, due_time, due_date, subtask_parent):
        global checked, task_row
        task = NewButton(page=category_pane)
        task.add_new_button(name=title, command=lambda: view_task(title), n=task_row)

        def check_task():
            if task["state"] == "disabled":
                task["state"] = "active"
            else:
                task["state"] = "disabled"

        execution_button_pane = Tab(page=category_pane)
        execution_button_pane.grid(column=0, row=task_row, sticky="ne")
        task_check = CheckStuff(page=execution_button_pane)
        task_check.complete_check(command=check_task, n=task_row)

        tasks_details["title"] = title
        tasks_details["description"] = desc
        tasks_details["time"] = due_time
        tasks_details["date"] = due_date

        delete_task_button = NewButton(page=execution_button_pane)
        delete_task_button.add_delete_button(command=lambda: delete_task(name=title, task_pane=task,
                                                                         task_checking=task_check,
                                                                         self_button=delete_task_button,
                                                                         execute_pane=execution_button_pane),
                                             n=task_row)

        task_row += 1
        save_task()

    ''''Function to call window used to edit a task before added'''
    def add_new_task():
        new_task = EditPage(name="Add Task", due_date=Kairos().date, due_time=Kairos().time, execution=post_task)

    '''Function to add the panes for the categories '''
    def add_pane(title, desc, scale):
        global cat_scale
        category_pane.grid(column=0, row=scale, pady=5)
        category_name = Title(page=category_pane)
        category_name.add_title(name=title)
        add_task = NewButton(page=category_pane)
        add_task.add_to_category(command=add_new_task)

        category_details["name"] = title
        category_details["description"] = desc
        category_details["scale"] = scale
        cat_scale = scale

        save_category()

    new_category = EditCategory(name="Add Category", execution=add_pane)


'''Main page for manipulations'''
interface = Interface()
interface.title("TO DO LIST")
interface.geometry("410x600")
interface.config(bg="#125685")
interface.wm_resizable(False, False)

'''Title bar for the program'''
title_bar = Title(page=interface)
title_bar.config(width=54, height=2, text="TO DO LIST")
title_bar.grid(column=0, row=0, columnspan=2, pady=10, padx=10, sticky="nw")

'''This is where the categories are arranged'''
task_panel = Tab()
task_panel.config(bg="#125685", padx=4)
task_panel.grid(column=0, rowspan=20, row=1, ipadx=2, sticky="nw")

'''This the add button the adds the category'''
add_image = PhotoImage(file="add_intermediate.png")
add_button = NewButton()
add_button.config(image=add_image, height=120, width=120, border=0, bg="#125685", activebackground="#125685", command=add_category)
add_button.grid(sticky="e", column=1, row=4, pady=400)



if __name__ == "__main__":
    interface.mainloop()



