class Math:

    def __init__(self, a = 0, b = 0):
        self.a = int(a)
        self.b = int(b)

    def addition(self, a, b):
        return a + b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        return a % b

    def subtraction(self, a, b):
        return a - b

number = (Math())

while True:
    menu = input("Выберите действие:\n"
                 "1- Сложить \n"
                 "2- Умножить \n"
                 "3- Вычесть \n"
                 "4 - Разделить  ")

    if menu == '1':
        print(number.addition(a=int(input('Введите первое число ')), b=int(input('Введите второе число '))))
    elif menu == '2':
        print(number.multiplication(a=int(input('Введите первое число ')), b=int(input('Введите второе число '))))
    elif menu == '3':
        print(number.subtraction(a=int(input('Введите первое число ')), b=int(input('Введите второе число '))))
    elif menu == '4':
        print(number.division(a=int(input('Введите первое число ')), b=int(input('Введите второе число '))))
    else:
        print('Повторите попытку ')



