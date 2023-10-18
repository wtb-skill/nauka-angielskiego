from random import randint
import json
from datetime import datetime
from typing import List, Dict, Union


class Model:

    # Define a type hint for a single word dictionary
    WordDict = Dict[str, Union[str, Dict[str, Union[str, int]]]]

    STARTER = "VocabularyData/3000-Most-Common-English-Words"
    TO_LEARN = "VocabularyData/words_to_learn.json"
    HAND = "VocabularyData/words_in_hand.json"
    MASTERED = "VocabularyData/words_mastered.json"
    SETTINGS = "VocabularyData/settings.json"

    def __init__(self):
        """Initialize the Model by loading data and settings."""
        self.starting_list = self.get_starting_list()
        self.words_to_learn = self.get_words_to_learn()
        self.hand = self.get_hand()
        self.words_mastered = self.get_words_mastered()
        self.quiz_date = self.get_quiz_date()

    def get_starting_list(self) -> List[WordDict]:
        """Load the starting list of words from a file."""
        with open(self.STARTER, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def get_words_to_learn(self) -> List[WordDict]:
        """Load the words to learn from a file or use the starting list if not found."""
        try:
            with open(self.TO_LEARN, "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = self.starting_list
        return data

    def get_hand(self) -> List[WordDict]:
        """Load the words currently in the user's hand from a file or return an empty list if not found."""
        try:
            with open(self.HAND, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []
        return data

    def get_words_mastered(self) -> List[WordDict]:
        """Load the words that the user has mastered from a file or return an empty list if not found."""
        try:
            with open(self.MASTERED, "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []
        return data

    def draw_one_word(self) -> WordDict:
        """Draw a random word from the words to learn and update the hand."""
        word = self.words_to_learn[randint(0, len(self.words_to_learn))]
        self.update_words_in_hand(word)
        self.update_words_to_learn(word)
        return word

    def update_words_to_learn(self, word: WordDict):
        """Update the words to learn by removing a word from the list."""
        self.words_to_learn.remove(word)
        self.save_to_learn()

    def update_words_in_hand(self, word: WordDict):
        """Update the words in hand by adding or removing a word."""
        if word in self.hand:
            self.hand.remove(word)
        else:
            self.hand.append(word)
        self.save_hand()

    def update_words_mastered(self, word: WordDict):
        """Update the words that the user has mastered by adding a word."""
        self.words_mastered.append(word)
        self.save_mastered()

    def save_hand(self):
        """Save the words in hand to a file."""
        with open(self.HAND, 'w', encoding='utf-8') as file:
            json.dump(self.hand, file)

    def save_to_learn(self):
        """Save the words to learn to a file."""
        with open(self.TO_LEARN, 'w', encoding='utf-8') as file:
            json.dump(self.words_to_learn, file)

    def save_mastered(self):
        """Save the words that the user has mastered to a file."""
        with open(self.MASTERED, 'w', encoding='utf-8') as file:
            json.dump(self.words_mastered, file)

    @staticmethod
    def star_add(word: WordDict):
        """Add a star to a word's status."""
        word['PL']['stars'] += 1

    @staticmethod
    def star_remove(word: WordDict):
        """Remove a star from a word's status, with a minimum value of 0."""
        word['PL']['stars'] -= 1
        word['PL']['stars'] = max(word['PL']['stars'], 0)

    @staticmethod
    def star_number(word: WordDict) -> int:
        """Get the number of stars in a word's status."""
        return word['PL']['stars']

    def get_quiz_date(self) -> Dict[str, str]:
        """Get the date of the last quiz from the settings or return a default value if not found."""
        try:
            with open(self.SETTINGS, "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {"data": "0"}
        return data

    def save_quiz_date(self):
        """Save the date of the last quiz to settings."""
        today = self.today()
        self.quiz_date = {"data": today}
        with open(self.SETTINGS, "w", encoding="utf-8") as file:
            json.dump(self.quiz_date, file)

    @staticmethod
    def today() -> str:
        """Get the current date in a string format (YYYY-MM-DD)."""
        today = str(datetime.today()).split(" ")[0]
        return today


if __name__ == "__main__":
    model = Model()
    # print(model.get_starting_list())
    # print(model.starting_hand)
    # model.get_hand()
    # model.save_hand()
    # model.get_words_to_learn()
    # print(model.words_to_learn)
    # model.save_to_learn()
    model.save_quiz_date()
    model.today()
