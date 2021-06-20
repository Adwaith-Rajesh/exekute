import os
from pathlib import Path
from tkinter import *  # noqa: F403

IMAGE_ASSETS = os.path.join(
    Path(os.path.dirname(__file__)).parent, "assets", "images")


class AllTasksWindow(Frame):

    def __init__(self, parent: Tk) -> None:
        super(AllTasksWindow, self).__init__(parent, width=1000, height=700)

        self.setup_ui()

    def setup_ui(self) -> None:
        bg_image = PhotoImage(file=os.path.join(
            IMAGE_ASSETS, "all-task-window.png"))
        self.bg_label = Label(self, image=bg_image,
                              borderwidth=0, background="#ffffff")
        self.bg_label.image = bg_image
        self.bg_label.place(x=0, y=0)
