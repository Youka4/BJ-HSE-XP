
import tkinter as tk

class MainMenu:
    def __init__(self, root, start_game_callback):
        self.root = root
        self.start_game_callback = start_game_callback
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Welcome to Blackjack!", font=("Arial", 20)).pack(pady=20)
        
        start_button = tk.Button(self.root, text="Start Game", command=self.start_game_callback, font=("Arial", 14))
        start_button.pack(pady=10)
        
        quit_button = tk.Button(self.root, text="Quit", command=self.root.quit, font=("Arial", 14))
        quit_button.pack(side=tk.BOTTOM, pady=10)
