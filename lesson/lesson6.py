# # Множественные наследование
#
# # Горизонтальное наследование
#
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
#
# # ромбовидное наследование
#
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

import sqlite3

# A4
connect = sqlite3.connect('User.db')

# Рука с Ручкой
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name VARCHAR (40) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
               ''')

# Сохранение изменений
connect.commit()


# CRUD - Create - Read - Update - Delete


# Create
def add_user(name, age, hobby):
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES (?,?,?)',
        (name, age, hobby)
    )
    connect.commit()
    print(f"Пользователь {name} добавлен")


# name = input("Введите имя")
# age = input("Введите возраст")
# hobby = input("Введите Хоби")

# add_user("user1", 23, "плавать")
# add_user("user2", 23, "плавать")
# add_user("user3", 23, "плавать")
# add_user("user4", 23, "плавать")
# add_user("user5", 23, "плавать")


def get_all_users():
    cursor.execute('SELECT name, age, hobby FROM users')
    users = cursor.fetchall()
    print(users)
    print('Список всех пользователей')

    for i in users:
        print(f"NAME: {i[0]}, AGE: {i[1]}, HOBBY: {i[2]}")


# get_all_users()


def get_user_by_name(name):
    cursor.execute(
        'SELECT * FROM users WHERE name = ?',
        (name,)
    )
    user = cursor.fetchall()

    print(user)


get_user_by_name('TEST_2')


# Update


def update_user(new_name, user_id):
    cursor.execute(
        'UPDATE users SET name = ? WHERE rowid = ?',
        (new_name, user_id)
    )
    connect.commit()
    connect.close()
    print("User Updated!!")


update_user(user_id=1, new_name="TEST_2")

# Delete
def delete_user(row_id):
    cursor.execute(
        'DELETE from users WHERE rowid = ?',
        (row_id,)
    )
    connect.commit()
    print('User Deleted!!')

# delete_user(3)

