# Simulate a basic calculator that performs operations based on user input (+, -, *, /).


print("Welcome to the basic calculator!What kind of operation you want to perform?")
print("1. Addition <<")
print("2. Subtraction <<")
print("3. Multiplication <<")
print("4. Division <<")

choice = int(input("Enter the number corresponding to the operations. "))

num1 = float(input("Enter the first number :"))
num2 = float(input("Enter the second number :"))


match choice:
    case 1:
        result = num1 + num2
    case 2:
        result = num1 - num2
    case 3:
        result = num1 * num2
    case 4:
        if num2 == 0:
            result = "Not defined value!"
        else:
           result = num1 / num2

print(result)
