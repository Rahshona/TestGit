class Worker:
    def __init__(self,name,hours,who):
        self.name = name
        self.hours = hours
        self.who = who

    def work(self):
        return f'{self.name} работает {self.hours} часов'

class Manager(Worker):
    def __init__(self, name, hours, who):
        super().__init__(name, hours, who)

    def name_get(self):
        return f'{self.name} работает {self.who}'


worker1 = Worker('Artur', 8, 'builder')
print(worker1.work())

manager1 = Manager('Kunkuha', 24, 'manager')
print(manager1.name_get())

