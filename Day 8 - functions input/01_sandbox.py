def greet():
    print("Hello")
    print("How do yo do?")
    print("Isn't the weather nice today?")
# greet()

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do?")
# greet_with_name(input("What is your name? "))

def greet_with_loc(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with_loc(input("What's your name? "), input("Where are you now? "))
