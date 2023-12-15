import json
from typing import List, Dict


class FileManager:
    """Class for managing loading and saving json data."""

    def __init__(self, filename: str) -> None:
        self.filename = filename

    def load(self) -> List[Dict[str, str]]:
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []
        return data

    def save(self, data: List[Dict[str, str]]):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(data, file)
