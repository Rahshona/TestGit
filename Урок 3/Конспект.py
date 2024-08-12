# Цикл - это многократно исполняемое действие для выполннения любых операций

# Цикл for:

#Цикл for пробегается по каждому значению элемента.
# Помещает каждую из них в переменную, а затем мы можем произвести различные действия над ними

#for новая_переменная in набор_значений:          сделай что-то с новой переменной

# 1) name = 'Pasha'                               #Примеры
#    for item in name:
#    print(item)

#nabor = ('1', 2,'a')
#for b in nabor:
#print(b)

#p =['m','my', 23]
#for tor in p:
#print(tor)

# range - диапазон.

#my_tuple = (6, 4, '2')                #Функция range() в основном используется чтобы задать
#for i in range(1, 100):               #количество повторений (итераций)
#print(f'{my_tuple}')                  #Итерируемый обьект - это набор значений ими могут
                                       #быть строки(str), списки(list), кортежи(tuple)

                                       #range() - не включает в себя последнее число.
                                       #Например: range(1, 100) не включает в себя 100

#names = ['Ivan','Pavel','Jordan', 5]    #Пример
#for i in range(1, 20):
#if 'Pavel' in names:
#print('Pavel есть в списке')
#else:
#print('Не понимаю о ком вы')


#Цикл while

#While - цикл, который работает до тех пор пока
#переданное условие возвращает True и если условие
#приводит к Flase цикл останавливается
#Простыми словами (Пока это правда - делай, а если нет -остановись.

#while True:                      # делай все по условию

#p = ['m', 'my', 23]                    #Переделка for в while и наоборот
#i = 0
#while i < len(p):
#    print(p[i])
#    i = i + 1
#for i in p:
#    print(i)


#names = ['Ivan', 'Pavel', 'Jordan']
#while True:
#    new = input('Кого добавить? ')
#    if new == 'Список':
#        print(names)
#    else:
#        names.append(new)
#        print(f'{new} добавлен')


#Моя практика

#name = []
#number = []
#ser = []

#while True:
#    p = input('Имя, номер, услуга или список? ')
#    if p == 'имя':
#        name1 = input('Введите имя ')
#        name.append(name1)
#    elif p == 'номер':
#        number1 = input('Введите номер ')
#        number.append(number1)
#    elif p == 'услуга':
#        ser1 = input('Введите услугу ')
#        ser.append(ser1)
#    else:
#        print(name)
#        print(number)
#        print(ser)