balance = 50000

while True:
    print(f"\n--- ATM Menu ---")
    print(f"1. Check Balance")
    print(f"2. Deposit")
    print(f"3. Withdraw")
    print(f"4. Exit")

    choice = int(input(f"Enter your choice (1-4): "))

    if choice == 1:
        print(f"Your current balance is: {balance}")

    elif choice == 2:
        amount = int(input(f"Enter amount to deposit: "))
        balance = balance + amount
        print(f"{amount} deposited. New balance is: {balance}")

    elif choice == 3:
        amount = int(input(f"Enter amount to withdraw: "))
        if amount <= balance:
            balance = balance - amount
            print(f"{amount} withdrawn. New balance is: {balance}")
        else:
            print(f"Insufficient balance!")

    elif choice == 4:
        print(f"Thank you for using ATM. Goodbye!")
        break

    else:
        print(f"Invalid choice. Please try again.")