class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
       
        if card:
            self.hand.append(card)
            print(f"{self.name} drew {card}")
            
    def get_score(self):
        
        score = 0
        aces = 0
        for card in self.hand:
            rank = card.split(" ")[0]
            if rank in ["Jack", "Queen", "King"]:
                score += 10
            elif rank == "Ace":
                aces += 1
                score += 11
            else:
                score += int(rank)

        while score > 21 and aces:
            score -= 10
            aces -= 1

        return score
