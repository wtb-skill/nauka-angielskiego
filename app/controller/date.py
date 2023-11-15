from app.model.date_manager import ManageDate
from app.model.file_manager import FileManager
from app.model.vocabulary_data import VocabularyData
from typing import List, Dict, Type, Union


class DateController:
    def __init__(self):
        self._file_manager = FileManager(VocabularyData.SETTINGS)
        self.date_data = self._load_date_data()
        self.manage_date = ManageDate(self.date_data)
        self.current_date = self.manage_date.current_date
        self.quiz_date = self.manage_date.quiz_date
        self.was_test_done_today = self.manage_date.are_dates_the_same

    def _load_date_data(self) -> List[Dict]:
        """Load date data from a JSON file."""
        return self._file_manager.load()

    def save_quiz_date(self):
        """Save the date of the last quiz to settings."""
        _quiz_date_data = {"date": self.current_date}
        self._file_manager.save(_quiz_date_data)



