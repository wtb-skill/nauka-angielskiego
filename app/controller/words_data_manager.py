from app.controller.word_list_creator import WordListCreator
from app.model.word_list import WordList, WordsInHand, WordsMastered, WordsToLearn
from app.model.file_manager import FileManager
from app.model.vocabulary_data import *
from typing import List, Dict, Type


class WordsDataManager:
    # simple version:
    # def __init__(self, filename: str):
    #     self.filename = filename
    #     self.file_manager = FileManager(self.filename)

    def __init__(self, word_list_class: Type[WordList]) -> None:
        self.word_list_class = word_list_class

        name = word_list_class.__name__[5:].upper()
        self.filename = f'{getattr(VocabularyData, name)}'
        self.file_manager = FileManager(self.filename)

    def load_words_data(self) -> List[Dict]:
        """Load words data from a JSON file."""
        return self.file_manager.load()

    # simple version:
    # def create_word_list(self) -> WordList:
    #     """Create a WordList instance from the loaded data."""
    #     word_list_data = self.load_words_data()
    #     word_list_creator = WordListCreator(word_list_data)
    #     return WordList(word_list_creator.words)

    def create_word_list(self) -> WordList | WordsInHand | WordsMastered | WordsToLearn:
        """Create a WordList instance from the loaded data."""
        word_list_data = self.load_words_data()
        word_list_creator = WordListCreator(word_list_data)
        return self.word_list_class(word_list_creator.words)

    def save_word_list(self, words: WordList) -> None:
        """Save WordList data to a JSON file."""
        words_data = [word.to_dict() for word in words.words]
        self.file_manager.save(words_data)
