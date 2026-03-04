def display_balance(balance):
    print("Current Balance:", balance)

def deposit(balance):
    amount = float(input("Enter amount to deposit: "))
    balance = balance + amount
    print("Amount Deposited:", amount)
    return balance

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    if amount > balance:
        print("Insufficient balance")
    else:
        balance = balance - amount
        print("Amount Withdrawn:", amount)
    return balance

balance = 0

while True:
    print("\n1. Display Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        display_balance(balance)

    elif choice == "2":
        balance = deposit(balance)

    elif choice == "3":
        balance = withdraw(balance)

    elif choice == "4":
        print("Exiting")
        break

    else:
        print("Invalid choice")