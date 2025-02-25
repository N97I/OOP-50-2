import sqlite3

# A4
connect = sqlite3.connect('User.db')

# Рука с Ручкой
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name VARCHAR (40) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
               ''')

cursor.execute("""
        CREATE TABLE IF NOT EXISTS grades (
            grade_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER, 
            subject VARCHAR (50) NOT NULL,
            grade INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
                """)
connect.commit()

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
#
add_user("Ardager", 23, "плавать")
add_user("Oleg", 23, "плавать")
add_user("John", 23, "плавать")
add_user("Doe", 23, "плавать")
add_user("Anna", 23, "плавать")

def add_grades(user_id, subject, grade):
    cursor.execute("""
            INSERT INTO grades (user_id, subject, grade) VALUES (?, ?, ?)""",
            (user_id,subject, grade))
    connect.commit()
    print(f'Оценка добавлена для пользователя c ID {user_id}!!!')

add_grades(4, "Алгебра",5)
add_grades(2, "Химия",2)
add_grades(1, "Физика",4)
add_grades(3, "Геометрия",3)
add_grades(5, "Русский",5)

def get_users_with_grades():
    cursor.execute("""
        SELECT users.name, grades.subject, grades.grade
        FROM users
        LEFT JOIN grades ON users.user_id = grades.user_id
                    """)

    users = cursor.fetchall()
    for i in users:
        print(f'NAME: {i[0]}, SUBJECT: {i[1]}, GRADE: {i[2]}')

def update_grade_by_id(new_grade, grade_id):
    cursor.execute("""
        UPDATE grades
        SET grade = ?
        WHERE grade_id = ?""",(new_grade, grade_id))
    connect.commit()
    print(f'Subject with ID {grade_id} updated!')

update_grade_by_id(1,3)