class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f"Your balance is: ${self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount 
            print(f"${amount} deposited successfully")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"${amount} withdrawn successfully")
        else:
            print("Invalid amount or insufficient balance")

def main():
    atm = ATM(balance=1000)

    while True:
        print("\nWelcome to the ATM")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            atm.check_balance()
        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            atm.deposit(amount)
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            atm.withdraw(amount)
        elif choice == "4":
            print("Thank you for using the ATM")
            break
        else:
            print("Invalid choice, please try again")
            

if __name__ == "__main__":
    main() 
    