# Develop a program to decide if a student is eligible for a scholarship based on grades and income.

grade = int(input("Enter your grade:"))

income = int(input("Enter your annual income:"))

if grade >= 75 and income < 500000:
    print("Congratulations! You are eligible for the scholarship!")
else:
    print("You are not eligible for the scholarship.")