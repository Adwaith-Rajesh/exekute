import os
import subprocess
import uuid
from tkinter import *  # noqa: F403
from typing import List

from .task import Task
from exekute.core.const import TASK_ORDER
from exekute.core.db import DataBase
from exekute.core.utils import load_image


class AllTasksWindow(Frame):

    def __init__(self, parent: Tk, task_win_cb) -> None:
        super(AllTasksWindow, self).__init__(parent, width=1000, height=700)

        self.parent = parent

        self.task_win_cb = task_win_cb
        self.db = DataBase()
        self.setup_ui()
        self.order_number = 1
        self.tasks: List[Task] = []
        self.load_task_from_db()

    def setup_ui(self) -> None:
        bg_image = load_image("all-task-window.png")
        add_button_bg = load_image("add-button.png")

        self.bg_label = Label(self, image=bg_image,
                              borderwidth=0, background="#ffffff")
        self.bg_label.image = bg_image
        self.bg_label.place(x=0, y=0)

        self.add_button = Button(
            self, image=add_button_bg, borderwidth=0, bg="#282828", activebackground="#282828",
            command=self.add_task)
        self.add_button.image = add_button_bg
        self.add_button.place(x=911, y=40)

    def edit_call_back(self, _id: str):
        self.task_win_cb(_id)

    def exc_call_back(self, _id: str):
        apps = self.db.get_by_id(_id)["apps"]
        for app in apps:
            os.startfile(app)

        script = self.db.get_by_id(_id)["script"]
        if script:
            subprocess.call([script])

    def add_task(self) -> None:
        new_id = str(int(uuid.uuid4()))[:8]
        self.db.add(new_id, data={"name": "", "apps": [], "script": ""})
        self.task_win_cb(new_id)

    def display_task(self) -> None:
        if self.order_number <= 8:
            for task in self.tasks:
                task.place(**TASK_ORDER[self.order_number])
                self.order_number += 1

    def load_task_from_db(self) -> None:
        data = self.db.get_all()

        for d in data:
            self.tasks.append(Task(self, data[d]["name"], _id=d, edit_cb=self.edit_call_back,
                                   exc_cb=self.exc_call_back))
        self.display_task()
