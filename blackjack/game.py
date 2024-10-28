from player import Player
from deck import Deck
from bot import DealerBot

class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player = Player("Player")
        self.dealer = DealerBot("Dealer")
        self.game_over = False

    def start_game(self):
        
        self.player.add_card(self.deck.draw_card())
        self.player.add_card(self.deck.draw_card())
        self.dealer.add_card(self.deck.draw_card())
        self.dealer.add_card(self.deck.draw_card())

    def player_hit(self):
        
        if not self.game_over:
            self.player.add_card(self.deck.draw_card())
            if self.player.get_score() > 21:
                self.game_over = True
                print("Player busts! Dealer wins.")

    def dealer_turn(self):
       
        while self.dealer.decide_hit():
            self.dealer.add_card(self.deck.draw_card())
        self.check_winner()

    def check_winner(self):
        
        player_score = self.player.get_score()
        dealer_score = self.dealer.get_score()
        
        if player_score > 21:
            print("Player busts! Dealer wins.")
        elif dealer_score > 21 or player_score > dealer_score:
            print("Player wins!")
        elif player_score < dealer_score:
            print("Dealer wins!")
        else:
            print("It's a tie!")
        self.game_over = True
