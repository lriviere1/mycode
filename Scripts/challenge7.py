# Chapter 7, Challenge 1
# Trivia Game (File-Based)
# Created by Labady Riviere

import sys

def open_file(file_name, mode):
    try:
        return open(file_name, mode)
    except IOError:
        print("Error: Cannot open file.")
        input("Press Enter to exit...")
        sys.exit()

def next_line(file):
    line = file.readline()
    return line.replace("/", "\n").strip()

def next_block(file):
    category = next_line(file)
    if not category:
        return None, None, None, None, None, None

    question = next_line(file)

    answers = []
    for i in range(4):
        answers.append(next_line(file))

    points = next_line(file)
    correct = next_line(file)
    explanation = next_line(file)

    return category, question, answers, points, correct, explanation

def welcome(title):
    print("\n🎮 WELCOME TO LABADY'S TRIVIA GAME 🎮")
    print("Category:", title)
    print("-" * 40)

def main():
    file = open_file("trivia_file2.txt", "r")
    title = next_line(file)
    welcome(title)

    score = 0

    while True:
        category, question, answers, points, correct, explanation = next_block(file)

        if not category:
            break

        print("\nCategory:", category)
        print("Question:", question)

        for i in range(4):
            print(f"{i+1}. {answers[i]}")

        # 🔥 SHOW CORRECT ANSWER (so user can win)
        print(f"(Hint: Correct answer is option {correct})")

        answer = input("Your answer (1-4): ")

        if answer == correct:
            print("✅ Correct!")
            score += int(points)
        else:
            print("❌ Wrong!")

        # ALWAYS SHOW CORRECT ANSWER AFTER
        print(f"Correct Answer: {correct} - {answers[int(correct)-1]}")
        print("Explanation:", explanation)
        print("Current Score:", score)

    file.close()

    print("\n🎉 Game Over!")
    print("Final Score:", score)
    print("Created by Labady Riviere")

main()