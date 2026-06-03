import random


word_list = ["skoda", "ford", "audi", "volvo", "mercedes", "bmw", "honda", "toyota"]
word_to_guess = random.choice(word_list)
health = len(word_to_guess) + 3

chars_guessed_correctly = []
chars_guessed_wrong = []

def tip():
    print(f"Tip: The word has {len(word_to_guess)} letters.")
    #debug:
    print(f"Debug: The word to guess is '{word_to_guess}'.")
def display_word():
    display = ""
    for char in word_to_guess:
        if char in chars_guessed_correctly:
            display += char
        else:
            display += "_ "
    print(display)

def guess():
    guess = input("Guess a letter: ").lower()
    if guess:
        guess = guess[0]
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input! Please enter a single letter.")
    global health
    if guess in word_to_guess:
        chars_guessed_correctly.append(guess)
        print("Correct guess!")
        display_word()
    elif guess in chars_guessed_wrong or guess in chars_guessed_correctly:
       print("You already guessed that letter. Try again.")
       display_word()
    else:
        chars_guessed_wrong.append(guess)
        health -= 1
        print(f"Wrong guess! You have {health} health left.")
        display_word()

tip()
display_word()

while(True):
    if health == 0:
        print(f"You lost! The word was: {word_to_guess}")
        break
    elif set(chars_guessed_correctly) == set(word_to_guess):  # Check if all unique letters are guessed
        print(f"You won! The word was: {word_to_guess}")  # Display the winning message
        print(f"You had {health} health left.")
        break
    else:
        guess()