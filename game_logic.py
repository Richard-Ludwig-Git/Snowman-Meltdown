import random
from ascii_art import STAGES


# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def display_game_state(mistakes, secret_word, guessed_letters):
    print((f"\n"*6))
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


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def play_game():
    playing = True
    while playing:
        secret_word = get_random_word()
        guessed_letters = []
        mistakes = 0
        print("Welcome to Snowman Meltdown!")
        print(STAGES[0])
        for char in secret_word:
            print("_ ", end="")
        while mistakes < 4 and not game_won:
            guess= input("\nGuess a letter: ").lower()
            if len(guess) > 1 or guess.isdigit():
                print("You did not enter a single Letter")
                continue
            print("You guessed:", guess)
            if guess in secret_word and guess not in guessed_letters:
                guessed_letters.append(guess)
            elif guess not in secret_word:
                mistakes += 1
            display_game_state(mistakes, secret_word, guessed_letters)
        print("\nGAME OVER\n")
        replay = input("Play another Round?(y/n): ")
        if replay == "n":
            exit()


if __name__ == "__main__":
    play_game()