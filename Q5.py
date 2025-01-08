# items = "1. Laptop - ₹45000.00",
# "2. Smartphone - ₹25000.00",
# "3. Headphones - ₹2000.00",
# "4. Smartwatch - ₹5000.00",
# "5. Gaming Console - ₹40000.00"

print(f"Available itmes:\n 1. Laptop - ₹45000.00\n 2. Smartphone - ₹25000.00\n3. Headphones - ₹2000.00\n4. Smartwatch - ₹5000.00\n5. Gaming Console - ₹40000.00")

item_no = int(input("Enter the number of item you want to buy (1-5) : "))

if item_no == 1:
    item_name = "Laptop"
    item_price = 45000
elif item_no == 2:
    item_name = "Smartphone"
    item_price = 25000
elif item_no == 3:
    item_name = "Headphones"
    item_price = 2000
elif item_no == 4:
    item_name = "Smartwatch"
    item_price = 5000
elif item_no == 5:
    item_name = "Gaming console"
    item_price = 40000
else:
    print("Invalid choice! Please select a valid item.")

print(f"You have selected {item_name} of cost {item_price}")

budget = int(input("Please Enter your budget: "))

if budget >= item_price:
   remaining_budget = budget - item_price
   print("You can afford this item! You will have", remaining_budget,"Rs.left after purchasing it.")
else:
    needed_money = item_price - budget
    print("You cannot afford this item. You need an additional amount of Rs.",needed_money)
