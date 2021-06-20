import os
from dataclasses import dataclass
from pathlib import Path

from appdirs import user_data_dir

IMAGE_ASSETS = os.path.join(
    Path(os.path.dirname(__file__)).parent.parent, "assets", "images")

DB_PATH = user_data_dir(appauthor="exekute", appname="db")


@dataclass
class Colors:
    black: str = "#282828"
    grey: str = "#C4C4C4"
    blue: str = "#0853E3"
    task_grey: str = "#DDDDDD"
