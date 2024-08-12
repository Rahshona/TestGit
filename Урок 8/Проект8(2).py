class BankAccaunt:
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance

    def deposit(self, deposit_add):
        self.balance = deposit_add + self.balance


    def cash(self, deposit_vivod):
        self.balance = self.balance - deposit_vivod

    def my_balance(self):
        print(self.balance)


person1 = BankAccaunt('Maria', 2500)
person1.deposit(500)
print(person1.balance)
person1.cash(1000)
print(person1.balance)
print(person1.my_balance())
