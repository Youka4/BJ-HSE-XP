import tkinter as tk
from PIL import Image, ImageTk
from blackjack.game import BlackjackGame
import os 
class GameScreen:
    def __init__(self, root, back_to_menu_callback):
        self.root = root
        self.back_to_menu_callback = back_to_menu_callback
        self.game = BlackjackGame()  
        self.game.start_game()       

        self.card_images = {}        
        self.player_card_labels = [] 
        self.dealer_card_labels = [] 

        self.create_widgets()
        self.update_display()

    def create_widgets(self):

        tk.Label(self.root, text="Blackjack Game", font=("Arial", 20)).pack(pady=20)

        self.dealer_frame = tk.Frame(self.root)
        self.dealer_frame.pack(pady=10)
        tk.Label(self.dealer_frame, text="Dealer's Cards:", font=("Arial", 14)).pack()

        self.player_frame = tk.Frame(self.root)
        self.player_frame.pack(pady=10)
        tk.Label(self.player_frame, text="Player's Cards:", font=("Arial", 14)).pack()

        self.hit_button = tk.Button(self.root, text="Hit", command=self.player_hit, font=("Arial", 14))
        self.hit_button.pack( padx=10)

        self.stand_button = tk.Button(self.root, text="Stand", command=self.dealer_turn, font=("Arial", 14))
        self.stand_button.pack( padx=10)

        back_button = tk.Button(self.root, text="Back to Menu", command=self.back_to_menu_callback, font=("Arial", 14))
        back_button.pack(side=tk.BOTTOM, pady=20)

    def player_hit(self):
        self.game.player_hit()
        self.update_display()
        if self.game.game_over:
            self.end_game("Player busts! Dealer wins.")

    def dealer_turn(self):
       
        self.game.dealer_turn()
        self.update_display()
        if self.game.game_over:
            winner_message = self.get_winner_message()
            self.end_game(winner_message)

    def update_display(self):
       
        self.clear_card_labels(self.player_card_labels)
        self.player_card_labels = self.display_cards(self.game.player.hand, self.player_frame)

        
        self.clear_card_labels(self.dealer_card_labels)
        self.dealer_card_labels = self.display_cards(self.game.dealer.hand, self.dealer_frame)

    def display_cards(self, hand, frame):
        
        card_labels = []
        for index, card_name in enumerate(hand):
            card_image = self.load_card_image(card_name)
            card_label = tk.Label(frame, image=card_image)
            card_label.image = card_image  
            card_label.pack(side=tk.LEFT, padx=(0 if index == 0 else 10, 0)) 
            card_labels.append(card_label)
        return card_labels

    def load_card_image(self, card_name):
        

        image_path = os.path.join("assets", "images", "cards", f"{card_name}.png")

        try:
            image = Image.open(image_path)
            image = image.resize((100, 150))  
            return ImageTk.PhotoImage(image)
        except FileNotFoundError:
            print(f"Image not found for {card_name}")
            return None

    def clear_card_labels(self, labels):
        
        for label in labels:
            label.pack_forget()

    def end_game(self, message):
        
        self.hit_button.config(state=tk.DISABLED)
        self.stand_button.config(state=tk.DISABLED)
        result_label = tk.Label(self.root, text=message, font=("Arial", 16), fg="red")
        result_label.pack(pady=20)

    def get_winner_message(self):
        
        player_score = self.game.player.get_score()
        dealer_score = self.game.dealer.get_score()

        if player_score > 21:
            return "Player busts! Dealer wins."
        elif dealer_score > 21 or player_score > dealer_score:
            return "Player wins!"
        elif player_score < dealer_score:
            return "Dealer wins!"
        else:
            return "It's a tie!"
