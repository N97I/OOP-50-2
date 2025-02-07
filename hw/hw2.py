class Heroes:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def action(self):
        print(f"{self.name} готов к бою!")

    def attack(self):
        print(f"{self.name} атакует врага!")


class Archer(Heroes):
    def __init__(self, name, hp, arrows, precision):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision

    def attack(self):
        if self.arrows > 0:
            self.arrows -= 1
            from random import random
            if random() < self.precision:
                print(f"{self.name} попадание!")
            else:
                print(f"{self.name} промах")
        else:
            print(f"у {self.name} закончились стрелы")

    def recharge(self):
        self.arrows += 5
        print(f"у {self.name} перезарядка Теперь у него {self.arrows} стрел.")

    def status(self):
        return f"Имя: {self.name}, Здоровье: {self.hp}, Стрелы: {self.arrows}, Точность: {self.precision:.2f}"


# Тестирование кода
if __name__ == "__main__":
    archer = Archer("joker", 50, 3, 0.5)

    # Проверяем методы
    print(archer.status())
    archer.action()
    archer.attack()
    archer.attack()
    archer.attack()
    archer.attack()
    archer.recharge()
    print(archer.status())