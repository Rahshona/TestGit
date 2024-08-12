l = float(input('Vvedite chislo '))
r = float(input('Vvedite vtoroye chislo '))
b = str(input('+, -, /, * ? '))
if b == '+':
    print(l+r)
elif b == '-':
    print(l-r)
elif b == '/':
    if r == 0:
        print('No no no nelzya pisat 0')
    else:
        print(l/r)
else:
    print(l*r)
