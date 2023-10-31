class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod  # Метод для работы только с атрибутами класса
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = self.y = 0
        if Vector.validate(x) and Vector.validate(y):
            self.x = x
            self.y = y

        print('Вызов нормы вектора из init: ', self.norm2(self.x, self.y))

    def get_coord(self):
        return self.x, self.y

    @staticmethod  # Метод для работы с сервисной функции и параметрами только внутри нее
    def norm2(x, y):  # Вычисляем квадрат нормы
        return x*x + y*y


v = Vector(10, 20)
print(Vector.validate(5))
print(Vector.norm2(5, 6))  # Вызов нормы из статического метода
res = Vector.get_coord(v)
print(res)
