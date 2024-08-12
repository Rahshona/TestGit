#БИБЛИОТЕКИ

#Зайти в терменал и написать pip install название библиотеки (которая не встроена, чтобы скачать)
#Можно написать именно версию через равно pip install requests = 10.0

#Можно так же через настройки в файлах

#3 способ через директорию и создания файла. Важно! НАзвание файла писать точь в точь. Написать внутрь все, что нужно
# из библ. После это написать в терминале pip install -r reqirements.txt

#Если хочешь посмотреть весь список библиотек у себя, то в терминале pip freeze

#Если хочешь достать свою функцию с другого файла, то пишется
#from название файла import название функции

# import requests
# url = (сайт с ххтп)
# response = requests.get(url)
#print(response.txt)

#Функции2

#lambda - анонимная функция

# Example: lambda параметр: что нужно сделать

#a = lambda x: x**2
#print(a(10))     Ответ:100

#Пример такой же функции, если бы она не была анонимной:
#def primer_lambda(x):
#    return x+1

#a = lambda x, y: 2*(x+y)
#print(a(4, 5))

#MAP

#map(функция, итерируемый аргумент)
#primer = [3, 2, 5]
#a = map(lambda x: x + 2, primer)
#print(list(a))

#x = [1, 2, 3, '4']
#a = map(lambda  d: d*2, x)
#print(list(a))

#FILTER
#primer = [3, 2, 5]
#a = filter(lambda x: x > 2, primer)
#print(list(a))

#x = [1, 2, -4, -4, -8, -7, 4, 15, 18, 19, 21, -98]
#y = filter(lambda a: a > 0, x)
#print(list(y))

