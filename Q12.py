# Write a program to calculate the tax payable based on income slabs.


annual_income = float(input("Enter your annual income: "))

if annual_income <= 250000:
    tax = 0
elif annual_income <= 500000:
    tax = (annual_income - 250000) * 0.10 
elif annual_income <= 1000000:
    tax = (annual_income - 500000) * 0.20 
else:
    tax = (annual_income - 100000) * 0.30


