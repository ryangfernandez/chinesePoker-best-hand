class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"card('{self.rank}', '{self.suit}')"
    
    def value(self):
        ranks = '23456789tjqka'
        return ranks.index(self.rank) + 2
    
