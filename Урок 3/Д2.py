name = []
number = []
ser = []

while True:
    p = input('Имя, номер, услуга или список? ')
    if p == 'имя':
        name1 = input('Введите имя ')
        name.append(name1)
    elif p == 'номер':
        number1 = input('Введите номер ')
        number.append(number1)
    elif p == 'услуга':
        ser1 = input('Введите услугу ')
        ser.append(ser1)
    else:
        print(name)
        print(number)
        print(ser)




