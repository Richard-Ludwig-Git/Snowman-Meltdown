import random
from ascii_art import STAGES


# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def display_game_state(mistakes, secret_word, guessed_letters):
    print(STAGES[mistakes])
    all_guessed = 0
    for char in secret_word:
        if char in guessed_letters:
            print(f"{char} ", end="")
            all_guessed += 1
        if char not in guessed_letters:
            print("_ ", end="")
    if all_guessed == len(secret_word):
        print()
        print("\nYOU WON - AND SAVED THE SNOWMAN!")
        exit()


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    print("Welcome to Snowman Meltdown!")
    print(STAGES[0])
    for char in secret_word:
        print("_ ", end="")
    while mistakes < 3:
        guess= input("\nGuess a letter: ").lower()
        print("You guessed:", guess)
        if guess in secret_word and guess not in guessed_letters:
            guessed_letters.append(guess)
            print("letter appended")
            print(guessed_letters)
        elif guess not in secret_word:
            mistakes += 1
        display_game_state(mistakes, secret_word, guessed_letters)
    print()
    print("\nYOU LOST - SNOWMAN DIED")
    exit()


if __name__ == "__main__":
    play_game()