#import random

#Пример 1.

#kvadrati = [i ** 2 for i in range(1, 51)]
#print(kvadrati)

#Пример 2.

#troyka = [i for i in range(1, 100) if i % 3 == 0]
#print(troyka)

#Пример 3

#II = random.randint(1, 11)
#num = input('Введите число от 1 по 10 ')
#numbers = [num for n in num if num == II]
#print(numbers)

#Пример 4

#second_names = ['седенкова', 'маслова', 'шарипов', 'ботирова', 'исламбеков', 'кукурузов']
#bolshiye_bukvi = [i.title() for i in second_names]
#print(bolshiye_bukvi)

#Пример 5
#second_names = ['Седенкова', 'маслова', 'Шарипов', 'ботирова', 'исламбеков', 'кукурузов']
#title_letter = [i for i in second_names if i[0] == i.title()[0]]
#print(title_letter)

#Пример 6

#ceni= [233.5, 344, 422.4, 700.6, 234.2, 544.8]
#s_nalogom = [(i, i * 0.1) for i in ceni]
#print(s_nalogom)

#Пример 7
producti = ['помидор', 'картофель', 'свекла', 'лук']
koli_4_estvo = [len(i) for i in producti]
print(koli_4_estvo)





