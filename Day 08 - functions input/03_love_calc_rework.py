def calculate_love_score(name1, name2):
    combined_names = name1.lower() + name2.lower()
    true_score = 0
    love_score = 0
    
    for char in combined_names:
        if char in "true":
            true_score+=1
        if char in "love":
            love_score+=1

    total_score = love_score + true_score
    
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