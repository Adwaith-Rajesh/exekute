import os
from tkinter import PhotoImage

from .const import IMAGE_ASSETS


def load_image(image_name: str) -> PhotoImage:
    return PhotoImage(file=os.path.join(IMAGE_ASSETS, image_name))
