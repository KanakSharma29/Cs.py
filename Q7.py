"""
Infant: 0–2 years
Child: 3–12 years
Teenager: 13–17 years
Young Adult: 18–35 years
Middle-aged Adult: 36–55 years
Senior Citizen: 56 years and above

"""
name = input("Enter your name : ")
age = int(input("Enter your age : "))

if age < 0:
    print("Invalid age! Age cannot be negative.")
elif 0 <= age <= 2:
    print(f"{name}:You are a Infant and your age is {age}.")
elif 3 <= age <= 12:
    print(f"{name}:You are a Child and your age is {age}.")
elif 13 <= age <= 17:
    print(f"{name}:You are a Teenager and your age is {age}.")
elif 18 <= age <= 35:
    print(f"{name}:You are a Young Adult and your age is {age}.")
elif 36 <= age <= 55:
    print(f"{name}:You are a Middle - aged Adult and your age is {age}.")
else:
    print(f"{name}:You are a Senior Citizen and your age is {age}.")

    

    

    

    

    

