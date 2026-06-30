from random import randint


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)

    turns = set_difficulty()
    print(f"You have {turns} attempts remaining to guess the number.")

    guess = 0
    while guess != answer and turns > 0:
        guess = get_valid_guess()
        if guess is None:
            print("Game ended.")
            return
        turns = check_guess(guess, answer, turns)
        if guess != answer and turns > 0:
            print("Guess again.")
            print(f"You have {turns} attempts remaining to guess the number.")
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return

def set_difficulty():
    while True:
        try:
            level = input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            return HARD_LEVEL_TURNS

        if level == "easy":
            return EASY_LEVEL_TURNS
        if level == "hard":
            return HARD_LEVEL_TURNS

        print("Invalid choice. Please type 'easy' or 'hard'.")

def get_valid_guess():
    while True:
        try:
            raw_guess = input("Make a guess: ").strip()
        except (EOFError, KeyboardInterrupt):
            return None

        if not raw_guess:
            print("Please enter a number between 1 and 100.")
            continue

        try:
            guess = int(raw_guess)
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        if 1 <= guess <= 100:
            return guess

        print("Out of range. Please choose a number from 1 to 100.")

def check_guess(guess, answer, turns):
    if guess < answer:
        print("Too low.")
        return turns - 1
    elif guess > answer:
        print("Too high.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")
        return turns

game()