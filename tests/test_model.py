import os, sys

sys.path.insert(0, os.getcwd())  # necessary order for tests to be placed in a subfolder
import pytest
from app.model.model import Model
from app.controller.controller import Controller
from pathlib import Path


def test_if_starting_list_exists():
    assert Path("../VocabularyData/3000-Most-Common-English-Words").is_file()


def test_is_hand_size_equal_to_10():
    model = Model()
    hand_size = model.hand
    assert len(hand_size) == 10 or len(hand_size) == 0


def test_is_words_mastered_being_created():
    model = Model()
    test_word = {"ENG": "test", "PL": {"translation": "test", "stars": 0}}
    model.update_words_mastered(test_word)
    assert Path("../VocabularyData/words_mastered.json").is_file()
    model.words_mastered.remove(test_word)
    model.save_mastered()


def test_if_the_star_count_is_correct():
    model = Model()
    for i in range(0, 7):
        test_word = {"ENG": "test", "PL": {"translation": "test", "stars": i}}
        assert model.star_number(test_word) == i


def test_if_stars_are_removed():
    model = Model()
    for i in range(0, 7):
        test_word = {"ENG": "test", "PL": {"translation": "test", "stars": i}}
        model.star_remove(test_word)
        assert model.star_number(test_word) == max(i - 1, 0)


def test_if_stars_are_added():
    model = Model()
    for i in range(0, 7):
        test_word = {"ENG": "test", "PL": {"translation": "test", "stars": i}}
        model.star_add(test_word)
        assert model.star_number(test_word) == i + 1


def test_is_word_mastered_when_it_reaches_6_stars():
    controller = Controller()
    test_word = {"ENG": "test", "PL": {"translation": "test", "stars": 6}}
    controller.word_is_mastered(test_word)
    pass


if __name__ == "__main__":
    pytest.main()

"""
- are all the files created?
- is the new data saved correctly?
- can you start the quiz more than once per day?
- when the word has 0, 1 or 2 stars is the user asked to translate from eng to pol?
- when the word has 3, 4, or 5 stars is the user asked to translate from pol to eng?
- is the word mastered when it reaches 6 stars?
- does the app know if it's the first time it's being used?
- are 10 words drawn when the app is run for the first time ever?
- when the word is mastered is the new word drawn?
- when the word is mastered does it appear in mastered list?
- when a word is drawn does it disappear from the to_learn list?
- during the quiz are stars being awarded or detracted depending on user answers?
- are there 10 questions during the quiz?
- do all the menu options work correctly?
- is the user answer judged correctly?
"""
