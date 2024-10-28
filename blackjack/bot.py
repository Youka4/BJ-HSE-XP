from .player import Player

class DealerBot(Player):
    def __init__(self, name="Dealer"):
        super().__init__(name)

    def decide_hit(self):
        return self.get_score() < 17  
