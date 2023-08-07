from tkinter import *
from tkinter import messagebox


class Interface(Tk):
    def __int__(self):
        super().__init__()

        self.title("To do list")
        self.mainloop()

    def close_window(self):
        self.destroy()


class Title(Label):
    def __init__(self, page):
        super().__init__(master=page)

    def add_title(self, name):
        name = name.title()
        name = name + " Category: "
        self.config(text=name, border=0, bg="#d0f1df", fg="#222", width=35, anchor="w", justify=LEFT, height=2)
        self.grid(sticky="w", column=0, row=0, ipadx=10)


class NewButton(Button):
    def __init__(self, page=None, state=None):
        super().__init__(master=page, state=state)
        self.add_image = PhotoImage(file="add_task_new.png")
        self.delete_image = PhotoImage(file="delete_button.png")

    def add_new_button(self, name, command=None, n=1):
        self.config(text=name, bg="#66d399", border=0, width=32, height=2, command=command, activebackground="#66d399")
        self.grid(sticky="nw", column=0, row=n, pady=5)

    def add_delete_button(self, command=None, n=1):
        self.config(image=self.delete_image, bg="#66d399", border=0, width=20, height=34, command=command,
                    activebackground="#66d399")
        self.grid(sticky="ne", column=1, row=n, pady=5)

    def add_to_category(self, command=None):
        self.config(image=self.add_image, command=command, height=20, width=20,
                    border=0, bg="#d0f1df", activebackground="#d0f1df")
        self.grid(sticky="e", column=0, row=0, padx=7)


class CheckStuff(Checkbutton):
    def __init__(self, page=None):
        super().__init__(master=page)

    def complete_check(self, command=None, n=1):
        self.config(command=command, bg="#d0f1df", height=2)
        self.grid(column=0, row=n, sticky="nw", pady=2)


class InputPanel(Text):
    def __init__(self):
        super().__init__()


class Tab(Frame):
    def __init__(self, page=None):
        super().__init__(master=page)

    def add_tab(self, row_position):
        self.config(bg="#d0f1df")
        self.grid(column=0, row=row_position)


class EditPage:
    def __init__(self, name, due_date, due_time, execution=None, subtask_parent_name=None, task_properties=None):
        self.page = Tk()
        self.content = {}
        self.name = name
        self.due_time = due_time
        self.due_date = due_date
        self.task_properties = []
        self.out_properties = task_properties
        self.execution = execution
        self.subtask_parent_name = subtask_parent_name
        self.page.wm_resizable(False, False)

        self.page.title(self.name)
        self.page.config(bg="#125685")

        if self.out_properties is None:
            self.task_properties.insert(0, "Enter task title")
            self.task_properties.append("Enter Description")
            self.task_properties.append(self.due_date)
            self.task_properties.append(self.due_time)
        else:
            self.task_properties = self.out_properties

        self.task_name_label = Label(self.page, text="Title:", bg="#125685")
        self.task_name_label.grid(column=0, row=0)
        self.task_name = Entry(self.page, width=28)
        self.task_name.grid(column=1, row=0, padx=20, pady=10)
        self.task_name.insert(0, self.task_properties[0])
        if self.task_name.get() != "Enter task title":
            self.task_name.config(state="disabled")

        self.task_desc_label = Label(self.page, text="Description:", bg="#125685")
        self.task_desc_label.grid(column=0, row=1)
        self.task_desc = Text(self.page, height=10, width=20)
        self.task_desc.grid(column=1, row=1, padx=10)
        self.task_desc.insert(1.0, self.task_properties[1], "end")

        self.task_due_date_label = Label(self.page, text="Due date:", bg="#125685")
        self.task_due_date_label.grid(column=0, row=2)
        self.task_due_date = Entry(self.page, width=28)
        self.task_due_date.grid(column=1, row=2, padx=20, pady=10)
        self.task_due_date.insert(0, self.task_properties[2])

        self.task_due_label = Label(self.page, text="Due time:", bg="#125685")
        self.task_due_label.grid(column=0, row=3)
        self.task_due = Entry(self.page, width=28)
        self.task_due.grid(column=1, row=3, padx=20, pady=10)
        self.task_due.insert(0, self.task_properties[3])

        def save_it():
            details = {
                "title": self.task_name.get(),
                "description": self.task_desc.get("1.0", "end"),
                "due_date": self.task_due_date.get(),
                "due_time": self.task_due.get(),
            }
            self.content = details
            if execution is None:
                pass
            else:
                self.execution(self.content["title"], self.content["description"],
                               self.content["due_time"], self.content["due_date"], subtask_parent=self.subtask_parent_name)
            self.exit_page()

        self.save = Button(self.page, text="Save", command=save_it, width=15, bg="#22ef8c")
        self.save.grid(column=0, row=4, pady=10)

        self.exit = Button(self.page, text="Exit", command=self.exit_page, width=15, bg="red")
        self.exit.grid(column=1, row=4, pady=10)

        self.page.mainloop()

    def save_done(self):
        self.save["state"] = "disable"

    def exit_page(self):
        self.page.destroy()


