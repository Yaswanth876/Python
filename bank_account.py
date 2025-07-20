class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"✅ {amount} Rs. deposited successfully.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"✅ {amount} Rs. withdrawn successfully.")
        else:
            print("❌ Insufficient balance!")

    def show_balance(self):
        print(f"💰 Current Balance: {self.balance} Rs.")


acc = BankAccount(5000)

acc.deposit(2000)
acc.withdraw(3000)
acc.show_balance()