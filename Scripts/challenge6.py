# Chapter 6, Challenge 2
# Guess My Number Game
# Created by Labady Riviere

import random

def ask_number(question, low, high):
    """Ask the player for a number within a range."""
    response = None
    while response not in range(low, high + 1):
        print(f"Guess a number between {low} and {high}")
        response = int(input(question))
    return response

print("\n\tWELCOME TO LABADY'S GUESS MY NUMBER GAME!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

# initial setup
the_number = 42
low = 1
high = 100
tries = 1

# first guess
guess = ask_number("Take a guess: ", low, high)

# game loop
while guess != the_number:
    if guess > the_number:
        print("Too high... Try lower!")
        high = guess - 1
    else:
        print("Too low... Try higher!")
        low = guess + 1

    guess = ask_number("Take a guess: ", low, high)
    tries += 1

# result
print("\n🎉 Congratulations Labady! You guessed it!")
print(f"The number was {the_number}")
print(f"It took you {tries} tries.\n")

input("Press Enter to exit...")