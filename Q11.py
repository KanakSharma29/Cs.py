# Check if a given year, month, and day form a valid date.

# year = int(input("Enter year:"))
# month = int(input("Enter month:"))
# day = int(input("Enter day:"))

# if month < 1 or month > 12:
#     print(f"{day}-{month}-{year} is not a valid date")
# else:
#     if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
#         max_days = 31
#     elif month == 4 or month == 6 or month == 9 or month == 11:
#         max_days = 30
#     elif month == 2:
#         if(year % 4 == 0 and year%100!= 0)or year % 400 == 0:
#             max_days = 29
#         else:
#             max_days = 28

# if day < 1 or day > max_days:
#     print(f"{day}-{month}-{year} is not a valid date")
# else:
#     print(f"{day}-{month}-{year} is a valid date")



#using module
from datetime import datetime


year = int(input("Enter year:"))
month = int(input("Enter month:"))
day = int(input("Enter day:"))

a =  datetime(year,month, day)
