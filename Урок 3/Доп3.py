number = input('Введите положительное натуральное число.' 
               '\n Если число будет десятичным (не натуральное), оно автоматически округлится!  ')
num = float(number)
n = round(num)

if n > 0:
    sum = n ** 2 + n
    s = sum / 2
    print(s)
elif n < 0:
    print('Не мухлюй! Только ПОЛОЖИТЕЛЬНОЕ число! ')
