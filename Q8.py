print("Movie Ratings:")
print("1. G (General Audience - All Ages)")
print("2. PG (Parental Guidance - Some Material May Not Be Suitable for Children)")
print("3. R (Restricted - Under 17 Requires Accompanying Parent or Adult Guardian)")

rating_choice = int(input("Enter the number corresponding to the movie rating(1-3) : "))

age = int(input("enter your age :"))

if rating_choice == 1:
  print("The movie is appropriate for all ages. Enjoy!")
elif rating_choice == 2:
  if age >= 10:
    print("The movie is appropriate for your age. Enjoy!")
  else:
    print("The movie may not be suitable for your age. Parental guidance is recommended.")
elif rating_choice == 3:
  if age >= 17:
    print("The movie is appropriate for your age. Enjoy!")
  else:
    print("The movie is not appropriate for your age. Restricted to viewers 17 and older. ")
else:
  print("Invalid choice! Please enter a number between 1 and 3. ")