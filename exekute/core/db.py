import json
import os
from json.decoder import JSONDecodeError
from pathlib import Path
from typing import Dict
from typing import List
from typing import Union

from .const import DB_PATH

DBType = Dict[str, Dict[str, Union[List[str], str]]]


class DataBase:

    def __init__(self) -> None:
        self.db = os.path.join(DB_PATH, "data.json")

        if not Path(self.db).is_file():
            if not Path(DB_PATH).is_dir():
                os.makedirs(DB_PATH, exist_ok=True)
            self.__create_db()

        self.data = self.__load_data()

    def get_all(self) -> DBType:
        return self.data

    def add(self, _id: str, data: Dict[str, Union[List[str], str]]) -> None:
        self.data[_id] = data
        self.__dump_data()

    def get_by_id(self, _id: str) -> Dict[str, Union[List[str], str, int]]:
        if _id in self.data:
            return self.data[_id]

    def __create_db(self) -> None:
        with open(self.db, "w") as f:
            f.write("{}")

    def __load_data(self) -> DBType:
        try:
            with open(self.db, "r") as f:
                data = json.load(f)
                return data
        except JSONDecodeError:
            self.__create_db()
            return self.__load_data()

    def __dump_data(self) -> None:
        with open(self.db, "w") as f:
            json.dump(self.data, f)
