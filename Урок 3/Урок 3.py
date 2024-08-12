#my_list = (6, 4, '2')
#for t in my_list:
 #   print(t+2)

#my_list2 = ('2', 4, '2')
#count = 0
#for t in range(1, 100):
#    print(t)

p = ['m', 'my', 23]
i = 0
while i < len(p):
    print(p[i])
    i = i + 1
for i in p:
    print(i)

names = ['Ivan', 'Pavel', 'Jordan']
while True:
    new = input('Кого добавить? ')
    if new == 'Список':
        print(names)
    else:
        names.append(new)
        print(f'{new} добавлен')