class MenuView:
    @staticmethod
    def display_menu() -> None:
        """Display the main menu of the application."""
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
    def menu_option() -> int:
        """Prompt the user to enter a menu option and return the chosen option as an integer."""
        user_input = input("Please enter the number corresponding to your choice: ")
        return int(user_input)
