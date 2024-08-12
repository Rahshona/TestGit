all_products = {'Весь склад': {}}
korzina = {'Ваша корзина': {} }


while True:
    menu_1 = input("Выберите действие:\n"
                     "1- Я админка-любимка\n"
                     "2- Я покупатель: ")
    if menu_1 == "1":
        menu_2 = input("Выберите действие:\n"
                     "1- Добавить продукты\n"
                     "2- Посмотреть склад: ")
        if menu_2 == '1':
            name = input("Введите название продукта: ").lower()
            amount = int(input("Введите количество: "))
            all_products["Весь склад"][name] = int(amount)
            print("Продукт добавлен")
        elif menu_2 == '2':
            count = 0
            for k, v in all_products["Весь склад"].items():
                count += 1
                print(f"{count}. {k} : {v} кг")
    elif menu_1 == "2":
        menu_3 = input("Выберите действие:\n"
                       "1- Добавить продукты\n"
                       "2- Удалить продукты\n"
                       "3- Посмотреть корзину: ")
        if menu_3 == '1':
            name_1 = input("Введите название продукта: ").lower()
            amount_1 = int(input("Введите количество: "))
            if name_1 in all_products["Весь склад"].keys():
                korzina['Ваша корзина'][name_1] = int(amount_1)
                if amount_1 <= all_products["Весь склад"][name_1]:
                    all_products["Весь склад"][name_1] -= amount_1
                    print("Продукт добавлен")
                else:
                    print('В складе нет нужного количества вашего продукта')
        elif menu_3 == '2':
            name_1 = input("Введите название продукта: ").lower()
            amount_1 = int(input("Введите количество: "))
            if name_1 in korzina["Ваша корзина"].keys():
                print("Нужное количество продукта удалено")
                if name_1 in all_products["Весь склад"].keys():
                    korzina["Ваша корзина"][name_1] -= amount_1
                    if amount_1 <= all_products["Весь склад"][name_1]:
                        all_products["Весь склад"][name_1] += amount_1
        elif menu_3 == '3':
            count = 0
            for k, v in korzina["Ваша корзина"].items():
                count += 1
                print(f"{count}. {k} : {v} кг")
        else:
            print('Перепроверьте, правильно ли вы ввели цифру')
    else:
        print('Перепроверьте, правильно ли вы ввели цифру')





