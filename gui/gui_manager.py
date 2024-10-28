
import tkinter as tk
from .main_menu import MainMenu
from .game_screen import GameScreen

class GUIManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Blackjack")
        self.root.geometry("600x400")
        self.show_main_menu()

    def show_main_menu(self):
        self.clear_screen()
        main_menu = MainMenu(self.root, self.show_game_screen)

    def show_game_screen(self):
        self.clear_screen()
        game_screen = GameScreen(self.root, self.show_main_menu)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = GUIManager(root)
    root.mainloop()
