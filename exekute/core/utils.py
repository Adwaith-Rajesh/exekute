import os
from pathlib import Path
from tkinter import PhotoImage

from .const import IMAGE_ASSETS


def load_image(image_name: str) -> PhotoImage:
    return PhotoImage(file=os.path.join(IMAGE_ASSETS, image_name))


def load_task_image(image_name: str) -> str:
    return PhotoImage(file=os.path.join(IMAGE_ASSETS, "task", image_name))


def verify_exe_file(file_path: str) -> bool:
    return Path(file_path).is_file() and file_path.endswith(".exe")


def verify_script_file(file_path: str) -> bool:
    return Path(file_path).is_file() and file_path.endswith(".bat")
