from app.model.word import Word
from typing import List, Dict


class WordListCreator:
    def __init__(self, data: List[Dict]) -> None:
        self.data = data
        self.words = self.create_list_of_words()

    @staticmethod
    def _create_word(word_dict: Dict) -> Word:
        word = Word(
            eng=word_dict['ENG'],
            pol=word_dict['PL'],
            stars=word_dict['stars']
            )
        return word

    def create_list_of_words(self) -> List[Word]:
        words = []
        for word_data in self.data:
            _word = self._create_word(word_data)
            words.append(_word)
        return words



