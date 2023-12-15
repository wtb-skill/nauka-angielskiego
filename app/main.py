from app.controller.quiz import QuizController as Quiz
from app.controller.mastery import MasteryController as Mastery
from app.controller.dates import DateController as Date
from app.controller.menu import MenuController as Menu
from app.controller.first_run import FirstRun
from app.controller.file_init import FileInitController as Initialize


def run():
    if Initialize().is_first_run:
        FirstRun()
    while True:
        Menu().display_menu()
        menu_option = Menu().get_user_input()
        if menu_option == 1:
            if Date().first_quiz_today():
                Quiz()
                Mastery()
                Date().save_quiz_date()
            else:
                Date().display_message_that_quiz_was_done_today()
        elif menu_option == 2:
            Menu().display_hand()
        elif menu_option == 3:
            Menu().display_words_mastered()
        else:
            break
