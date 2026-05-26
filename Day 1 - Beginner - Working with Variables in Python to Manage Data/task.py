"""
This script generates a band name based on user input.

The program prompts the user to input the name of the city they grew up in
and the name of their pet. It then combines these inputs to create and display
a potential band name.
"""

print("Welcome the bandname generator!")

city = input("What's the name of the city you grew up in?\n")
pet = input("What's the name of your pet?\n")
print("Your band name could be " + city + " " + pet)