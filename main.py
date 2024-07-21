class Card:
    def __init__(self, rank, suit):
        self.rank = rank.lower()
        self.suit = suit.lower()

    def __repr__(self):
        return f"card('{self.rank}', '{self.suit}')"
    
    def __str__(self):
        return f"'{self.rank}{self.suit}'"
    
    def value(self):
        ranks = '23456789tjqka'
        return ranks.index(self.rank) + 2
    
def validate_input(str_input):
    ranks = '23456789tjqka'
    suits = 'cshd'

    while True:
        split_str = str_input.split()
        if (len(split_str) != 13):
            str_input = input("Input not recognised, please enter 13 cards: ")
            continue

        if not all(len(card) == 2 and card[0] in ranks and card[1] in suits for card in split_str):
            str_input = input("Input not recognised, please enter 13 cards: ")
            continue

        cards = [Card(card[0], card[1]) for card in split_str]

        seen = []
        unique = True
        for card in cards:
            str_card = str(card)
            if str_card in seen:
                unique = False
                break
            seen.append(str(card))

        if not unique:
            str_input = input("Input not recognised, please enter 13 cards: ")
            continue
        
        return cards

str_input = input("Please enter 13 cards: ")
cards = validate_input(str_input)

print(cards)