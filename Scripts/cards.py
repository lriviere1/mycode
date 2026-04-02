class Card:
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]

    def __init__(self, rank, suit, face_up=True):
        self.rank = rank
        self.suit = suit
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            return self.rank + self.suit
        else:
            return "XX"

    def flip(self):
        self.is_face_up = not self.is_face_up


class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            return "\t".join(str(card) for card in self.cards)
        else:
            return "<empty>"

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)


class Deck(Hand):
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand=1):
        for _ in range(per_hand):
            for hand in hands:
                if self.cards:
                    hand.add(self.cards.pop())
                else:
                    print("Out of cards!")