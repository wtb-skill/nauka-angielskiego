from typing import List, Dict
from random import randint
import json

FILE = "3000-Most-Common-English-Words"
HAND = "words_in_hand"


class Model:

    def __init__(self):
        self.starting_list = self.get_starting_list()
        self.hand = self.get_hand()

    @staticmethod
    def get_starting_list():
        with open(FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def draw_10_words(self):
        words_in_hand = []
        for i in range(0, 10):
            word = self.starting_list[randint(0, 3000)]
            if word not in words_in_hand:
                words_in_hand.append(word)
        return words_in_hand

    def get_hand(self):
        try:
            with open(HAND, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = self.draw_10_words()
        return data

    def save_hand(self):
        with open("words_in_hand", 'w', encoding='utf-8') as file:
            json.dump(self.hand, file)

    @staticmethod
    def star_add(word):
        word['PL']['stars'] += 1

    @staticmethod
    def star_remove(word):
        word['PL']['stars'] -= 1
        word['PL']['stars'] = max(word['PL']['stars'], 0)

    @staticmethod
    def star_number(word):
        return word['PL']['stars']






if __name__ == "__main__":
    model = Model()
    # print(model.get_starting_list())
    # print(model.starting_hand)
    # model.get_hand()
    # model.save_hand()
    model.save_hand()
    print(model.hand)
