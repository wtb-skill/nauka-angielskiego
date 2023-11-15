from datetime import datetime


class ManageDate:
    """Class for managing quiz date and current date."""
    def __init__(self, settings_data):
        self.settings_data = settings_data
        self.current_date = self._get_current_date()
        self.quiz_date = self._get_quiz_date()
        self.are_dates_the_same = self._is_quiz_and_current_date_same

    def _get_quiz_date(self):
        """Get the quiz date in a string format (YYYY-MM-DD)."""
        quiz_date = self.settings_data["date"]
        return quiz_date

    @staticmethod
    def _get_current_date() -> str:
        """Get the current date in a string format (YYYY-MM-DD)."""
        today = str(datetime.today()).split(" ")[0]
        return today

    def _is_quiz_and_current_date_same(self):
        return self.quiz_date == self.current_date


'''  OLD: 
class ManageDate:
    """Class for managing quiz date and current date."""
    def __init__(self, file=VocabularyData.SETTINGS):
        if not os.path.exists(file):
            self.quiz_date = {"data": "0"}
        else:
            self.file_manager = FileManager(file)
            self.quiz_date = self.file_manager.load()

    def save_quiz_date(self):
        """Save the date of the last quiz to settings."""
        today = self.get_current_date()
        _quiz_date = {"data": today}
        self.file_manager.save(_quiz_date)

    @staticmethod
    def get_current_date() -> str:
        """Get the current date in a string format (YYYY-MM-DD)."""
        today = str(datetime.today()).split(" ")[0]
        return today
'''
