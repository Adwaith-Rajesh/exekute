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


TASK_ORDER = {
    1: {"x": 70, "y": 146},
    2: {"x": 290, "y": 146},
    3: {"x": 510, "y": 146},
    4: {"x": 730, "y": 146},
    5: {"x": 70, "y": 407},
    6: {"x": 290, "y": 407},
    7: {"x": 510, "y": 407},
    8: {"x": 730, "y": 407},
}

TASK_EDIT_ENTRY_BOX = {
    1: {"x": 87, "y": 155},
    2: {"x": 87, "y": 215},
    3: {"x": 87, "y": 273},
    4: {"x": 87, "y": 331},
    5: {"x": 87, "y": 389},
    6: {"x": 87, "y": 571},
}

TASK_EDIT_BTNS = {
    1: {"x": 833, "y": 81},
    2: {"x": 833, "y": 129},
    3: {"x": 833, "y": 177},
    4: {"x": 833, "y": 616}
}
