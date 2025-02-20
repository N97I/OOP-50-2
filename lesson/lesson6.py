# Множественные наследование

# Горизонтальное наследование

# class Flyable:
#
#
#     def fly(self):
#         return 'Летит'
#
#
# class Swimmable:
#
#     def swim(self):
#         return 'Плавает'
#
# class Duck(Flyable, Swimmable):
#
#     def make_sound(self):
#         return "Кря-Кря"
#
# donald_duck = Duck()
# print(donald_duck.fly())
# print(donald_duck.swim())

# ромбовидное наследование

# class Animal:
#
#     def __init__(self,name):
#         self.name = name
#
#
#     def make_sound(self):
#         return "Издает звук"
#
# class Swimmable(Animal):
#
#     def swim(self):
#         return 'Плавает'
#
#     def action(self):
#         return 'Base action'
#
# class Flyable(Animal):
#
#
#     def fly(self):
#         return 'Летит'
#     def action(self):
#         return 'Base action'
#
#
#
# class Duck(Flyable, Swimmable):
#
#     def __init__(self, name):
#         super().__init__(name)
#
#
#     def make_sound(self):
#         return "Кря-Кря"
#
#     def action(self):
#         return 'fly and swim'
#
#
# donald_duck = Duck()
# print(donald_duck.fly())
# print(donald_duck.swim())
# print(donald_duck.action())
# print(Duck.mro())

# import sqlite3
#
# # A4
# connect = sqlite3.connect('User.db')
#
#
# # визуализируем рука с ручкой
# cursor = connect.cursor()
#
# # cursor.execute("DROP TABLE IF EXISTS users")
# # connect.commit()
#
#
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS users(
#         name VARCHAR (40) NOT NULL,
#         age INTEGER NOT NULL,
#         hobby TEXT
#     )
#                 """)
# # сохранение изменений
# connect.commit()
#
# def add_user(name, age, hobby):
#
#     cursor.execute(
#         'INSERT INTO users(name, age, hobby) VALUES (?, ?, ?)', # правильный вариант
#         # f'INSERT INTO users(name, age, hobby) VALUES ({name}, {age}, {hobby})',
#         # так писать не желательно так как не будет код защищен
#         (name, age, hobby)
#     )
#     # cursor.execute(
#     #     'DROP DATA BASE'
#     # )
#     connect.commit()
#     print(f'Пользователь {name} добавлен')
#
# # name = input('DROP DATA BASE')
# add_user("John", 33, 'плавание')
# add_user("Ardager", 25, 'спать')
# add_user("Вася", 22, 'бегать')
# add_user("Олег", 11, 'ничего')
#
#
# def get_all_users():
#
#
#     users = cursor.fetchall()
#     cursor.execute('SELECT * FROM users')
#     print(users)
#     print(f'Список всех пользователей')
#
#     for i in users:
#         print(f"NAME: {i[0]}, AGE {i[1]}, HOBBY: {i[2]}")
#
# get_all_users()
# connect.close()
