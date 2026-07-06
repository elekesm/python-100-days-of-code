from random import randint

# example 1
def my_funtion():
    for i in range(1,20): # fix it by incrementing the range to include 20
        if i == 20:
            print("i is 20")

# example 2
dice_image = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣"]
dice_num = randint(1, 6)
print(dice_image[dice_num]) # fix it by subtracting 1 from dice_num to get the correct index

#example 3
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year > 1994: #fix it by changing the condition to year >= 1994 to include 1994
    print("You are a Gen Z.")

# example 4
try:
    age = int(input("How old are you?"))
except ValueError:
    print("Please enter a valid number.")

if age >= 18:
    print("You can drive at age {age}.")

# example 5
word_per_page = 0
pages = int(input("Number of pages: "))
words == int(input("Number of words: ")) # fix it by changing '==' to '=' to assign the value to words
total_words = pages * words
print(f"Total words: {total_words}")