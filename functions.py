

# Spades, Hearts, Diamonds, Clubs
# AS = Ace of Spades
# JS = Jack of Spades


def deck(rules):
    deck_of_cards = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    playable_deck = []
    if rules == 'Blackajck++':
        for suit in ['S', 'H', 'D', 'C']:
            playable_deck += [f'{card}{suit}' for card in deck_of_cards]
        playable_deck += ['Joker', 'Joker'] #Adicionando os Jokers
        playable_deck += ['GC','SC'] #Adicionando a Golden Card e a Skull Card
    else:
        playable_deck += deck_of_cards * 4

    return playable_deck



print(deck('Blackajck++'))