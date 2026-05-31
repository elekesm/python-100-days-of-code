import random


rock = "Rock"
paper = "Paper"
scissors = "Scissors"

game_possibilities = [rock, paper, scissors]
game_choice = random.choice(game_possibilities)

user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
if user_choice == "0":
    user_choice = rock
elif user_choice == "1":
    user_choice = paper 
elif user_choice == "2":
    user_choice = scissors
else:
    print("Invalid choice, you lose!")
    exit()

if user_choice == game_choice:
    print(f"Both players chose {user_choice}. It's a draw!")
elif (user_choice == rock and game_choice == scissors) or (user_choice == paper and game_choice == rock) or (user_choice == scissors and game_choice == paper):
    print(f"You chose {user_choice} and the computer chose {game_choice}. You win!")