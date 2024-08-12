suvenir = input('Сколько сувениров хотите купить? ')
suv = int(suvenir)

ves_suvenira = suv * 75

bezdelushka = input('Сколько безделушек желаете купить? ')
bezdel = int(bezdelushka)

ves_bezdel = bezdel * 112

total = ves_bezdel + ves_suvenira

print(f'Общий вес посылки составил {total} г')

menu = input('Желаете ли перевести г в кг? '
      '\n 1 - да'
      '\n 2 - нет'
      '\n')

if menu == '1':
    kg = total / 1000
    print(f'Ваши {total} г составляют {kg} kg.'
          '\n Спасибо, что пользуетесь нашим сервисом!'
          '\n Приходите к нам еще!')
else:
    print('Спасибо, что пользуетесь нашим сервисом!'
          '\n Приходите к нам еще!')
