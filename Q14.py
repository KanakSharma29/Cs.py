# Determine the type of quadrilateral based on four given angles.



angle1 = int(input("Enter angle1 :"))
angle2 = int(input("Enter angle2 :"))
angle3 = int(input("Enter angle3 :"))
angle4 = int(input("Enter angle4 :"))


if angle1 + angle2 + angle3 + angle4 != 360 :
    print("The angles do not form a valid quadrilateral.")
else:
    if angle1 == 90 and angle2 == 90 and angle3 == 90 and angle4 == 90:
        print("This is a Square or a Rectangle (all angles are 90°).")
    elif angle1 == angle3 and angle2 == angle4:
        print("This is a Parallelogram.")
    elif angle1 == angle3 and angle2 == angle4 and angle1 != 90:
        print("This is a Rhombus.")
    elif angle1 == angle2 and angle3 == angle4 and angle1 != angle3:
        print("This is a Trapezoid.")
    else:
        print("This is a General Quadrilateral.")