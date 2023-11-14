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
    def display_correct():
        """Display a message when the user's answer is correct."""
        print("Correct!")

    @staticmethod
    def display_wrong():
        """Display a message when the user's answer is wrong."""
        print("Wrong!")

    @staticmethod
    def word_mastered(word: Word):
        """Display a message when a word is mastered."""
        print(f"The word: '{word.eng}' got mastered!")

    @staticmethod
    def new_word(word: Word):
        """Display a new word for the user to learn."""
        print(f"The new word for you to learn is: '{word.eng}'!")

    @staticmethod
    def quiz_completed():
        """Display a message when the user has already completed the quiz for the day."""
        print("You have already completed the quiz for today. Come back tomorrow! <3")
