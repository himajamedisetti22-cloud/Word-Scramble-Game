import random

words = [
    "python",
    "computer",
    "program",
    "keyboard",
    "internet",
    "student",
    "college",
    "project",
    "science",
    "technology"
]

print("===== WORD SCRAMBLE GAME =====")

while True:
    word = random.choice(words)

    scrambled = list(word)
    random.shuffle(scrambled)
    scrambled_word = ''.join(scrambled)

    print("\nScrambled Word:", scrambled_word)

    guess = input("Enter your guess: ").lower()

    if guess == word:
        print("Congratulations! Correct Answer.")
    else:
        print("Wrong Guess!")
        print("Correct Word is:", word)

    choice = input("\nDo you want to play again? (yes/no): ").lower()

    if choice != "yes":
        print("Thank you for playing!")
        break