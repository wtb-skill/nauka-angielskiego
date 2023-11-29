from app.model.date_manager import ManageDate
from app.model.file_manager import FileManager
from app.model.vocabulary_data import VocabularyData
from app.view.quiz import QuizView


class DateController:  # do ogarnięcia i zmiany
    def __init__(self) -> None:
        self._file_manager = FileManager(VocabularyData.SETTINGS)
        self.date_data = self._load_date_data()
        self.manage_date = ManageDate(self.date_data)
        self.current_date = self.manage_date.current_date
        self.quiz_date = self.manage_date.quiz_date
        self.first_quiz_today = self.manage_date.are_dates_the_same

    def _load_date_data(self) -> dict[str, str]:
        """Load date data from a JSON file."""
        return self._file_manager.load()

    def save_quiz_date(self) -> None:
        """Save the date of the last quiz to settings."""
        _quiz_date_data = {"date": self.current_date}
        self._file_manager.save(_quiz_date_data)

    @staticmethod
    def display_message_that_quiz_was_done_today() -> None:
        _view = QuizView()
        _view.quiz_completed()




