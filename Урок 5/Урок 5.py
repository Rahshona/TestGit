#my_dict = {'names':['Jordan', 'Pavel', 'Sasha'],
#           'user': 'Pasha', 'numbers': (99, 80)}
#print(my_dict)

#instructor = {'name': 'Jordan', 'age': 21, 'job': 'programmer'}
#a = list(instructor.values())
#print(a)
#print(instructor.values())
#print(instructor.keys())
#print(instructor.items())
#print(type(a))

#if 'name' in instructor.items():     #Если после инструктор ничего не писать, то по умолчанию он посмотрит ключи. Поэтому нужно уточнять где мы ищем то, что ищем
#    print('Да, есть')
#else:
#    print('Не понимаю о чем вы')

#if 21 in instructor.items():
#    print('Да, есть')
#else:
#    print('Не понимаю о чем вы') ыйдет не понимаю о чем вы, потому что 21 упоковывается как кортеж

#instructor['gender'] = 'male'
#print(instructor)

#cafees = {'Evos':{'Gorod': 'Tashkent', 'Filialov': 'Много', 'Otkritie': 2007}}
#cafees['Evos']['кухня'] = 'Fast Food'
#print(cafees)                                  Добавил элемент в словарь, который находился в другом словаре

#instructor = {'name': 'Jordan'}
#instructor['name'] = [instructor['name'], 'Pasha']
#print(instructor)
#instructor['name'].append('Oleg')
#print(instructor)

#Удаление

#my_dict = {'song':'Godzilla', 'singer':'Eminem'}
#my_dict.clear() #Удаляет все, но оставляет пустой словарь
#print((my_dict))

#my_dict.pop('song')   #удаляет пару ключ:значение по указанному ключу
#print(my_dict)

#my_dict.popitem() - удаляет последнее добавленное в словарь ключ:значение

#a = {}.fromkeys([1,2,3,4,5], 0) #Разные ключи с одинаковым значением
#print(a)

#.get - работа с ключом. Но если данного ключа нет, то он даст ответ None, но продолжит работу!
#a = {}.fromkeys([1,2,3,4,5], 0)
#print(a)
#print(a.get(6))
#print('hello')

#a = dict(name = 'Jordan', age = 23)     #Можно и так писать словари
#print(a)

#Сеты. Тут нет ИНДЕКСОВ! Но все равно тип данных считается. Не работают так же методы
#nums2 = [2,4,5,6,6,3,3,4,5,5,6,5,6,6,4,2,]
#nums1 = list(set(nums2))
#print(nums1)


#my_dict = {'names':['Jordan', 'Pavel', 'Sasha'],
#           'user': 'Pasha', 'numbers': (99, 80)}
#for k,v in my_dict.items():
#    print(k,v)

producti = {}

while True:
    menu = input('1 - добавить продукт '
                 '\n2 - увидеть список продуктов ')
    if menu == '1':
        producti_1 = input('Введите продукт ')
        kolichestvo = input('Введите количество ')
        print(producti_1)
        print(kolichestvo)
        producti[producti_1] = kolichestvo
    else:
        print(producti)
