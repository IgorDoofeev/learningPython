'''class Point:
    color = 'red'
    circle = 2

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y


pt = Point()  # Создаем экземляр класса
pt.set_coords(1, 2)
print(pt.__dict__)'''


class Point:
    color = 'red'
    circle = 2

    def __init__(self, a=0, b=0):
        print('Вызов __init__')
        self.x = a
        self.y = b

    def __del__(self):
        print('удаление экземпляра: ' + str(self))


    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y

pt = Point(1, 2)
print(pt.__dict__)