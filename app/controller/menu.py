from app.view.menu import MenuView


class MenuController:
    def __init__(self) -> None:
        self.view = MenuView()

    def display_main_menu(self) -> None:
        self.view.display_menu()
