from app.controller.word_list_creator import WordListCreator
from app.controller.words_data_manager import WordsDataManager
from app.model.vocabulary_data import *
from app.model.word_list import WordList, WordsInHand, WordsToLearn


class FirstRun:
    words_to_learn_manager = WordsDataManager(WordsToLearn)
    words_to_learn = words_to_learn_manager.create_word_list()

    words_in_hand_manager = WordsDataManager(WordsInHand)
    words_in_hand = words_in_hand_manager.create_word_list()

    while not words_in_hand.check_if_size_is_10():
        # Choose a random word:
        random_word = words_to_learn.choose_random_word()

        # Update the Lists of Words:
        words_in_hand.update_word(random_word)
        words_to_learn.update_word(random_word)

    for word in words_in_hand.words:
        print(word)

    words_to_learn_manager.save_word_list(words_to_learn)
    words_in_hand_manager.save_word_list(words_in_hand)
