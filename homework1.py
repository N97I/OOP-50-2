class Hero:

    # это функция конструктор
    def __init__(self, name, lvl, hp):
        # Атрибуты класса
        self.name = name
        self.lvl = lvl
        self.hp = hp

    # self - это ссылка OBJECT на или экземпляр класса
    # Метод класса
    def introduce(self,):
        print(f"Привет меня зовут {self.name}, Мой уровень {self.lvl}, Мое HP {self.hp}")

    def is_adults(self):
        if self.lvl >= 10:
            return True
        else:
            return False


class ShiledHero(Hero):
    pass

# Класс OBJECT - экземпляр класс
miracle = ShiledHero('Miracle', 2, 70)

miracle.introduce()
print(miracle.is_adults())

class Hero1:

    # это функция конструктор
    def __init__(self, name1, lvl1, hp1):
        # Атрибуты класса
        self.name1 = name1
        self.lvl1 = lvl1
        self.hp1 = hp1

    # self - это ссылка OBJECT на или экземпляр класса
    # Метод класса
    def introduce(self,):
        print(f"Привет меня зовут {self.name1}, Мой уровень {self.lvl1}, Мое HP {self.hp1}")

    def is_adults_1(self):
        if self.lvl1 >= 5:
            return True
        else:
            return False


class ShiledHero1(Hero1):
    pass

# Класс OBJECT - экземпляр класс
jackson = ShiledHero1('Jackson', 7, 87)

jackson.introduce()
print(jackson.is_adults_1())


class Hero2:

    # это функция конструктор
    def __init__(self, name2, lvl2, hp2):
        # Атрибуты класса
        self.name2 = name2
        self.lvl2 = lvl2
        self.hp2 = hp2

    # self - это ссылка OBJECT на или экземпляр класса
    # Метод класса
    def introduce(self,):
        print(f"Привет меня зовут {self.name2}, Мой уровень {self.lvl2}, Мое HP {self.hp2}")

    def is_adults_2(self):
        if self.lvl2 >= 1:
            return True
        else:
            return False


class ShiledHero2(Hero2):
    pass

# Класс OBJECT - экземпляр класс
hobs = ShiledHero2('Hobs', 0, 12)

hobs.introduce()
print(hobs.is_adults_2())