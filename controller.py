from model import Model
from view import View
from pathlib import Path


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def first_run(self):
        for _ in range(0, 10):
            new_word = self.model.draw_one_word()
            self.view.new_word(new_word)

    def quiz(self):
        for _word in self.model.hand:
            self.ask_translation(_word)
        self.model.save_hand()

    def ask_translation(self, _word):
        if self.model.star_number(_word) < 3:
            user_answer = self.view.quiz_eng_to_pol(_word)
            if user_answer == _word['PL']['translation']:
                self.view.display_correct()
                self.model.star_add(_word)
            else:
                self.view.display_wrong()
                self.model.star_remove(_word)
        else:
            user_answer = self.view.quiz_pol_to_eng(_word)
            if user_answer == _word['ENG']:
                self.view.display_correct()
                self.model.star_add(_word)
            else:
                self.view.display_wrong()
                self.model.star_remove(_word)

    def word_is_mastered(self, _word):
        if self.model.star_number(_word) == 6:
            self.view.word_mastered(_word)
            self.model.update_words_mastered(_word)
            self.model.update_words_in_hand(_word)
            new_word = self.model.draw_one_word()
            self.view.new_word(new_word)

    def check_words_for_mastery(self):
        for _word in self.model.hand:
            self.word_is_mastered(_word)

    def it_is_first_run(self):
        if Path(self.model.HAND).is_file():
            return False
        else:
            return True

    def display_hand(self):
        for _word in self.model.hand:
            self.view.display_word(_word)

    def display_words_mastered(self):
        for _word in self.model.words_mastered:
            self.view.display_word(_word)

    def first_quiz_today(self):
        if self.model.get_quiz_date()["data"] == self.model.today():
            return False
        else:
            return True


if __name__ == "__main__":
    controller = Controller()
    if controller.it_is_first_run():
        controller.first_run()
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

# TODO 1: Add more leeway for the user to input words- no case sensitivity, allow single letter spelling mistakes.
# TODO 1: Add docstrings and type hints.






