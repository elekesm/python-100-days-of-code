def calculate_love_score(name1, name2):
    combined_names = name1.lower() + name2.lower()
    true_score = combined_names.count("t") + combined_names.count("r") + combined_names.count("u") + combined_names.count("e")
    love_score = combined_names.count("l") + combined_names.count("o") + combined_names.count("v") + combined_names.count("e")
    total_score = int(str(true_score) + str(love_score))
    
    if total_score < 10 or total_score > 90:
        print("You go together like coke and mentos.")
    elif total_score >= 40 and total_score <= 50:
        print("You are alright together.")
    else:
        print(f"Your score {total_score} is just average.")

print("Welcome to the love calculator!")
print("whis is an example of how to use the love calculator staring Brad Pitt and Angelina Jolie")
calculate_love_score("Brad Pitt", "Angelina Jolie")

calculate_love_score(input("What is your name? "), input("What is their name? "))