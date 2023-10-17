from typing import List, Dict
from random import randint
import json

STARTER = "3000-Most-Common-English-Words"
TO_LEARN = "words_to_learn.json"
HAND = "words_in_hand.json"


class Model:

    def __init__(self):
        self.starting_list = self.get_starting_list()
        self.words_to_learn = self.get_words_to_learn()
        self.hand = self.get_hand()

    @staticmethod
    def get_starting_list() -> List[Dict[str, str]]:
        with open(STARTER, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def get_words_to_learn(self):
        try:
            with open(TO_LEARN, "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = self.starting_list
        return data

    def get_hand(self):
        try:
            with open(HAND, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = self.draw_10_words()
        return data

    def draw_10_words(self):
        words_in_hand = []
        for _ in range(0, 10):
            word = self.words_to_learn[randint(0, len(self.words_to_learn))]
            words_in_hand.append(word)
            self.update_words_to_learn(word)
        return words_in_hand

    def update_words_to_learn(self, word):
        self.words_to_learn.remove(word)

    def update_words_in_hand(self, word):
        if word in self.hand:
            self.hand.remove(word)
        else:
            self.hand.append(word)

    def save_hand(self):
        with open(HAND, 'w', encoding='utf-8') as file:
            json.dump(self.hand, file)

    def save_to_learn(self):
        with open(TO_LEARN, 'w', encoding='utf-8') as file:
            json.dump(self.words_to_learn, file)

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
    # model.get_words_to_learn()
    print(model.words_to_learn)
    model.save_to_learn()
