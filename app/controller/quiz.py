from app.model.hand import Hand
from app.model.words_to_learn import WordDict, WordsToLearn
from app.view.quiz import QuizView


class QuizController:
    def __init__(self) -> None:
        # We use underscore to mark a variable as private.
        # Meaning it should not be accessed directly from outside the class.
        self._view = QuizView()
        self._hand = Hand()
        self._words_to_learn = WordsToLearn()

    def run_quiz(self) -> None:
        if not self._hand.exists:
            self._initialize()

        for word in self._hand.words:
            answer = self._view.display_quiz_eng_to_pol(word)
            if self._is_polish_translation_valid(answer=answer, word=word):
                self._view.display_correct()
                self._hand.increase_word_score(word)
            else:
                self._view.display_wrong()
                self._hand.decrease_word_score(word)
        self._hand.save()
        self._view.display_quiz_summary(self._hand)

    def _is_polish_translation_valid(self, answer: str, word: WordDict) -> bool:
        # It's good to extract the logic to a separate method like this
        #  then it's easier to understand the business logic in the run_quiz() method.
        #  however this could be a method of the Word class if it existed.
        #  Then you can do: word.is_polish_translation_valid(answer)
        return answer.lower() == word['PL']['translation'].lower()

    def _initialize(self) -> None:
        """
        Initiates the first run of the application
        by putting 10 new words in hand.
        """
        for _ in range(0, 10):
            new_word = self._words_to_learn.get_word()
            self._hand.add_word(new_word)
