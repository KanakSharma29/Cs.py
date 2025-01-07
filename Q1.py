# Write a program to calculate electricity bills based on consumption slabs.

units = float(input("Enter the number of units consumed:"))

if units < 0:
    print("Invalid input. Units cannot be negative")
else:
    if units <= 100:
        bill = units * 3.0    # 3 rupees per unit for the first 100 units
    elif units <=200:
        bill = (units * 3)+((units - 100)* 5.0)  # 5 rupee per unit for the next 100 units
    else:
        bill =(100*3.0)+(100*5.0)+((units - 200)* 8.0) # 8 rupee per unit for the unit above 200

print("Electricity Bill Amount : Rs.",bill)
