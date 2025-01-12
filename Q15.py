# Write a program to find whether a given string is a palindrome.

str = input("Enter any string:")

str_reverse = str[::-1]

if str == str_reverse:
    print("Palindrome")
else:
    print("Not a Plaindrome!")