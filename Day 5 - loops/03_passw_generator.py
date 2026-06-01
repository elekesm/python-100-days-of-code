"""
This script generates a random password based on user-specified criteria.

Modules:
    - string: Provides access to string constants for letters, digits, and punctuation.
    - random: Used for random selection and shuffling.

Functions:
    - None

Variables:
    - all_letters: List of all uppercase and lowercase letters.
    - all_numbers: List of all digits.
    - all_punctuation: List of all punctuation characters.
    - nr_letters: Number of letters in the password (user input).
    - nr_numbers: Number of numbers in the password (user input).
    - nr_symbols: Number of symbols in the password (user input).
    - password_list: List to store password characters before shuffling.
    - password: Final password string after shuffling.

Usage:
    - Run the script and follow the prompts to specify the number of letters, numbers, and symbols.
    - The script will generate and display a random password based on the input.
"""


import string
import random


all_letters = list(string.ascii_letters)
print(all_letters)

all_numbers = list(string.digits)
print(all_numbers)

all_punctuation = list(string.punctuation)
print(all_punctuation)

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))

# Hard level:
password_list = []
for char in range(0, nr_letters):
    password_list.append(random.choice(all_letters))

for char in range(0, nr_numbers):
    password_list.append(random.choice(all_numbers))

for char in range(0, nr_symbols):
    password_list.append(random.choice(all_punctuation))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")