import random

# Convert student scores to grades
student_scores = [random.randint(30, 150) for _ in range(10)]
for score in student_scores:
    if score >= 90:
        print(f"Score: {score} - Grade: A")
    elif score >= 80:
        print(f"Score: {score} - Grade: B")
    elif score >= 70:
        print(f"Score: {score} - Grade: C")
    elif score >= 60:
        print(f"Score: {score} - Grade: D")
    else:
        print(f"Score: {score} - Grade: F")

# Embedded for loop to generate a list of 10 random integers between 1 and 10
print([random.randint(1,10) for _ in range(10)])

# Using a for loop with a step of 3 to print numbers from 1 to 10
for i in range (1,11,3):
    print(i)

# Gauss formula for sum of first 100 natural numbers
total = 0
for i in range(1, 101):
    total += i
print(total)