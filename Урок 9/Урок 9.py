class Animals:
    def eat(self):
        print(f'{self} кушает')

class Mammal(Animals):
    def milf_feed(self):
        print(f'{self} кормит молоком')

class Horse(Mammal):
    def jump(self):
        print(f'{self} прыгает')

horse1 = Horse()
horse1.milf_feed()

class Disease:
    def name(self):
        print('Бронхиальная астма')

class Syndrome(Disease):
    def synd(self):
        print('Синдром отдышки')

class Symptom(Disease):
    def symp(self):
        print('Свистящие хрипы')

diag1 = Symptom()
diag1.name()

class Car:
    def __init__(self,model,color,year):
        self.model = model
        self.color = color
        self.year = year

class SuperCar(Car):
    def __init__(self,model,color,year,sponsor):
        super().__init__(model,color,year)
        self.sponsor = sponsor

class Parent1:
    pass
class Parent2:
    pass
class Child(Parent1,Parent2):
    pass

class MyClass:
    @classmethod
    def class_info(cls):
        return f'This is the {cls.__name__} class'
print(MyClass.class_info())

class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.height * self.width

rectangle = Rectangle(4,5)
print(rectangle.area)

rectangle.width = 6
print(rectangle.area)