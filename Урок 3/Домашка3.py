palin = ['Анна']

while True:

    p = input('Введите палиндром (слово, которое читается в обе стороны) ')

    nij = p.lower()
    reversed_1 = nij[::-1]
    if nij == reversed_1:
        palin.append(p)
        print(f'Ваше слово {p} добавлено в список палиндром ')
        print(palin)
    else:
        print('Ваше слово не является палиндромом. Повторите попытку ')
