from app.archive.old_controller import Controller
from app.controller.menu import MenuController
from app.controller.quiz import QuizController


def setup():
    pass


def run_old():
    controller = Controller()
    while True:
        controller.view.display_menu()
        option = controller.view.menu_option()
        if option == 1:
            if controller.first_quiz_today():
                controller.quiz()
                controller.check_words_for_mastery()
                controller.model.save_quiz_date()
            else:
                controller.view.quiz_completed()
        elif option == 2:
            controller.display_hand()
        elif option == 3:
            controller.display_words_mastered()
        else:
            break


def run():
    menu_controller = MenuController()
    quiz_controller = QuizController()

    choice = None
    # It's better to avoid infinite loops if possible.
    while choice != "4":
        # You should never need to access the view directly from the main file.
        menu_controller.display_main_menu()
        choice = input("Choose option: ")
        if choice == "1":
            quiz_controller.run_quiz()
