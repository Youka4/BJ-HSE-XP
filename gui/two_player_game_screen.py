import tkinter as tk
from PIL import ImageTk, Image
from blackjack.game import BlackjackGame
import os

class TwoPlayerGameScreen:
    def __init__(self, root, back_to_menu_callback):
        self.root = root
        self.back_to_menu_callback = back_to_menu_callback
        self.game = BlackjackGame()
        self.game.start_game()      
        self.current_player = "Player 1" 

        self.card_images = {}       
        self.player1_card_labels = [] 
        self.player2_card_labels = [] 

        self.create_widgets()
        self.update_display()

    def create_widgets(self):

        tk.Label(self.root, text="Blackjack - Player vs Player", font=("Arial", 20)).pack(pady=20)

        self.player1_frame = tk.Frame(self.root)
        self.player1_frame.pack(pady=10)
        tk.Label(self.player1_frame, text="Player 1's Cards:", font=("Arial", 14)).pack()
        self.player1_score_label = tk.Label(self.root, text="Player 1 Score: 0", font=("Arial", 14))
        self.player1_score_label.pack()
        self.player2_frame = tk.Frame(self.root)
        self.player2_frame.pack(pady=10)
        tk.Label(self.player2_frame, text="Player 2's Cards:", font=("Arial", 14)).pack()
        self.player2_score_label = tk.Label(self.root, text="Player 2 Score: 0", font=("Arial", 14))
        self.player2_score_label.pack()
        self.hit_button = tk.Button(self.root, text="Hit", command=self.hit, font=("Arial", 14))
        self.hit_button.pack(side=tk.LEFT, padx=10)

        self.stand_button = tk.Button(self.root, text="Stand", command=self.switch_turn, font=("Arial", 14))
        self.stand_button.pack(side=tk.LEFT, padx=10)

        back_button = tk.Button(self.root, text="Back to Menu", command=self.back_to_menu_callback, font=("Arial", 14))
        back_button.pack(pady=20)

        self.current_player_label = tk.Label(self.root, text="Current Turn: Player 1", font=("Arial", 14), fg="blue")
        self.current_player_label.pack(pady=10)

    def hit(self):
        if self.current_player == "Player 1":
            self.game.player.add_card(self.game.deck.draw_card())
            self.update_display()
            if self.game.player.get_score() > 21:
                self.end_game("Player 1 busts! Player 2 wins.")
        else:
            self.game.dealer.add_card(self.game.deck.draw_card())
            self.update_display()
            if self.game.dealer.get_score() > 21:
                self.end_game("Player 2 busts! Player 1 wins.")

    def switch_turn(self):
        if self.current_player == "Player 1":
            self.current_player = "Player 2"
        else:
            self.current_player = "Player 1"
            player1_score=self.game.player.get_score()
            print(player1_score)
            self.current_player = "Player 2"
            player2_score=self.game.dealer.get_score()
            print(player2_score)
            if player1_score > player2_score:
                self.end_game("Player 1 wins.")
            elif player2_score > player1_score:
                self.end_game("Player 2 wins.")
            else:
                self.end_game("It's a tie!")

        self.current_player_label.config(text=f"Current Turn: {self.current_player}")

    def update_display(self):

        self.clear_card_labels(self.player1_card_labels)
        self.player1_card_labels = self.display_cards(self.game.player.hand, self.player1_frame)
        self.player1_score_label.config(text=f"Player 1 Score: {self.game.player.get_score()}")

        self.clear_card_labels(self.player2_card_labels)
        self.player2_card_labels = self.display_cards(self.game.dealer.hand, self.player2_frame)
        self.player2_score_label.config(text=f"Player 2 Score: {self.game.dealer.get_score()}")

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
