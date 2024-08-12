class Car:

    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def go(self):
        return f'{self.type} заведен'

    def stop(self):
        return f'{self.type} заглушен'

    def new_year(self, change_year):
        self.year = change_year

    def new_type(self, change_type):
        self.type = change_type

    def new_color(self, change_color):
        self.color = change_color

car1 = (Car('blue', 'Lamborghini', 1999  ))

print(vars(car1))
print(car1.go())
print(car1.stop())
car1.new_color('yellow')
car1.new_type('Tesla')
car1.new_year(2024)
print(vars(car1))

