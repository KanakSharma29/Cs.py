# Determine if a triangle is valid based on its sides (sum of two sides > third side).
 
side1 = float(input("Enter the first side of a triangle: "))
side2 = float(input("Enter the second side of a triangle: "))
side3 = float(input("Enter the third side of a triangle: "))
 
if (side1 - side2) < side3 <(side1 + side2):
    print("Triangle is valid!!")
else:
    print("The triangle is not valid!")