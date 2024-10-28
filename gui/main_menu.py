import tkinter as tk
from gui.game_screen import GameScreen
from gui.two_player_game_screen import TwoPlayerGameScreen

class MainMenu:
    def __init__(self, root):
        self.root = root
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Welcome to Blackjack!", font=("Arial", 20)).pack(pady=20)

        single_player_button = tk.Button(self.root, text="Play vs Dealer", command=self.start_single_player, font=("Arial", 14))
        single_player_button.pack(pady=10)

        multiplayer_button = tk.Button(self.root, text="Player vs Player", command=self.start_multiplayer, font=("Arial", 14))
        multiplayer_button.pack(pady=10)

        quit_button = tk.Button(self.root, text="Quit", command=self.root.quit, font=("Arial", 14))
        quit_button.pack(pady=10)

    def start_single_player(self):
        self.clear_screen()
        GameScreen(self.root, self.show_main_menu)

    def start_multiplayer(self):
        self.clear_screen()
        TwoPlayerGameScreen(self.root, self.show_main_menu)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_main_menu(self):
        self.clear_screen()
        self.create_widgets()
