class BankAccount:
    bank_name = "National Bank"
    interest_rate = 5.0

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New Balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount} withdrawn. New Balance: {self.balance}")
        else:
            print("Insufficient balance")

    def show_balance(self):
        print(f"{self.account_holder}'s Balance: {self.balance}")

    @staticmethod
    def bank_info():
        print(f"Welcome to {BankAccount.bank_name}. We value our customers!")
        print(f"Current interest rate is {BankAccount.interest_rate}%")

# ---------- Taking Input from User ----------
name = input("Enter account holder name: ")
balance = float(input("Enter initial balance: "))

# Create account
acc = BankAccount(name, balance)

while True:
    print("\n--- Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Bank Info")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        acc.deposit(amount)
    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        acc.withdraw(amount)
    elif choice == "3":
        acc.show_balance()
    elif choice == "4":
        BankAccount.bank_info()
    elif choice == "5":
        print("Thank you for using our bank system!")
        break
    else:
        print("Invalid choice, try again.")