
machine_resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def ask_user():
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    return user_input

def turn_off():
    print("Turning off the coffee machine. Goodbye!")
    exit()

def print_report():
    print(f"Water: {machine_resources['water']}ml")
    print(f"Milk: {machine_resources['milk']}ml")
    print(f"Coffee: {machine_resources['coffee']}g")
    print(f"Money: ${machine_resources['money']}")

# check resources
COFFEE_RECIPES = {
    "espresso": {"water": 50, "milk": 0, "coffee": 18, "cost": 1.5},
    "latte": {"water": 200, "milk": 150, "coffee": 24, "cost": 2.5},
    "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "cost": 3.0}
}

def check_resources(coffee_type):
    if coffee_type not in COFFEE_RECIPES:
        print("Invalid coffee type.")
        return False
    
    required_resources = COFFEE_RECIPES[coffee_type]
    for resource, amount in required_resources.items():
        if resource != "cost" and machine_resources[resource] < amount:
            print(f"Sorry, there is not enough {resource}.")
            return False
    return True

# process coins
def process_coins():
    print("Please insert coins.")
    total = 0
    total += int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total

# check transaction
def check_transaction(coffee_type, money_received):
    cost = COFFEE_RECIPES[coffee_type]["cost"]
    if money_received < cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    else:
        change = round(money_received - cost, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        machine_resources["money"] += cost
        return True
# make coffee
def make_coffee(coffee_type):
    required_resources = COFFEE_RECIPES[coffee_type]
    for resource, amount in required_resources.items():
        if resource != "cost":
            machine_resources[resource] -= amount
    print(f"Here is your {coffee_type}. Enjoy!")

# main loop
while True:
    user_choice = ask_user()
    
    if user_choice == "off":
        turn_off()
    elif user_choice == "report":
        print_report()
    elif user_choice in COFFEE_RECIPES:
        if check_resources(user_choice):
            money_received = process_coins()
            if check_transaction(user_choice, money_received):
                make_coffee(user_choice)
    else:
        print("Invalid choice. Please choose from (espresso/latte/cappuccino/report/off).")