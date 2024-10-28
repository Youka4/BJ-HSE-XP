
import tkinter as tk

class GameScreen:
    def __init__(self, root, back_to_menu_callback):
        self.root = root
        self.back_to_menu_callback = back_to_menu_callback
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Game Screen", font=("Arial", 20)).pack(pady=20)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)

        hit_button = tk.Button(button_frame, text="Hit", command=self.hit, font=("Arial", 14))
        hit_button.pack(side=tk.LEFT, padx=10)

        stand_button = tk.Button(button_frame, text="Stand", command=self.stand, font=("Arial", 14))
        stand_button.pack(side=tk.LEFT, padx=10)

        back_button = tk.Button(self.root, text="Back to Menu", command=self.back_to_menu_callback, font=("Arial", 14))
        back_button.pack(side=tk.BOTTOM, pady=20)

    def hit(self):
        # TODO: Placeholder for hit action
        print("Hit button pressed")

    def stand(self):
        # TODO: Placeholder for stand action
        print("Stand button pressed")
