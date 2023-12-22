from app.controller.words_data_manager import WordsDataManager
from app.model.word_list import WordsInHand, WordsToLearn
from app.view.quiz import QuizView


class FirstRun:
    def __init__(self) -> None:
        self._view = QuizView()
        self._words_to_learn_manager = WordsDataManager(WordsToLearn)
        self._words_to_learn = self._words_to_learn_manager.create_word_list()
        self._words_in_hand_manager = WordsDataManager(WordsInHand)
        self._words_in_hand = self._words_in_hand_manager.create_word_list()
        self._initialize()

    def _initialize(self) -> None:
        """Initiates the first run of the application by putting 10 new words in hand."""
        for _ in range(0, 10):
            new_word = self._words_to_learn.choose_random_word()
            print(new_word)
            self._words_in_hand.update_word(new_word)
            self._words_to_learn.update_word(new_word)
            self._words_to_learn_manager.save_word_list(self._words_to_learn)
            self._words_in_hand_manager.save_word_list(self._words_in_hand)
