from src import Card, Deck, Player

two_of_hearts = Card('Hearts', 'Two')

new_deck = Deck()
new_deck.shuffle()

new_player = Player('Singh')

my_card = new_deck.deal_one()
new_player.add_cards([my_card,my_card])

print(new_player)
