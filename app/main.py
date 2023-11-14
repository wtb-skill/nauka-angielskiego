from app.controller.create_list_of_words import WordListCreator
from app.controller.words_data_manager import WordsDataManager
from app.model.vocabulary_data import *
from app.model.word_list import WordsInHand


def run():
    # Example usage
    words_to_learn_manager = WordsDataManager(VocabularyData.TO_LEARN)
    words_to_learn = words_to_learn_manager.create_word_list()

    words_in_hand_manager = WordsDataManager(VocabularyData.HAND)
    words_in_hand = words_in_hand_manager.create_word_list()

    random_word = words_to_learn.choose_random_word()
    # print(random_word)
    print(words_in_hand.size)
    print(words_to_learn.size)
    words_in_hand.update_word(random_word)
    words_to_learn.update_word(random_word)

    # for word in words_in_hand.words:
    #     print(word)
    words_to_learn_manager.save_word_list(words_to_learn)
    words_in_hand_manager.save_word_list(words_in_hand)

    print(words_in_hand.size)
    print(words_to_learn.size)
    for word in words_in_hand.words:
        print(word)
