class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
    def deposit(self, summa):
        self.balance += summa
        print("успешно пополнено")
    def cash(self, summa):
        if self.balance >= summa:
            self.balance -= summa
            print("успешно снято")
        else:
            print("Недостаточно средств")
    def my_balacen(self):
        print(self.balance)

    def __repr__(self):
        return f'Этот объект относится к классу БанкАккаунт с атрибутами {vars(self)} '


user1 = BankAccount(name=input("Введите имя: "))

while True:
    menu = input("Выберите действие:\n"
                 "1- Пополнить счёт\n"
                 "2- Снять деньги\n"
                 "3- Ваш баланс: ")
    if menu == "1":
        user1.deposit(summa=int(input("внести деньги: ")))
    elif menu == "2":
        user1.cash(summa=int(input("укажите сумму вывода: ")))
    elif menu == "3":
        user1.my_balacen()