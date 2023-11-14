from typing import List, Dict
from app.controller.create_list_of_words import WordListCreator
from app.model.word_list import WordList
from app.model.file_manager import FileManager


class WordsDataManager:
    def __init__(self, filename: str):
        self.filename = filename
        self.file_manager = FileManager(self.filename)

    def load_words_data(self) -> List[Dict]:
        """Load words data from a JSON file."""
        return self.file_manager.load()

    def create_word_list(self) -> WordList:
        """Create a WordList instance from the loaded data."""
        word_list_data = self.load_words_data()
        word_list_creator = WordListCreator(word_list_data)
        return WordList(word_list_creator.words)

    def save_word_list(self, words: WordList):
        """Save WordList data to a JSON file."""
        words_data = [word.to_dict() for word in words.words]
        self.file_manager.save(words_data)
