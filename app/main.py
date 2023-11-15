from app.controller.word_list_creator import WordListCreator
from app.controller.words_data_manager import WordsDataManager
from app.model.vocabulary_data import *
from app.model.word_list import WordList, WordsInHand, WordsToLearn
from app.controller.quiz import QuizController
from app.controller.mastery import MasteryController
from app.controller.date import DateController


def run():
    date = DateController()
    if not date.was_test_done_today():
        quiz = QuizController()
        quiz.run_quiz()
        mastery = MasteryController()
        mastery.check_words_for_mastery()
        date.save_quiz_date()





