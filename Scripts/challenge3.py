# Chapter 3, Challenge 3
# Guess My Number with fixed number of tries

import random

print("\tWelcome to Labady's 'Guess My Number in 8 tries'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.")
print("You have 8 tries to get it right!\n")

# set the initial values
the_number = 59
guess = int(input("Take a guess: "))
tries = 1

# guessing loop
while guess != the_number and tries < 8:
    print("You've had", tries, "try/tries so far! Only", 8 - tries, "left!")
    
    if guess > the_number:
        print("Lower...\n")
    else:
        print("Higher...\n")
        
    tries += 1
    guess = int(input("Take a guess: "))

# result
if guess == the_number:
    print("\n🎉 Great job Labady! You guessed it!")
    print("The number was", the_number)
    print("And it only took you", tries, "tries!")
else:
    print("\n❌ Game Over Labady!")
    print("You ran out of tries!")
    print("The number was", the_number)

input("\nPress Enter to exit...")