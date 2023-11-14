from random import randint
from typing import List, Dict, Union
from app.model.word import Word
import os


class WordList:
    """Class for managing lists of Word objects. (size, add word, remove word, draw one random word)"""
    def __init__(self, words: List[Word]):
        self.words = words
        self.size = len(self.words)

    def _add_word(self, _word):
        self.words.append(_word)
        self.size += 1

    def _remove_word(self, _word):
        self.words.remove(_word)
        self.size -= 1

    def update_word(self, _word):
        if _word in self.words:
            self._remove_word(_word)
        else:
            self._add_word(_word)

    def choose_random_word(self):
        random_word = self.words[randint(0, self.size - 1)]
        return random_word


class WordsInHand(WordList):
    def __init__(self, words_in_hand_data):
        super().__init__(words_in_hand_data)

    def is_size_10(self):
        return self.size == 10


class WordsMastered(WordList):
    def __init__(self, words_mastered_data):
        super().__init__(words_mastered_data)


class WordsToLearn(WordList):
    def __init__(self, words_to_learn_data):
        super().__init__(words_to_learn_data)


'''
class WordList:
    """Class for managing lists of Word objects. (load words, save words, add word, remove word,
    draw one random word)"""
    def __init__(self, file):
        self.file_manager = FileManager(file)  # to controller
        self.data = self.file_manager.load()
        self.words = self.get_words()
        self.size = len(self.words)

    def get_words(self):
        words = []
        for entry in self.data:
            _word = Word(
                eng=entry['ENG'],
                pol=entry['PL'],
                stars=entry['stars']
            )
            words.append(_word)
        return words

    def add_word(self, _word):
        self.words.append(_word)
        self.size += 1

    def remove_word(self, _word):
        self.words.remove(_word)
        self.size -= 1

    def update_word(self, _word):
        if _word in self.words:
            self.remove_word(_word)
        else:
            self.add_word(_word)
        self.save()  # not sure if it can be done smarter (logic: change occurs->save)

    def choose_random_word(self):
        random_word = self.words[randint(0, self.size - 1)]
        return random_word

    def to_dict(self):
        self.data = []
        for _ in self.words:
            self.data.append(word.to_dict())

    def save(self):
        self.to_dict()
        self.file_manager.save(self.data)


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

    def is_size_10(self):
        return self.size == 10


class WordsMastered(WordList):
    def __init__(self, file=VocabularyData.MASTERED):
        super().__init__(file)
'''
