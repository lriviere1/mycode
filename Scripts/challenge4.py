# Chapter 4, Challenge 4

print("\t\t'GUESS THE COLOUR GAME!'. \nGuess the colour after "
      "choosing 5 different letters. \nGood luck!\n\n")

word = "blue"
chances = 5

print("The length of the word I've chosen is ", len(word))

while chances > 0:
    letter_guess = input("\nWhat letter would you like to guess? ")
    chances = chances - 1
    if letter_guess in word:
        print("That letter is in the word!")
    else:
        print("Nope, not that letter.")

guess = input("\nWhat colour would you like to guess? ")

if guess.lower() == word:
    print("Congratulations Labady! You got it!")
else:
    print("Ah, bummer. You got it wrong. The word was ", word, ".", sep="")

input("\n\nPress enter to exit")