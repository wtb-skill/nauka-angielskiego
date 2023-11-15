from app.view.menu import MenuView
from app.controller.words_data_manager import WordsDataManager
from app.model.word_list import WordsInHand, WordsMastered


class MenuController:
    def __init__(self) -> None:
        self._menu = MenuView()
        self._words_in_hand_manager = WordsDataManager(WordsInHand)
        self._words_in_hand = self._words_in_hand_manager.create_word_list()
        self._words_mastered_manager = WordsDataManager(WordsMastered)
        self._words_mastered = self._words_mastered_manager.create_word_list()

    def display_menu(self):
        self._menu.display_menu()

    def get_user_input(self):
        return self._menu.menu_option()

    def display_hand(self):
        for word in self._words_in_hand.words:
            print(word)

    def display_words_mastered(self):
        for word in self._words_mastered.words:
            print(word)

