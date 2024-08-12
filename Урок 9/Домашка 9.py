class Player:

    def __init__(self,name = 'Unknown', age = 0):
        self.name = name
        self.age = age

    def kick(self):
        return f'{self.name} пинает мяч'

    def pas_s(self):
        return f'{self.name} пасс мяча'

    def run(self):
        return f'{self.name} бежит'

class Napadayushiy(Player):

    def __init__(self,name,age):
        super().__init__(name, age)

    def gol(self):
        return f'{self.name} забивает гол'

    def fail(self):
        return f'{self.name} промахивается'

class Zashitnik(Player):
    def __init__(self, name, age):
        super().__init__(name, age)


    def zashita(self):
        return f'{self.name} отбирает мяч'

class Semizashitnik(Player):

    def __init__(self, name, age):
        super().__init__(name, age)

    def head(self):
        return f'{self.name} отбивает головой'

class Vratar(Player):

    def __init__(self, name, age):
        super().__init__(name, age)

    def catch(self):
        return f'{self.name} ловит мяч'

    def mistake(self):
        return f'{self.name} пропустил мяч'

player1 = Napadayushiy('Vasya', 15)
player2 = Zashitnik('Petya', 14)
player3 = Semizashitnik('Volodya', 15)
player4 = Vratar('Sasha', 14)

print(player1.kick())
print(player1.gol())