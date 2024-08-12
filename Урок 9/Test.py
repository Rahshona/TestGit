password = input('Введите пароль ')
def length(i):
    for i in password:
        if len(password) > 8 and len(password) <17:
            return True
        else:
            return 'Пароль слишком мал или наоборот'

def integer(i):
    for i in password:
        if '1' or '2' or '3' or '4' or '5' or '6' or '7' or '7' or '8' or '9' in password:
            return True
        else:
            return 'Пароль должен содержать в себе цифру'

def iskl(i):
    for i in password:
        if '!' or '@' or '#' or '$' or '%' or '^' or '&' or '*' or '(' or ')' or '>' or '<' or '+' or '=' or '-' not in password:
            return True
        else:
            return 'Пароль содержит недопустимые символы'

def check():
    length(password)
    iskl(password)
    integer(password)

check()






