from app.model.word import Word


class MessagesView:

    @staticmethod
    def display_word(word: Word):
        """Display an English word and its Polish translation."""
        print(f"English: {word.eng:<15} Polish: {word.pol:<15}")


