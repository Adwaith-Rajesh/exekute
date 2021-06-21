from tkinter import *  # noqa: F403

from .all_tasks import AllTasksWindow
from .edit_task import EditTask
from exekute.core.utils import load_image


class MainWindow(Tk):

    def __init__(self, *args, **kwargs) -> None:
        super(MainWindow, self).__init__(*args, **kwargs)

        self.title("Exekute")
        self._width = 1000
        self._height = 700

        self.resizable(False, False)
        icon = load_image("execute-button.png")
        self.iconphoto(False, icon)
        self.center_window()

    def center_window(self) -> None:
        _height = self._height
        _width = self._width
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_cord = int((screen_width / 2) - (_width / 2))
        y_cord = int((screen_height / 2) - (_height / 2))
        self.geometry(f"{_width}x{_height}+{x_cord}+{y_cord}")

        self.setup_ui()

    def setup_ui(self) -> None:
        self.load_main_task_win()

    def load_main_task_win(self) -> None:
        self.task_window = AllTasksWindow(self, self.task_win_call_back)
        self.task_window.pack(fill=BOTH, expand=True)

    def task_edit_win_call_back(self) -> None:
        self.load_main_task_win()

    def task_win_call_back(self, _id: str) -> None:
        self.task_window.destroy()

        self.edit_window = EditTask(
            self, task_id=_id, te_cb=self.task_edit_win_call_back)
        self.edit_window.pack(fill=BOTH, expand=True)
