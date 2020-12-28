from src import Card, Deck, Player

# Assign two players to play the game
player_one = Player('One')
player_two = Player('Two')

# make a deck of 52 cards and shuffle them
new_deck = Deck()
new_deck.shuffle()

# distribute the cards evenly to 2 players
for card in range(52):
    if card % 2 == 0:
        player_one.add_cards(new_deck.deal_one())
    else:
        player_two.add_cards(new_deck.deal_one())


# WAR Game
game_on = True

round_num = 0

while game_on:
    round_num += 1
    print(f'Round {round_num}')

    # check if any player has no cards left to play
    if len(player_one.cards) == 0:
        print('Player One, out of cards ! Player Two Wins!')
        game_on = False
        break

    elif len(player_two.cards) == 0:
        print('Player Two, out of cards ! Player One Wins!')
        game_on = False
        break

    # Start putting the cards out
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    print(player_one_cards[-1])
    print(player_two_cards[-1])

    # war
    war_on = True

    while war_on:


        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            war_on = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            war_on = False

        else:
            print('WAR!')

            if len(player_one.cards) < 3:
                print('Player One is out of cards to play war')
                print('Player Two wins')
                game_on = False
                break

            elif len(player_two.cards) < 3:
                print('Player Two is out of cards to play war')
                print('Player One wins')
                game_on = False
                break

            else:
                for num in range(3):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
