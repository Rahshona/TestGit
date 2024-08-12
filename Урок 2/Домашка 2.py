spisok = ['Ботир', '123456789']
name_spisok = ['Ботир']
number_spisok = ['123456789']

name = input('Введите имя контакта ')
number = input('Введите номер телефона ')

if name in name_spisok or number in number_spisok:
    print('Данное имя контакта или номер контакта уже существуют.'
          '\nВведите новые данные или замените уже существующий.'
          '\nЕсли создать другой новый контакт - 0 '
          'Если хотите удалить существующий - 1;'
          'Если заменить существующий - 2')
    a = input('0, 1 или 2 ')
    print(a)
    if a == '0':
        name = input('Введите имя контакта ')
        number = input('Введите номер телефона ')
        print(name)
        print(number)
        name_spisok.append(name)
        number_spisok.append(number)
        spisok.append([name_spisok, number_spisok])
    elif a == '2':
        if name in name_spisok:
            ind = name_spisok.index(name)               #Добавить намбер
            name2 = input('Новое имя контакта ')
            name_spisok[ind] = name2
            ind2 = spisok.index(name)
            spisok[ind2] = name2
            number = input('Введите номер телефона ')
            number_spisok[ind] = number
            spisok[ind+1] = number
        elif number in number_spisok:                   #Добавить нейм
            ind_numb = number_spisok.index(number)
            number2 = input('Новый номер контакта ')
            number_spisok[ind_numb] = number2
            ind_numb2 = spisok.index(number)
            spisok[ind_numb2] = number2
            name = input('Введите имя контакта ')
            name_spisok[ind_numb] = name
            spisok[ind_numb2-1] = name
        elif number in number_spisok and name in name_spisok:
            print('Ошибка. Данное имя контакта или номер не существуют в списке ')
    else:
        ind = name_spisok.index(name)
        name_spisok.pop(ind) # Добавить намбер
        ind2 = spisok.index(name)
        spisok.pop(ind2)
        number_spisok.pop(ind)
        ind_numb2 = spisok.index(number)
        spisok.pop(ind_numb2)

        #используй поп
else:
    spisok.append([name, number])
print(spisok)