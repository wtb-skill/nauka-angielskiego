import json
from copy import deepcopy

from app.model.words_to_learn import WordDict


class Hand:
    _PATH = 'VocabularyData/words_in_hand.json'

    def __init__(self):
        # A bit more advanced comment - keeping the list of words in a mutable
        #  data structure like a list is not a good idea.
        #  If it gets modified anywhere in the code, it will be modified everywhere.
        #  The same applies to the dict. It's better to create classes for these
        #  data structures to ensure immutability.
        #  good read - https://realpython.com/python-mutable-vs-immutable-types/
        self._initialize_hand()

    def _initialize_hand(self) -> None:
        """Load the words currently in the user's hand from a file
        or return an empty list if not found."""
        try:
            with open(self._PATH, 'r', encoding='utf-8') as file:
                self._words = json.load(file)
        except FileNotFoundError:
            self._words = []

    @property
    def exists(self) -> bool:
        return len(self._words) > 0

    @property
    def words(self) -> list[WordDict]:
        return deepcopy(self._words)

    def add_word(self, new_word: WordDict) -> None:
        self._words.append(new_word)

    def remove_word(self, word: WordDict) -> None:
        self._words.remove(word)

    def increase_word_score(self, word: WordDict) -> None:
        # TODO: This is quite ineffective, it'd be better if the words were stored
        #  in a dict with the word as a key.
        for _word in self._words:
            if _word['ENG'] == word['ENG']:
                _word['PL']['stars'] += 1
                break

    def decrease_word_score(self, word: WordDict) -> None:
        for _word in self._words:
            if _word['ENG'] == word['ENG'] and _word['PL']['stars'] > 0:
                _word['PL']['stars'] -= 1
                break

    def save(self) -> None:
        with open(self._PATH, 'w', encoding='utf-8') as f:
            json.dump(self._words, f)