class EditCategory:
    def __init__(self, name, scale=0, execution=None):
        self.page = Tk()
        self.page.wm_resizable(False, False)
        self.name = name
        self.scale = scale
        self.execution = execution
        self.content = {}

        self.page.title(self.name)
        self.page.config(bg="#125685")

        self.cat_name_label = Label(self.page, text="Title:", bg="#125685")
        self.cat_name_label.grid(column=0, row=0)
        self.cat_name = Entry(self.page, width=28)
        self.cat_name.grid(column=1, row=0, padx=20, pady=10)

        self.cat_desc_label = Label(self.page, text="Description:", bg="#125685")
        self.cat_desc_label.grid(column=0, row=1)
        self.cat_desc = Text(self.page, height=6, width=20)
        self.cat_desc.grid(column=1, row=1, padx=10)

        self.cat_scale_label = Label(self.page, text="Scale Priority:", bg="#125685")
        self.cat_scale_label.grid(column=0, row=2)
        self.cat_scale = Entry(self.page, width=28)
        self.cat_scale.grid(column=1, row=2, padx=20, pady=10)
        self.cat_scale.insert(0, str(self.scale))

        def save_it():
            details = {
                "title": self.cat_name.get(),
                "description": self.cat_desc.get("1.0", "end"),
                "scale": self.cat_scale.get(),
            }
            self.content = details

            if self.execution is None:
                pass
            else:
                self.execution(self.content["title"], self.content["description"], self.content["scale"])

            self.exit_page()

        self.save = Button(self.page, text="Save", command=save_it, width=15, border=0, bg="#22ef8c")
        self.save.grid(column=1, row=3, pady=10)

        self.page.mainloop()

    def exit_page(self):
        self.page.destroy()


class TaskPage:
    def __init__(self, add_task=None, delete=None, edit=None, task_description=None, subtasks=None, task_properties=None):
        self.content = {}
        self.add_task = add_task
        self.delete = delete
        self.edit = edit
        self.description = task_description
        self.subtasks = subtasks
        self.task_properties = task_properties
        self.page = Tk()
        self.page.title("Task")
        self.page.config(bg="#125685")
        self.page.wm_resizable(False, False)

        self.task = Canvas(self.page, bg="white", height=200, width=200)
        self.task.pack()
        self.task.create_text(100, 100, text=self.description)

        self.edit_button = Button(self.page, text="Edit", command=self.edit_task)
        self.edit_button.config(bg="#2dae69", width=3)
        self.edit_button.pack(side="left", anchor="sw")

        self.add_subtask_button = Button(self.page, text="Subtasks", command=self.subtasks)
        self.add_subtask_button.config(bg="#35c4ce", width=9)
        self.add_subtask_button.pack(side="right", anchor="se")

        self.page.mainloop()

    def add_subtask(self):
        self.page.destroy()
        self.add_task()
        self.page.destroy()

    def edit_task(self):
        self.page.destroy()
        edit_new = EditPage(name="Edit Task", due_date=0, due_time=0,
                            task_properties=self.task_properties)
        self.content = edit_new.content
        self.edit(name=self.content["title"], new_desc=self.content["description"], new_time=self.content["due_time"],
                  new_date=self.content["due_date"])


'''Class of subtasks page'''


class SubtaskPage(Tk):
    def __init__(self, add_task=None, subtasks=None, add_subtask=None, name=None, delete=None):
        super().__init__()
        self.name = name
        self.content = {}
        self.add_task = add_task
        self.delete = delete
        self.subtasks = list(subtasks)
        self.title(self.name)
        self.config(bg="#125685")
        self.geometry("200x240")
        self.wm_resizable(False, False)

        def delete_subtask(subtask, frame):
            frame.destroy()
            subtask_name = subtask.get_task()
            self.delete(child_name=subtask_name, parent_name=self.name)

        def view_subtask(desc):
            disp = TaskPage(task_description=desc)

        '''Logic for posting subtasks'''
        if len(self.subtasks) == 0:
            self.task = Canvas(self, bg="white", height=200, width=200)
            self.task.pack(pady=5)
            self.task.create_text(100, 100, text="There are no subtasks to exhibit")
        else:
            for subtasks in self.subtasks:
                subtask_frame = Tab(page=self)
                subtask_frame.pack()
                subtask_button = NewButton(page=subtask_frame)
                subtask_button.config(text=subtasks.get_task(), width=20, height=1,
                                      bg="#1d97a0", command=lambda: view_subtask(subtasks.get_description()), border=0)
                subtask_button.grid(column=0, row=0, sticky="w")

                subtask_delete_button = NewButton(page=subtask_frame)
                subtask_delete_button.config(text="del", command=lambda: delete_subtask(subtask=subtasks,
                                                                                        frame=subtask_frame), border=0,
                                             activebackground="#2ad7e3", activeforeground="#2ad7e3", bg="#2ad7e3")
                subtask_delete_button.grid(column=1, row=0, sticky="w")

                def check_button():
                    if subtask_button["state"] == "disabled":
                        subtask_button["state"] = "active"
                    else:
                        subtask_button["state"] = "disabled"

                subtask_check = CheckStuff(page=subtask_frame)
                subtask_check.config(command=check_button, height=1, bg="#2ad7e3", border=0)
                subtask_check.grid(column=2, row=0, sticky="w")

        self.add_subtask_button = Button(self, text="Add subtasks", command=self.add_task)
        self.add_subtask_button.config(bg="#35c4ce", width=10)
        self.add_subtask_button.pack(side="bottom", anchor="s")

        self.mainloop()

    def add_subtask(self):
        self.destroy()
        self.add_task()


class ReminderPopUp:
    def show_reminder(self, taskname):
        messagebox.showinfo(title="Time up", message=f"It is time for {taskname} task")
