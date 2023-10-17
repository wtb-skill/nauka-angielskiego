from model import Model
from view import View

file_path = "words_in_hand"


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def first_run(self):
        self.model.save_to_learn()
        self.model.save_hand()

    def quiz(self):
        for word in self.model.hand:
            self.ask_translation(word)
        self.model.save_hand()

    def ask_translation(self, word):
        if self.model.star_number(word) <= 3:
            user_answer = self.view.quiz_eng_to_pol(word)
            if user_answer == word['PL']['translation']:
                print("YEP")  # move to view
                self.model.star_add(word)
            else:
                print("NOPE")  # move to view
                self.model.star_remove(word)
        else:
            user_answer = self.view.quiz_pol_to_eng(word)
            if user_answer == word['ENG']:
                print("YEP")  # move to view
                self.model.star_add(word)
            else:
                print("NOPE")  # move to view
                self.model.star_remove(word)

    def word_is_mastered(self, word):
        if self.model.star_number(word) == 7:
            self.view.word_mastered(word)
            self.model.update_words_mastered(word)
            self.model.update_words_in_hand(word)
            new_word = self.model.draw_one_word()
            self.view.new_word(new_word)

    def check_words_for_mastery(self):
        for word in self.model.hand:
            self.word_is_mastered(word)



if __name__ == "__main__":
    controller = Controller()
    controller.first_run()
    controller.quiz()
    controller.check_words_for_mastery()




# TODO 1✅: Import list of 3000 most common English words.
# TODO 2✅: First time use. User draws 10 random words from the list. The list is saved in a file.
# TODO 3✅: User is tested by being asked to translate eng->pol.
# TODO 4✅: User is tested by being asked to translate pol->eng.
# TODO 5✅: A word gains a star/point.
# TODO 6✅: A word loses a star/point.
# TODO 7✅: A word is mastered (6 stars achieved)- word goes to Mastered Pile. A new word is drawn from To-Learn List.
# TODO 7.5✅: And tell the user when a word is mastered and what a new word is.
# TODO 8: A word is shown to the user.
# TODO 9: User gets access to Menu:
#         - his hand and can view the words within.
#         - Mastered Pile and can view the words within.
#         - quiz
# TODO 11: Display word to the user when it first appears in the hand.



