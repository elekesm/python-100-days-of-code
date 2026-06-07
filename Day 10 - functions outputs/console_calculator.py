def add (n1, n2):
    return n1 + n2

def subtract (n1, n2):
    return n1 - n2

def multiply (n1, n2):
    return n1 * n2

def divide (n1, n2):
    return n1 / n2 

dict_operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

#print(dict_operators["-"](10,3))

while True:
    num1 = float(input("What's the first number? "))
    while True:
        for symbol in dict_operators:
            print(symbol)
        operation_symbol = input("Pick an operation: +, -, *, /: ")
        num2 = float(input("What's the second number? "))

        result = dict_operators[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")
        continue_calculating = input(f"Type 'y' to continue calculating with {result}, 'n' to start a new calculation, or any other key to exit: ")
        if continue_calculating == "y":
            num1 = result
        elif continue_calculating == "n":
            print("Starting a new calculation...")
            break
        else:
            print("Exiting the calculator. Goodbye!")
            exit()