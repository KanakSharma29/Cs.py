# Check if a user-input number is a prime number.

number = int(input("enter number:"))
count = 0
i = 2
while i < number/2:
  if number % i == 0:
    counter = 1
    break
  i =  i + 1
if counter == 0 :
  print(f"The number {number} is Prime!")
else:
  print(f"The number {number} is not Prime!")