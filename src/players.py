class Player:

    def __init__(self, name):
        self.name = name
        self.cards = []

    def remove_one(self):
        return self.cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.cards.extend(new_cards)
        else:
            self.cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.cards)} cards.'
