class View:
    def __init__(self):
        pass

    @staticmethod
    def quiz_eng_to_pol(word):
        user_answer = input(f"Please translate the English word: '{word['ENG']}' to Polish: ")
        return user_answer

    @staticmethod
    def quiz_pol_to_eng(word):
        user_answer = input(f"Please translate the Polish word: '{word['PL']['translation']}' to English: ")
        return user_answer

    @staticmethod
    def word_mastered(word):
        print(f"The word: '{word['ENG']}' got mastered!")

    @staticmethod
    def new_word(word):
        print(f"The new word for you to learn is: '{word['ENG']}'!")

    @staticmethod
    def display_word(word):
        print(f"English: {word['ENG']:<15} Polish: {word['PL']['translation']:<15}")

    @staticmethod
    def display_correct():
        print("Correct!")

    @staticmethod
    def display_wrong():
        print("Wrong!")

    @staticmethod
    def display_menu():
        menu = """
================================================
  3000 most common English words App
================================================
[1] Quiz
[2] View Current Words 
[3] View Mastered Words 
[4] Exit 
        """
        print(menu)

    @staticmethod
    def menu_option():
        user_input = input("Please enter the number corresponding to your choice: ")
        return int(user_input)

    @staticmethod
    def quiz_completed():
        print("You have already completed the quiz for today.Come back tomorrow! <3")

