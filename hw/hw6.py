import sqlite3
from types import new_class

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


def get_user_by_name(name):
    cursor.execute('SELECT * FROM users WHERE name = ?', (name,))
    user = cursor.fetchone()
    print(user)



get_user_by_name('Mike')

def update_user(new_name,row_id):

    cursor.execute(
        'UPDATE users SET name = ? WHERE rowid = ?',
        (new_name,row_id)
    )
    connect.commit()
    print('Users Updated!')

update_user(row_id=3, new_name='Test')

# Delete
def delete_user(row_id):
    cursor.execute(
        'DELETE from users WHERE rowid = ?',
        (row_id,)
    )
    connect.commit()
    print('User Deleted!')

delete_user(2)
