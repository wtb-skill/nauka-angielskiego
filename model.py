from random import randint
import json
from datetime import datetime
from typing import List, Dict, Union
import os


class VocabularyData:
    """Class for storing file paths."""
    STARTER = "VocabularyData/3000-Most-Common-English-Words"
    TO_LEARN = "VocabularyData/words_to_learn.json"
    HAND = "VocabularyData/words_in_hand.json"
    MASTERED = "VocabularyData/words_mastered.json"
    SETTINGS = "VocabularyData/settings.json"


class FileManager:
    """Class for managing loading and saving data."""
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []
        return data

    def save(self, data):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(data, file)


class Word:
    """Class for storing translations, nr of stars and managing stars."""
    def __init__(self, eng, pol, stars):
        self.eng = eng
        self.pol = pol
        self.stars = stars

    def __str__(self):
        return f"{self.eng}, {self.pol}, {self.stars}"

    def add_star(self):
        """Add a star to a word's status."""
        self.stars += 1

    def remove_star(self):
        """Remove a star from a word's status, with a minimum value of 0."""
        self.stars -= 1
        self.stars = max(self.stars, 0)

    def to_dict(self):
        """Return a dictionary representation of the Word object."""
        return {
            "ENG": self.eng,
            "PL": self.pol,
            "stars": self.stars
        }


class WordList:
    """Class for managing whole lists of Word objects. (load words, save words, add word, remove word,
    draw one random word)"""
    def __init__(self, file):
        self.file_manager = FileManager(file)
        self.data = self.file_manager.load()
        self.words = self.get_words()

    def get_words(self):
        words = []
        for entry in self.data:
            word = Word(
                eng=entry['ENG'],
                pol=entry['PL'],
                stars=entry['stars']
            )
            words.append(word)
        return words

    def add_word(self, word):
        self.words.append(word)

    def remove_word(self, word):
        self.words.remove(word)

    def update_word(self, word):
        if word in self.words:
            self.remove_word(word)
        else:
            self.add_word(word)
        self.save()  # not sure if it can be done smarter (logic: change occurs->save)

    def choose_random_word(self):
        random_word = self.words[randint(0, self.size)]
        return random_word

    def to_dict(self):
        self.data = []
        for word in self.words:
            self.data.append(word.to_dict())

    def save(self):
        self.to_dict()
        self.file_manager.save(self.data)

    @property
    def size(self):
        return len(self.words)


class WordsToLearn(WordList):
    def __init__(self, file=VocabularyData.TO_LEARN):
        if not os.path.exists(file):  # when there is no file, use STARTER as a word source
            file = VocabularyData.STARTER
        super().__init__(file)

    def save(self):
        self.file_manager.filename = VocabularyData.TO_LEARN  # when saving data, create TO_LEARN (instead of saving into STARTER)
        super().save()


class WordsInHand(WordList):
    def __init__(self, file=VocabularyData.HAND):
        super().__init__(file)


class WordsMastered(WordList):
    def __init__(self, file=VocabularyData.MASTERED):
        super().__init__(file)


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
OLD VERSION:
class Model:

    # Define a type hint for a single word dictionary
    WordDict = Dict[str, Union[str, Dict[str, Union[str, int]]]]
    
<ALREADY DONE>
    # STARTER = "VocabularyData/3000-Most-Common-English-Words"
    # TO_LEARN = "VocabularyData/words_to_learn.json"
    # HAND = "VocabularyData/words_in_hand.json"
    # MASTERED = "VocabularyData/words_mastered.json"
    # SETTINGS = "VocabularyData/settings.json"

    def __init__(self):
        """Initialize the Model by loading data and settings."""
        self.starting_list = self.get_starting_list()
        self.words_to_learn = self.get_words_to_learn()
        self.hand = self.get_hand()
        self.words_mastered = self.get_words_mastered()
        self.quiz_date = self.get_quiz_date()
        
<ALREADY DONE>
    def get_starting_list(self, path=STARTER) -> List[WordDict]:
        """Load the starting list of words from a file."""
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

<ALREADY DONE>
    def get_words_to_learn(self, path=TO_LEARN) -> List[WordDict]:
        """Load the words to learn from a file or use the starting list if not found."""
        try:
            with open(path, "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = self.starting_list
        return data

<ALREADY DONE>
    def get_hand(self, path=HAND) -> List[WordDict]:
        """Load the words currently in the user's hand from a file or return an empty list if not found."""
        try:
            with open(path, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []
        return data

<ALREADY DONE>
    def get_words_mastered(self, path=MASTERED) -> List[WordDict]:
        """Load the words that the user has mastered from a file or return an empty list if not found."""
        try:
            with open(path, "r", encoding="utf-8") as file:
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

<ALREADY DONE>
    def save_hand(self, path=HAND):
        """Save the words in hand to a file."""
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(self.hand, file)

<ALREADY DONE>
    def save_to_learn(self, path=TO_LEARN):
        """Save the words to learn to a file."""
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(self.words_to_learn, file)

<ALREADY DONE>
    def save_mastered(self, path=MASTERED):
        """Save the words that the user has mastered to a file."""
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(self.words_mastered, file)


<ALREADY DONE>
    @staticmethod
    def star_number(word: WordDict) -> int:
        """Get the number of stars in a word's status."""
        return word['PL']['stars']

<ALREADY DONE>
    def get_quiz_date(self, path=SETTINGS) -> Dict[str, str]:
        """Get the date of the last quiz from the settings or return a default value if not found."""
        try:
            with open(path, "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {"data": "0"}
        return data

<ALREADY DONE>
    def save_quiz_date(self, path=SETTINGS):
        """Save the date of the last quiz to settings."""
        today = self.get_current_date()
        self.quiz_date = {"data": today}
        with open(path, "w", encoding="utf-8") as file:
            json.dump(self.quiz_date, file)

<ALREADY DONE>
    @staticmethod
    def get_current_date() -> str:
        """Get the current date in a string format (YYYY-MM-DD)."""
        today = str(datetime.today()).split(" ")[0]
        return today
'''

if __name__ == "__main__":
    words_to_learn = WordsToLearn()
    words_in_hand = WordsInHand()
    print(words_in_hand.size)
    print(words_to_learn.size)
    word = words_to_learn.choose_random_word()
    words_to_learn.update_word(word)
    words_in_hand.update_word(word)
    print(words_in_hand.size)
    print(words_to_learn.size)

    # print(words_to_learn.size)
    # word_to_remove = words_to_learn.choose_random_word()
    # words_to_learn.remove_word(word_to_remove)
    # print(words_to_learn.size)
    # words_to_learn.save()




