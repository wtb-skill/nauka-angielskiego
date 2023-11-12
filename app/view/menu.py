from app.model.menu import Menu


class MenuView:
    def __init__(self) -> None:
        self.menu = Menu()

    def display_menu(self) -> None:
        print(
            "================================================\n"
            "3000 most common English words App\n"
            "================================================"
        )
        for number, item in self.menu.main_menu.items():
            print(f"[{number}]: {item}")
