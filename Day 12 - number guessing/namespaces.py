enemies = 1

def increase_enemies():
    enemies = 2
    print(f"Enemies inside the function: {enemies}")

increase_enemies()
print(f"Enemies outside the function: {enemies}")  # This will raise a NameError since 'enemies' is not defined in this scope

# Local scope 
# def drink_potion():
#     potion_strength = 5
#     print(f"Potion strength inside the function: {potion_strength}")

# drink_potion()
# print(f"Potion strength outside the function: {potion_strength}")  # This will raise a NameError since 'potion_strength' is not defined in this scope

# Global scope

player_health = 10

def drink_potion():
    global player_health
    player_health = 15

