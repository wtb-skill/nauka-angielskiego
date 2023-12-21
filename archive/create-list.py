import json
from typing import List, Dict, Tuple


def get_eng_list():
    with open("../VocabularyData/3000-English-words.txt", encoding="utf-8") as file:
        lines = file.readlines()
    list_of_3000_words = [line.strip() for line in lines]
    return list_of_3000_words


def get_pol_list():
    with open("../VocabularyData/3000-Polish-words.txt", encoding="utf-8") as file:
        lines = file.readlines()
    list_of_3000_words = [line.strip() for line in lines]
    return list_of_3000_words


if __name__ == "__main__":
    eng_list = get_eng_list()
    pol_list = get_pol_list()

    eng_3000_translations: List[Dict[str, str | int]] = [
        {"ENG": eng_word, "PL": pol_word, "stars": 0}
        for eng_word, pol_word in zip(eng_list, pol_list)
    ]

    with open(
        "../VocabularyData/3000-Most-Common-English-Words.json", "w", encoding="utf-8"
    ) as file:
        json.dump(eng_3000_translations, file)
