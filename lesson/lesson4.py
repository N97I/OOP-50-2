# Что такое декоратор?
# Декоратор — это функция, которая принимает другую функцию в качестве аргумента и возвращает
# измененную или новую функцию. Они позволяют добавлять новую функциональность к существующим
# функциям без изменения их кода.


# Пример простого декоратора
def my_decorator(func):  # 2

    def wrapper():
        print('Перед выполнением функции')  # 4
        func()  # 5
        print('После выполнением функции')  # 6

    return wrapper  # 3


@my_decorator
def hello():
    print("Привет мир!!")


hello()  # 1


# Декораторы с аргументами
# n = 3
def repeat(n):  # step 2
    # func = greet()
    def decorator(func):  # step 4
        def wrapper(*args, **kwargs):
            for i in range(n):  # step 6
                func(*args, **kwargs)  # step 6

        return wrapper  # step 5

    return decorator


@repeat(3)
def greet():
    print("Привет!!")


greet()  # step 1

def class_decorator(cls):

    class NewClass(cls):

        def new_method(self):
            return print('Новый Метод')

    return NewClass


@class_decorator
class MyClass:

    def old_method(self):
        return print('Старый метод')

obj = MyClass()
obj.old_method()
obj.new_method()


class Person:


    def __init__(self, name, age):
        self.name = name
        self.age = age


    def __str__(self,):
        return f'bla bla bla'

# obj = Person('Pavel', 25)

# print(obj)

class Money:

    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        print(f'{self.amount}------{other.amount}')
        return f'bla'

    def __str__(self,):
        return f'{self.amount} som'

    def __len__(self):
        return f'pass'

m1 = Money(100)
m2 = Money(200)
m3 = m1 + m2
len(m3)


class Math:

    def add(self, a, b):
        return a + b

obj3 = Math()

print(obj3.add(1,2))


class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    @classmethod
    def get_population(cls):
        return cls.count

    @classmethod
    def create_person(cls, name):
        return cls(name)

person1 = Person('Alice')
person2 = Person('Bob')
person3 = Person('Bobs')
print(Person.get_population())
person4 = Person.create_person('John')
print(person4.name)