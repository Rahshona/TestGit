litr_1 = []
litr_poltara = []
litr_2 = []
litr_5 = []
litr_10 = []
summa_total = []

while True:
    butilka = input('Обозначьте обьем бутылки, которую вы хотите сдать: '
                    '\n  1 - 1 литр'
                    '\n  2 - 1,5 литра'
                    '\n  3 - 2 литра'
                    '\n  4 - 5 литров'
                    '\n  5 - 10 литров'
                    '\n  6 - посчитать общую сумму '
                    '\n ')

    if butilka == '1':
        litr_1.append(butilka)
        a = len(litr_1)
        summa_1 = a * 0.10
        summa_total.append(summa_1)
    elif butilka == '2':
        litr_poltara.append(butilka)
        b = len(litr_poltara)
        summa_2 = b * 0.25
        summa_total.append(summa_2)
    elif butilka == '3':
        litr_2.append(butilka)
        c = len(litr_2)
        summa_3 = c * 0.25
        summa_total.append(summa_3)
    elif butilka == '4':
        litr_5.append(butilka)
        d = len(litr_5)
        summa_4 = d * 0.25
        summa_total.append(summa_4)
    elif butilka == '5':
        litr_10.append(butilka)
        e = len(litr_10)
        summa_5 = e * 0.25
        summa_total.append(summa_5)
    else:
        summa = sum(summa_total)
        s = round(summa, 2)
        print(f'Общая сумма составила: {s} $ ')
        break