import os
from tkinter import PhotoImage

from .const import IMAGE_ASSETS


def load_image(image_name: str) -> PhotoImage:
    return PhotoImage(file=os.path.join(IMAGE_ASSETS, image_name))


def load_task_image(image_name: str) -> str:
    return PhotoImage(file=os.path.join(IMAGE_ASSETS, "task", image_name))
