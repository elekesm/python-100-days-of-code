"""
This script demonstrates basic Python concepts including print statements, string concatenation, 
user input, and variable usage. It is structured as follows:

1. Basic Print Statements:
    - Outputs simple messages to the console.
    - Demonstrates the use of newline characters (`\n`) and string concatenation.

2. User Input:
    - Prompts the user for their name and personalizes the output message.

3. Variables:
    - Introduces the concept of variables to store and manipulate data.
    - Demonstrates how to calculate and display the length of a user-provided name.

Usage:
- Run the script and follow the prompts to see personalized messages and interact with the program.
"""


print("Hello Python!")
print("Hello! \nI's Mark")
print("Hello" + " " + "World" + "!" )

# Includes user input to personalize the output.
print("Hello, i's Mark\n" + "Nice to meet you " + input("What's your name?\n"))

# This section demonstrates how to use variables to store and manipulate data.
print("------variables------")
name = "Mark"
print(name)

# How to calculate the length of a name
print("The lenght of the name is: " + str(len(input("Add a name to calculate the length of it\n"))) + " char long")