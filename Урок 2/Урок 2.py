klient = input('Имя: ')
n_klient = input('Номер: ')
vmeste = klient + ' ' + n_klient + ' номер'
baza = []
baza.append(vmeste)

print(baza)

guests = [['Ботир', '10'], ["Oleg","9"]]
menu = input("Выберите действие:\n1-посмотреть список\n"
             "2-добавить клиента: ")
if menu == "1":
    print(guests)
elif menu == "2":
    name = input("введите имя клиента: ")
    number = input("введите номер комнаты: ")
    guests.append([name, number])
    print(f"Клиент {name} заселен в комнату {number}")
    print(guests)








