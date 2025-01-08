# Create a traffic light simulation that determines actions for red, yellow, and green lights.

print(f"Traffic light simulation:\n1.Red light\n 2.Yellow light.\n 3.Green light." )

choice = int(input("Enter the number corresponding to the traffic light color : "))

if choice == 1:
    print("Red light : Stop your vehicle.")
elif choice == 2:
    print("Yellow light : Get ready to stop or proceed with caution.")
elif choice == 3:
    print("Green light : Goooooooo!!")
else:
    print("Invalid choice! Please enter the valid number.")
