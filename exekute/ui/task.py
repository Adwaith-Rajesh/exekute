from random import choice
from tkinter import *  # noqa: F403

from exekute.core.const import Colors
from exekute.core.const import TASK_COLORS
from exekute.core.utils import load_image
from exekute.core.utils import load_task_image


class Task(Frame):

    def __init__(self, parent: Frame, task_name: str, _id: str, edit_cb, exc_cb):
        super(Task, self).__init__(parent, width=185,
                                   height=185, background=Colors.black, borderwidth=0)

        self.task_name = task_name
        self.edit_cb = edit_cb  # edit callback
        self.exc_cb = exc_cb  # execute callback
        self._id = _id
        self.color = choice(TASK_COLORS)

        self.setup_ui()
        self.bind("<Enter>", self.show_tool_buttons)
        self.bind("<Leave>", self.remove_tool_buttons)

    def setup_ui(self) -> None:
        task_bg = load_task_image(self.color[1:] + ".png")

        self.task_bg = Label(self, image=task_bg,
                             background=Colors.black)
        self.task_bg.image = task_bg
        self.task_bg.place(x=0, y=0)

        self.task_name = Label(self, text=self.task_name, font=("arial rounded", 18, "bold"),
                               wraplength=170, justify=CENTER, background=self.color, width=11, height=5)
        self.task_name.place(x=8, y=15)

    def show_tool_buttons(self, e) -> None:
        edit_button_bg = load_image("edit-button.png")
        exc_button_bg = load_image("execute-button.png")

        self.task_name.place_forget()

        self.edit_button = Button(self, image=edit_button_bg, borderwidth=0, background=self.color,
                                  activebackground=self.color,
                                  command=lambda x=self._id: self.edit_cb(x), cursor="hand2")
        self.edit_button.image = edit_button_bg

        self.exc_button = Button(self, image=exc_button_bg, borderwidth=0, background=self.color,
                                 activebackground=self.color,
                                 command=lambda x=self._id: self.exc_cb(x),
                                 cursor="hand2")
        self.exc_button.image = exc_button_bg

        i = 0

        def animate_in():
            nonlocal i
            i += 1
            try:
                self.exc_button.place(x=10 + i, y=63)
                self.edit_button.place(x=123 - i, y=63)

                if i != 20:
                    self.after(10, animate_in)

                else:
                    self.task_name.place_forget()

            except Exception:
                pass

        animate_in()

    def remove_tool_buttons(self, e) -> None:
        self.task_name.place(x=8, y=15)
        self.edit_button.destroy()
        self.exc_button.destroy()
