class Card:

    #.lower used for consistency 
    def __init__(self, rank, suit):
        self.rank = rank.lower()
        self.suit = suit.lower()

    #representation for debugging
    def __repr__(self):
        return f"card('{self.rank}', '{self.suit}')"
    
    #string representation used for uniqueness comparison
    def __str__(self):
        return f"'{self.rank}{self.suit}'"
    
    #function for getting the value of card as an int
    def value(self):
        ranks = '23456789tjqka'
        return ranks.index(self.rank) + 2
    
def validate_input(str_input):

    #accepted values
    ranks = '23456789tjqka'
    suits = 'cshd'

    while True:
        split_str = str_input.split()
        #first check for if there are 13 elements once the string is split
        if (len(split_str) != 13):
            str_input = input("Input not recognised, please enter 13 cards: ")
            continue

        #second check for if all elements are 2 in length and each character is an accepted value
        if not all(len(card) == 2 and card[0] in ranks and card[1] in suits for card in split_str):
            str_input = input("Input not recognised, please enter 13 cards: ")
            continue

        #cards can now be parsed for the final check
        cards = [Card(card[0], card[1]) for card in split_str]

        #i am unfamiliar with __eq__ and __hash__ in classes so i utilised a basic uniqueness check using the __str__ definitions
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
        
        #if it returns, the input is valid
        return cards

str_input = input("Please enter 13 cards: ")
cards = validate_input(str_input)

print(cards)