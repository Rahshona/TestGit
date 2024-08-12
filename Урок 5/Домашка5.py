all_products = {'Весь склад': {}}

while True:
    menu = input("Выберите действие:\n"
                 "2- Продукты\n"
                 "1- Добавить: ")
    if menu == "1":
        name = input("Введите название продукта: ")
        amount = input("Введите количество: ")
        all_products["Весь склад"][name]=int(amount)
        print("Продукт добавлен")
    elif menu == "2":
        count = 0
        for k,v in all_products["Весь склад"].items():
            count += 1
            print(f"{count}. {k} : {v} кг")

all_1 = list(all_products)
print(all_1)