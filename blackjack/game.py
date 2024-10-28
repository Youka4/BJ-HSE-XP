from blackjack.player import Player
from blackjack.deck import Deck
from blackjack.bot import DealerBot



class BlackjackGame:
    def __init__(self, is_two_player=False):
        self.deck = Deck()
        self.is_two_player = is_two_player
        if is_two_player:
            self.player = Player("Player1")
            self.player2 = Player("Player2")
            self.dealer = None
        else:
            self.player = Player("Player")
            self.dealer = DealerBot("Dealer")
            self.player2 = None
        self.game_over = False

    def start_game(self):
        if self.is_two_player :
            self.get_two_cards(self.player2)
        else:
            self.get_two_cards(self.dealer)
        self.get_two_cards(self.player)

    def get_two_cards(self, player: Player):
        player.add_card(self.deck.draw_card())
        player.add_card(self.deck.draw_card())

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
