from random import randint
from model import Model
from view import View
from pathlib import Path

file_path = "words_in_hand"


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def quiz(self):
        for word in self.model.hand:
            self.ask_translation(word)
        self.model.save_hand()

    def ask_translation(self, word):
        if self.model.star_number(word) <= 3:
            user_answer = self.view.quiz_eng_to_pol(word)
            if user_answer == word['PL']['translation']:
                print("YEP")
                self.model.star_add(word)
            else:
                print("NOPE")
                self.model.star_remove(word)
        else:
            user_answer = self.view.quiz_pol_to_eng(word)
            if user_answer == word['ENG']:
                print("YEP")
                self.model.star_add(word)
            else:
                print("NOPE")
                self.model.star_remove(word)


    # def is_it_first_activation(self):
    #     if Path(file_path).is_file():
    #         self.model.get_hand()
    #     else:
    #         self.model.draw_10_words()
    #         self.model.save_hand()


if __name__ == "__main__":
    controller = Controller()
    controller.quiz()




# TODO 1✅: Import list of 3000 most common English words.
# TODO 2✅: First time use. User draws 10 random words from the list. The list is saved in a file.
# TODO 3✅: User is tested by being asked to translate eng->pol.
# TODO 4✅: User is tested by being asked to translate pol->eng.
# TODO 5✅: A word gains a star/point.
# TODO 6✅: A word loses a star/point.
# TODO 7: A word is mastered (6 stars achieved)- word goes to Mastered Pile. A new word is drawn from To-Learn List.
# TODO 8: A word is shown to the user.
# TODO 9: User gets access to his hand and can view the words within.
# TODO 10: User gets access to Mastered Pile and can view the words within.
