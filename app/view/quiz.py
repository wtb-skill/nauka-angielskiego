from app.model.word import Word


class QuizView:

    @staticmethod
    def display_quiz_eng_to_pol(word: Word) -> str:
        """Ask the user to translate an English word to Polish and return their answer."""
        user_answer = input(f"Please translate the English word: '{word.eng}' to Polish: ")
        return user_answer

    @staticmethod
    def display_quiz_pol_to_eng(word: Word) -> str:
        """Ask the user to translate a Polish word to English and return their answer."""
        user_answer = input(f"Please translate the Polish word: '{word.pol}' to English: ")
        return user_answer

    @staticmethod
    def display_correct() -> None:
        """Display a message when the user's answer is correct."""
        print("Correct!")

    @staticmethod
    def display_wrong() -> None:
        """Display a message when the user's answer is wrong."""
        print("Wrong!")

    @staticmethod
    def quiz_completed() -> None:
        """Display a message when the user has already completed the quiz for the day."""
        print("You have already completed the quiz for today. Come back tomorrow! <3")
