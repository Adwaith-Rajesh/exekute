from tkinter import *  # noqa: F403

from .all_tasks import AllTasksWindow


class MainWindow(Tk):

    def __init__(self, *args, **kwargs) -> None:
        super(MainWindow, self).__init__(*args, **kwargs)

        self.title("Exekute")
        self._width = 1000
        self._height = 700
        # self.geometry("500x500")
        # self.iconbitmap(ICON_FILE)
        self.resizable(False, False)
        # self.icon = PhotoImage(file=ICON_FILE)
        # self.iconphoto(False, self.icon)

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
        task_window = AllTasksWindow(self)
        task_window.pack(fill=BOTH, expand=True)
