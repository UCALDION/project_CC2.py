print ("WELCOME TO FORDION DEALS")
class ATM:
    def __init__(self):
        self.balance = 100.00

    def check_balance(self):
        print(f"Your current balance is: {self.balance:.2f} PHP")

    def withdraw_money(self):
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount:.2f} PHP successful.")
            self.check_balance()
        else:
            print("Insufficient funds.")

    def deposit_money(self):
        amount = float(input("Enter the amount to deposit: "))
        if amount > 0:
            self.balance += amount
            print(f"Deposit of {amount:.2f} PHP successful.")
            self.check_balance()
        else:
            print("Invalid amount.")

def main():
    atm = ATM()
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Exit Application")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            atm.withdraw_money()
        elif choice == '3':
            atm.deposit_money()
        elif choice == '4':
            print("Thank you for choosing FORDION DEALS. Have a great day!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
