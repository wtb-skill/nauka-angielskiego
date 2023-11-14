from typing import Dict, Union


class View:

    # Define a type hint for a single word dictionary
    WordDict = Dict[str, Union[str, Dict[str, Union[str, int]]]]

    def __init__(self):
        pass

    @staticmethod
    def quiz_eng_to_pol(word: WordDict) -> str:
        """Ask the user to translate an English word to Polish and return their answer."""
        user_answer = input(f"Please translate the English word: '{word['ENG']}' to Polish: ")
        return user_answer

    @staticmethod
    def quiz_pol_to_eng(word: WordDict) -> str:
        """Ask the user to translate a Polish word to English and return their answer."""
        user_answer = input(f"Please translate the Polish word: '{word['PL']['translation']}' to English: ")
        return user_answer

    @staticmethod
    def word_mastered(word: WordDict):
        """Display a message when a word is mastered."""
        print(f"The word: '{word['ENG']}' got mastered!")

    @staticmethod
    def new_word(word: WordDict):
        """Display a new word for the user to learn."""
        print(f"The new word for you to learn is: '{word['ENG']}'!")

    @staticmethod
    def display_word(word: WordDict):
        """Display an English word and its Polish translation."""
        print(f"English: {word['ENG']:<15} Polish: {word['PL']['translation']:<15}")

    @staticmethod
    def display_correct():
        """Display a message when the user's answer is correct."""
        print("Correct!")

    @staticmethod
    def display_wrong():
        """Display a message when the user's answer is wrong."""
        print("Wrong!")

    @staticmethod
    def display_menu():
        """Display the main menu of the application."""
        menu = """
================================================
  3000 most common English words App
================================================
[1] Quiz
[2] View Current Words
[3] View Mastered Words
[4] Exit
        """
        print(menu)

    @staticmethod
    def menu_option() -> int:
        """Prompt the user to enter a menu option and return the chosen option as an integer."""
        user_input = input("Please enter the number corresponding to your choice: ")
        return int(user_input)

    @staticmethod
    def quiz_completed():
        """Display a message when the user has already completed the quiz for the day."""
        print("You have already completed the quiz for today. Come back tomorrow! <3")

