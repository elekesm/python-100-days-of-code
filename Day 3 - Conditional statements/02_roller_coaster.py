print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bill = 7
        print("Please pay $7.")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Your ride is free!")
    else:
        bill = 12
        print(f"Please pay ${bill}.")
    input("Do you want a photo taken? It's $3. Y or N. ")
    if(input().upper() == "Y"):
        bill += 3
    print(f"Your total bill is ${bill}.")
else:
    print("Sorry, you have to grow taller before you can ride.")