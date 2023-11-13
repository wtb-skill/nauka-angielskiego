from app.model.model import Word


class CreateListOfWord:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def _create_word(word_dict):
        word = Word(
            eng=word_dict['ENG'],
            pol=word_dict['PL'],
            stars=word_dict['stars']
            )
        return word

    def create_list_of_words(self):
        words = []
        for word_data in self.data:
            _word = self._create_word(word_data)
            words.append(_word)
        return words



