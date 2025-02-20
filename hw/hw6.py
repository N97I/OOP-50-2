import sqlite3

# A4
connect = sqlite3.connect('User.db')


# визуализируем рука с ручкой
cursor = connect.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        name VARCHAR (40) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
                """)
# сохранение изменений
connect.commit()
def add_user(name, age, hobby):

    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES (?, ?, ?)', # правильный вариант
        (name, age, hobby)
    )
    connect.commit()
    # print(f'Пользователь {name} добавлен')

# name = input('DROP DATA BASE')
add_user("Mike", 28, 'Сноуборд')
add_user("John", 33, 'плавание')
add_user("Вася", 22, 'бегать')
add_user("Олег", 11, 'ничего')


def get_all_users():


    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    print(users)
    print(f'Список всех пользователей')

    for i in users:
        print(f"NAME: {i[0]}, AGE {i[1]}, HOBBY: {i[2]}")


def get_users_by_name(name):
    connect = sqlite3.connect('User.db')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM users WHERE name = ?', (name,))
    users = cursor.fetchone()
    connect.close()

    if users:
        return f"NAME: {users[0]}, AGE {users[1]}, HOBBY: {users[2]}"
    else:
        return 'Пользователь не найден!'


# get_all_users()
print(get_users_by_name('Mike'))
print(get_users_by_name('Misha'))


