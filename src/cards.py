import random

# GLOBALS
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
# dictionary to store the values of cards
card_dict = {'Two': 2,
            'Three': 3,
            'Four': 4,
            'Five': 5,
            'Six': 6,
            'Seven': 7,
            'Eight': 8,
            'Nine': 9,
            'Ten': 10,
            'Jack': 11,
            'Queen': 12,
            'King': 13,
            'Ace': 14
            }

class Cards:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = card_dict[rank]

    def __str__(self):
        return self.rank + " of " + self.suit
