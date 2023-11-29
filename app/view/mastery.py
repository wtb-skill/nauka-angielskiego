from app.model.word import Word


class MasteryView:

    @staticmethod
    def display_word_is_mastered(word: Word) -> None:
        """Display a message when a word is mastered."""
        print(f"The word: '{word.eng}' got mastered!")

    @staticmethod
    def new_word(word: Word) -> None:
        """Display a new word for the user to learn."""
        print(f"The new word for you to learn is: '{word.eng}'!")