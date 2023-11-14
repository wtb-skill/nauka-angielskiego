from app.controller.word_list_creator import WordListCreator
from app.controller.words_data_manager import WordsDataManager
from app.model.vocabulary_data import *
from app.model.word_list import WordList, WordsInHand, WordsToLearn, WordsMastered
from app.model.word import Word


class QuizController:
    def __init__(self) -> None:
        # self._view = QuizView()
        self._words_to_learn_manager = WordsDataManager(WordsToLearn)
        self._words_to_learn = self._words_to_learn_manager.create_word_list()
        self._words_in_hand_manager = WordsDataManager(WordsInHand)
        self._words_in_hand = self._words_in_hand_manager.create_word_list()
        self._words_mastered = WordsDataManager(WordsMastered)
        self._words_mastered = self._words_mastered.create_word_list()

    def run_quiz(self) -> None:

    #     if not self._hand.exists:
    #         self._initialize()

        for word in self._words_in_hand.words:
            answer = self._view.display_quiz_eng_to_pol(word)
            if self._is_polish_translation_valid(answer=answer, word=word):
                self._view.display_correct()
                self._hand.increase_word_score(word)
            else:
                self._view.display_wrong()
                self._hand.decrease_word_score(word)
        self._hand.save()
        self._view.display_quiz_summary(self._hand)

    @staticmethod
    def _is_polish_translation_valid(answer: str, word: Word) -> bool:
        # It's good to extract the logic to a separate method like this
        #  then it's easier to understand the business logic in the run_quiz() method.
        #  however this could be a method of the Word class if it existed.
        #  Then you can do: word.is_polish_translation_valid(answer)
        return answer.lower() == word.pol.lower()

    def initialize(self) -> None:
        """
        Initiates the first run of the application
        by putting 10 new words in hand.
        """
        for _ in range(0, 10):
            new_word = self._words_to_learn.choose_random_word()
            self._words_in_hand.update_word(new_word)
            self._words_to_learn.update_word(new_word)
            self._words_to_learn_manager.save_word_list(self._words_to_learn)
            self._words_in_hand_manager.save_word_list(self._words_in_hand)


