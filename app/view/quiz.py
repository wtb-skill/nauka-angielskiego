from app.model.hand import Hand
from app.model.words_to_learn import WordDict


class QuizView:
    def display_quiz_eng_to_pol(self, word: WordDict) -> str:
        return input(f"Please translate the English word: '{word['ENG']}' to Polish: ")

    def display_correct(self):
        """Display a message when the user's answer is correct."""
        print("Correct!")

    def display_wrong(self):
        """Display a message when the user's answer is wrong."""
        print("Wrong!")  # TODO: display the correct answer

    def display_quiz_summary(self, hand: Hand) -> None:
        print(
            "================================================\n"
            "Quiz Summary\n"
            "================================================"
        )
        for word in hand.words:
            print(f"{word['ENG']}: {word['PL']['stars']}")
        print(
            "================================================\n"
        )
