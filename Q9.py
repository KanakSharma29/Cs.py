# Simulate an ATM withdrawal process that checks balance, amount, and limits.


balance = 10000
withdrawal_limit = 5000

print("Welcome to the ATM!")
print(f"Your current balance is ₹{balance}")
print(f"Withdrawal limit per transaction:₹{withdrawal_limit} ")

withdraw_amount = int(input("Enter the amount you want to withdraw: ₹"))

if withdraw_amount < 0:
    print("Invalid amount! Please enter a positive amount to withdraw.")
elif withdraw_amount > balance:
    print("Insufficient balance!Withdrawal denied..")
elif withdraw_amount > withdrawal_limit:
    print(" Withdrawal  denied ! The amount exceeds the transaction limits.")
else:
    balance =  balance - withdraw_amount
    print("Withdrawal successful! You have withdrawn ₹",withdraw_amount)
    print("Your remaining balance is : ₹",balance)