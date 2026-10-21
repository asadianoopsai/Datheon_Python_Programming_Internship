import random

WORD_FILE = "google-10000-english-no-swears.txt"
MAX_ATTEMPTS = 6

HANGMAN_STAGES = [
    """
     +---+
         |
         |
         |
        ===
    """,
    """
     +---+
     O   |
         |
         |
        ===
    """,
    """
     +---+
     O   |
     |   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ===
    """
]


def load_words():
    """Load suitable words from the provided word list."""
    try:
        with open(WORD_FILE, "r", encoding="utf-8") as file:
            words = [
                line.strip().lower()
                for line in file
                if line.strip().isalpha()
                and 4 <= len(line.strip()) <= 10
            ]

        if not words:
            raise ValueError("The word list contains no suitable words.")

        return words

    except FileNotFoundError:
        print(f"Error: Could not find '{WORD_FILE}'.")
        print("Place the word list in the same folder as hangman.py.")
        raise SystemExit(1)

    except ValueError as error:
        print(f"Error: {error}")
        raise SystemExit(1)


def display_game(secret_word, guessed_letters, attempts_left):
    """Display the gallows and the current game progress."""
    wrong_guesses = MAX_ATTEMPTS - attempts_left

    print(HANGMAN_STAGES[wrong_guesses])
    print("Word:", " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    ))

    print("Guessed letters:", " ".join(sorted(guessed_letters))
          if guessed_letters else "None")
    print(f"Attempts remaining: {attempts_left}")


def get_guess(guessed_letters):
    """Get and validate one letter from the player."""
    while True:
        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter one alphabetic letter.")
        elif guess in guessed_letters:
            print("You already guessed that letter. Try another!")
        else:
            return guess


def play_game(words):
    """Run one complete Hangman game."""
    secret_word = random.choice(words)
    guessed_letters = set()
    attempts_left = MAX_ATTEMPTS

    print("\nWelcome to Hangman!")
    print("Guess the hidden word one letter at a time.")
    print(f"The word contains {len(secret_word)} letters.")

    while attempts_left > 0:
        display_game(secret_word, guessed_letters, attempts_left)

        if all(letter in guessed_letters for letter in secret_word):
            print(f"\nCongratulations! You guessed '{secret_word}'.")
            print("You win!")
            return

        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in secret_word:
            print("Correct guess!")
        else:
            attempts_left -= 1
            print("Wrong guess!")

    display_game(secret_word, guessed_letters, attempts_left)
    print(f"\nGame over! The word was '{secret_word}'.")
    print("Better luck next time!")


def main():
    """Start the game and allow replay."""
    words = load_words()

    while True:
        play_game(words)

        play_again = input("\nPlay again? (yes/no): ").strip().lower()

        if play_again not in ("yes", "y"):
            print("Thanks for playing Hangman!")
            break


if __name__ == "__main__":
    main()