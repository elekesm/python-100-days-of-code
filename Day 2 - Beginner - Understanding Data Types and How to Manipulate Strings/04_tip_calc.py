print("Welcome to the tip calculator!")
total = int(input("What was the total bill?"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))

pay_per_person = total * (1+tip_percent / 100) / float(people)
pay_per_person = round(pay_per_person, 2)
print(f"Each person should pay: ${pay_per_person}")