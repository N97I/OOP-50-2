# class def

class Person:

    # это функция конструктор
    def __init__(self, name, age):
        # Атрибуты класса
        self.name = name
        self.age = age

    # self - это ссылка OBJECT на или экземпляр класса
    # Метод класса
    def introduce(self,):
        print(f"Hi i'm {self.name}")
# Класс OBJECT - экземпляр класс
ardager = Person('Ardager', 25)

# ardager.introduce()
#
# print(type(ardager))
# print(type(123))
# print(type('Hello'))

# Родительский класс
class Hero:
    def __init__(self, name, hp, lvl):

        self.name = name
        self.hp = hp
        self.lvl = lvl

    def action(self,):
        print(f'{self.name} делает базовое действие')

# naofume = Hero('NaoFume', 100, 3)
# Дочерний класс
class ShiledHero(Hero):
    pass # ---
    ... # ---


naofume = ShiledHero('NaoFume', 100, 3)

naofume.action()

# class -- CamelCase
# используется для переменных, методов, функций -- snek_case
