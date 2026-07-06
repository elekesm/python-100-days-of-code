import art
import game_data
import random


def format_data(account):
    """Return account text for display."""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
    """Return whether the guess is correct."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def get_random_account():
    """Return a random account."""
    return random.choice(game_data.data)


print(art.logo)

score = 0
game_should_continue = True
account_a = get_random_account()
account_b = get_random_account()

while game_should_continue:
    if account_a == account_b:
        account_b = get_random_account()

    print(f"Compare A: {format_data(account_a)}.")
    print(f"Against B: {format_data(account_b)}.")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    result = check_answer(guess, account_a["follower_count"], account_b["follower_count"])
    if result:
        score += 1
        print("You got it right!")
        print(f"Your current score is: {score}")
        print("--------")
        account_a = account_b
        account_b = get_random_account()
    else:
        game_should_continue = False
        print("Sorry, that's wrong.")
        print(f"Final score: {score}")
