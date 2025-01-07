# Simulate a simple login system with username and password validation.
import re

username = input("Enter your username: ")
password = input("Enter your password: ")


username_regex = r"^[a-zA-Z][a-zA-Z0-9._]{2,15}$"
password_regex = r"^[A-Za-z0-9]{6,12}$"

if not re.match(username_regex, username):
    print("Login failed. Invalid username or password.")
elif not re.match(password_regex,password):
    print("Login failed. Invalid username or password.")
else:
    print("Login successful! Welcome!")



