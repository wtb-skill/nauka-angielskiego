from app.controller.words_data_manager import WordsDataManager
from app.model.word_list import WordsInHand, WordsToLearn, WordsMastered
from app.model.word import Word
from app.view.mastery import MasteryView


class MasteryController:
    def __init__(self) -> None:
        self._view = MasteryView()
        self._words_to_learn_manager = WordsDataManager(WordsToLearn)
        self._words_to_learn = self._words_to_learn_manager.create_word_list()
        self._words_in_hand_manager = WordsDataManager(WordsInHand)
        self._words_in_hand = self._words_in_hand_manager.create_word_list()
        self._words_mastered_manager = WordsDataManager(WordsMastered)
        self._words_mastered = self._words_mastered_manager.create_word_list()
        self._check_words_for_mastery()

    def _is_mastered(self, word: Word) -> None:
        """
        Checks if a word is mastered and updates its status accordingly.
        """
        if word.stars == 6:
            self._view.display_word_is_mastered(word)
            self._words_mastered.update_word(word)
            self._words_in_hand.update_word(word)
            new_word = self._words_to_learn.choose_random_word()
            print(new_word)
            self._words_in_hand.update_word(new_word)
            self._words_to_learn.update_word(new_word)
            self._words_to_learn_manager.save_word_list(self._words_to_learn)
            self._words_in_hand_manager.save_word_list(self._words_in_hand)
            self._words_mastered_manager.save_word_list(self._words_mastered)

    def _check_words_for_mastery(self) -> None:
        """Checks words in the hand for mastery and updates their status."""
        for word in self._words_in_hand.words:
            self._is_mastered(word)
