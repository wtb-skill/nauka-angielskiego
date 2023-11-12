from app.model.menu import Menu


class MenuController:
    def __init__(self) -> None:
        self._menu = Menu()

    def display_main_menu(self) -> None:
        #  TODO: This could be later extracted to a separate view,
        #   once we have more views.
        print(
            "================================================\n"
            "3000 most common English words App\n"
            "================================================"
        )
        for number, item in self._menu.main_menu.items():
            print(f"[{number}]: {item}")
