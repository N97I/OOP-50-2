def logger(n=1):

    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
        return wrapper

    return decorator

@logger()
def greet(name):
    print(f'Привет, {name}!')

greet('Алиса')


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self,):
        return f'Прямоугольник {self.width}x{self.height}'

    def __add__(self, other):
        return f'Прямоугольник {self.width + other.width}x{self.height + other.height}'

rect1 = Rectangle(3,4)
rect2 = Rectangle(2,5)
rect3 = rect1 + rect2

print(rect1)
print(rect2)
print(rect3)