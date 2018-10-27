import random

cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
def hand_total(hand):
    values = [None, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10]
    value_map = {k: v for k, v in zip(cards, values)}

    total = sum([value_map[card] for card in hand if card != 'A'])
    ace_count = hand.count('A')

    for i in range(ace_count, -1, -1):
        if i == 0:
            total = total + ace_count
        elif total + (i * 11) + (ace_count - i) <= 21:
            total = total + (i * 11) + ace_count - i
            break

    return total


def next_card():
    return random.choice(cards)

class Dealer():
    def __init__(self):
        self.hand = []
        self.total = 0

    def new_round(self):
        self.hand =[next_card(),next_card()]

    def get_hand_total(self):
        return hand_total(self.hand)

    def determine_play(self, total):
        if int(total) < 17:
            return 'hit'
        else:
            return 'stand'

