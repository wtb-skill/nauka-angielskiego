from app.controller.words_data_manager import WordsDataManager
from app.model.word_list import WordsInHand, WordsToLearn
from app.model.word import Word
from app.view.quiz import QuizView


class QuizController:
    def __init__(self) -> None:
        self._view = QuizView()
        self._words_to_learn_manager = WordsDataManager(WordsToLearn)
        self._words_to_learn = self._words_to_learn_manager.create_word_list()
        self._words_in_hand_manager = WordsDataManager(WordsInHand)
        self._words_in_hand = self._words_in_hand_manager.create_word_list()

    def run_quiz(self) -> None:
        for word in self._words_in_hand.words:  # do not change it, it's the right quiz logic:
            self._ask_for_translation(word=word)
        self._words_in_hand_manager.save_word_list(self._words_in_hand)

    def _ask_for_translation(self, word):
        if word.stars < 3:
            self._ask_for_pol_translation(word=word)
        else:
            self._ask_for_eng_translation(word=word)

    def _ask_for_pol_translation(self, word):
        answer = self._view.display_quiz_eng_to_pol(word)
        if self._is_polish_translation_valid(answer=answer, word=word):
            self._view.display_correct()
            word.add_star()
        else:
            self._view.display_wrong()
            word.remove_star()

    def _ask_for_eng_translation(self, word):
        answer = self._view.display_quiz_pol_to_eng(word)
        if self._is_english_translation_valid(answer=answer, word=word):
            self._view.display_correct()
            word.add_star()
        else:
            self._view.display_wrong()
            word.remove_star()

    @staticmethod
    def _is_polish_translation_valid(answer: str, word: Word) -> bool:
        # It's good to extract the logic to a separate method like this
        #  then it's easier to understand the business logic in the run_quiz() method.
        #  however this could be a method of the Word class if it existed.
        #  Then you can do: word.is_polish_translation_valid(answer)
        return answer.lower() == word.pol.lower()

    @staticmethod
    def _is_english_translation_valid(answer: str, word: Word) -> bool:
        return answer.lower() == word.eng.lower()



