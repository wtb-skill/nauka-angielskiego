import json
import random
from typing import Union

# TODO: This should be a separate model, a QuizWord for example with
#  useful methods like increase_score(), validate_translation(), etc.
#  This would remove those responsibility from the Hand class.
WordDict = dict[str, Union[str, dict[str, Union[str, int]]]]


class WordsToLearn:
    # TODO: There is no point keeping the "stars" or other points in the source data.
    #  The points should be kept in the "hand" file only.
    #  The source data should be kept as simple as possible -
    #  e.g. {"sausage": "kiełbasa"}.

    _PATH = "VocabularyData/words_to_learn.json"
    _STARTING_LIST_PATH = "VocabularyData/3000-Most-Common-English-Words"

    def __init__(self) -> None:
        self._words = []
        self._load_from_file()

    def get_word(self) -> WordDict:
        return random.choice(self._words)

    def _load_from_file(self) -> None:
        try:
            with open(self._PATH, "r", encoding="utf-8") as f:
                self._words = json.load(f)
        except FileNotFoundError:
            self._words = self._get_default_list()

    def _get_default_list(self) -> list[WordDict]:
        with open(self._STARTING_LIST_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
