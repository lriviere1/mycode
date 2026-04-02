# Chapter 9, Challenge 1
# Blackjack Game (Improved + Bonus Game)
# Created by Labady Riviere

import cards, games
import random

class BJ_Card(cards.Card):
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v


class BJ_Deck(cards.Deck):
    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank, suit))


class BJ_Hand(cards.Hand):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super().__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep

    @property
    def total(self):
        for card in self.cards:
            if not card.value:
                return None

        t = sum(card.value for card in self.cards)

        contains_ace = any(card.value == BJ_Card.ACE_VALUE for card in self.cards)

        if contains_ace and t <= 11:
            t += 10

        return t

    def is_busted(self):
        return self.total > 21


class BJ_Player(BJ_Hand):
    def is_hitting(self):
        if self.total == 21:
            print("\n", self.name, "has Blackjack.")
            return False
        else:
            response = games.ask_yes_no(f"\n{self.name}, do you want a hit? (Y/N): ")
            return response == "y"

    def bust(self):
        print(self.name, "busts.")
        self.lose()

    def lose(self):
        print(self.name, "loses.")

    def win(self):
        print("🎉", self.name, "wins!")

    def push(self):
        print(self.name, "pushes.")


class BJ_Dealer(BJ_Hand):
    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(self.name, "busts.")

    def flip_first_card(self):
        self.cards[0].flip()


# 🔥 BONUS GAME
def bonus_game(player_name):
    print(f"\n🎯 BONUS ROUND for {player_name}!")
    lucky = random.randint(1, 5)
    guess = input("Guess number (1-5): ")

    if guess.isdigit() and int(guess) == lucky:
        print("🔥 BONUS WIN! Extra victory!")
        return True
    else:
        print("No bonus. Lucky number was:", lucky)
        return False


class BJ_Game(object):
    def __init__(self, names):
        self.players = [BJ_Player(name) for name in names]
        self.dealer = BJ_Dealer("Dealer")

        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()

    @property
    def still_playing(self):
        return [p for p in self.players if not p.is_busted()]

    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()

    def play(self):
        # 🔥 Deck safety check
        if len(self.deck.cards) < (len(self.players) * 7):
            print("🔄 Reshuffling deck...")
            self.deck.clear()
            self.deck.populate()
            self.deck.shuffle()

        # deal cards
        self.deck.deal(self.players + [self.dealer], per_hand=2)
        self.dealer.flip_first_card()

        for player in self.players:
            print(player)
        print(self.dealer)

        # players turn
        for player in self.players:
            self.__additional_cards(player)

        self.dealer.flip_first_card()

        if not self.still_playing:
            print(self.dealer)
        else:
            print(self.dealer)
            self.__additional_cards(self.dealer)

            if self.dealer.is_busted():
                for player in self.still_playing:
                    player.win()
                    bonus_game(player.name)   # 🔥 BONUS

            else:
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win()
                        bonus_game(player.name)  # 🔥 BONUS
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()

        # clear hands
        for player in self.players:
            player.clear()
        self.dealer.clear()


def main():
    print("\n🔥 Welcome to Labady Riviere Blackjack 🔥\n")

    names = []
    number = games.ask_number("How many players? (1 - 7): ", low=1, high=8)

    for i in range(number):
        name = input("Enter player name: ")
        names.append(name)

    game = BJ_Game(names)

    again = "y"
    while again != "n":
        game.play()
        again = games.ask_yes_no("\nPlay again? (y/n): ")

    print("\n💻 Created by Labady Riviere")


main()
input("\nPress Enter to exit...")