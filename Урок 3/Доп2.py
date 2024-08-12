sum = input('Сумма вашего заказа ')
summa = float(sum)
summa1 = round(summa,2)

tax = summa * 0.1
tax1 = round(tax,2)

tip = summa * 0.18
tip1 = round(tip,2)

total = summa + tax + tip
total1 = round(total)

print(f'Ваша сумма заказа {summa1} $ '
      f'\n Налог составил (10%) {tax1} $ '
      f'\n Чаевые для официанта (18%) {tip1} $ '
      f'\n Общая сумма платежа {total1} $ '
      'Спасибо за заказ. Приходите к нам еще :) ')


