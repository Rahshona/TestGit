#Функция это коробка в коробке. Нужна для того, чтобы некоторые действия не повторять по несколько раз и сделать код компактнее
#Все данные в ней находятся только в ней. И не считаются глобальной переменной. "КОРОБКА В КОРОБКЕ"


#def spam2(a, b, c=7):    Аргумента а и b мы можем вводить в скобках функций, где хотим исползовать.
#print(a+b+c)             Но параметр с он необязательный, но если необходимо, то его значение, которое должно не меняться
#spam2(3, 5)              мы можем написать в самой функции

#def spam1(*args):          #ТУт самое важное - это звездочка. Одна звездочка позволяет вводить несколько аргументов, по которым будет выполняться функция
#    return args            Запомни! ретерн и принт разные вещи. ретерн для конечного результата функции, а принт лишь для визуализации

#print(spam1(1,2,3,'Hello'))

#def spam1(**kwargs):                   Две звездочки то же самое, как и одна, но тут все вводится как в словаре: ключ и его значение
#    for k,v in kwargs.items():
#        return k,v
#print(spam1(name = 'my1', age = 23))


#def num(a):                                     Пример деления на четное и нечетное
#    if a % 2 == 0:
#        print('Четное')
#    elif a % 2 != 0:
#        print('Нечетное')
#while True:
#    a = int(input('Введите число '))
#    num(a)


#management_system = {}                                         Моя проектная работа(нужно исправить. Эта заметка для себя!!!)



#def klient_add(klient):
#    for a, b in management_system.items():
#        print(a,b)
#        if nomer not in management_system.values():
#            management_system[klient] = nomer
#        elif nomer in management_system.values():
#            print('Номер занят ')


#def klient_delete(delete):
#    if delete in management_system.keys():
#        management_system.pop(delete)

#def reserved(nomer):
#    print(management_system.values())

#while True:
#    menu = input('1- добавить клиента'
#                 '\n 2 - удалить клиента'
#                 '\n 3 - увидеть занятые номера ')
#    if menu == '1':
#        klient = input('Введите имя клиента ')
#        klient_add(klient)
#    elif menu == '2':
#        delete = input('Введите имя клиента ')
#        klient_delete(delete)
#    elif menu == '3':
#        nomer = int(input('Введите номер комнаты '))
#        reserved(nomer)


clients = {}                                                           #Пример учителя по проектной работе
def add_client(name, number):
    if name in clients.keys() or number in clients.values():
        print("такой клиент уже существует")
    else:
        clients[name] = number
        print("клиент добавлен")
def remove_client(name):
    if name not in clients.keys():
        print("такого клиента нет")
    else:
        clients.pop(name)
        print("успешно удалено")
def rooms():
    print("занятые номер: ", list(clients.values()))

while True:
    menu = input("что хотите сделать?\n"
                 "1- Добавить клиента\n"
                 "2- Удалить клиента\n"
                 "3- Список занятых номеров: ")
    if menu == "1":
        rooms()
        add_client(name=input("Введите имя: "), number=input("Введите номер: "))
    elif menu == "2":
        remove_client(name=input("Введите имя: "))
    elif menu == "3":
        rooms()





