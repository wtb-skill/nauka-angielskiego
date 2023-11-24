from app.controller.quiz import QuizController
from app.controller.mastery import MasteryController
from app.controller.date import DateController
from app.controller.menu import MenuController


from app.controller.file_init import FileInitController


def run():
    fic = FileInitController()
    # Todo 1: Add initialise class to create files and check their integrity. (Karol)
    while True:
        menu = MenuController()
        menu.display_menu()
        menu_option = menu.get_user_input()
        if menu_option == 1:
            date = DateController()
            if date.first_quiz_today():
                quiz = QuizController()
                quiz.run_quiz()
                mastery = MasteryController()
                mastery.check_words_for_mastery()
                date.save_quiz_date()
            else:
                date.display_message_that_quiz_was_done_today()
        elif menu_option == 2:
            menu.display_hand()
        elif menu_option == 3:
            menu.display_words_mastered()
        else:
            break

    return fic






