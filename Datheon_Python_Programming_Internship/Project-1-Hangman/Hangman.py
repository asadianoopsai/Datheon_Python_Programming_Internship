
import random
from pathlib import Path


def load_words():
    file_path = Path(__file__).parent / "words.txt"

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            words = [
                line.strip().lower()
                for line in file
                if line.strip().isalpha()
            ]

        if not words:
            print("Error: The word list is empty.")
            return []

        return words

    except FileNotFoundError:
        print("Error: words.txt was not found.")
        print("Place words.txt in the same folder as hangman.py.")
        return []


def display_hangman(wrong_guesses):
    stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """
    ]

    print(stages[wrong_guesses])


def play_hangman(words):
    word = random.choice(words)
    guessed_letters = set()
    wrong_guesses = 0
    max_attempts = 6

    print("\nWelcome to Hangman!")
    print("Guess the hidden word one letter at a time.")
    print(f"You have {max_attempts} incorrect guesses available.")

    while wrong_guesses < max_attempts:
        display_hangman(wrong_guesses)

        display_word = " ".join(
            letter if letter in guessed_letters else "_"
            for letter in word
        )

        print("Word:", display_word)
        print("Guessed letters:", " ".join(sorted(guessed_letters)))

        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            return

        guess = input("Enter one letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one alphabetic letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. No penalty!")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct guess!")
        else:
            wrong_guesses += 1
            print(
                f"Incorrect guess! Attempts remaining: "
                f"{max_attempts - wrong_guesses}"
            )

    display_hangman(wrong_guesses)
    print("Game over! The word was:", word)


def main():
    words = load_words()

    if not words:
        return

    while True:
        play_hangman(words)

        while True:
            choice = input(
                "\nDo you want to play again? (Y/N): "
            ).strip().lower()

            if choice in ("y", "yes"):
                break

            if choice in ("n", "no"):
                print("Thanks for playing Hangman! Goodbye!")
                return

            print("Invalid choice. Please enter Y or N.")


if __name__ == "__main__":
    main()
