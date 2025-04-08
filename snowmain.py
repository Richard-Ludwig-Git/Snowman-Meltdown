import random

# Snowman ASCII Art stages
STAGES = [
     # Stage 0: Full snowman
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
     """,
     # Stage 1: Bottom part starts melting
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     """,
     # Stage 2: Only the head remains
     """
      ___  
     /___\\ 
     (o o) 
     """,
     # Stage 3: Snowman completely melted
     """
      ___  
     /___\\ 
     """
 ]


# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

#def display_game_state(mistakes, secret_word, guessed_letters):



def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def play_game():
    secret_word = get_random_word()
    mistakes = 0
    print("Welcome to Snowman Meltdown!")
    print(STAGES[mistakes])
    for char in secret_word:
        print("_ ", end="")
    while mistakes < 3:
        guessed_letter = input("\nGuess a letter: ").lower()
        print("You guessed:", guessed_letter)
        display_game_state(mistakes, secret_word, guessed_letter)


if __name__ == "__main__":
    play_game()