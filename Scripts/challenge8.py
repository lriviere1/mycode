# Chapter 8, Challenge 2
# Television Simulator + Lucky Win Game
# Created by Labady Riviere

import random

class Tele(object):
    """A virtual Television"""

    def __init__(self, channel, volume):
        self.channel = channel
        self.volume = volume
        print("📺 TV ON")
        print("Channel:", self.channel)
        print("Volume:", self.volume)

    def chngchan(self, chan_choice):
        if 0 <= chan_choice <= 99:
            self.channel = chan_choice
            print("📡 Channel changed to:", self.channel)
        else:
            print("❌ Invalid channel.")

    def chngvol(self, vol_up_down):
        if vol_up_down == 'up':
            if self.volume < 10:
                self.volume += 1
            else:
                print("🔊 Volume at maximum.")
        elif vol_up_down == 'down':
            if self.volume > 0:
                self.volume -= 1
            else:
                print("🔇 Volume at minimum.")
        
        print("Volume:", self.volume)


def tryint(sentence):
    while True:
        value = input(sentence)
        try:
            number = int(value)
            if 0 <= number <= 99:
                return number
            else:
                print("❌ Choose between 0 and 99.")
        except ValueError:
            print("❌ Not a number.")


def updown(sentence):
    while True:
        vol_ud = input(sentence).lower()
        if vol_ud in ["up", "down"]:
            return vol_ud
        else:
            print("❌ Type 'up' or 'down'.")


# 🔥 NEW GAME FUNCTION
def lucky_game():
    print("\n🎯 LUCKY NUMBER GAME 🎯")
    print("Guess the number between 1 and 5")

    lucky_number = random.randint(1, 5)
    guess = input("Your guess: ")

    if guess.isdigit() and int(guess) == lucky_number:
        print("🎉 YOU WIN!!! 🎉")
    else:
        print("❌ You lose. Lucky number was:", lucky_number)


def main():
    print("\n🔥 Welcome to Labady Riviere TV System 🔥")

    television = Tele(1, 3)

    while True:
        print("""
Remote control choices:
0 - Change channel
1 - Change volume
2 - Play Lucky Game 🎯
3 - Turn TV off
""")

        choice = input("Choice: ")

        if choice == '0':
            chan_choice = tryint("Enter channel (0-99): ")
            television.chngchan(chan_choice)

        elif choice == '1':
            vol_updown = updown("Type 'up' or 'down': ")
            television.chngvol(vol_updown)

        elif choice == '2':
            lucky_game()

        elif choice == '3':
            print("\n📴 TV turned off.")
            break

        else:
            print("❌ Invalid choice.")


# Run program
main()

print("\n💻 Program created by Labady Riviere")
input("Press Enter to exit...")