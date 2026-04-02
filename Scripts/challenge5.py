# Chapter 5, Challenge 2
# Character Creator Program
# Created by Labady Riviere

print("""
            LABADY'S CHARACTER CREATOR PROGRAM

You have 30 points to distribute between the following attributes:
    Strength, Health, Wisdom, Dexterity.

You can also remove points from an attribute and return them to the pool.
""")

attributes = {
    'strength': 0,
    'health': 0,
    'wisdom': 0,
    'dexterity': 0
}

pool = 30
choice = None

while choice != "0":
    print("\n--- Current Character Stats ---")
    for attribute, points in attributes.items():
        print(f"{attribute.title()}: {points}")

    print(f"\nPoints remaining in pool: {pool}")

    print("""
Choose an option:
0 - Exit
1 - Add points to an attribute
2 - Remove points from an attribute
""")

    choice = input("Your choice: ")

    # OPTION 1: ADD POINTS
    if choice == "1":
        if pool == 0:
            print("No points left to spend.")
            continue

        att = input("Which attribute? ").lower()

        if att not in attributes:
            print("Invalid attribute.")
            continue

        points = int(input("How many points to add? "))

        if points > pool:
            print("Not enough points.")
        else:
            attributes[att] += points
            pool -= points
            print("Points added successfully!")

    # OPTION 2: REMOVE POINTS
    elif choice == "2":
        att = input("Which attribute? ").lower()

        if att not in attributes:
            print("Invalid attribute.")
            continue

        if attributes[att] == 0:
            print("No points to remove.")
            continue

        points = int(input("How many points to remove? "))

        if points > attributes[att]:
            print("You don't have that many points.")
        else:
            attributes[att] -= points
            pool += points
            print("Points returned to pool!")

print("\nFinal Character Stats:")
for attribute, points in attributes.items():
    print(f"{attribute.title()}: {points}")

print("\nProgram created by Labady Riviere")
input("\nPress Enter to exit...")