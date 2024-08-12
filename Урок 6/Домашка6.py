pupils = {}



def add_pupils(name,grade):
    if name not in pupils:
        pupils[name] = grade
        pupils.values()
        for grade in pupils.values():
            grade = grade + ' класс'
        print (f'{name} добавлен в {grade}')
    elif name in pupils:
        print('Данное Ф.И.О. ученика уже существуют.')


def delete_pupils(name):
    if name in pupils:
        pupils.pop(name)
        print(f'{name} удален из списка')
    elif name not in pupils:
        print('Данного ученика нет в списке. ')


def change_pupils(name,grade):
    if name in pupils:
        pupils.pop(name)
        pupils[name] = grade
        pupils.values()
        for grade in pupils.values():
            grade = grade + ' класс'
        print('Изменения сохранены')
    elif name not in pupils:
        print('Данного ученика нет в списке ')


while True:
    menu = input('Выберите действие'
                 '\n 1 - добавить ученика'
                 '\n 2 - удалить ученика'
                 '\n 3 - редактировать список учеников'
                 '\n 4 - показать список учеников'
                 '\n 5 - выход \n')


    if menu == '1':
        print(add_pupils(name = input('Введите фамилию и имя ученика ').title(), grade = input('Введите класс ')))
    elif menu == '2':
        print(delete_pupils(name = input('Введите фамилию и имя ученика ').title()))
    elif menu == '3':
        print(change_pupils(name = input('Введите фамилию и имя ученика ').title(), grade = input('Введите класс ')))
    elif menu == '4':
        print(pupils)
    else:
        break

